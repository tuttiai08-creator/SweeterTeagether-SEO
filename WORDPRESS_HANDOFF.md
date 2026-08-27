# WordPress draft handoff (v1)

Create a **WordPress blog post Draft** from a verified markdown file without copy/paste. This repo remains the source of truth (`AGENTS.md`). **Publication stays a human action in wp-admin.**

## Purpose

Move an owner-approved article from `content/ready-for-review/` into WordPress as `status=draft` via the REST API, using a revocable Application Password on a low-privilege user.

v1 does **not**: publish, update existing posts, upload featured images, write Elementor JSON, or set SEO-plugin meta.

## Eligibility

**Only** files under `content/ready-for-review/` are eligible.

Never send `content/research/`, `content/drafts/`, or any other path to WordPress.

The approved CLI is `python3 scripts/wp_create_draft.py <file.md>`. Default mode is **dry-run** (no network).

## Architecture

```
ready-for-review markdown
  → parse ARTICLE_TEMPLATE.md sections
  → Markdown (Full article only) → HTML
  → map category/tag names → WordPress term IDs
  → POST /wp-json/wp/v2/posts   (HTTPS, Application Password)
  → write wordpress_post_id back into the same markdown file
```

- Endpoint: `{WP_BASE_URL}/wp-json/wp/v2/posts`
- Method: `POST`
- Body: JSON (`title`, `content`, `excerpt`, `slug`, `categories`, `tags`, `status`)
- **`status` is hard-coded to `draft`.** There is no publish flag.

Elementor Pro does not replace this path. v1 writes ordinary `post_content`. The single-post Theme Builder template should include a **Post Content** widget. Do not send `_elementor_data`.

## Authentication

- WordPress **Application Password** (not the owner’s login password)
- HTTP Basic: `WP_USERNAME` + `WP_APPLICATION_PASSWORD`
- HTTPS only
- Secrets live in `.env` (gitignored). Never commit, print, or paste them into tickets or chat.
- `.env` is loaded **before** `WP_POST_STATUS` is checked. A non-draft value in `.env` aborts before any live-path work.

## Dedicated WordPress user

Use a **dedicated** user (not the owner’s daily account), preferably **Author** or a custom role that can create posts but **cannot publish**. The script still forces `draft` even if the user could publish.

## Forced draft / no publish

- Script constant: `status = "draft"`
- No CLI option for `publish`, `pending`, or other statuses
- If `WP_POST_STATUS` is set to anything other than `draft`, the script exits without posting
- Agents must not publish from wp-admin either; owner publishes after review

## Duplicate / idempotency (v1)

1. If the markdown already contains `wordpress_post_id` with a positive integer, **refuse** (no POST, no overwrite).
2. On `--apply` only: `GET /wp/v2/posts?slug={slug}&status=draft,pending,publish,private,future`. If any post matches, **refuse**. Do not `PUT`/`PATCH`.
3. Dry-run performs **no** slug lookup (no network).

v1 never overwrites an existing WordPress post.

## Field map

| Template section | WordPress field |
| --- | --- |
| `## SEO title` | `title` |
| `## Full article` | `content` (HTML) |
| `## Excerpt` | `excerpt` |
| `## Slug` | `slug` |
| `**Category:**` | `categories` (IDs from `config/wordpress-taxonomy.json`) |
| `**Tags:**` | `tags` (IDs from the same file) |
| *(script)* | `status`: `draft` |

**Not uploaded:** target query, search intent, audience, why-this-topic, sources, outline, meta description, internal-link table, CTA *metadata* (the CTA sentence inside Full article *is* part of the body), featured-image brief, verification table, blockers, agent instructions.

Fail closed if required sections are missing or if any category/tag lacks a **positive integer** ID in the taxonomy file (`null` / placeholders fail).

## Write-back (after a successful `--apply` only)

Append to the same markdown file (do not rewrite the article body):

```markdown
## WordPress handoff
- wordpress_post_id:
- wordpress_status: draft
- wordpress_edit_url:
- wordpress_slug:
- created_at:
```

Dry-run does not write this block.

## First-test procedure

Do this only when the owner has filled `.env` and real term IDs, and has **explicitly** asked to run `--apply`.

1. `GET {WP_BASE_URL}/wp-json/` over HTTPS.
2. `GET /wp-json/wp/v2/users/me` with the Application Password.
3. `--apply` a **throwaway** fixture titled clearly as TEST, unique slug, then **delete** that draft in wp-admin.
4. Re-run against a file that already has `wordpress_post_id` and confirm refusal.
5. Only then `--apply` a real `content/ready-for-review/` article.

Until then: dry-run only.

## Manual WordPress verification (first real draft)

- Posts → Drafts: exists, **Draft**, not on the public site
- Title, slug, excerpt, category, tags match the markdown
- Body is the Full article only (no research dump or verification table)
- Preview uses the theme / Elementor single template around `post_content`
- No Elementor builder data required to read the draft
- Edit URL recorded in the markdown handoff block

## Commands

```bash
# Default: parse + preview, no network
python3 scripts/wp_create_draft.py content/ready-for-review/YOUR-FILE.md

python3 -m unittest discover -s tests -v
```

`--apply` is the eventual live POST. Do not use it unless the owner requested a live test and `.env` is configured. This milestone does not run `--apply`.
