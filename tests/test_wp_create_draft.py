from __future__ import annotations

import json
import shutil
import sys
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

import wordpress_handoff as handoff

FIXTURES = Path(__file__).resolve().parent / "fixtures"
VALID_MD = (FIXTURES / "valid-article.md").read_text(encoding="utf-8")
TAXONOMY_PATH = FIXTURES / "taxonomy.json"


class RepoLayoutTests(unittest.TestCase):
    def setUp(self) -> None:
        self.tmp = Path(tempfile.mkdtemp())
        self.ready = self.tmp / "content" / "ready-for-review"
        self.ready.mkdir(parents=True)
        self.source = self.ready / "valid.md"
        self.source.write_text(VALID_MD, encoding="utf-8")
        self.taxonomy = self.tmp / "taxonomy.json"
        shutil.copy(TAXONOMY_PATH, self.taxonomy)

    def tearDown(self) -> None:
        shutil.rmtree(self.tmp, ignore_errors=True)

    def test_valid_ready_for_review_parses(self) -> None:
        article = handoff.parse_article(VALID_MD)
        self.assertEqual(article.seo_title, "Fixture SEO title for WordPress")
        self.assertEqual(article.slug, "fixture-handoff-article")
        self.assertIn("public body", article.full_article_markdown)
        self.assertEqual(article.category_name, "South Asian weddings")
        self.assertEqual(article.tag_names, ["Dallas/DFW", "reception"])
        self.assertIsNone(article.wordpress_post_id)

    def test_file_outside_ready_for_review_rejected(self) -> None:
        other = self.tmp / "content" / "research" / "note.md"
        other.parent.mkdir(parents=True)
        other.write_text(VALID_MD, encoding="utf-8")
        with self.assertRaises(handoff.HandoffError) as ctx:
            handoff.assert_eligible_source(other, self.tmp)
        self.assertIn("ready-for-review", str(ctx.exception))

    def test_missing_full_article_fails(self) -> None:
        broken = VALID_MD.replace("## Full article", "## Not the article")
        with self.assertRaises(handoff.HandoffError) as ctx:
            handoff.parse_article(broken)
        self.assertIn("Full article", str(ctx.exception))

    def test_missing_taxonomy_mapping_fails(self) -> None:
        article = handoff.parse_article(VALID_MD)
        empty = {"categories": {}, "tags": {}}
        with self.assertRaises(handoff.HandoffError) as ctx:
            handoff.resolve_taxonomy(article, empty)
        self.assertIn("No category mapping", str(ctx.exception))

    def test_missing_unmapped_tag_fails(self) -> None:
        article = handoff.parse_article(VALID_MD)
        partial = {
            "categories": {"South Asian weddings": 9001},
            "tags": {"Dallas/DFW": 9002},
        }
        with self.assertRaises(handoff.HandoffError) as ctx:
            handoff.resolve_taxonomy(article, partial)
        self.assertIn("No tag mapping", str(ctx.exception))
        article = handoff.parse_article(VALID_MD)
        placeholders = {
            "categories": {"South Asian weddings": None},
            "tags": {"Dallas/DFW": 9002, "reception": 9003},
        }
        with self.assertRaises(handoff.HandoffError):
            handoff.resolve_taxonomy(article, placeholders)

    def test_existing_wordpress_post_id_blocks_creation(self) -> None:
        text = VALID_MD + "\n## WordPress handoff\n- wordpress_post_id: 444\n"
        self.source.write_text(text, encoding="utf-8")
        with self.assertRaises(handoff.HandoffError) as ctx:
            handoff.run(self.source, self.tmp, self.taxonomy, apply=False)
        self.assertIn("wordpress_post_id", str(ctx.exception))

    def test_status_can_only_be_draft(self) -> None:
        article = handoff.parse_article(VALID_MD)
        cats, tags = handoff.resolve_taxonomy(
            article, json.loads(self.taxonomy.read_text(encoding="utf-8"))
        )
        payload = handoff.build_payload(article, cats, tags)
        self.assertEqual(payload.status, "draft")
        self.assertEqual(payload.to_dict()["status"], "draft")
        payload.status = "publish"
        with self.assertRaises(handoff.HandoffError):
            payload.to_dict()

    def test_research_sections_not_in_wordpress_body(self) -> None:
        article = handoff.parse_article(VALID_MD)
        html = handoff.markdown_to_html(article.full_article_markdown)
        for token in (
            "SECRET_RESEARCH_TOKEN",
            "SECRET_SOURCE_TOKEN",
            "SECRET_VERIFY_TOKEN",
            "SECRET_BLOCKER_TOKEN",
            "SECRET_INTERNAL_LINK_TOKEN",
            "SECRET_IMAGE_BRIEF_TOKEN",
            "secret query not for wordpress",
        ):
            self.assertNotIn(token, html)
            self.assertNotIn(token, article.full_article_markdown)
        self.assertIn("public body", html)
        payload = handoff.build_payload(article, [9001], [9002, 9003])
        blob = json.dumps(payload.to_dict())
        self.assertNotIn("SECRET_RESEARCH_TOKEN", blob)

    def test_dry_run_performs_no_network_call(self) -> None:
        with patch.object(handoff, "urlopen", side_effect=AssertionError("network")):
            with patch("urllib.request.urlopen", side_effect=AssertionError("network")):
                code = handoff.run(self.source, self.tmp, self.taxonomy, apply=False)
        self.assertEqual(code, 0)

    def test_non_draft_env_refused(self) -> None:
        with patch.dict("os.environ", {"WP_POST_STATUS": "publish"}):
            with self.assertRaises(handoff.HandoffError):
                handoff.assert_draft_only_env()


class LivePathGuardTests(unittest.TestCase):
    def test_create_draft_refuses_non_draft_payload(self) -> None:
        with self.assertRaises(handoff.HandoffError):
            handoff.create_draft_post(
                "https://example.invalid",
                "user",
                "pass",
                {"title": "x", "status": "publish"},
            )


class SampleReadyForReviewTests(unittest.TestCase):
    def test_sample_article_body_excludes_research(self) -> None:
        path = ROOT / "content/ready-for-review/2026-08-27-post-south-asian-wedding-dallas-draft.md"
        article = handoff.parse_article(path.read_text(encoding="utf-8"))
        html = handoff.markdown_to_html(article.full_article_markdown)
        self.assertEqual(article.slug, "post-south-asian-wedding-dallas")
        self.assertNotIn("Factual claims requiring verification", html)
        self.assertNotIn("Blockers / stop notes", html)
        self.assertIn("decision map", html.lower())

    def test_default_taxonomy_placeholders_fail_closed(self) -> None:
        path = ROOT / "content/ready-for-review/2026-08-27-post-south-asian-wedding-dallas-draft.md"
        article = handoff.parse_article(path.read_text(encoding="utf-8"))
        taxonomy = handoff.load_taxonomy(ROOT / "config" / "wordpress-taxonomy.json")
        with self.assertRaises(handoff.HandoffError):
            handoff.resolve_taxonomy(article, taxonomy)


if __name__ == "__main__":
    unittest.main()
