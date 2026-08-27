from __future__ import annotations

import io
import json
import os
import shutil
import sys
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch
from contextlib import redirect_stderr, redirect_stdout


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


FAKE_PASSWORD = "not-a-real-secret-UNITTEST-ONLY-xyz"


class HardenReviewTests(unittest.TestCase):
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

    def test_append_writeback_preserves_article_body(self) -> None:
        before = self.source.read_text(encoding="utf-8")
        body_before = handoff.parse_article(before).full_article_markdown
        handoff.append_handoff_block(
            self.source,
            {
                "id": 321,
                "slug": "fixture-handoff-article",
                "link": "https://example.invalid/?p=321",
            },
        )
        after = self.source.read_text(encoding="utf-8")
        parsed = handoff.parse_article(after)
        self.assertEqual(parsed.full_article_markdown, body_before)
        self.assertEqual(parsed.seo_title, "Fixture SEO title for WordPress")
        self.assertEqual(parsed.excerpt.strip(), "A short public excerpt for listings.")
        self.assertIn("## WordPress handoff", after)
        self.assertIn("wordpress_post_id: 321", after)
        self.assertTrue(before.rstrip() in after)

    def test_mocked_apply_refuses_when_slug_duplicate_exists(self) -> None:
        posted = {"called": False}

        def opener(request, timeout=30):
            method = request.get_method()
            if method == "POST":
                posted["called"] = True
                raise AssertionError("POST must not run when slug already exists")

            class _Resp:
                def read(self):
                    return json.dumps([{"id": 77, "slug": "fixture-handoff-article"}]).encode()

                def __enter__(self):
                    return self

                def __exit__(self, *args):
                    return False

            return _Resp()

        env = {
            "WP_BASE_URL": "https://example.invalid",
            "WP_USERNAME": "handoff-bot",
            "WP_APPLICATION_PASSWORD": FAKE_PASSWORD,
        }
        with patch.dict(os.environ, env, clear=False):
            with self.assertRaises(handoff.HandoffError) as ctx:
                handoff.run(self.source, self.tmp, self.taxonomy, apply=True, opener=opener)
        self.assertIn("already exists", str(ctx.exception))
        self.assertIn("will not overwrite", str(ctx.exception))
        self.assertFalse(posted["called"])
        self.assertNotIn(FAKE_PASSWORD, str(ctx.exception))

    def test_https_required_for_live_mode(self) -> None:
        def opener(request, timeout=30):
            raise AssertionError("network must not run when URL is not HTTPS")

        env = {
            "WP_BASE_URL": "http://example.invalid",
            "WP_USERNAME": "handoff-bot",
            "WP_APPLICATION_PASSWORD": FAKE_PASSWORD,
        }
        with patch.dict(os.environ, env, clear=False):
            with self.assertRaises(handoff.HandoffError) as ctx:
                handoff.run(self.source, self.tmp, self.taxonomy, apply=True, opener=opener)
        self.assertIn("HTTPS", str(ctx.exception))
        self.assertNotIn(FAKE_PASSWORD, str(ctx.exception))

    def test_source_under_content_drafts_is_rejected(self) -> None:
        draft = self.tmp / "content" / "drafts" / "note.md"
        draft.parent.mkdir(parents=True)
        draft.write_text(VALID_MD, encoding="utf-8")
        with self.assertRaises(handoff.HandoffError) as ctx:
            handoff.assert_eligible_source(draft, self.tmp)
        self.assertIn("ready-for-review", str(ctx.exception))

    def test_argparse_rejects_extra_source_and_publish_flags(self) -> None:
        parser = handoff.build_parser()
        stderr = io.StringIO()
        with self.assertRaises(SystemExit):
            with redirect_stderr(stderr):
                parser.parse_args(["one.md", "two.md"])
        extra_err = stderr.getvalue()
        self.assertTrue(extra_err)
        self.assertNotIn(FAKE_PASSWORD, extra_err)

        stderr2 = io.StringIO()
        with self.assertRaises(SystemExit):
            with redirect_stderr(stderr2):
                parser.parse_args(["one.md", "--publish"])
        self.assertIn("unrecognized arguments", stderr2.getvalue())

        stderr3 = io.StringIO()
        with self.assertRaises(SystemExit):
            with redirect_stderr(stderr3):
                parser.parse_args(["one.md", "--status", "publish"])
        self.assertIn("unrecognized arguments", stderr3.getvalue())

    def test_credentials_do_not_appear_in_dry_run_or_error_output(self) -> None:
        env = {"WP_APPLICATION_PASSWORD": FAKE_PASSWORD, "WP_USERNAME": "handoff-bot"}
        stdout = io.StringIO()
        with patch.dict(os.environ, env, clear=False):
            with redirect_stdout(stdout):
                code = handoff.run(self.source, self.tmp, self.taxonomy, apply=False)
        self.assertEqual(code, 0)
        out = stdout.getvalue()
        self.assertNotIn(FAKE_PASSWORD, out)
        self.assertNotIn("handoff-bot", out)
        self.assertIn("DRY RUN", out)

        stderr = io.StringIO()
        stdout2 = io.StringIO()
        with patch.dict(
            os.environ,
            {
                "WP_BASE_URL": "http://example.invalid",
                "WP_USERNAME": "handoff-bot",
                "WP_APPLICATION_PASSWORD": FAKE_PASSWORD,
            },
            clear=False,
        ):
            with redirect_stdout(stdout2):
                with redirect_stderr(stderr):
                    rc = handoff.main(
                        [
                            str(self.source),
                            "--repo-root",
                            str(self.tmp),
                            "--taxonomy",
                            str(self.taxonomy),
                            "--apply",
                        ]
                    )
        self.assertEqual(rc, 1)
        combined = stdout2.getvalue() + stderr.getvalue()
        self.assertNotIn(FAKE_PASSWORD, combined)
        self.assertIn("HTTPS", combined)

    def test_wp_post_status_publish_in_dotenv_is_rejected(self) -> None:
        (self.tmp / ".env").write_text(
            "WP_POST_STATUS=publish\n"
            f"WP_APPLICATION_PASSWORD={FAKE_PASSWORD}\n"
            "WP_BASE_URL=https://example.invalid\n",
            encoding="utf-8",
        )
        env_minus = {k: v for k, v in os.environ.items() if k != "WP_POST_STATUS"}
        with patch.dict(os.environ, env_minus, clear=True):
            def opener(request, timeout=30):
                raise AssertionError("network must not run when WP_POST_STATUS is publish")

            with self.assertRaises(handoff.HandoffError) as ctx:
                handoff.run(
                    self.source, self.tmp, self.taxonomy, apply=True, opener=opener
                )
        self.assertIn("WP_POST_STATUS", str(ctx.exception))
        self.assertIn("non-draft", str(ctx.exception))
        self.assertNotIn(FAKE_PASSWORD, str(ctx.exception))


if __name__ == "__main__":
    unittest.main()
