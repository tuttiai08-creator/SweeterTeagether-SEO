# Topic scoring

Use this **before** assigning research. Scores are **judgments**, not measurements. **Do not invent search-volume, CPC, or keyword-difficulty numbers.** If a tool later provides real data, paste the figure and the date; never fabricate a stand-in.

## How to score

Rate each dimension **1–5** (1 = weak / poor fit, 5 = strong / clear fit).  
**Opportunity** and **competition** stay qualitative unless verified tool data exists.

Write a one-line note under any score that is a guess.

### Dimensions

| ID | Dimension | 1 means | 5 means |
| --- | --- | --- | --- |
| C | Commercial relevance to Sweeter Teagether | No path to a boba/dessert cart | Searcher is comparing or hiring this kind of service |
| L | Dallas / DFW local intent | National or other-city | Query or need is clearly DFW (or “near me” for this market) |
| E | Event-planning intent | Entertainment, recipes, trivia | Host/planner is making event decisions |
| S | South Asian relevance | Irrelevant | Topic is specifically useful for South Asian weddings/events (use N/A if the cluster is not SA) |
| O | Likely search opportunity | Niche with no evident demand *or* impossible to judge | Clear that people search this *kind* of question (from SERP inspection, not made-up volume) |
| D | Competition / difficulty | Page-one dominated by strong official / huge publishers you cannot match honestly | Room for a specific, better-localized, or better-explained page |
| U | Ability to be genuinely useful | Would be fluff or unverifiable | We can add checklists, local process, cultural clarity, or service education with real sources |
| I | Internal-link potential | Orphan; no cluster fit | Strengthens a hub or connects commercial ↔ planning clusters |
| Q | Likelihood of driving an inquiry | Reader will never book a cart | High overlap with people who hire event F&B in DFW |

**South Asian (S):** If the topic is not in the South Asian cluster and has no SA angle, record **S = N/A** and **do not** average it into the total. Do not boost a generic wedding topic by stuffing an SA keyword.

**Opportunity (O):** Base this on inspecting live SERPs and query wording — e.g. “people ask this in local Facebook groups / the SERP is thin local guides.” If you cannot tell, score **3** and write “unknown demand.” Never write “KD 28” or “1.2k volume” without a cited export.

**Difficulty (D):** Invert intuition: **higher score = easier / more winnable for us**, so it aligns with “higher is better” on the total. A 1 is “we would lose to Wikipedia/Brides/The Knot clones with no unique angle.”

## Total and decision

**When S is a number:**  
`Total = C + L + E + S + O + D + U + I + Q`  
Range: 9–45.

**When S is N/A:**  
`Total = C + L + E + O + D + U + I + Q`  
Range: 8–40.

### Suggested bar (adjust once real topics exist)

These are starting heuristics, not science:

| Result | Typical action |
| --- | --- |
| Strong | Prioritize research (roughly top quartile once you have a batch) |
| Viable | Queue if it fills a cluster hole |
| Weak | Skip unless a human overrides |
| Hard fail | Skip regardless of total |

**Hard fails (any one is enough):**

- C = 1 and Q = 1 (no commercial or inquiry path)
- L = 1 and the piece cannot be localized without lying
- U = 1 (we would have to fabricate or write empty filler)
- Editorial: would require unverifiable vendor roundups as the core of the article

Minimum to enter the cluster log as `idea`: no hard fail, and **C ≥ 3** or **Q ≥ 3**.

## Scorecard (copy per topic)

```markdown
## Topic:

**Working query:**  
**Cluster (proposed):**  
**Intent layer:**  
**Date scored:**  
**Scored by:**  
**Tool data attached?** no / yes (tool, date, metric names only — paste real numbers)

| Dim | Score | Note |
| --- | --- | --- |
| C Commercial |  |  |
| L Local DFW |  |  |
| E Event-planning |  |  |
| S South Asian |  | or N/A |
| O Opportunity |  | no invented volume |
| D Difficulty (high = more winnable) |  |  |
| U Usefulness |  |  |
| I Internal links |  |  |
| Q Inquiry likelihood |  |  |

**Total:**  
**Decision:** research / queue / skip  
**Hard fail?** yes/no — which:
```

## Batch research later

When an agent scores many candidates, output a table: topic, query, total, decision, one-line rationale. Do not write articles in the same task. Do not pretend volumes exist “to make the table look complete.”
