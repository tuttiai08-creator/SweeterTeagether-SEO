# Topic discovery batch — 2026-08-27

**Status:** research only. **No topic in this file has been approved for drafting.**  
**Do not draft articles from this batch until a human explicitly approves a topic.**

---

## Research date

Thursday, 27 August 2026 (America/Chicago).

SERP checks and live-site fetches were performed the same day.

## Research method

- **SERP-only qualitative research** (live search results + representative page fetches).
- Source-of-truth files used (read from `main`, not modified): `AGENTS.md`, `BUSINESS_BRIEF.md`, `CONTENT_STRATEGY.md`, `CONTENT_CLUSTERS.md`, `TOPIC_SCORING.md`, `EDITORIAL_RULES.md`.
- Live site checked as a fact source: [sweeterteagether.com](https://sweeterteagether.com) (Home, `/menu`, `/about`, `/contact`).
- **No keyword-tool data.** Do not invent search volume, CPC, traffic estimates, keyword difficulty, or other keyword-tool metrics.
- If demand could not be judged from SERP composition, Opportunity (O) is **3** with note “unknown demand,” per `TOPIC_SCORING.md`.
- Competitor / venue operational claims are used only when verified on that business’s own site (URL + date). Directory listings and search snippets are labeled unverified.
- Geography: Dallas–Fort Worth (DFW) only, per `BUSINESS_BRIEF.md`. Named suburbs are not treated as Sweeter Teagether service areas.
- Ads / Maps packs were **not** visible in the search tooling used. Local-service queries of this type commonly trigger them; that is unverified here.

## Priority clusters searched

First discovery pass, in the order required by `BUSINESS_BRIEF.md`:

1. South Asian weddings in Dallas/DFW
2. Dallas/DFW weddings (`Dallas weddings` cluster)
3. Direct boba / dessert catering

Other defined clusters (bridal showers, baby showers, birthdays, corporate events, graduations, engagement parties) were **not** filled as first-pass cluster logs. Shower-only and corporate-only boba URLs were inspected during the direct-catering SERP pass, then dropped from this batch as out of first-pass scope.

## Scoring rules used

Copied from `TOPIC_SCORING.md` (judgments, not measurements). Dimensions 1–5:

| ID | Dimension | Notes |
| --- | --- | --- |
| C | Commercial relevance to Sweeter Teagether | |
| L | Dallas / DFW local intent | |
| E | Event-planning intent | |
| S | South Asian relevance | **N/A** and omitted from the total when the topic is not in the South Asian cluster and has no SA angle |
| O | Likely search opportunity | Qualitative SERP inspection only |
| D | Competition / difficulty | **Higher = more winnable** |
| U | Ability to be genuinely useful | |
| I | Internal-link potential | |
| Q | Likelihood of driving an inquiry | |

**When S is a number:** `Total = C+L+E+S+O+D+U+I+Q` (range 9–45).  
**When S is N/A:** `Total = C+L+E+O+D+U+I+Q` (range 8–40).

Hard fails (any one is enough to skip): C=1 and Q=1; L=1 and the piece cannot be localized without lying; U=1; editorial core would be an unverifiable vendor roundup.

Minimum to enter as `idea`: no hard fail, and **C ≥ 3 or Q ≥ 3**.

**Rank in this file** is unchanged from the 2026-08-27 discovery delivery: by total as a share of its max (45 vs 40), then by commercial/inquiry fit.

**Scored by:** Sweeter Teagether SEO Research agent.  
**Tool data attached?** no.

---

## Ranked candidates

| Rank | Topic | Cluster | Intent | Content type | Total | Decision | CTA | Hard-fail now? |
| ---: | --- | --- | --- | --- | ---: | --- | --- | --- |
| 1 | Add a dessert/boba/fruit-chaat cart beside an existing DFW South Asian caterer | South Asian weddings | Commercial + logistics | FAQ / process | 40/45 | research | yes | no, if it stays process |
| 2 | Mehndi hospitality: drinks and snacks while henna is drying | South Asian weddings | SA event-planning | Planning guide + hands-free checklist | 40/45 | research | yes | no, if not a caterer list |
| 3 | Dessert carts vs dessert tables at Dallas weddings (cake can still belong) | Dallas weddings | Split hire + planning | Decision guide | 35/40 | research | yes | no, if not “best carts” |
| 4 | Outside dessert/beverage carts: open-vendor vs exclusive DFW venues | Dallas weddings | Venue-policy planning | Process checklist | 35/40 | research | yes | no, if not a venue roundup |
| 5 | Feeding a DFW sangeet without killing the performances | South Asian weddings | SA event-planning | Timing explainer | 39/45 | research | yes | no, if not a caterer list |
| 6 | Pakistani wedding weekend in DFW: mehndi vs baraat dinner vs walima hospitality | South Asian weddings | SA event-planning | Explainer + short checklist | 39/45 | research | yes (mehndi/walima); no for nikah | no, if not a vendor list |
| 7 | A boba bar for DFW weddings | Direct catering | Direct hire | Event-fit explainer | 34/40 | research | yes | no, if not “best wedding boba” |
| 8 | Late-night bites at Dallas weddings | Dallas weddings | Event-planning | Timeline / format explainer | 34/40 | research | yes | no, if not a vendor list |
| 9 | Late-night after a DFW South Asian reception or walima | South Asian weddings | SA guest-experience | Explainer / FAQ | 38/45 | research | yes | no, if not a vendor list |
| 10 | Hire a mobile boba cart in Dallas–Fort Worth | Direct catering | Direct hire | Service explainer | 33/40 | research | yes | no, if not priced packages or a roundup |
| 11 | Mobile dessert cart catering in Dallas (not a truck, not a bakery) | Direct catering | Direct hire | Format comparison | 33/40 | research | yes, if it teaches format | no, if not a best-of list |
| 12 | What to serve at which event: DFW South Asian weekend hospitality map | South Asian weddings | SA planning | Planning guide | 37/45 | queue | yes | **fails if it becomes a venue/vendor list** |
| 13 | Cocktail hour at Dallas weddings when photos run long | Dallas weddings | Event-planning | Timeline piece | 32/40 | queue | yes | no, if it stays local and not generic ideas |
| 14 | Fruit chaat catering for DFW parties (dessert cart, not a live chaat station) | Direct catering | Mixed / clarifying | Comparison-education | 28/40 | queue | weak unless they already want fruit chaat | **fails if it ranks into savory Indian catering** |
| 15 | Ice cream cookie skillet catering for DFW events | Direct catering | Direct hire, thin demand | Service explainer | 26/40 | queue | weak as a head term | no, if we don’t invent a skillet SERP that isn’t there |

---

## Dimension scores

| Rank | C | L | E | S | O | D | U | I | Q | O note |
| ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | 5 | 5 | 4 | 4 | 3 | 4 | 5 | 5 | 5 | Unknown as a typed query; high usefulness to the actual buyer |
| 2 | 4 | 4 | 5 | 5 | 4 | 4 | 5 | 5 | 4 | People search mehndi food/planning; DFW hospitality pages are empty |
| 3 | 5 | 4 | 4 | N/A | 4 | 3 | 5 | 5 | 5 | Hire + cake-alternative SERPs exist; vendor homepages dominate |
| 4 | 4 | 5 | 5 | N/A | 3 | 4 | 5 | 5 | 4 | Unknown demand; venue pages answer it only for themselves |
| 5 | 4 | 4 | 5 | 5 | 4 | 3 | 5 | 5 | 4 | Sangeet food/planning is a real question type; DFW is caterer SEO |
| 6 | 4 | 4 | 5 | 5 | 4 | 4 | 5 | 4 | 4 | Pakistani vs Indian confusion is searched; local is venue + decor |
| 7 | 5 | 5 | 3 | N/A | 4 | 3 | 4 | 5 | 5 | Wedding-boba hire SERP exists (Boba Plug page is the clearest) |
| 8 | 4 | 4 | 5 | N/A | 4 | 3 | 5 | 5 | 4 | Local mag already calls late-night a Dallas staple; independent copy is thin |
| 9 | 4 | 4 | 5 | 5 | 3 | 4 | 4 | 5 | 4 | Generic late-night is known; SA-specific demand unknown |
| 10 | 5 | 5 | 3 | N/A | 4 | 2 | 4 | 5 | 5 | Dense hire SERP; sweeterteagether.com did not appear |
| 11 | 5 | 5 | 3 | N/A | 4 | 2 | 5 | 5 | 4 | Head term is ice-cream trucks + luxury snack carts |
| 12 | 4 | 5 | 5 | 4 | 4 | 3 | 4 | 5 | 3 | DFW Indian/SA wedding planning is searched; ranking pages are thin lists |
| 13 | 4 | 4 | 5 | N/A | 3 | 4 | 4 | 4 | 4 | Unknown demand; cocktail hour is caterer-owned |
| 14 | 4 | 4 | 3 | N/A | 3 | 3 | 4 | 4 | 3 | Fruit-chaat cart query has no dedicated DFW hire page |
| 15 | 4 | 3 | 2 | N/A | 2 | 5 | 3 | 4 | 3 | No DFW skillet-cart hire SERP found; uniqueness ≠ demand |

---

## Top 5 recommendations

1. Cart beside an existing DFW South Asian caterer
2. Mehndi hospitality while henna is drying
3. Dessert carts vs tables at Dallas weddings
4. Open-vendor vs exclusive venue rules for a dessert/drink cart
5. Sangeet food timing (stations in the performance gaps)

**Why these five are strongest**

They share the same pattern: live SERPs prove people already ask the question, independent DFW answers are missing or are sales pages, and the cart is a natural add-on rather than fake “we are the wedding caterer” positioning. 1, 2, and 5 also honor the brief’s first-pass order (South Asian weddings first) without flattening rituals. 3 and 4 are the Dallas-wedding spine that every later commercial page has to sit on (format + whether the venue even allows the cart).

“Hire a mobile boba cart” was left out of the top 5 even though commercial intent is highest. The hire SERP is already packed with specialist pages, Sweeter Teagether is invisible on it, and the public site still cannot answer guest min, duration, power, or attended vs drop-off. That page is research-worthy, but it will stay thin until those owner facts exist.

---

## Candidate notes (commercial relevance, SERP, CTA, blockers)

### 1. Cart beside an existing DFW South Asian caterer

- **Working query inspected:** `Indian wedding vendors Dallas Fort Worth` plus outside-catering language on fetched venue pages.
- **Related:** `South Asian wedding Dallas`; `dessert station Indian wedding Dallas`; `boba bar wedding Dallas` (generic, not SA).
- Sweeter Teagether is not the shaadi kitchen. Families already booking a cultural caterer still need a specialty station.
- **SERP (2026-08-27):** Maharani / directories; venue FAQs. Dallas Palms, Penrose House, and Knotting Hill Place state open/outside catering **on their own sites**. Generic boba wedding SERP (The Boba Plug, Fat Straws, Ellie & Juice) has no mehndi/sangeet/walima frame.
- **CTA:** yes — send the venue’s outside-food / COI rules with the inquiry. Do not invent which URL is the conversion page.
- **Blockers:** Do not quote fees, insurance, or named-venue rules beyond what those venues publish. Do not claim Sweeter Teagether is on Maharani/The Knot. Do not list “who to book.”
- **Hard-fail risk:** Medium if it becomes a vendor roundup. Low if it stays FAQ/process.

### 2. Mehndi hospitality: drinks and snacks while henna is drying

- **Working query inspected:** `what to serve at a mehndi party`
- **Related:** `mehndi party food ideas Dallas`; `mehndi party Dallas wedding`
- Wet henna is a serving constraint in national mehndi-food guides (Anvaya, WeddingBazaar). Straw drinks, cup/spoon fruit chaat, staffed dessert cart = hospitality add-on, not the meal or the ritual.
- **SERP (2026-08-27):** National/India magazines and SaaS blogs; DFW overlay is venue landings (Knotting Hill Place, Penrose House, Dallas Oasis, Dallas Palms), not independent hospitality guides.
- **CTA:** yes — mehndi drink / fruit-chaat / dessert cart, straw- and cup-friendly, timed around henna drying.
- **Blockers:** Cannot claim Sweeter Teagether has done DFW mehndi. Cannot flatten Hindu vs Pakistani/Bangladeshi Muslim vs Sikh/Punjabi vs combined mehndi+sangeet. Anvaya’s US artist-price table is their claim, not ours.
- **Hard-fail risk:** Low if logistics + cultural clarity. High if “best DFW mehndi caterers.”

### 3. Dessert carts vs dessert tables at Dallas weddings

- **Working query inspected:** `Dallas wedding dessert cart`
- **Related:** `Dallas wedding cake alternative dessert station`; `Dallas wedding dessert catering`
- Direct category match (mobile sweet cart). Differentiator is cart-as-guest-station, not bakery cake.
- **SERP (2026-08-27):** Bite & Bloom weddings page; Zola marketplace (ZZ’s); Mr Sugar Rush dessert URLs; Lakefront Acres cake-alternatives (8 Mar 2026; not a DFW-core process piece); Brides of North Texas dessert-bar article (16 Jun) and stale “6 North Texas dessert vendors” (12 Jun 2020). Almost no independent “how a staffed cart runs at a reception.”
- **CTA:** yes — inquiry after “cart vs table vs cake.”
- **Blockers:** Directory listings are not confirmation of current wedding work. Do not recycle the 2020 roundup or Lakefront Acres lists as DFW fact.
- **Hard-fail risk:** Medium. Query gravity pulls toward “best dessert carts Dallas.” Viable only if the spine is format/process.

### 4. Outside dessert/beverage carts: open-vendor vs exclusive DFW venues

- **Working query inspected:** `Dallas wedding venue outside catering preferred vendor dessert cart`
- A cart only books if the venue allows outside food.
- **SERP (2026-08-27):** Dallas Palms (open vendor, Carrollton page); Stone Crest Venue (open, own site); Davis & Grey Farms (open + in-house bar, own site); Milagro Ranch (outside catering allowed, own site); Dallas Arboretum 2024–2026 wedding guide **search snippet** said exclusive catering (PDF fetch failed / rate limited — re-verify before citing); national food-truck guides.
- **CTA:** yes — “send your venue’s outside-food / COI requirements with the inquiry.”
- **Blockers:** Do not generalize named-venue policies. Do not invent fees or “most DFW venues allow carts.” Carrollton may appear because a page is Carrollton-specific; still frame service as DFW.
- **Hard-fail risk:** Medium if it becomes a venue roundup. Low if it stays questions + how policies differ, cited to venues’ own pages.

### 5. Feeding a DFW sangeet without killing the performances

- **Working query inspected:** `sangeet food ideas Dallas`
- **Related:** `sangeet Dallas wedding`; `how to plan a sangeet night Dallas`
- Curry Up Now (own page, dated 4 May 2026) describes performances in short blocks and guests eating in 10–20 minute gaps. Tiffins ToGo (own site) already sells a late-night chaat station for sangeet/reception. Cart = guest activity in the gaps, not dinner.
- **SERP (2026-08-27):** Those two caterer SEO posts + venue sales (Dallas Palms sangeet, Dallas Oasis, Penrose House sample 8:00 PM sangeet) + national choreography guides.
- **CTA:** yes — station for dance breaks / open-floor hours, booked alongside (not instead of) the family’s caterer.
- **Blockers:** Do not treat Curry Up Now’s or Tiffins’ menus as Sweeter Teagether offerings. Do not use their named suburbs as ST service areas. Dallas Palms in-house late-night (chicken and waffles / biscuits and gravy, their page) is their menu, not a South Asian late-night template. Do not claim sangeet is universal across Pakistani walima weekends or Nepali/Sri Lankan programs.
- **Hard-fail risk:** Low if timing/station placement. High if “best sangeet caterers in DFW.”

### 6. Pakistani wedding weekend in DFW: mehndi vs baraat dinner vs walima hospitality

- **Working query inspected:** `Pakistani wedding Dallas planning`
- **Related:** `walima Dallas wedding`; `nikah walima Dallas venue`; `dholki Dallas wedding`
- Natural cart fits: dholki/home gathering chai-and-sweet hospitality; mehndi hands-free drinks; walima late dessert/drink station after the main dinner. Never a stand-in for biryani/nihari or for nikah.
- **SERP (2026-08-27):** National structure pages (EventAtlas 1 Jun 2026; Dallas named only as one US city); local venue + decor (Dallas Palms, Dallas Oasis Pakistani page with Hindu/Pakistani flattening, Wedding Wonders dholki/walima decor, 7Elements Nikah/Walima). Heritage Caterers (own site) claims Dallas-based SA wedding catering and Halal menus. Usmania walima catering: search snippet only; full fetch returned an incomplete 2024 fragment — incompletely verified.
- **CTA:** yes for mehndi and walima; weak/no for nikah or rukhsati.
- **Blockers:** Do not flatten Pakistani practice into sangeet/haldi/mandap language. Do not claim ST is a Pakistani or halal kitchen. Heritage’s “all of our menus are Halal” is theirs, not transferable.
- **Hard-fail risk:** Low if event definitions + hospitality. High if “best Pakistani caterers/venues in DFW.”

### 7. A boba bar for DFW weddings

- **Working query inspected:** `boba bar wedding Dallas`
- **Related:** `boba bar for events Dallas`; The Boba Plug weddings page; `dessert cart wedding Dallas`
- ST About lists weddings/engagements; contact form includes event type. Combo boba + skillet + chaat is a differentiator **only if the owner confirms they actually book that combo**.
- **SERP (2026-08-27):** bobabarexperience.com (snippet; live fetch 404 — unverified); The Boba Plug weddings/showers/quinceañeras page (own site); Fat Straws catering; Bobaddiction on The Desi Bride directory (unverified until business site confirms). Adjacent dessert-cart wedding SERP is Bite & Bloom / Mr Sugar Rush.
- **CTA:** yes — couples/planners requesting a quote. Do not invent CTA URL.
- **Blockers:** ST does not publish wedding-specific inclusions (late-night, cocktail hour, venue load-in, guest counts).
- **Hard-fail risk:** Inventing wedding packages; “best wedding boba in Dallas”; copying Boba Plug DIY vs full-service structure as if it were ST’s.

### 8. Late-night bites at Dallas weddings

- **Working query inspected:** `Dallas wedding late night snacks food station`
- Warm cookie skillet, boba, or fruit chaat can occupy the same “second-wind / send-off” slot local mag copy describes for smash burgers — without competing as dinner catering.
- **SERP (2026-08-27):** Food Truck Club / Curbside national template; Best Food Trucks Dallas; Brides of North Texas Hamburger Man (23 Mar) and “Top Wedding Catering Trends in Dallas Right Now” (25 Aug 2026; Trend No. 04: late-night bite as “Dallas wedding staple”); Mr Sugar Rush late-night dessert-truck URLs. Independent non-sales planning copy is thin. Savory handhelds own the “staple” conversation; sweet late-night is ice-cream-truck keyword stuffing.
- **CTA:** yes — “ask about a late-night cart window at your DFW reception.”
- **Blockers:** Do not copy competitor prices. Do not treat Brides of North Texas “non-negotiable” language as market fact. Venue generator/noise/load-in rules are venue-specific.
- **Hard-fail risk:** Low if timing/logistics. High if “best late-night vendors in Dallas.”

### 9. Late-night after a DFW South Asian reception or walima

- **Working query inspected:** `Indian wedding late night treats Dallas`
- **Related:** `late night snacks Indian wedding Dallas`; `Dallas wedding late night snack station`; `dessert station Indian wedding Dallas`
- Position as the late window after the main catering line, not a replacement for mithai. Tiffins ToGo productizes “late-night chaat to extend the service window” (own site). Dallas Palms in-house late-night is chicken-and-waffles — a cultural mismatch some families will want to replace.
- **SERP (2026-08-27):** SA query almost no planning content — Tiffins ToGo, Richi Caterers, Sahjanand (dessert bars / mithai counters on their sites). Generic DFW late-night: Mr Sugar Rush, Gil’s Elegant Catering, Food Truck Club. Sinful Temptations via The Desi Bride directory; own site confirms DFW fusion desserts, not full wedding-package verification.
- **CTA:** yes — late-night add-on after the main caterer packs up.
- **Blockers:** Do not invent after-10pm venue rules, hours, or minimums. Do not claim ST is “the late-night chaat vendor of record.”
- **Hard-fail risk:** Medium if it becomes a vendor list.

### 10. Hire a mobile boba cart in Dallas–Fort Worth

- **Working query inspected:** `boba catering Dallas` (also `boba cart Dallas`, `mobile boba bar Dallas`, `boba bar for events Dallas`)
- Matches ST’s named Boba Bar and hire-intent queries.
- **SERP (2026-08-27):** The Boba Plug catering page (own site: DIY bar, full-service, half-gallon pickup, ~2 weeks’ notice — **their** specs, not ST’s); Ellie & Juice boba catering Dallas (own site); Fat Straws catering + on-site; SK² Boba On Tap (multi-city, own site); Yeehaw Brew Carrollton (own site; booking UX looked unfinished — treat as unverified); PartySlate / WeddingWire directories for Bobaddiction (unverified); Uni Uni nationwide. **sweeterteagether.com: not present.** bobabarexperience.com ranked in snippets; `/` and `/get-a-quote` **404’d** on live fetch — offerings unverified.
- **CTA:** yes — inquiry. Do not invent package math.
- **Blockers:** ST menu has no flavors. No public lead time, duration, guest min, indoor/outdoor spec, attended vs drop-off details. Contact form *collects* some of those fields; that is not publishable service copy until the owner confirms. Brand-ish queries can hit **Teagether Boba & Smoothies (Grand Prairie shop)** — different business.
- **Hard-fail risk:** Publishing competitor prices; treating Fat Straws gallon/drop-off as the same product as a cart; claiming ST rankings.

### 11. Mobile dessert cart catering in Dallas (not a truck, not a bakery)

- **Working query inspected:** `mobile dessert bar Dallas` and `dessert catering Dallas`
- Broader net for hosts who do not search “boba.” ST is a cart, not a cafe/truck/bakery.
- **SERP (2026-08-27):** Mr Sugar Rush (multiple thin SEO URLs); Bite & Bloom (own site: mini pancake, Dubai chocolate strawberries, soft serve, churros; private-party minimum 45 guests — **theirs**); Allure Bites (ice cream + charcuterie carts); Trio Snack Co.; Sweet Shoppe DFW; Dallas Event Rentals candy-cart **rentals** (empty display cart); Iced Out; bakeries/gifting. Format confusion is the SERP.
- **CTA:** yes if the page teaches format; weak if it tries to win generic “dessert catering Dallas” against bakeries and ice cream trucks.
- **Blockers:** Do not claim pancake/churro/soft-serve/s’mores/charcuterie. Only boba, cookie skillet, fruit chaat (+ “custom sweet experiences” with no public detail). Ice cream cart-only is on the contact form, not the menu page — owner must reconcile.
- **Hard-fail risk:** Best-of dessert carts list; inventing a fourth dessert.

### 12. DFW South Asian weekend hospitality map

- **Working query inspected:** `how to plan Indian wedding Dallas multi-day`
- Multi-day weekends create several honest cart slots (welcome/cocktail hour, mehndi circulating, sangeet gaps, reception late-night, day-after brunch dessert) without replacing biryani, nikah hospitality, or ritual food.
- **SERP (2026-08-27):** Thin local “guides” that are mostly venue/vendor lists (THE ONE EVENT ~400-word post naming Omni Dallas, The Olana, Knotting Hill Place); Dallas Palms Indian/Pakistani planning (venue sales); Dream Ranch Events; Dallas Oasis “How To Plan Your Indian Wedding in the USA” URL unstable on fetch; Penrose House sample Thu–Sat timeline; PhotoKumar top-10 venues (photographer opinion); Maharani Dallas index.
- **CTA:** yes if the page teaches which events a hospitality cart fits.
- **Blockers:** Must not publish one “Day 1 Haldi / Day 2 Mehndi+Sangeet / Day 3 Ceremony / Day 4 Reception” as **the** DFW South Asian weekend. PhotoKumar’s list is not a ranking to echo. Cannot claim ST works at named venues.
- **Decision: queue.** Useful hub, but first-pass ranking pages are venue SEO. **Hard-fail if drafted as a venue/vendor list.**

### 13. Cocktail hour at Dallas weddings when photos run long

- **Working query inspected:** `Dallas wedding cocktail hour food ideas stations`
- Cocktail hour is a documented DFW planning gap (Ferah: often an hour or longer depending on photography). Boba and fruit chaat are circulating, non-alcohol, photo-friendly stations. Cookie skillet is warmer/heavier — better flagged as reception/late-night unless the couple wants that.
- **SERP (2026-08-27):** Ferah Catering cocktail-hour article; Crave Catering chef action stations; Tastefully Yours stations; mocktail overlay (Dallas Observer Halal Fizz profile; Ellie & Juice; Southern Pour TX). No page treats a staffed sweet/boba cart as a cocktail-hour occupancy tool.
- **CTA:** yes — cocktail-hour or welcome-hour cart inquiry. Do not claim dry/multicultural/family-forward as ST specialties beyond the menu itself.
- **Blockers:** Ferah’s tenure and menu items are that caterer’s claims. Mocktail studios are not boba; do not conflate.
- **Decision: queue.** City-swap risk if it becomes generic “cocktail hour ideas.”

### 14. Fruit chaat catering for DFW parties (dessert cart, not a live chaat station)

- **Working query inspected:** `fruit chaat catering Dallas` / `fruit chaat catering DFW Dallas`
- Named ST offering (“fresh seasonal fruit tossed with a sweet and tangy South Asian-inspired blend… made to share”). Cultural gatherings are listed on ST About.
- **SERP (2026-08-27):** Tiffins ToGo live chaat or pani puri counter (own site); Ekta’s Kitchen live chaat (savory items, min 40 guests, own site); Richi Caterers live chaat; India Chaat Cafe platters; Indori Spice Frisco; Bite & Bloom “Chaat Bar” (build-your-own with chutneys — savory-leaning, not fruit chaat); Chaat Party (Bay Area — out of market); no dedicated DFW fruit-chaat **cart** hire page; no sweeterteagether.com.
- **CTA:** yes for hosts who already want fruit chaat; weak/no if the page tries to rank for generic `chaat catering Dallas`.
- **Blockers:** No ST ingredients, spice level, seasonal list, allergen, halal, or serving format. Do not fill that in.
- **Decision: queue.** **Hard-fail if it ranks into savory Indian catering or becomes a best-of chaat list.**

### 15. Ice cream cookie skillet catering for DFW events

- **Working query inspected:** `"cookie skillet" catering OR cart OR event Dallas OR DFW`
- Named offering on homepage, menu heading, and contact form (“Ice Cream - Cookie Skillet Cart”). Unique vs boba-only competitors. **No couple-facing DFW hire SERP.**
- **SERP (2026-08-27):** Cookie Society catering is food truck + boxed cookies, **not skillets** (own site); Cookie Whipped custom cookies; Pokey O’s cookie/ice cream sandwiches via directory; Scookie Bar is Phoenix (not DFW).
- **CTA:** yes if someone already wants this; weak as a head-term play (searchers use “dessert cart” or “cookie catering”).
- **Blockers:** Menu page has no skillet flavors, serving style, shareable vs individual, or whether ice cream is always included. Homepage vs About vs contact-form ice-cream-cart-only must be reconciled by the owner.
- **Decision: queue.** Fold into cart-format or late-night pieces. Do not force a standalone topic.

---

## Important SERP observations

- **sweeterteagether.com did not appear** on any hiring-intent SERP inspected 2026-08-27 (`boba cart Dallas`, `mobile boba bar Dallas`, `boba catering Dallas`, `boba bar for events Dallas`, `boba bar wedding Dallas`, `boba bar baby shower Dallas`, `corporate boba catering Dallas`, `dessert catering Dallas`, `mobile dessert bar Dallas`, `dessert cart wedding Dallas`, `cookie skillet catering`, `fruit chaat catering Dallas`). WebSearch for `"Sweeter Teagether"` and `site:sweeterteagether.com` returned no results in that tooling, even though the site fetched live.
- Brand-ish query `sweeter teagether Dallas boba` hit **Teagether Boba & Smoothies (Grand Prairie shop)** — name collision, different business.
- Independent DFW planning copy about dessert/beverage **carts** barely exists. Live SERPs are vendor homepages, marketplace templates, and Wed Society / Brides of North Texas advertorials.
- Late-night is culturally established in local mag copy (Brides of North Texas, 25 Aug 2026), but the sweet version is vendor SEO; savory handhelds own the narrative.
- Boba-at-weddings SERP is shop/catering homepages only. `bobabarexperience.com` 404’d on live fetch while still appearing in search snippets — treat as unstable.
- Fruit chaat exists on cultural caterers’ own wedding pages (savory live chaat), not as a couple query with a fruit-chaat-cart planning SERP.
- Cookie skillet has no inspectable DFW hire demand; do not force a standalone topic.
- “Best of Dallas” is the default SERP shape for dessert (mag roundups, Zola, package pages). Any article whose core is a ranked list will hard-fail verification.
- South Asian food-timing is only explained by people selling catering (Curry Up Now, Tiffins ToGo). Existing DFW SA “guides” flatten Pakistani/Indian weekends and default to venue lists.
- Open-vendor vs exclusive catering is answered only on individual venue sales pages, not as an independent DFW cart-specific explainer.
- Directory pages (The Knot, Maharani, The Desi Bride, PartySlate, Zola, Eventective, WeddingWire) appeared often; they are not verification of current offerings.

## Business / system gaps discovered

The operating system is ready for discovery; several public facts are not.

- `BUSINESS_BRIEF.md` still marks menu / about / contact URLs as `TODO — OWNER INPUT REQUIRED`, but those pages live today: `/menu`, `/about`, `/contact`.
- `/menu` is category headings only (Boba; Ice Cream and Cookie Skillet; Fruit Chaat) — no item-level menu.
- `/contact` already asks indoor vs outdoor, guest-count buckets starting at **50–99**, attended vs self-serve vs **boba drop-off**, and **ice cream cart only**. None of those are specified in the brief. The form collecting a field is not a published spec.
- About page names owners (Zahra and Taha Aziz), Dallas base, and additional event types (quinceañeras, school celebrations, cultural gatherings) plus “refreshing fruit beverages” — not all of this is in the brief.
- Cluster topic logs are still empty, which is expected before a human accepts this batch.
- Hiring questions that appear on ranking vendor FAQs and that ST’s public pages do **not** answer: guest min/max; indoor/outdoor/weather/venue rules; space/power/water/load-in; service duration; attended vs self-serve vs drop-off definitions; lead time; flavor/topping counts; whether ice cream is a standalone cart vs skillet add-on; combining boba + skillet + chaat on one booking; dietary / allergen / halal / vegan (do not claim); pricing/packages/deposits/travel/overtime; staff count; exact DFW cities / travel radius; hours / blackout dates.
- Keyword-tool metrics still should not be invented; Opportunity stayed qualitative. No approved keyword platform in the brief.
- First-pass clusters should not be back-filled with shower-only or corporate-only pages unless the owner expands scope.

### Queries inspected and dropped (not candidates)

- Cookie skillet as a standalone DFW couple query — no hire SERP.
- `boba bar baby shower Dallas` / corporate boba — out of first-pass cluster scope.
- `baraat Dallas wedding` — horse/carriage vendors; no honest cart fit.
- `boba bar wedding Dallas` as a **South Asian cluster** article — generic boba caterers; SA element would be title-only.
- `Bangladeshi wedding Dallas` / `Sri Lankan wedding Dallas` — no distinct local hospitality SERP; do not fake topics.
- `Nepali wedding Dallas` — still venue sales; Tiffins already occupies momo-bar hospitality.
- `haldi party Dallas` — messy/turmeric; not a natural cart-first topic this pass.
- How to start a food truck / park concession permitting — operator, not couple/planner.
- Stale “6 North Texas Dessert Vendors” (Jun 2020) and 2015 advertorials — not models.
- Recipes / at-home boba — absent from the live wedding SERPs inspected; correctly out of scope.

---

## Explicit stop line

**No topic in this batch has been approved for drafting.**

This file is a scored discovery dump only. Do not write intros, outlines, or article body copy from it. Do not move any candidate into `content/drafts/`. Do not publish. Owner approval is required before a research batch advances to drafting (`BUSINESS_BRIEF.md`).
