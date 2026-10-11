# Research log · 2026-10-11 · X marketing for indie devs selling software

## Questions
1. How to write short daily posts from products already built?
2. Which X tips are backed by evidence, and which are folklore?
3. What does X Premium actually give, and how to use it for traffic?
4. Which open-source repos and agent skills for X are worth using to get the first paying subscribers?

## Sources read

| Source | Type | What we took |
|---|---|---|
| [xai-org/x-algorithm README](https://github.com/xai-org/x-algorithm) | Official code | Pipeline, action list, author diversity, OON discount, new-author boost, 48 h filter, Under the Hood tool |
| [`home-mixer/params/param.rs`](https://github.com/xai-org/x-algorithm/blob/main/home-mixer/params/param.rs) | Official code | Default action weights (see [x-algorithm-and-premium-facts.md](x-algorithm-and-premium-facts.md)) |
| [About X Premium](https://help.x.com/en/using-x/x-premium) | Official help | Tiers, US prices, reply prioritization by tier, checkmark rules, Articles, Media Studio |
| [X automation rules](https://help.x.com/en/rules-and-policies/x-automation) (updated April 2026) | Official policy | No duplicate posts, no keyword auto-replies, no website scripting |
| GitHub API for 10 repos | Data | Stars, licence, last push → [x-repos.md](x-repos.md) |
| [Social Media Today on a Buffer study](https://www.socialmediatoday.com/news/report-shows-paying-for-x-twitter-premkum-has-significant-reach-benefits/801881) | Third party | "Premium ≈ 10× reach" claim; **not used** as fact (correlation, not X data) |
| Third-party Premium guides (tweetarchivist, autotweet, tryordinal) | Third party | Only to cross-check; they disagreed with each other on tier details, so the help page wins |

## Findings
1. **Ranking is personal and prediction-based.** Weights multiply each viewer's predicted probability, not raw counts.
2. **Conversation and shares beat likes.** Copy-link share 20, reply/quote/DM share 5, like 0.5.
3. **Negative feedback is expensive.** Not interested −47.5, mute −58.8, report −234.
4. **Two-day life.** Posts older than 48 hours leave For You.
5. **Premium's documented growth lever is reply prioritization**, larger on higher tiers. Nothing in the code shows
   Premium boosting original posts in For You.
6. **Repos:** the best-maintained X writing skill is `sergebulaev/x-skills` (MIT); general marketing at scale is
   `coreyhaines31/marketingskills` (54k stars). Several small X repos scrape the website, which breaks X's rules.
7. **First dollar** depends more on the profile → landing → trial chain than on post volume.

## Not verified (don't quote as fact)
- Best posting times, hashtag penalties, exact link-post penalties.
- Production values of the ranker weights (the repo shows defaults).
- Creator Subscriptions eligibility thresholds (the help page for it returned 404 on 2026-10-11; check the
  Monetization tab in the app).

## Output of this research
Skills: [social-x-growth](../skills/social-x-growth/SKILL.md), [social-x-reply](../skills/social-x-reply/SKILL.md),
[social-x-profile-funnel](../skills/social-x-profile-funnel/SKILL.md). Docs: [../docs/](../docs/).
