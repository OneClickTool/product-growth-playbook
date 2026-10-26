---
name: research-gap-source-scoring
description: Score every place you could look for product gaps (search suggestions, Q&A sites, app stores, review sites, marketplaces, feature-request boards, freelance jobs, your own Search Console) on the same six criteria, then apply a fixed rule to decide which sources deserve an automated collector, which you check by hand, and which you drop. Includes 12 gap-finding methods and a terms-of-service checklist. Use when choosing data sources for niche research or an idea-validation tool, or when someone asks "where should I look for unmet needs", "which sources are worth scraping", "is it allowed to scrape X", "best free API to find app ideas", or "how do indie hackers find gaps".
license: MIT
metadata:
  category: research
  difficulty: intermediate
  time: 2-4 hours
  version: 1.0.0
  author: nvminhtu
---

# Gap Source Scoring

> In an afternoon you will have every candidate source scored on one scale, with a clear decision for each: build a
> collector, check by hand, or drop.

## Goal
Stop picking research sources by gut feeling. Put every source on the same six criteria, apply one fixed decision rule,
and spend build time only on sources that show real unmet needs *and* that you are allowed to read automatically.

## When to use
- Before building a scraper, collector or MCP integration for a new data source.
- When a niche-research tool or workflow keeps growing sources and you need to cut the weak ones.
- When you want to know which places show *needs that are not met yet*, not just what already exists.
- **Not for:** listing the communities where your users ask for tools → [research-where-users-ask](../research-where-users-ask/SKILL.md).
  Mining one competitor's reviews → [research-review-mining](../research-review-mining/SKILL.md).

## Inputs
- The product types you care about (Mac app, mobile app, SaaS, browser extension, physical product).
- A starting list of 20–50 candidate sources. Use the list in Step 1 if you have none.
- A browser and `curl`, to open each source and call its public endpoint once.

## The six criteria
Score each one **Strong / Medium / Weak**, with one sentence of reason and a link as evidence.

1. **Gap signal**: does the source show people *needing something that does not exist yet* (repeated questions,
   "is there an app that…", complaints, "I wish…", paying someone to do it by hand)? Or does it only show what
   already exists (a ranking, a trend line, a list of products)?
2. **Measurable interest**: can you rank topics by upvotes, views, review counts, reactions or search volume?
3. **Access**: exactly one of *free API* · *paid API* · *readable in a browser* · *manual only* · *forbidden*.
4. **Cost**: free · free tier · paid. Write the price, a link and the date you checked it. Never guess.
5. **Terms risk**: Low / Medium / High. Read the terms of service or API policy for automated access and commercial use.
6. **Product fit**: Mac · iOS / Android · SaaS · browser extension · physical.

## The decision rule
Write the rule down before you start scoring, so you cannot bend it for a source you like.

- Gap **Strong** + access is a free or paid API (not forbidden, not manual only) → **Build a collector.**
- Gap **Strong** but manual only or forbidden to automate → **Check by hand when needed.** Write down the manual steps.
- Gap **Weak** → **Drop.** Log why, so nobody re-evaluates it next month without new information.
- Gap **Medium** → choose hand-check or drop, and write one sentence on why.

## Steps
1. **List candidates (20 min).** Cover six groups, so you do not only look where you already look:
   - *Search and trends:* Google Autocomplete, "People also ask", Google Trends, YouTube and Amazon suggestions,
     Pinterest Trends, TikTok Creative Center, paid trend tools.
   - *Q&A communities:* Reddit, Stack Exchange (Ask Different, Super User, Software Recommendations), Hacker News
     (Ask HN), Apple Community, Product Hunt, Quora, X, Discord, Facebook groups.
   - *App stores and review sites:* App Store and Mac App Store reviews, Chrome Web Store, Firefox Add-ons, Shopify App
     Store, AlternativeTo, G2, Capterra, Trustpilot.
   - *Money evidence:* verified-revenue directories, business-for-sale marketplaces, template marketplaces (Etsy,
     Notion, Gumroad).
   - *Feature requests:* GitHub issues sorted by 👍, public feedback boards (Canny, Featurebase), Upwork / Fiverr jobs.
   - *Your own data:* Google Search Console queries for your site.
2. **Open each source for real (5 min each).** Load one real page, or call the public endpoint once with `curl`.
   Note what you got: data, a login wall, a JavaScript-only page, or an HTTP 403. "Could not open" is a result.
   Write it down.
3. **Read the terms (3 min each).** Search the terms for *scrape, crawl, robot, spider, data mining, automated,
   commercial*. Many large review sites forbid automated collection even of public pages. An official API with its
   own policy usually beats scraping the website.
4. **Score and decide (2 min each).** Fill the six criteria, then apply the rule. Do not make up prices or limits.
   Write `not measured` instead.
5. **Check what you already have.** Mark sources your tool already covers as *Already covered*, so you do not
   rebuild them.
6. **Pick the top 3 to build.** From *Build a collector*, prefer sources that (a) are free, (b) need no key or only a
   personal one, and (c) fit a pipeline you already have (for example "classify posts into topics → rank topics").
7. **Log the drops** with one line each in your research notes ([research-doc-organization](../research-doc-organization/SKILL.md)).

## 12 methods for finding gaps
Use them with the sources you keep. For each one, note whether your current tool already supports it.

1. **Forum-owned results.** Search a question on Google. If the top 3 results are Reddit, Quora or a vendor's community
   forum, nobody has written a good page or built a good tool for it yet.
2. **"X alternative", "X vs Y", "X free".** People who want to leave the tool they use now.
3. **"I'd pay for", "is there an app that", "wish there was".** Search these exact phrases in Q&A communities.
4. **Abandoned feature requests.** Issues with many 👍 that are still open after a year, or closed as "won't fix".
5. **Unanswered software requests.** Stack Exchange questions with high views and no accepted answer, or where the top
   answer is "there isn't one".
6. **Platform shifts.** A new OS version breaks old apps or opens a new API. The window is short. Watch rising queries
   and help forums in the weeks after each major release.
7. **Unbundling.** People use a big tool (spreadsheet, notes app, image editor) for one small, repeated job. A small app
   that does only that job can win.
8. **Best-selling templates.** A template that sells well is a workflow people want as a product.
9. **Popular extensions with low ratings.** Many users plus a bad score means demand is proven and the current answer
   is weak.
10. **Jobs-to-be-done from reviews.** Read reviews as "when I use it · the job I need done · why I switched".
11. **Repeated freelance jobs.** A task people pay someone to do by hand every week.
12. **Your own Search Console.** Queries with many impressions where your site has no real answer.

## Prompt (copy-paste)
Works best with web browsing on. Replace everything in `{{ }}`.

````text
You are a research analyst. Score data sources for finding unmet product needs.

Product types I care about: {{e.g. Mac apps, browser extensions}}
Sources to score: {{list, or "propose 30 across search, Q&A, app stores, money evidence, feature requests, own data"}}
Today's date: {{YYYY-MM-DD}}

For each source:
1. Open one real page or call its public endpoint once. Say what you got (data / login wall / JS-only / HTTP code).
2. Find its terms of service or API policy. Quote the idea (not long text) about scraping, automated access and
   commercial use, with the link.
3. Score: Gap signal, Measurable interest (Strong/Medium/Weak + one-sentence reason); Access (free API / paid API /
   browser / manual only / forbidden); Cost (price + link + date, or "not measured"); Terms risk (Low/Medium/High);
   Product fit.
4. Decide with this fixed rule: Strong gap + API access → Build a collector. Strong gap + manual/forbidden → Check by
   hand (give the manual steps). Weak gap → Drop. Medium → hand-check or drop, with a reason.
Never invent prices, rate limits, star counts or numbers. Write "not measured".
End with: the top 3 sources to build (free, low terms risk, best gap signal) and the sources you could not open.
````

## Example output

> **Illustrative example.** The format of one scored source. Re-check every number on the day you use it.

### Stack Exchange (Ask Different, Super User)
- **Decision: Build a collector.**
- **Gap signal:** Strong. The `software-recommendation` tag is full of "an app that does X on macOS" questions, some
  answered "there isn't one".
- **Measurable interest:** Strong. The API returns `score`, `view_count` and `is_answered`.
- **Access:** free API. A test call without a key showed `quota_max: 300` requests per day.
- **Cost:** free.
- **Terms risk:** Medium. Content is CC BY-SA, so credit the source. Low request volume for internal research.
- **Product fit:** Mac, iOS, Windows desktop.
- Checked 2026-10-26: [API call](https://api.stackexchange.com/2.3/search/advanced?order=desc&sort=votes&tagged=software-recommendation&site=apple)

What a full scoring run of about 50 sources tends to show (checked 2026-10-26, re-check before you rely on it):

- **Usually worth a collector:** Stack Exchange API, GitHub issue search sorted by reactions
  ([GitHub AUP](https://docs.github.com/en/site-policy/acceptable-use-policies/github-acceptable-use-policies) allows
  research on public data), Hacker News via the [Algolia API](https://hn.algolia.com/api).
- **Strong but hand-check only:** Apple Community, AlternativeTo, Shopify App Store reviews, Canny / Featurebase boards,
  Upwork jobs.
- **Usually dropped:** paid trend tools that only show what already rises, and review sites whose terms forbid automated
  collection even of public pages.
- **Paid but strong:** the X API charges per post read ([pricing](https://docs.x.com/x-api/getting-started/pricing)).
  Narrow queries plus a 24-hour cache keep it cheap.

## Common mistakes
- **Scoring on reputation instead of opening the source.** A source that returns HTTP 403 or a JavaScript shell is
  not something you can build on. Write that down.
- **Treating trend data as a gap.** A rising trend shows interest, not an unmet need. Pair it with a Q&A or complaint
  source.
- **Ignoring the terms because the page is public.** Several big review sites forbid collection "even of publicly
  available content". Use official APIs, or check by hand.
- **Guessing prices and rate limits.** Write the number, the link and the date, or `not measured`.
- **Building a new pipeline per source.** Most Q&A sources fit one shape: post → topic → ranked gap table. Add
  collectors to that one pipeline.
- **Trusting community MCP servers blindly.** Read the server code first. Disable write or delete tools, and keep API
  keys out of URLs.

## Related skills
- [research-where-users-ask](../research-where-users-ask/SKILL.md): the community map to start your candidate list.
- [research-review-mining](../research-review-mining/SKILL.md): go deep on one competitor once a source points to a gap.
- [research-source-finding](../research-source-finding/SKILL.md): find trustworthy facts for each open question.
- [research-doc-organization](../research-doc-organization/SKILL.md): keep the scores, drops and decisions in one place.

## Credits
Written by @nvminhtu. Sources: [Stack Exchange API](https://api.stackexchange.com/docs),
[HN Search API](https://hn.algolia.com/api), [GitHub REST search](https://docs.github.com/en/rest/search/search),
[GitHub Acceptable Use Policies](https://docs.github.com/en/site-policy/acceptable-use-policies/github-acceptable-use-policies),
[X API pricing](https://docs.x.com/x-api/getting-started/pricing), [Trustpilot terms](https://legal.trustpilot.com/for-everyone/terms-of-use-for-consumers),
[G2 terms](https://legal.g2.com/terms-of-use), [Apple website terms](https://www.apple.com/legal/internet-services/terms/site.html).
