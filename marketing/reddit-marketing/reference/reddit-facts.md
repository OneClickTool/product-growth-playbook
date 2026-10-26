# Reddit facts, with sources

Checked 2026-10-12. Official = Reddit's own policy, help or blog pages. Secondary = news, third-party guides or
community posts; treat as a hint and verify before relying on it.

## Rules and spam

| Fact | Source | Type |
|---|---|---|
| Rule 2: participate authentically, no spam, no vote or content manipulation. Rule 5: don't mislead about who you are | [Reddit Rules](https://redditinc.com/policies/reddit-rules) | Official |
| Promotion isn't spam by itself; spam is repeated, unsolicited or automated posting, mass DMs, bots/AI posting for you, masked links | [Reddit Help: Spam](https://support.reddithelp.com/hc/en-us/articles/360043504051-Spam) | Official |
| Each community sets its own promotion rules; some use a 10% self-promotion ratio | [Reddit Help: keeping spam out of a community](https://support.reddithelp.com/hc/en-us/articles/28012014962580-How-do-I-keep-spam-out-of-my-community) | Official |
| Reddit replaced sitewide shadowbans with account suspensions in 2015 | [TechCrunch, 2015](https://techcrunch.com/2015/11/11/reddit-account-suspensions/) | Secondary |
| Moderators can still hide a user's posts in their subreddit through AutoModerator | [Wikipedia: Shadow banning](https://en.wikipedia.org/wiki/Shadow_banning) | Secondary |

## Ranking

| Fact | Source | Type |
|---|---|---|
| The archived "hot" sort: log10 of the vote score plus the post's age term (seconds / 45,000). So votes count on a log scale and age pushes posts down on a fixed clock. Current ranking isn't published | [reddit-archive/reddit](https://github.com/reddit-archive/reddit) (`r2/r2/lib/db/_sorts.pyx`) · explained in [socialboostdigital, 2026](https://socialboostdigital.com/blog/reddit-ranking-algorithm-2026) | Code (archived) |
| The "Best" comment sort (2009) ranks by the lower bound of the Wilson confidence interval on the upvote share: few votes = low confidence = stays low | [Evan Miller](https://www.evanmiller.org/how-not-to-sort-by-average-rating.html) · [Salihefendic](https://medium.com/hacking-and-gonzo/how-reddit-ranking-algorithms-work-ef111e33d0d9) · `_sorts.pyx` (`confidence`) | Secondary + Code |
| Moderators can filter by Contributor Quality Score (since Sep 2023): 5 tiers from signals such as past account actions and account verification | r/modnews announcement, read via [mirror](https://lr.vern.cc/r/modnews/comments/16is6dh/contributor_quality_score_available_to_all/) | Secondary |
| Reddit Answers (test from Dec 2024) summarizes Reddit conversations and links back to them | [Engadget](https://www.engadget.com/social-media/reddit-introduces-ai-powered-reddit-answers-search-feature-140028655.html) | Secondary |

## Karma

| Fact | Source | Type |
|---|---|---|
| Karma comes from votes on posts and comments (and awards), but Reddit doesn't publish the formula; it isn't one point per vote | [Android Authority](https://androidauthority.com/reddit-karma-explained-3156433) | Secondary |
| Many subreddits set karma or account-age minimums to post | subreddit rules pages · [docs/subreddits](../../../docs/subreddits/README.md) | Per subreddit |

## Profile

| Fact | Source | Type |
|---|---|---|
| Up to 5 social links on a profile, shown as buttons under the name, not counted in the bio | 2021 [r/changelog](https://www.reddit.com/r/changelog/) announcement (read via a mirror) · [Adweek how-to](https://www.adweek.com/?p=1376335) | Secondary |

## Search and discovery

| Fact | Source | Type |
|---|---|---|
| Reddit and Google expanded their partnership in 2024 (Reddit content in Google products, Reddit using Vertex AI) | [Reddit blog, 2024](https://redditinc.com/blog/expanding-our-partnership-with-google) | Official |
| Reddit Pro is a free set of business tools; its Trends tab tracks keyword volume, communities and conversations | [TechCrunch, Jan 2025](https://techcrunch.com/2025/01/07/reddit-intros-new-trends-tools-for-businesses-and-an-ama-ad-format/) · [Search Engine Land](https://searchengineland.com/reddit-business-analytics-tools-ama-ads-450270) | Secondary (launch coverage) |
| F5Bot sends free email alerts for keywords on Reddit and Hacker News | [f5bot.com](https://f5bot.com/) | Tool's own page |
| On r/macapps, comparison / "alternative to" posts had the highest average score in an analysis of 496 top posts | [upvote.net, 2026](https://upvote.net/blog/macapps-reddit-analysis) | Secondary |

## Ads

| Fact | Source | Type |
|---|---|---|
| Self-serve minimum is about $5 per day per campaign; lifetime minimums are reported differently by different guides | [WordStream](https://www.wordstream.com/blog/reddit-advertising-cost) · [Stackmatix, 2026](https://stackmatix.com/blog/reddit-ads-cost-guide-2026) | Secondary — check Ads Manager |

## Not verified (don't rely on)
- Exact karma thresholds of subreddits you haven't read yourself.
- "Best time to post" charts: each subreddit differs; look at its *new* queue.
- Any claim that a specific number of upvotes in the first hour guarantees the front page.
