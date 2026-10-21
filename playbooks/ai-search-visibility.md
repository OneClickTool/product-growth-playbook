# Playbook: AI Search Visibility (SEO, AEO, AIO, GEO)

What the four acronyms mean, how they stack, what still works in 2026, how strong the evidence is, and the order to
do it in for a small product. It's a research and knowledge doc: read it once, then use the skills linked at the end.

> Last checked: 21 Oct 2026. AI search changes month to month. Re-check the [Sources](#sources) before quoting a
> number to anyone. For the deeper mechanics (how answers pick sources, crawler access, daily measurement), read the
> [GEO & AEO learning guide](../skills/launch/launch-geo-aeo-feature-preview/references/geo-aeo-learning-guide.md).

## In one minute
- **SEO** gets a page indexed and ranked. **AEO** gets one passage used as *the* answer. **AIO** means showing up as a
  source in Google's **AI Overviews** (and AI Mode). **GEO** means being cited and named by ChatGPT, Perplexity,
  Gemini, Claude and Copilot.
- They are **layers, not alternatives**. Every AI search product retrieves pages from an index before it writes. No
  index, no citation.
- Layers 1–2 are mostly work on your own site. Layers 3–4 depend more and more on **what other sites say about you**.
- Why now: when an AI Overview shows, people click results much less (a 2026 randomized study measured −38%), but
  pages **cited inside** the Overview still get more clicks than pages that aren't.

## Why it matters in 2026

| Finding | Source | Strength |
|---|---|---|
| With an AI Overview, organic clicks fell **38%** and zero-click searches rose from 54% to 72% | Randomized experiment, 1,065 US users, Jan–Feb 2026 (Agarwal & Sen, SSRN, Apr 2026) | **High**: has a control group |
| Top-ranked page CTR about **58% lower** when an AI Overview shows (34.5% in the 2025 run) | Ahrefs, 300,000 keywords, Feb 2026 | Medium: correlational |
| About 68% of US Google searches ended without a click in early 2026 | SparkToro data | Medium |
| On queries with an AI Overview: cited pages ~2.1% CTR, uncited ~0.9% | Seer Interactive | Medium |
| Oct 2026: Google moves inline source links higher in AI Mode / AI Overviews and tests a separate block for **official sites** | Google announcement, 15 Oct 2026 (via press) | High, but read Google's own post |

**What it means:** a top-10 ranking alone earns less than it used to. Being **cited in the answer** is the new goal,
and clearly structured **official pages** (product, pricing, docs) are gaining weight.

## The four terms

| | **SEO** | **AEO** | **AIO** | **GEO** |
|---|---|---|---|---|
| Stands for | Search engine optimization | Answer engine optimization | Google AI Overviews | Generative engine optimization |
| Goal | Rank in the list of links | Your passage is picked as the answer | You are a source in the AI Overview / AI Mode | AI assistants cite and recommend you |
| Where | Google, Bing | Featured snippets, People Also Ask, voice, AI answers | Google Search | ChatGPT, Perplexity, Gemini, Claude, Copilot |
| You win when | Top 10, with clicks | Your paragraph is quoted | Your link is in the Overview | The answer says "use X" and X is you |
| Mostly done | On your site | On your site | On your site + trust | **Off your site** |
| Measure with | Search Console | Snippets, AIO sources | Manual checks, rank trackers with AIO data | A fixed prompt set, re-run monthly |

> "AIO" is ambiguous: here it means **Google AI Overviews**. Some people use it for "AI optimization" in general.
> Ask which one someone means.

```
 Layer 4  GEO  — RECOMMENDED by name   ← mentions off your site (press, Reddit, reviews, comparisons)
 Layer 3  AIO  — in the AI Overview    ← complete coverage + sources + a real author
 Layer 2  AEO  — QUOTED as the answer  ← answer first, question headings, tables, FAQ
 Layer 1  SEO  — INDEXED and ranking   ← technical, on-page, links
```

## Where each engine gets its pages

| Engine | Main source of pages | What helps most |
|---|---|---|
| Google AI Overviews / AI Mode / Gemini | Google's index. **No separate "AI index"** | Classic SEO, snippet eligibility, trust signals |
| ChatGPT search | Bing + OpenAI's own crawler (reported) | **Being in Bing**, fresh pages, clear official pages |
| Perplexity | Own index + web search | Self-contained passages, recent updates |
| Copilot | Bing | Bing Webmaster Tools, IndexNow, speed |
| Claude (web search) | Third-party search (reported: Brave) | Fact-dense pages with clear sources |

Practical consequence: get indexed in **both Google and Bing**. Many small sites skip Bing and are close to invisible
in ChatGPT and Copilot.

## What to do for each layer (and what to drop)

A common checklist circulates for "SEO + AEO + AIO + GEO". Here it is, item by item, with 2026 corrections.

### Layer 1: SEO

| Checklist item | Still valid? | Note |
|---|---|---|
| Title, meta description, H1–H4, internal links | ✅ | Title ≲ 60 characters, description ~140–155, one main topic per page |
| Keyword density | ❌ **Drop** | Google doesn't use it. Stuffing makes pages worse for readers and AI summaries. Cover the search intent instead |
| Core Web Vitals, mobile-friendly | ✅ | LCP < 2.5 s, INP < 200 ms |
| XML sitemap, robots.txt | ✅ | Honest `lastmod` dates. Don't block OAI-SearchBot or PerplexityBot if you want to be cited |
| *(missing)* Server-rendered HTML | ➕ | Many AI crawlers run JavaScript poorly. Content that only appears after JS may look empty |
| *(missing)* Bing Webmaster Tools + IndexNow | ➕ | For ChatGPT search and Copilot |
| Backlinks, "Domain Authority" | ⚠️ | Links still matter. "Domain Authority" is a Moz/Ahrefs metric that **Google doesn't use**. Count relevant referring domains |
| Local SEO, Google Business Profile | ✅ if you sell locally | Usually skip for a global app or SaaS |

### Layer 2: AEO

| Checklist item | Still valid? | Note |
|---|---|---|
| Answer first, 40–50 words | ✅ | Open each section with 40–60 words that make sense **cut out on their own** |
| Real questions as H2/H3 | ✅ | From Google autocomplete, People Also Ask, Reddit and your Search Console queries |
| `FAQPage`, `HowTo`, `Article` schema | ⚠️ **Update** | Since Aug 2023 Google **dropped HowTo rich results** and shows **FAQ rich results only for well-known government and health sites**. Keep the markup for clarity, but don't expect FAQ dropdowns in Google |
| Tables, bullets, summary numbers | ✅ | Comparison tables and checklists are the easiest blocks to lift |

### Layer 3: AIO (Google AI Overviews / AI Mode)

| Checklist item | Still valid? | Note |
|---|---|---|
| Comprehensive coverage, several angles | ✅ | AI search splits a question into sub-searches (query fan-out). Cover the follow-up questions too |
| Cite numbers, experts, official sources | ✅ | Add at least one number **you measured yourself** |
| Clear, natural language | ✅ | One idea per paragraph, define terms the first time |
| *(missing)* E-E-A-T signals | ➕ | A real author with a bio, a "last updated" date, "tested on" notes |
| *(missing)* No special markup needed | ➕ | Google states AI Overviews need no special markup or file: the page must be indexed and eligible for a snippet. AIO is SEO + AEO done well, plus trust |

### Layer 4: GEO (ChatGPT, Perplexity, Gemini, Claude)

| Checklist item | Still valid? | Note |
|---|---|---|
| Entity building | ✅ | **The same one-sentence description** on your site, store pages, LinkedIn, X, GitHub, Product Hunt and directories, linked with `sameAs` in your schema |
| Wikipedia | ⚠️ | A new brand usually **can't** get a Wikipedia page (it needs independent press). Start with press, niche blogs and Wikidata |
| Long-form, case studies, opinion | ✅ | **Original data** works best: something others will cite |
| Digital PR, brand mentions | ✅ **Most important** | A Muck Rack analysis (reported by a vendor) found ~84% of AI citations came from earned media, not brands' own pages |
| *(missing)* Structured official pages | ➕ | Clear pricing, feature and docs pages. Listicle citations reportedly fell after ChatGPT 5.6; Google is testing an official-sites block |
| *(missing)* `llms.txt` | ➕ | Cheap to add. **No strong public evidence yet** that it raises citations |

## How strong is the evidence?

Use this before you promise anything to a client, a boss or yourself.

| Claim | Evidence |
|---|---|
| AI Overviews reduce clicks | **Strong**: a randomized experiment plus several large studies |
| You must be indexed to be cited | **Strong**: Google says so |
| Statistics and cited sources raise AI visibility | **Fair**: the KDD 2024 GEO paper measured up to ~30–40%. A Jul 2026 survey of GEO research found general tactics **transfer poorly** between engines, engines cite different sources, and results vary run to run |
| Third-party mentions matter more than your own pages | **Fair**: PR-industry data, no independent study yet |
| ChatGPT citations overlap ~87% with top Bing results | **Weak**: vendor figure, original study not verified |
| `llms.txt` increases citations | **No evidence yet** |
| "Guaranteed ChatGPT placement" | **Nobody can guarantee it**: answers change by prompt, user and week |

## How to measure each layer

| Layer | Question | Tool |
|---|---|---|
| SEO | Are Google and Bing indexing me? Where do I rank? | Google Search Console, Bing Webmaster Tools |
| AEO | Do my passages become snippets? | Search Console queries + manual checks |
| AIO | Am I a source in AI Overviews? | Manual checks; rank trackers with AIO features |
| GEO | Do ChatGPT and Perplexity name me? | **A fixed set of 20 prompts**, re-run on the 1st of each month, screenshots saved. Paid trackers later if needed |
| Traffic from AI | Does anyone click through from AI? | GA4 with an "AI assistants" channel: `chatgpt.com`, `perplexity.ai`, `gemini.google.com`, `copilot.microsoft.com` |

Set up GA4 with [analytics-ga4-setup](../skills/analytics/analytics-ga4-setup/SKILL.md) and the channel rules in
[utm-convention.md](../skills/analytics/analytics-tracking-plan/references/utm-convention.md).

## Myths to skip
1. **"SEO is dead, only GEO matters."** AI engines retrieve from search indexes. SEO is the foundation.
2. **"FAQ schema gets you into AI Overviews."** Google says no special markup is needed, and FAQ rich results are restricted.
3. **"Publish 100 AI-written posts."** Thin, mass-produced pages don't get cited and can be demoted.
4. **"Write a Top 10 listicle with yourself at #1."** Listicle citations are falling; engines prefer official pages and independent sources.
5. **"Add llms.txt and ChatGPT will read you."** No evidence yet.
6. **"Buy links or reviews to speed it up."** Risks a manual action for the whole domain. A frequent version: one shared
   SEO template that puts the same hardcoded star rating on every page. Only mark up ratings that are real.

## The order for a small product

| When | Layer | Do |
|---|---|---|
| Week 1 | Measure | Search Console, Bing Webmaster Tools, GA4, and a sheet of 20 buyer questions with today's AI answers saved |
| Week 2 | SEO | Fix indexing, sitemap, robots, canonicals, speed |
| Weeks 3–4 | AEO | Rewrite your 5 most important pages answer-first; add tables and schema |
| Month 2 | AIO | One deep guide per main topic, with sources and your own numbers |
| Month 2 → | GEO | One description everywhere, directory listings, one honest community contribution a week, one piece of original data a month |
| Every month | All | Re-run the same 20 prompts and compare |

## Skills that do each step
- Learn the mechanics, set up crawler access and run a 28-day test on a preview page:
  [launch-geo-aeo-feature-preview](../skills/launch/launch-geo-aeo-feature-preview/SKILL.md)
- Find the questions buyers really ask: [research-where-users-ask](../skills/research/research-where-users-ask/SKILL.md)
- Get mentioned in communities without being removed: [launch-reddit-posting](../skills/launch/launch-reddit-posting/SKILL.md)
- Directory and launch listings: [launch-quick-download-wins](../skills/launch/launch-quick-download-wins/SKILL.md),
  [launch-product-hunt-launch](../skills/launch/launch-product-hunt-launch/SKILL.md)
- Measure it: [analytics-ga4-setup](../skills/analytics/analytics-ga4-setup/SKILL.md),
  [analytics-ga4-reports-101](../skills/analytics/analytics-ga4-reports-101/SKILL.md)
- For app stores, the same "be the answer" idea: [Playbook: ASO Optimization](aso-optimization.md)

## Glossary

| Term | Meaning |
|---|---|
| **AI Overviews** | AI-written summary above Google results, with source links |
| **AI Mode** | Chat-style answer mode inside Google Search |
| **Featured snippet** | The quoted answer block at the top of classic Google results |
| **Zero-click** | A search that ends without a click on any result |
| **Query fan-out** | An AI engine splitting one question into several background searches |
| **Entity** | A brand, product or person that machines recognise as one clear thing |
| **E-E-A-T** | Experience, Expertise, Authoritativeness, Trust: how Google's raters judge reliability |
| **Schema / JSON-LD** | Structured data that describes a page for machines |
| **IndexNow** | A protocol that tells Bing (and others) a page changed |
| **llms.txt** | A proposed root file summarising a site for language models |
| **Earned media** | Coverage others write about you: press, reviews, community posts |

## Sources
- Google Search Central: [AI features and your website](https://developers.google.com/search/docs/appearance/ai-features) ·
  [Changes to HowTo and FAQ rich results (Aug 2023)](https://developers.google.com/search/blog/2023/08/howto-faq-changes)
- Google's Oct 2026 inline links and official-sites test, as reported by
  [Business Today](https://www.businesstoday.in/technology/news/story/google-ai-search-now-makes-it-easier-to-find-the-websites-behind-its-answers-heres-how-562057-2026-10-16) and
  [BetaNews](https://betanews.com/article/google-ai-mode-inline-links-higher-click-data/)
- Summary of Google's AI Overviews / AI Mode requirements:
  [Trusted Shops](https://ai-trust-audit.trustedshops.com/en/blog/ai-overviews-and-ai-mode-google-s-requirements-for-websites-2026)
- Click-through studies: [Ahrefs](https://ahrefs.com/blog/ai-overviews-reduce-clicks/) ·
  [Search Engine Land on Seer Interactive](https://searchengineland.com/google-ai-overviews-ctr-recovery-study-475566) ·
  [TechWyse on SparkToro](https://www.techwyse.com/news/reports-data/google-zero-click-searches-68-percent-2026) ·
  [SEOWorth on Ahrefs 2026](https://seoworth.it.com/news/ahrefs-ai-overviews-ctr-study/)
- GEO research: [Aggarwal et al., "GEO: Generative Engine Optimization" (KDD 2024)](https://arxiv.org/abs/2311.09735) ·
  [Survey of GEO, 2023–2026 (arXiv, Jul 2026)](https://arxiv.org/pdf/2607.14035)
- Vendor guides quoted with caution: [Averi (Muck Rack figure)](https://www.averi.ai/learn/the-definitive-guide-to-geo-get-cited-by-ai-in-2026) ·
  [LLM Pulse](https://llmpulse.ai/blog/geo-guide/)
- Bing: [Bing Webmaster Tools](https://www.bing.com/webmasters) · [IndexNow](https://www.indexnow.org/)
