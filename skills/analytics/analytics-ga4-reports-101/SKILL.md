---
name: analytics-ga4-reports-101
description: Learn to read Google Analytics 4 and Google Search Console without drowning in menus - the 6 GA4 reports that matter (Realtime, Traffic acquisition vs User acquisition, Pages and screens, Landing page, Events and Key events, Explorations) plus the Search Console Performance report (clicks, impressions, CTR, average position), what each metric means in plain words with its API name, the misreadings that lead to wrong decisions, and a 7-lesson practice path in your own property. Use when someone says "learn GA4", "how to read Google Analytics", "what does engagement rate mean", "users vs sessions", "where does my traffic come from", "which pages bring traffic", "Search Console for beginners", "what is average position", "impressions but no clicks", "GA4 is confusing", or has GA4 set up and never opens it.
license: MIT
metadata:
  category: analytics
  difficulty: beginner
  time: 1-2 h (read + practice), then 15 min a week
  version: 1.0.0
  author: nvminhtu
---

# GA4 + Search Console Reports 101

> In one or two hours you'll know the 7 screens worth opening, what each number means, and you'll have written your
> first one-paragraph "where my traffic comes from and what it does" note from your own data.

## Goal
GA4 has hundreds of reports; a maker needs about seven. This skill teaches those seven, the metrics on them (with the
API name so an AI agent can pull the same numbers), and the common misreadings. The output is a short baseline note
you'll compare against every week.

## When to use
- GA4 is set up ([analytics-ga4-setup](../analytics-ga4-setup/SKILL.md)) and has at least 7 days of data.
- You open GA4, see a wall of charts, and close it.
- You're about to decide something (which channel, which page to improve) from a number you're not sure about.
- **Not for:** setting things up ([analytics-ga4-setup](../analytics-ga4-setup/SKILL.md)), choosing events
  ([analytics-tracking-plan](../analytics-tracking-plan/SKILL.md)).

## Inputs
- A GA4 property with 7+ days of data (28 is better), Viewer role or higher.
- Search Console verified and linked (Search Console data appears with a 2–3 day delay).
- Your key event name from the [tracking plan](../analytics-tracking-plan/SKILL.md).
- 1–2 hours. Do the lessons in [references/learning-path.md](references/learning-path.md) with your property open.

## Steps
Set the date range to **last 28 days** and turn on *Compare to: preceding period* for every report below.
Plain-word meanings and API names for every metric are in
[references/metrics-glossary.md](references/metrics-glossary.md).

1. **Realtime — "is it working right now?"** Reports → Realtime. Use it to check a new link, post or tag, not to
   judge performance. *Read:* users in the last 30 minutes, by source and by event.
2. **Traffic acquisition — "where do visits come from?"** Reports → Acquisition → Traffic acquisition. Rows are
   *Session default channel group* (`sessionDefaultChannelGroup`). *Read:* `sessions`, `engagedSessions`,
   `engagementRate`, `keyEvents` per channel. Switch the row dimension to *Session source / medium* to see your
   UTM links. This report covers new and returning users, by their latest session
   ([help](https://support.google.com/analytics/answer/12923437)).
3. **User acquisition — "where do *new* people first come from?"** Same menu. Rows are *First user default channel
   group* (`firstUserDefaultChannelGroup`). Use it to judge which channel **finds** new people; use Traffic
   acquisition to judge which channel brings **visits** (including returning users). Don't mix them in one sentence
   ([user vs traffic acquisition](https://support.google.com/analytics/answer/14731736)).
4. **Pages and screens — "what do people read?"** Reports → Engagement → Pages and screens (`pagePath`,
   `screenPageViews`, `userEngagementDuration`). Shows every page viewed, wherever the visit started.
5. **Landing page — "which page brings people in?"** Reports → Engagement → Landing page
   (`landingPagePlusQueryString`). This is the one to use for growth decisions: the first page of the visit, with
   sessions, engagement and key events. A page with many views but few landings is read *after* arriving; a page with
   many landings is a door.
6. **Events and Key events — "did visits do the thing?"** Reports → Engagement → Events (`eventName`,
   `eventCount`), and the *Key events* column in reports 2–5. *Read:* key events by channel and by landing page; the
   rate is `sessionKeyEventRate`.
7. **Search Console Performance — "what do people search to find me?"** In
   [Search Console](https://search.google.com/search-console) → Performance → Search results (or GA4 → Reports →
   Search Console → Queries once the collection is published). Four numbers: **clicks**, **impressions**, **CTR**
   (clicks ÷ impressions) and **average position** (the average position of your *topmost* result)
   ([definitions](https://support.google.com/webmasters/answer/7576553)). Tabs *Queries* and *Pages* are the two
   you need.
8. **Explorations — only when a report can't answer.** Explore → Free form, to cross two dimensions (e.g. landing
   page × channel). Explorations respect the data retention setting (2 or 14 months)
   ([help](https://support.google.com/analytics/answer/7667196)); standard reports don't.
9. **Write the baseline note (15 min).** Use the prompt below with your numbers. Save it as
   `growth/analytics-baseline-YYYY-MM-DD.md`. Next week, compare these 5 numbers (the same fields an agent pulls):

   | # | Number | Where | API names |
   |---|---|---|---|
   | 1 | Sessions by channel (top 5) | Traffic acquisition | `sessions` × `sessionDefaultChannelGroup` |
   | 2 | Engaged sessions and rate | Traffic acquisition | `engagedSessions`, `engagementRate` |
   | 3 | Top 5 landing pages | Landing page | `sessions`, `keyEvents` × `landingPagePlusQueryString` |
   | 4 | Key events by channel | Traffic acquisition | `keyEvents`, `sessionKeyEventRate` |
   | 5 | Top 5 Google queries | Search Console → Queries | `query`: clicks, impressions, CTR, position |

   Write a number only if the report shows it. "No data" with the reason is a valid answer.

## Prompt (copy-paste)
Works in Claude, ChatGPT, Gemini, Cursor. Paste exported tables (CSV or copied rows), or let an agent with the GA4
and Search Console MCP servers pull them read-only. Replace everything in `{{ }}`.

````text
You are a patient analytics teacher for a solo maker. My site: {{url}}. My key event: {{event name}}.
Date range: {{last 28 days vs preceding 28 days}}.

Here are my tables (don't invent any number that isn't in them):
- Traffic acquisition by session default channel group: sessions, engaged sessions, engagement rate, key events
  {{paste}}
- Landing page: sessions, engagement rate, key events {{paste}}
- Search Console Queries: query, clicks, impressions, CTR, average position {{paste top 20}}

Write my baseline note in plain words, max 200 words:
1. Where visits come from (top 3 channels, with change vs previous period).
2. Which 3 landing pages bring people in, and which one turns visits into key events best.
3. What people search to find me: top queries by impressions, and any query with many impressions but CTR under 2%.
4. ONE thing that looks wrong or surprising, and the likely reason (tracking, a missing filter, seasonality, a post).
5. ONE question to check next week.
Name every metric the way GA4 shows it. If a table is empty or too small to judge (fewer than ~50 sessions), say
"not enough data" instead of guessing. Explain any term I might not know in one short sentence.
````

**Agent mode.** With the Google Analytics MCP server an agent can pull each table itself, read-only, with
`run_report` (the dimensions and metrics in the [glossary](references/metrics-glossary.md); two `dateRanges`: last
28 days and the 28 before) and `run_realtime_report` for lesson 1. Search Console rows come from the Search Console
MCP server (`get_search_analytics`, dimension `query` or `page`) or the GA4 Search Console reports. It shows the user
the table it read before writing the note, and never fills a number it didn't read.

## Example output

> **Illustrative example.** Numbers are made up to show the format.

> **Baseline, 2026-09-21 → 2026-10-18 (vs previous 28 days).**
> Visits mostly come from **Organic Search** (412 sessions, +18%), then **Direct** (160, −4%) and **Organic Social**
> (95, +60% after the Reddit thread on 10-02). Organic Search also has the best engagement rate (61%).
> The top door is `/blog/habit-streak-tips` (230 sessions) but it brings almost no `store_click`; the product page
> `/apps/habit` has only 70 sessions yet 14 key events (20% session key event rate).
> People find me with "how to keep a habit streak" (3,100 impressions, position 7.8, CTR 1.4%): many impressions, few
> clicks → the title or snippet doesn't win the click.
> Surprising: 40 sessions from my own city on a Sunday → internal filter is still in Testing.
> Next week: does a link from the blog post to `/apps/habit` raise `store_click`?

## Common mistakes
- **Comparing users with sessions.** One user can have many sessions. Pick one unit per comparison.
- **Using Pages and screens to pick pages to grow.** It counts every view. Use **Landing page** for "which page
  brings people in".
- **Reading bounce rate like Universal Analytics.** In GA4, bounce rate is simply the share of sessions that were
  *not engaged* (engaged = over 10 seconds, or a key event, or 2+ page views;
  [help](https://support.google.com/analytics/answer/12195621)).
- **Treating average position as a rank.** It's an average of your topmost result across all impressions. A query
  at 8.4 may show at 3 for some people and 15 for others.
- **Judging a week with 30 sessions.** Small numbers swing a lot. Use 28 days and look at the direction.
- **Reading Search Console's last 2 days.** They're preliminary and change.
- **Reading Realtime as a trend.** It's the last 30 minutes. Compare weeks, not minutes.
- **Comparing a period with a launch, a Reddit spike or a holiday in it** without saying so. Write the event next to
  the number.
- **Trusting a card with "Google Analytics has applied thresholding".** Rows are withheld; widen the date range or
  drop demographic dimensions ([data thresholds](https://support.google.com/analytics/answer/9383630)).
- **"Direct" = people typing my URL.** It also holds untagged links from apps, chats and email. Tag your links
  ([UTM convention](../analytics-tracking-plan/references/utm-convention.md)).

## Related skills
- [analytics-ga4-setup](../analytics-ga4-setup/SKILL.md) and
  [analytics-tracking-plan](../analytics-tracking-plan/SKILL.md): do these first.
- Next (*planned*, see [the area plan](../../../docs/plan-analytics-ga4.md)): `analytics-traffic-diagnosis` turns
  this baseline into a weekly check, and `analytics-traffic-growth-loop` picks one lever a week from the data.
- [launch-geo-aeo-feature-preview](../../launch/launch-geo-aeo-feature-preview/SKILL.md): reading AI-assistant
  referrals and AI Overviews impressions.
- Free course: [Google Analytics Certification on Skillshop](https://skillshop.withgoogle.com).

## Credits
Written by [@nvminhtu](https://github.com/nvminhtu). Sources: Google Analytics Help, Search Console Help and the GA4
Data API schema ([api-schema](https://developers.google.com/analytics/devguides/reporting/data/v1/api-schema)),
linked inline (checked 2026-10-19).
