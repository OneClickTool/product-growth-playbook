# GEO & AEO: a learning guide

> Read this once, top to bottom (about 40 minutes). Then use [the skill](../SKILL.md) to apply it to one feature.
> Last checked: 18 Oct 2026. AI search changes fast: re-check the official pages in [Sources](#sources) every quarter.

## Contents
1. [The words](#1-the-words)
2. [How an AI answer picks its sources](#2-how-an-ai-answer-picks-its-sources)
3. [What the official docs say](#3-what-the-official-docs-say)
4. [What the research says](#4-what-the-research-says)
5. [The three pillars](#5-the-three-pillars-structure-authority-presence)
6. [GEO before the product exists](#6-geo-before-the-product-exists)
7. [Crawler access](#7-crawler-access-robotstxt)
8. [Measuring it day by day](#8-measuring-it-day-by-day)
9. [Myths](#9-myths)
10. [A 4-week study plan](#10-a-4-week-study-plan)

---

## 1. The words

| Term | Plain meaning | Where it shows up |
|---|---|---|
| **SEO** (search engine optimization) | Get a page **ranked** in a list of links. | Google, Bing classic results |
| **AEO** (answer engine optimization) | Get a passage **used as the direct answer** to a question. | Featured snippets, People Also Ask, voice assistants, AI Overviews |
| **GEO** (generative engine optimization) | Get your page **cited or your product named** inside an answer an AI model writes. | ChatGPT search, Perplexity, Google AI Overviews / AI Mode, Copilot, Gemini, Claude |
| **LLMO / AI SEO** | Other names for GEO. | Vendor blogs |
| **Citation** | The answer links to your page as a source. | All AI engines |
| **Mention / recommendation** | The answer names your product, ideally on the shortlist. | Mostly ChatGPT, Perplexity, Gemini |
| **Grounding query** | The search the AI ran in the background to find sources. | Bing AI Performance report |
| **Query fan-out** | One question split into many background searches. | Google AI Mode, ChatGPT |

AEO and GEO overlap. In practice: **AEO = write the answer so it can be lifted; GEO = be the source the model trusts
enough to cite or recommend.** Both sit on top of normal SEO. They do not replace it.

## 2. How an AI answer picks its sources

Most AI search products follow the same loop (retrieval-augmented generation):

```
User question
   │
   ▼
Fan-out: 3–20 background searches ("best X for Y", "X vs Z", "X pricing", "site:official")
   │
   ▼
Retrieve: pages from the engine's index (Google, Bing, own crawler)  ← you must be crawlable + indexed
   │
   ▼
Pick passages: short blocks that answer one sub-question clearly    ← AEO: structure
   │
   ▼
Write answer + cite the passages it leaned on                        ← GEO: authority, facts, consensus
```

Three things follow from this:
- **No index, no citation.** If the engine can't crawl the page, nothing else matters.
- **Passages win, not pages.** A clear 40–60 word block under a question heading is easy to lift. A wall of marketing copy is not.
- **Other sites count.** Engines also retrieve Reddit threads, reviews, directories, YouTube text and news. What
  *they* say about you shapes whether you get recommended.

## 3. What the official docs say

These are the only "rules". Everything else in this guide is research or practice.

**Google (AI Overviews, AI Mode).** From [AI features and your website](https://developers.google.com/search/docs/appearance/ai-features) (updated 10 Dec 2025):
- To be shown, a page must be **indexed and eligible to show a snippet**. There are **no extra requirements** and no
  special optimization needed.
- You **don't need** new machine-readable files, AI text files or special schema.org markup.
- Clicks and impressions from AI features are **counted in Search Console → Performance, search type "Web"**. There
  is no separate AI report.
- Controls: `nosnippet`, `data-nosnippet`, `max-snippet`, `noindex`. `Google-Extended` controls use in Gemini training
  and grounding, not Search.

**Google spam policies** ([Spam policies for Google web search](https://developers.google.com/search/docs/essentials/spam-policies)). Three matter for feature previews:
- **Misleading functionality**: pages that make users think they can get a service that they can't. A "Try it now"
  button for a feature that doesn't exist is exactly this.
- **Doorway abuse**: many near-identical pages made to rank for similar queries.
- **Scaled content abuse**: many pages generated mainly to manipulate rankings.

**OpenAI** ([Overview of OpenAI crawlers](https://developers.openai.com/api/docs/bots)):
- `OAI-SearchBot` decides whether you can appear in **ChatGPT search** answers. Allow it in robots.txt and in your
  firewall. Changes take about 24 hours.
- `GPTBot` is for model **training**. Blocking it does not remove you from ChatGPT search.
- `ChatGPT-User` fetches a page when a user asks; it is not an automatic crawler.

**Perplexity** ([Perplexity crawlers](https://docs.perplexity.ai/guides/bots)): allow `PerplexityBot` (search results,
not training) and its published IPs; `Perplexity-User` fetches on a user's request.

**Anthropic** ([About Claude's web crawlers](https://support.claude.com/en/articles/8896518-about-claude-s-web-crawler)): `ClaudeBot` (training),
`Claude-SearchBot` (search quality), `Claude-User` (user-requested fetches).

**Microsoft Bing** ([AI Performance in Bing Webmaster Tools, public preview, Feb 2026](https://blogs.bing.com/webmaster/February-2026/Introducing-AI-Performance-in-Bing-Webmaster-Tools-Public-Preview)):
the first first-party report of **citations** in Copilot and Bing AI answers (total citations, cited pages, grounding
queries). It shows no clicks.

**US FTC** ([Rule on consumer reviews and testimonials, 16 CFR Part 465](https://www.ftc.gov/news-events/news/press-releases/2024/08/federal-trade-commission-announces-final-rule-banning-fake-reviews-testimonials), in force 21 Oct 2024):
no fake or AI-written reviews, no undisclosed insider reviews, no "independent" review site you control. A pre-launch
page has **no reviews yet**. Don't invent them.

## 4. What the research says

**The GEO paper** (Aggarwal et al., Princeton / IIT Delhi, KDD 2024, [arXiv 2311.09735](https://arxiv.org/abs/2311.09735))
tested 9 ways to rewrite a source page and measured how much of the AI answer used it. Visibility change vs. no
change, on their GEO-bench (Table 1, word-count metric):

| Rewrite | Change |
|---|---|
| Add quotations from named people | about **+41%** |
| Add statistics | about **+33%** |
| Fluency (clearer, smoother writing) | about **+29%** |
| Cite sources | about **+28%** |
| Technical terms | about +18% |
| Easy-to-understand language | about +14% |
| Authoritative tone | about +12% |
| Keyword stuffing | about **−9%** |

Two findings matter most for a small, new site:
- **Lower-ranked pages gain the most.** For a page in 5th position, *cite sources* raised visibility by about +115%,
  while the page in 1st position *lost* share. GEO is one of the few levers where being small is not a handicap.
- **Results differ by topic.** Test on your own queries; don't copy percentages into a forecast.

Treat the numbers as **direction, not a promise**: it was a lab setup on a research engine and Perplexity in 2023–24.

**Industry practice** (vendor studies, re-check before quoting): AI Overviews show on a large share of informational
queries and lower click-through on the top link; ChatGPT's preferred page formats shifted during 2026 toward
official and primary pages and away from listicles. The lesson that holds across studies: **owned "official" pages
with plain facts, plus real third-party mentions, beat thin listicles.**

## 5. The three pillars: structure, authority, presence

### Structure (make it liftable) — this is AEO
- One page = one main question. H1 says what the thing is.
- Under each H2 written as a question ("Does X work offline?"), put the **answer first** in 40–60 words, then detail.
- Tables for comparisons, numbered lists for steps, one idea per paragraph.
- Key text is in HTML, not inside images or behind a JavaScript-only render. Images get `alt` text.
- A visible **"Last updated"** date and a named author.
- Optional structured data that matches the visible text (`SoftwareApplication`, `FAQPage`, `Article`). Google says
  it's not required for AI features; it can help other engines and is normal good SEO.

### Authority (make it worth citing) — this is GEO
- **Facts you own**: numbers from your own tests, a dated design decision, a measured benchmark. "Exports a 4K
  frame in 1.8 s on an M2 Air in our test" beats "blazing fast".
- **Cite sources** for every outside claim, with links.
- **Named people**: quote the designer or a beta tester (with permission, and real).
- **Show your work**: mockups, a design review log, a changelog. These are first-hand experience that a model can't
  get anywhere else.

### Presence (be where the AI looks)
- Answer real questions where people ask them (Reddit, forums, Discord, Stack Exchange) and link only when it helps.
- Get listed in directories and "alternatives" pages that are already cited for your queries.
- Short video with a written description and captions (the text layer is what gets read).
- Say the same one-line positioning everywhere: About page, store listing, directories, profiles. Models look for
  agreement between sources.

## 6. GEO before the product exists

You can do GEO before writing code, because the thing an AI cites is **a clear answer**, not a working binary. What
you publish is a **feature preview**: an honest page about something you are designing.

**What a preview page can honestly offer**
- The problem, in the words people use when they search for it (from your research).
- The design: mockups, a short clickable prototype video, the decision log from your design review.
- What it will and won't do, and the status: *In design · Not available yet · Planned for {{month}}*.
- A way to act: join the waitlist, vote, comment on the mockup, become a beta tester.
- How it compares with what people use today (facts about competitors, cited).

**What it must never do**
- Buttons like "Download" or "Start free trial" for something that doesn't exist (Google: misleading functionality).
- Fake reviews, fake user counts, fake "as seen on" logos (FTC rule).
- One page per keyword variant ("X for students", "X for teachers"… with the same text) (doorway / scaled content).
- Screenshots presented as the real app when they are mockups. Label them **"Design mockup"**.

**The validation loop.** Traffic tells you whether people are looking; sign-ups tell you whether they want it.

```
Research questions  →  1 preview page per feature  →  index + share in 3 places
        ▲                                                    │
        │                                                    ▼
 build / rework / drop  ◄──  read 7-day trend  ◄──  daily log: visits, AI visits, sign-ups
```

## 7. Crawler access (robots.txt)

Decide per purpose. A common setup for a new product that wants to be found but not used for training:

```text
# Search and answer engines: allow
User-agent: Googlebot
Allow: /
User-agent: Bingbot
Allow: /
User-agent: OAI-SearchBot
Allow: /
User-agent: PerplexityBot
Allow: /
User-agent: Claude-SearchBot
Allow: /

# Model training: your choice (blocking these does not remove you from search answers)
User-agent: GPTBot
Disallow: /
User-agent: ClaudeBot
Disallow: /
User-agent: Google-Extended
Disallow: /

Sitemap: https://example.com/sitemap.xml
```

Then check that your host's firewall or bot protection (Cloudflare, Vercel) isn't blocking the allowed bots anyway.

**`llms.txt`** is a community proposal ([llmstxt.org](https://llmstxt.org)). Google says AI text files aren't needed.
It costs 10 minutes and does no harm; don't expect traffic from it.

## 8. Measuring it day by day

### What you can measure, and where

| Signal | Tool | Delay | What it tells you |
|---|---|---|---|
| Impressions, clicks, queries per page (incl. AI Overviews / AI Mode) | Google Search Console → Performance → Web | 1–3 days | Google is showing the page, for which questions |
| AI citations in Copilot / Bing | Bing Webmaster Tools → AI Performance | days | Bing's AI uses your page, with grounding queries |
| Visits from AI assistants | GA4 (session source `chatgpt.com`, `perplexity.ai`, `claude.ai`, `gemini.google.com`, `copilot.microsoft.com`) | same day | People clicked through from an answer |
| Waitlist sign-ups, mockup votes | GA4 key event + your form tool | same day | They want it |
| Mentioned or not | Manual prompt checks (below) | weekly | The AI knows you exist |

**GA4 setup (10 minutes).** Admin → Data display → Channel groups → create a custom channel **"AI assistants"** with
*Session source matches regex*:

```text
chatgpt\.com|chat\.openai\.com|perplexity\.ai|claude\.ai|gemini\.google\.com|copilot\.microsoft\.com|bing\.com/chat
```

Put it **above** "Referral" (first match wins). ChatGPT usually adds `utm_source=chatgpt.com` to links; other
assistants often send no referrer, so some AI visits will show as *Direct*. Your AI number is a **floor**, not the total.

### Reading daily numbers without fooling yourself
- **Daily traffic on a new page is noise.** 3 visits one day and 11 the next means nothing. Read the
  **7-day rolling average** and compare it with the **baseline** (the 7 days before you published or changed the page).
- **One change at a time per page**, and write the date in the log. Otherwise you won't know what worked.
- **Expect a lag.** Indexing can take days to weeks; AI citations usually come later than Google impressions.
  Judge a page after **28 days**, not 3.
- **Count rates, not single runs.** AI answers vary. Run each prompt 3 times and record "mentioned 1/3".
- **Sign-ups per 100 visits** is the number that decides whether to build. Traffic without sign-ups means the
  page answers a question but the feature isn't wanted (or the page doesn't ask clearly).

### Weekly prompt check (15 minutes)
Pick 5 prompts a buyer would type (problem-aware: "how do I…"; solution-aware: "best app for…"; comparison: "X vs Y").
Run each 3 times in ChatGPT (search on), Perplexity and Google. Log: *mentioned? cited page? who else is cited?*
The sites cited instead of you are your outreach list.

## 9. Myths

| Myth | Reality |
|---|---|
| "GEO replaces SEO." | AI answers retrieve from search indexes. No index, no citation. |
| "You need llms.txt / special schema for Google AI." | Google says no special files or markup are needed. |
| "Blocking GPTBot hides me from ChatGPT." | Search inclusion is `OAI-SearchBot`. Training and search are separate tokens. |
| "Write separate pages for AI." | Google calls mass AI-targeted variants scaled content abuse. Write for people, structure clearly. |
| "More keywords = more citations." | Keyword stuffing lowered visibility in the GEO study. |
| "A preview page can't rank because the app isn't out." | Engines cite clear answers and original material. Honest previews with mockups and decisions are original material. |
| "A spike after a Reddit post means GEO works." | Separate channels in the log. GEO shows up as organic + AI sources over weeks. |

## 10. A 4-week study plan

| Week | Learn | Do (on your product) |
|---|---|---|
| 1 | Sections 1–3 | Verify the site in Search Console and Bing Webmaster Tools; add the GA4 "AI assistants" channel; fix robots.txt; start the daily log. |
| 2 | Sections 4–6 | Pick 1–3 features. Collect the real questions. Publish one preview page per feature with mockups and a waitlist. |
| 3 | Section 5 (presence) | Answer 5 real threads; get listed in 2 directories cited for your queries; post a 30-second mockup walk-through with captions. |
| 4 | Sections 8–9 | Run the weekly prompt check. Run `traffic_trend.py` on the log. Decide per feature: build, rework the page, or drop. |

## Sources
- Google Search Central: [AI features and your website](https://developers.google.com/search/docs/appearance/ai-features) · [Spam policies](https://developers.google.com/search/docs/essentials/spam-policies)
- OpenAI: [Overview of OpenAI crawlers](https://developers.openai.com/api/docs/bots)
- Perplexity: [Perplexity crawlers](https://docs.perplexity.ai/guides/bots)
- Anthropic: [Claude's web crawlers](https://support.claude.com/en/articles/8896518-about-claude-s-web-crawler)
- Microsoft: [AI Performance in Bing Webmaster Tools (public preview)](https://blogs.bing.com/webmaster/February-2026/Introducing-AI-Performance-in-Bing-Webmaster-Tools-Public-Preview)
- Aggarwal et al., [GEO: Generative Engine Optimization](https://arxiv.org/abs/2311.09735), KDD 2024
- US FTC: [Final rule banning fake reviews and testimonials](https://www.ftc.gov/news-events/news/press-releases/2024/08/federal-trade-commission-announces-final-rule-banning-fake-reviews-testimonials)
- [llms.txt proposal](https://llmstxt.org)
- Practice: the open-source `ai-seo` skill in [coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills) (MIT), for the audit checklist and content patterns.
