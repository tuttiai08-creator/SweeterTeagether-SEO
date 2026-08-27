# Sweeter Teagether SEO Operating System

This repository is the **content operating system** for Sweeter Teagether, a Dallas-area mobile boba and dessert catering business.

The job of this system is not to publish a blog for its own sake. It exists to:

1. Attract people who are actively planning celebrations in Dallas / DFW.
2. Send them to [sweeterteagether.com](https://sweeterteagether.com).
3. Introduce the mobile boba / dessert cart in a way that feels natural and useful.
4. Drive event inquiries.

Do **not** treat traffic volume as success. An article that ranks for an unrelated query is a miss if the reader is unlikely to book a cart.

## What this repo is (and is not)

**This is:** rules, strategy, cluster structure, scoring, and templates so Cursor / Grok Bot agents can research and draft consistently.

**This is not:** a keyword research dump, an article factory, or a live CMS. No articles are written here until a research task is explicitly assigned.

## Business context

Sweeter Teagether serves events in the Dallas / DFW area. Priority occasions include:

- Weddings (including South Asian weddings)
- Bridal showers
- Baby showers
- Birthdays
- Corporate events
- Graduations
- Engagement parties and other celebrations

The offer is a **mobile boba and dessert cart** for events — not a walk-in shop article strategy.

## Overall workflow

Work moves in one direction. Agents do not skip stages or publish.

```
Topic candidate
    → score (TOPIC_SCORING.md)
    → assign to a cluster (CONTENT_CLUSTERS.md)
    → research (one topic at a time)
    → draft using ARTICLE_TEMPLATE.md
    → human review
    → approved publish (outside this repo / by a human)
```

| Stage | Where it lives | Who may advance it |
| --- | --- | --- |
| Research notes | `content/research/` | Agent, then human check |
| Draft (not public) | `content/drafts/` | Agent |
| Ready for review | `content/ready-for-review/` | Human marks as ready |
| Published | CMS / site — not automatic | Human only |

## How to use these files

| File | Use it for |
| --- | --- |
| [CONTENT_STRATEGY.md](CONTENT_STRATEGY.md) | Whether a topic belongs in the system at all |
| [CONTENT_CLUSTERS.md](CONTENT_CLUSTERS.md) | Where a topic sits and what “good” looks like |
| [EDITORIAL_RULES.md](EDITORIAL_RULES.md) | What may and may not be written |
| [ARTICLE_TEMPLATE.md](ARTICLE_TEMPLATE.md) | How every draft is delivered |
| [TOPIC_SCORING.md](TOPIC_SCORING.md) | Ranking future topic ideas (no invented volumes) |
| [AGENTS.md](AGENTS.md) | Operating rules for autonomous content agents |

## Current status

Foundation only. Clusters are structured but **not** filled with article lists. Keyword research and writing have not started.
