# Metrics glossary: GA4 + Search Console

UI label, API name (so an agent can call the GA4 Data API or MCP `run_report` with the exact field), the plain
meaning, and the mistake people make. API names checked against the
[GA4 Data API schema](https://developers.google.com/analytics/devguides/reporting/data/v1/api-schema) on 2026-10-19.

## GA4 metrics

| UI label | API name | Plain meaning | Common mistake |
|---|---|---|---|
| Active users | `activeUsers` | People who had an engaged session (or were active) in the range. GA4's main "Users" | Adding up daily users to get a monthly number (the same person counts each day) |
| Total users | `totalUsers` | Everyone who triggered any event | Using it as "real audience"; it includes one-second visits |
| New users | `newUsers` | People on their first visit | Thinking new + returning always equals the total |
| Sessions | `sessions` | Visits. One user can have many | Comparing sessions of one channel with users of another |
| Engaged sessions | `engagedSessions` | Visits that lasted over 10 s, had a key event, or 2+ page views ([help](https://support.google.com/analytics/answer/12195621)) | — |
| Engagement rate | `engagementRate` | Engaged sessions ÷ sessions | Comparing a blog (people read and leave) with a checkout page |
| Bounce rate | `bounceRate` | Sessions that were *not* engaged (1 − engagement rate) | Reading it like the old Universal Analytics bounce rate |
| Views | `screenPageViews` | Page (or app screen) views, repeats included | Ranking pages to grow by views instead of landings |
| User engagement | `userEngagementDuration` | Total time the page was in focus | Dividing by sessions and calling it "time on page" |
| Average session duration | `averageSessionDuration` | Average visit length | Treating long = good (could be a confused user) |
| Event count | `eventCount` | How many times events fired | Counting `page_view` events as "success" |
| Key events | `keyEvents` | Events you marked as success (sign-up, lead, store click…) | Marking `scroll` or `page_view` as key events |
| Session key event rate | `sessionKeyEventRate` | Share of sessions with at least one key event | Judging it on fewer than ~50 sessions |
| User key event rate | `userKeyEventRate` | Share of users who did at least one key event | Comparing it with the session rate |

## GA4 dimensions

| UI label | API name | Plain meaning | Common mistake |
|---|---|---|---|
| Session default channel group | `sessionDefaultChannelGroup` | Channel of *this* visit (Organic Search, Direct, Referral, Organic Social, Email, Unassigned…) | Expecting your UTM medium names to appear here as-is ([rules](https://support.google.com/analytics/answer/9756891)) |
| Session source · Session medium | `sessionSource`, `sessionMedium` | The two halves of source / medium, for filters | Filtering `sessionSourceMedium` with `contains "x"` (matches every source with an x in it) |
| Session campaign | `sessionCampaignName` | The `utm_campaign` value | Expecting old untagged posts to show a campaign |
| Session source / medium | `sessionSourceMedium` | The exact `utm_source / utm_medium` (or `google / organic`) | Mixed-case UTMs split one channel into many rows |
| First user default channel group | `firstUserDefaultChannelGroup` | Channel that brought the person the *first* time | Mixing it with session channel in one comparison |
| Landing page + query string | `landingPagePlusQueryString` | First page of the visit | Forgetting query strings split the same page into rows |
| Page path | `pagePath` | Any page viewed, without the domain | Using it to judge which page "brings" traffic |
| Landing page | `landingPage` | First page of the visit, without query string | — (use this one to group a page's UTM variants) |
| Event name | `eventName` | Name of the event | Typos create a second event (`signup` vs `sign_up`) |
| Is key event | `isKeyEvent` | Whether an event is marked as a key event | Assuming an event is a key event without checking |
| Device category · Country · Date | `deviceCategory`, `country`, `date` | Splits for "who and when" | Splitting a small week by three dimensions and reading noise |

## Search Console metrics

From [Performance report help](https://support.google.com/webmasters/answer/7576553), checked 2026-10-19.
Search Console API dimension names: `query`, `page`, `country`, `device`, `date`.

| Metric | Plain meaning | Common mistake |
|---|---|---|
| Clicks | Clicks from Google Search results to your site | Expecting it to equal GA4 Organic Search sessions (different counting, consent, filters) |
| Impressions | Times your site appeared in results | Thinking someone *saw* it (a result far down the page still counts) |
| CTR | Clicks ÷ impressions | Comparing CTR of a brand query with a generic one |
| Average position | Average position of your *topmost* result | Reading 8.4 as "I'm 8th" — it's an average over many searches |

Search Console keeps **16 months** of data; data in GA4 arrives **48 hours** after Search Console collects it
([help](https://support.google.com/analytics/answer/10737381)); the newest days in Search Console are preliminary.
