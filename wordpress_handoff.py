"""Sweeter Teagether WordPress draft handoff (v1).

Dry-run is the default. Live POST is --apply only. Status is always draft.
"""

from __future__ import annotations

import argparse
import json
import os
import re
import sys
import urllib.error
import urllib.parse
import urllib.request
from dataclasses import dataclass, field
from datetime import datetime, timezone
from html import escape
from pathlib import Path
from typing import Any, Callable, Mapping

WORDPRESS_STATUS = "draft"
ELIGIBLE_DIR = Path("content") / "ready-for-review"
HANDOFF_HEADING = "## WordPress handoff"

PUBLISHABLE_SECTIONS = (
    "SEO title",
    "Full article",
    "Excerpt",
    "Slug",
    "Category / tags",
)

EXCLUDED_SECTION_NAMES = (
    "Target query",
    "Search intent",
    "Intended audience",
    "Why this topic matters",
    "Sources",
    "Outline",
    "Meta description",
    "Internal-link opportunities",
    "CTA",
    "Featured-image brief",
    "Factual claims requiring verification",
    "Blockers / stop notes",
    "WordPress handoff",
    "Author / agent",
    "Date researched",
)

REQUIRED_SECTIONS = ("SEO title", "Full article", "Excerpt", "Slug", "Category / tags")

# urllib is imported so tests can patch wordpress_handoff.urlopen.
urlopen = urllib.request.urlopen


class HandoffError(Exception):
    """Fail-closed operational error (user-facing message)."""


@dataclass
class ParsedArticle:
    seo_title: str
    full_article_markdown: str
    excerpt: str
    slug: str
    category_name: str
    tag_names: list[str]
    wordpress_post_id: int | None
    sections_present: list[str]


@dataclass
class WordPressPayload:
    title: str
    content: str
    excerpt: str
    slug: str
    categories: list[int]
    tags: list[int]
    status: str = field(default=WORDPRESS_STATUS)

    def to_dict(self) -> dict[str, Any]:
        if self.status != WORDPRESS_STATUS:
            raise HandoffError("status must be draft")
        return {
            "title": self.title,
            "content": self.content,
            "excerpt": self.excerpt,
            "slug": self.slug,
            "categories": self.categories,
            "tags": self.tags,
            "status": WORDPRESS_STATUS,
        }


def repo_root_from(start: Path | None = None) -> Path:
    if start is not None:
        return start.resolve()
    return Path(__file__).resolve().parent


def load_dotenv(repo_root: Path) -> None:
    """Load .env if present. Never prints values. Does not require .env for dry-run."""
    env_path = repo_root / ".env"
    if not env_path.is_file():
        return
    for raw in env_path.read_text(encoding="utf-8").splitlines():
        line = raw.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        key, _, value = line.partition("=")
        key = key.strip()
        value = value.strip().strip('"').strip("'")
        if key and key not in os.environ:
            os.environ[key] = value


def parse_sections(markdown: str) -> dict[str, str]:
    """Split on ATX ## headings (not ###)."""
    sections: dict[str, str] = {}
    matches = list(re.finditer(r"^## (.+)$", markdown, re.MULTILINE))
    for i, match in enumerate(matches):
        title = match.group(1).strip()
        start = match.end()
        end = matches[i + 1].start() if i + 1 < len(matches) else len(markdown)
        sections[title] = markdown[start:end].strip()
    return sections


def _first_line_or_block(text: str) -> str:
    text = text.strip()
    if not text:
        return ""
    return text


def parse_slug(section: str) -> str:
    text = section.strip()
    fenced = re.search(r"`([a-z0-9]+(?:-[a-z0-9]+)*)`", text)
    if fenced:
        return fenced.group(1)
    line = text.splitlines()[0].strip().strip("`")
    if re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", line):
        return line
    raise HandoffError("Slug section is missing a lowercase-hyphenated slug")


def parse_category_and_tags(section: str) -> tuple[str, list[str]]:
    category = ""
    tags_raw = ""
    for line in section.splitlines():
        stripped = line.strip()
        cat = re.match(r"\*\*Category:\*\*\s*(.+)$", stripped, re.I)
        if cat:
            category = cat.group(1).strip()
            continue
        tags = re.match(r"\*\*Tags:\*\*\s*(.+)$", stripped, re.I)
        if tags:
            tags_raw = tags.group(1).strip()
    if not category:
        raise HandoffError("Category / tags section is missing **Category:**")
    tag_names = [t.strip() for t in tags_raw.split(",") if t.strip()] if tags_raw else []
    return category, tag_names


def parse_existing_post_id(markdown: str) -> int | None:
    match = re.search(
        r"^[-*]\s*wordpress_post_id:\s*(\d+)\s*$",
        markdown,
        re.MULTILINE | re.I,
    )
    if not match:
        return None
    value = int(match.group(1))
    return value if value > 0 else None


def parse_article(markdown: str) -> ParsedArticle:
    sections = parse_sections(markdown)
    missing = [name for name in REQUIRED_SECTIONS if name not in sections or not sections[name].strip()]
    if missing:
        raise HandoffError("Missing required section(s): " + ", ".join(missing))

    category_name, tag_names = parse_category_and_tags(sections["Category / tags"])
    return ParsedArticle(
        seo_title=_first_line_or_block(sections["SEO title"]).split("\n", 1)[0].strip(),
        full_article_markdown=sections["Full article"].strip(),
        excerpt=_first_line_or_block(sections["Excerpt"]),
        slug=parse_slug(sections["Slug"]),
        category_name=category_name,
        tag_names=tag_names,
        wordpress_post_id=parse_existing_post_id(markdown),
        sections_present=list(sections.keys()),
    )


def _inline_md(text: str) -> str:
    def link(match: re.Match[str]) -> str:
        label, url = match.group(1), match.group(2)
        return f'<a href="{escape(url, quote=True)}">{_inline_md(label)}</a>'

    text = re.sub(r"\[([^\]]+)\]\(([^)]+)\)", link, text)
    text = re.sub(r"\*\*(.+?)\*\*", lambda m: f"<strong>{m.group(1)}</strong>", text)
    text = re.sub(r"(?<!\*)\*(?!\*)(.+?)(?<!\*)\*(?!\*)", lambda m: f"<em>{m.group(1)}</em>", text)
    return text


def markdown_to_html(markdown: str) -> str:
    """Small converter for article bodies (headings, lists, paragraphs, links, emphasis)."""
    lines = markdown.replace("\r\n", "\n").split("\n")
    html_parts: list[str] = []
    i = 0
    while i < len(lines):
        line = lines[i]
        heading = re.match(r"^(#{1,6})\s+(.+)$", line)
        if heading:
            level = len(heading.group(1))
            html_parts.append(f"<h{level}>{_inline_md(heading.group(2).strip())}</h{level}>")
            i += 1
            continue
        if re.match(r"^[-*]\s+", line):
            items: list[str] = []
            bullet = re.compile(r"^[-*]\s+")
            while i < len(lines) and bullet.match(lines[i]):
                item_text = bullet.sub("", lines[i], count=1)
                items.append("<li>" + _inline_md(item_text) + "</li>")
                i += 1
            html_parts.append("<ul>" + "".join(items) + "</ul>")
            continue
        if re.match(r"^\d+\.\s+", line):
            items = []
            numbered = re.compile(r"^\d+\.\s+")
            while i < len(lines) and numbered.match(lines[i]):
                item_text = numbered.sub("", lines[i], count=1)
                items.append("<li>" + _inline_md(item_text) + "</li>")
                i += 1
            html_parts.append("<ol>" + "".join(items) + "</ol>")
            continue
        if not line.strip():
            i += 1
            continue
        para: list[str] = []
        while i < len(lines) and lines[i].strip() and not re.match(r"^#{1,6}\s+", lines[i]) and not re.match(
            r"^[-*]\s+", lines[i]
        ) and not re.match(r"^\d+\.\s+", lines[i]):
            para.append(lines[i].strip())
            i += 1
        html_parts.append("<p>" + _inline_md(" ".join(para)) + "</p>")
    return "\n".join(html_parts)


def _term_id(value: Any, label: str) -> int:
    if isinstance(value, bool) or value is None:
        raise HandoffError(f"Taxonomy mapping missing for {label} (placeholder or null)")
    if isinstance(value, str) and value.strip().upper() in {"", "TODO", "NULL", "REPLACE_ME"}:
        raise HandoffError(f"Taxonomy mapping missing for {label} (placeholder)")
    try:
        number = int(value)
    except (TypeError, ValueError) as exc:
        raise HandoffError(f"Taxonomy mapping for {label} is not an integer ID") from exc
    if number <= 0:
        raise HandoffError(f"Taxonomy mapping missing for {label} (non-positive ID)")
    return number


def load_taxonomy(path: Path) -> dict[str, Any]:
    if not path.is_file():
        raise HandoffError(f"Taxonomy config not found: {path}")
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        raise HandoffError(f"Taxonomy config is not valid JSON: {path}") from exc
    if not isinstance(data, dict):
        raise HandoffError("Taxonomy config must be a JSON object")
    return data


def resolve_taxonomy(article: ParsedArticle, taxonomy: Mapping[str, Any]) -> tuple[list[int], list[int]]:
    categories_map = taxonomy.get("categories") or {}
    tags_map = taxonomy.get("tags") or {}
    if article.category_name not in categories_map:
        raise HandoffError(f"No category mapping for {article.category_name!r}")
    category_ids = [_term_id(categories_map[article.category_name], f"category {article.category_name!r}")]
    tag_ids: list[int] = []
    for name in article.tag_names:
        if name not in tags_map:
            raise HandoffError(f"No tag mapping for {name!r}")
        tag_ids.append(_term_id(tags_map[name], f"tag {name!r}"))
    return category_ids, tag_ids


def assert_eligible_source(source: Path, repo_root: Path) -> Path:
    resolved = source.expanduser().resolve()
    if not resolved.is_file():
        raise HandoffError(f"Source file not found: {source}")
    if resolved.suffix.lower() != ".md":
        raise HandoffError("Source must be a .md file")
    allowed = (repo_root / ELIGIBLE_DIR).resolve()
    try:
        resolved.relative_to(allowed)
    except ValueError as exc:
        raise HandoffError(
            f"Only files under {ELIGIBLE_DIR.as_posix()}/ are eligible (got {resolved})"
        ) from exc
    return resolved


def assert_draft_only_env() -> None:
    raw = os.environ.get("WP_POST_STATUS")
    if raw is None or raw.strip() == "" or raw.strip() == WORDPRESS_STATUS:
        return
    raise HandoffError("WP_POST_STATUS is set to a non-draft value; refusing to run")


def build_payload(article: ParsedArticle, category_ids: list[int], tag_ids: list[int]) -> WordPressPayload:
    if not article.seo_title.strip():
        raise HandoffError("SEO title is empty")
    if not article.full_article_markdown.strip():
        raise HandoffError("Full article is empty")
    if not article.excerpt.strip():
        raise HandoffError("Excerpt is empty")
    payload = WordPressPayload(
        title=article.seo_title.strip(),
        content=markdown_to_html(article.full_article_markdown),
        excerpt=article.excerpt.strip(),
        slug=article.slug,
        categories=category_ids,
        tags=tag_ids,
        status=WORDPRESS_STATUS,
    )
    if payload.status != WORDPRESS_STATUS:
        raise HandoffError("status must be draft")
    return payload


def included_excluded(article: ParsedArticle) -> tuple[list[str], list[str]]:
    included = [name for name in PUBLISHABLE_SECTIONS if name in article.sections_present]
    excluded = [name for name in article.sections_present if name not in PUBLISHABLE_SECTIONS]
    for name in EXCLUDED_SECTION_NAMES:
        if name not in excluded and name in article.sections_present:
            excluded.append(name)
    return included, excluded


def sanitize_preview(payload: dict[str, Any]) -> dict[str, Any]:
    """JSON-serializable preview. Never includes credentials."""
    content = payload.get("content") or ""
    preview_content = content if len(content) <= 1200 else content[:1200] + "\n… [truncated for dry-run preview]"
    return {
        "title": payload.get("title"),
        "slug": payload.get("slug"),
        "excerpt": payload.get("excerpt"),
        "categories": payload.get("categories"),
        "tags": payload.get("tags"),
        "status": payload.get("status"),
        "content_preview": preview_content,
        "content_length": len(content),
    }


def basic_auth_header(username: str, password: str) -> str:
    import base64

    token = base64.b64encode(f"{username}:{password}".encode("utf-8")).decode("ascii")
    return f"Basic {token}"


def posts_collection_url(base_url: str) -> str:
    base = base_url.rstrip("/")
    return f"{base}/wp-json/wp/v2/posts"


def find_posts_by_slug(
    base_url: str,
    username: str,
    password: str,
    slug: str,
    opener: Callable[..., Any] | None = None,
) -> list[dict[str, Any]]:
    """Live slug duplicate check. Not used in dry-run."""
    query = urllib.parse.urlencode(
        {"slug": slug, "status": "draft,pending,publish,private,future", "per_page": "10"}
    )
    url = f"{posts_collection_url(base_url)}?{query}"
    request = urllib.request.Request(
        url,
        headers={
            "Authorization": basic_auth_header(username, password),
            "Accept": "application/json",
        },
        method="GET",
    )
    open_fn = opener or urlopen
    try:
        with open_fn(request, timeout=30) as response:
            body = response.read().decode("utf-8")
    except urllib.error.URLError as exc:
        raise HandoffError("WordPress slug lookup failed (network or HTTP error)") from exc
    data = json.loads(body)
    if not isinstance(data, list):
        raise HandoffError("Unexpected WordPress slug-lookup response")
    return data


def create_draft_post(
    base_url: str,
    username: str,
    password: str,
    payload: dict[str, Any],
    opener: Callable[..., Any] | None = None,
) -> dict[str, Any]:
    """Live POST. Not used in dry-run. Never sends a non-draft status."""
    if payload.get("status") != WORDPRESS_STATUS:
        raise HandoffError("Refusing to POST: status is not draft")
    data = json.dumps(payload).encode("utf-8")
    request = urllib.request.Request(
        posts_collection_url(base_url),
        data=data,
        headers={
            "Authorization": basic_auth_header(username, password),
            "Accept": "application/json",
            "Content-Type": "application/json",
        },
        method="POST",
    )
    open_fn = opener or urlopen
    try:
        with open_fn(request, timeout=30) as response:
            body = response.read().decode("utf-8")
    except urllib.error.URLError as exc:
        raise HandoffError("WordPress POST failed (network or HTTP error)") from exc
    return json.loads(body)


def append_handoff_block(path: Path, wp_post: Mapping[str, Any]) -> None:
    post_id = wp_post.get("id")
    slug = wp_post.get("slug") or ""
    link = wp_post.get("link") or ""
    edit_url = ""
    if isinstance(link, str) and post_id:
        # wp-admin edit URL from site origin
        origin = urllib.parse.urlsplit(link)
        edit_url = f"{origin.scheme}://{origin.netloc}/wp-admin/post.php?post={post_id}&action=edit"
    created_at = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    block = (
        f"\n{HANDOFF_HEADING}\n"
        f"- wordpress_post_id: {post_id}\n"
        f"- wordpress_status: {WORDPRESS_STATUS}\n"
        f"- wordpress_edit_url: {edit_url}\n"
        f"- wordpress_slug: {slug}\n"
        f"- created_at: {created_at}\n"
    )
    text = path.read_text(encoding="utf-8")
    if HANDOFF_HEADING in text:
        raise HandoffError("File already contains a WordPress handoff block; refusing to append")
    path.write_text(text.rstrip() + block, encoding="utf-8")


def print_dry_run(
    source: Path,
    article: ParsedArticle,
    payload: WordPressPayload,
    taxonomy_path: Path,
) -> None:
    included, excluded = included_excluded(article)
    data = payload.to_dict()
    preview = sanitize_preview(data)
    print("DRY RUN — no network requests, nothing written to WordPress or the source file.")
    print(f"source: {source}")
    print(f"taxonomy: {taxonomy_path}")
    print(f"included sections: {', '.join(included)}")
    print(f"excluded sections: {', '.join(excluded) if excluded else '(none named)'}")
    print(f"resolved category IDs: {data['categories']}")
    print(f"resolved tag IDs: {data['tags']}")
    print(f"status: {data['status']}")
    if data["status"] != WORDPRESS_STATUS:
        raise HandoffError("Dry-run payload status is not draft")
    print("payload preview (no credentials):")
    print(json.dumps(preview, indent=2, ensure_ascii=False))


def run(
    source: Path,
    repo_root: Path,
    taxonomy_path: Path,
    apply: bool,
    opener: Callable[..., Any] | None = None,
) -> int:
    assert_draft_only_env()
    resolved = assert_eligible_source(source, repo_root)
    article = parse_article(resolved.read_text(encoding="utf-8"))
    if article.wordpress_post_id:
        raise HandoffError(
            f"wordpress_post_id {article.wordpress_post_id} already present; refusing to create another draft"
        )
    taxonomy = load_taxonomy(taxonomy_path)
    category_ids, tag_ids = resolve_taxonomy(article, taxonomy)
    payload = build_payload(article, category_ids, tag_ids)
    body = payload.to_dict()
    if apply:
        load_dotenv(repo_root)
        base = (os.environ.get("WP_BASE_URL") or "").strip()
        user = (os.environ.get("WP_USERNAME") or "").strip()
        password = (os.environ.get("WP_APPLICATION_PASSWORD") or "").strip()
        if not base or not user or not password:
            raise HandoffError("WP_BASE_URL, WP_USERNAME, and WP_APPLICATION_PASSWORD are required for --apply")
        if not base.lower().startswith("https://"):
            raise HandoffError("WP_BASE_URL must use HTTPS")
        existing = find_posts_by_slug(base, user, password, payload.slug, opener=opener)
        if existing:
            raise HandoffError(
                f"A WordPress post already exists for slug {payload.slug!r}; v1 will not overwrite"
            )
        created = create_draft_post(base, user, password, body, opener=opener)
        if created.get("status") != WORDPRESS_STATUS:
            raise HandoffError("WordPress returned a non-draft status; check the user role and do not publish")
        append_handoff_block(resolved, created)
        print(f"Created WordPress draft id={created.get('id')} slug={created.get('slug')}")
        return 0
    print_dry_run(resolved, article, payload, taxonomy_path)
    return 0


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Create a WordPress Draft from a ready-for-review markdown file. Default: dry-run."
    )
    parser.add_argument("source", type=Path, help="Path to a file under content/ready-for-review/")
    parser.add_argument(
        "--repo-root",
        type=Path,
        default=None,
        help="Repository root (defaults to the parent of this package)",
    )
    parser.add_argument(
        "--taxonomy",
        type=Path,
        default=None,
        help="JSON category/tag map (default: config/wordpress-taxonomy.json or WP_TAXONOMY_CONFIG)",
    )
    parser.add_argument(
        "--apply",
        action="store_true",
        help="POST a draft to WordPress (requires .env). Default is dry-run with no network.",
    )
    return parser


def main(argv: list[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)
    root = repo_root_from(args.repo_root)
    taxonomy = args.taxonomy
    if taxonomy is None:
        env_tax = os.environ.get("WP_TAXONOMY_CONFIG")
        taxonomy = Path(env_tax) if env_tax else root / "config" / "wordpress-taxonomy.json"
    if not taxonomy.is_absolute():
        taxonomy = (root / taxonomy).resolve()
    try:
        return run(args.source, root, taxonomy, apply=bool(args.apply))
    except HandoffError as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    sys.exit(main())
