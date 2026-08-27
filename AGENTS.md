# Agent operating rules

These rules bind future Cursor / Grok Bot (and similar) agents working in this repo. Humans may override in writing. Agents may not override themselves.

## Mission

Produce **reviewable research and drafts** that follow the SEO operating system. Do **not** publish. Do **not** optimize for word count or keyword density at the expense of EDITORIAL_RULES.md.

## Before any writing

1. Read README.md, CONTENT_STRATEGY.md, EDITORIAL_RULES.md, and the relevant cluster in CONTENT_CLUSTERS.md.
2. **Research before writing.** If the task is topic discovery, stop at scored candidates. If the task is an article, finish sources and the verification table before the full article body.
3. Use ARTICLE_TEMPLATE.md for drafts and TOPIC_SCORING.md for candidates.
4. Prefer primary sources. Record URLs and dates.

## One task at a time

- One **research** assignment **or** one **article draft** per run — not a cluster of five posts.
- Topic discovery may return a **list of scored ideas**, not drafts.
- Do not start the next article because “there was time left.”

## Do not publish

- No CMS uploads, no live site edits, no “just put it on the blog.”
- Output is files in this repo (or a clearly labeled draft the human asked for).
- Future Grok Bot work must produce a **reviewable draft**, never a published article.

## Do not invent facts

- No fake vendors, quotes, prices, awards, reviews, locations, or availability.
- Sweeter Teagether facts come from the live site or an approved internal brief only.
- Local vendor claims: cite the vendor’s site (or another primary source) and the date checked.
- If an important fact cannot be verified, **stop**, write it under **Blockers / stop notes**, and report to the human. Do not smooth over the gap.

## Do not overwrite

- Never overwrite existing drafts, research, or published copies without **explicit** human approval in that conversation or ticket.
- Prefer new files (`…-v2.md`) if a revision is requested without “replace the old file.”

## Keep states separate

| State | Directory | Agent may |
| --- | --- | --- |
| Research | `content/research/` | Create new notes |
| Draft | `content/drafts/` | Create new drafts from template |
| Ready for review | `content/ready-for-review/` | Only if a human asked to move a file there |
| Published | Not in-agent | Never |

Do not mix a research dump and a finished article in one file unless the template’s sections are clearly separated (the article template already does this).

## Naming

- Research: `content/research/YYYY-MM-DD-short-topic.md`
- Draft: `content/drafts/YYYY-MM-DD-slug-draft.md`
- Score batches: `content/research/YYYY-MM-DD-topic-scores.md`

## Scope limits

- Do not run keyword research or write articles unless the user asked for that stage.
- Do not expand into social posts, ads, or email unless asked.
- Do not scrape or store personal data from private groups beyond what a public page already shows.

## Done means

A human can open the file, see sources, see what is unverified, and accept or reject without guessing what the agent made up.
