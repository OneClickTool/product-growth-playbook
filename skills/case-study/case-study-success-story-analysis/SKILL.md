---
name: case-study-success-story-analysis
description: Learn from public growth stories of indie apps and SaaS (founder interviews, build-in-public posts, revenue milestones, launch retrospectives) by comparing 5 stories similar to your product with 2 failures, spotting survivorship bias, and extracting the tactics you can repeat this month. Use when looking for proven growth tactics, when stuck and wanting to see how similar products grew, or when someone asks "how did X get their first users", "indie app success stories", "what worked for similar apps", or "case studies for my niche".
license: MIT
metadata:
  category: case-study
  difficulty: beginner
  time: 60-90 min
  version: 1.0.0
  author: nvminhtu
---

# Success Story Analysis

> In about an hour you will have 5 comparable success stories and 2 failures side by side, the tactics they share,
> and 3 you can try this month, filtered for luck and survivorship bias.

## Goal
Borrow what actually worked for products like yours, and avoid copying tactics that only worked because of timing,
an existing audience, or luck.

## When to use
- You don't know which channel to bet on next.
- You want proof that a tactic works for products like yours (same platform, price and team size).
- **Not for:** your direct competitors → [case-study-competitor-teardown](../case-study-competitor-teardown/SKILL.md).

## Inputs
- Your product's profile: platform, price model, audience, team size, current stage.
- 1–2 hours of reading time.

## Where to find stories

| Source | What you get | Link |
|---|---|---|
| Indie Hackers | Founder interviews and milestone posts, often with revenue | [indiehackers.com/stories](https://www.indiehackers.com/stories) |
| Starter Story | Structured founder interviews (some content is paid) | [starterstory.com](https://www.starterstory.com/) |
| Hacker News | "Show HN" launches and "how I got to $X" posts, with honest comments | `site:news.ycombinator.com "how I"` |
| Build-in-public posts | Monthly revenue and user updates on X, LinkedIn and blogs | search `"MRR" OR "downloads" <your niche> indie` |
| Reddit | Retrospectives in r/SideProject, r/SaaS, r/iOSProgramming, r/androiddev | subreddit search: *Top → Past year* |
| Failory | Interviews about startups that **failed** | [failory.com](https://www.failory.com/) |
| Talks and podcasts | Launch retrospectives with numbers | YouTube search: `<niche> app launch retrospective` |

## Steps
1. **Define "similar" (5 min).** Same platform, a similar price model, a solo or small team, and ideally the same
   audience. A VC-funded team with a sales force is not a comparable for a solo iOS app.
2. **Collect 5 successes and 2 failures (30 min).** Save the link and date of each.
3. **Extract the same fields from each (20 min).** Starting point (audience? budget?), time to the first 100 users and
   **how**, the turning point, pricing changes, the main channel after month 6, and what they say didn't work.
4. **Filter for bias (10 min).** For each tactic, ask:
   - Did it depend on something you don't have (a big audience, press contacts, being early to a trend)?
   - Did the failures try the same thing? If so, it's not what made the difference.
   - Is there a number, or only a claim?
5. **Pick 3 tactics (10 min)** that appear in 2+ successes, that the failures didn't rely on, and that you can start
   this month. Link each to a skill in this repo.
6. **Save it** as a research note ([research-doc-organization](../../research/research-doc-organization/SKILL.md))
   and re-check in 30 days: did the tactic work for you?

## Prompt (copy-paste)
Works best with web browsing. Replace everything in `{{ }}`.

````text
You are a growth researcher. Help me learn from public success stories similar to my product.

My product: {{what it does}}   Platform: {{...}}   Price model: {{...}}   Team: {{solo / 2-5 / ...}}
Audience: {{...}}   Stage: {{idea / launched / N users / $X MRR}}

1. Find 5 public growth stories of comparable products (same platform, price model, small team) and 2 public
   failure stories in a similar niche. For each: link, date, and whether numbers are given. Never invent a story,
   a link or a number. If you can't browse, tell me which searches to run instead.
2. For each story extract: starting point (audience, budget), how they got the first 100 users, the turning point,
   pricing changes, main channel after 6 months, what didn't work.
3. Table of tactics: tactic | # successes using it | used by failures too? | depends on something unusual? | evidence strength.
4. Recommend 3 tactics I can start this month, with the first concrete step for each.
````

## Example output

> **Illustrative example.** Fictional stories, shown for format.

*My product:* a Mac utility, one-time purchase, solo developer.

| Tactic | Successes (of 5) | Failures used it? | Needs something unusual? | Verdict |
|---|---|---|---|---|
| Launched on r/macapps + Product Hunt the same week | 4 | 1 of 2 | No | ✅ Try |
| Free tier + one-time "Pro" unlock | 4 | 0 | No | ✅ Try |
| Viral X thread from an existing 20k following | 2 | 0 | **Yes**, existing audience | ❌ Not comparable |
| Got featured by Apple | 1 | 0 | Luck / timing | ⚠️ Can't plan on it |
| Weekly changelog posts that turned into SEO pages | 3 | 0 | No | ✅ Try |

**This month:** r/macapps + PH launch week → [launch-post-writing](../../launch/launch-post-writing/SKILL.md);
a one-time Pro unlock → [monetization-free-trial-vs-freemium](../../monetization/monetization-free-trial-vs-freemium/SKILL.md);
a public changelog.

## Common mistakes
- **Survivorship bias.** You only read stories from the winners. Always include failures that tried the same thing.
- **Non-comparable stories.** A funded team's playbook rarely fits a solo developer.
- **Believing round numbers without proof.** "$10k MRR in 30 days" with no screenshot or detail is a claim, not data.
- **Collecting stories instead of acting.** Cap it at 7 stories and 3 tactics.

## Related skills
- [case-study-competitor-teardown](../case-study-competitor-teardown/SKILL.md): the same idea, for your direct rivals.
- [case-study-write-your-own](../case-study-write-your-own/SKILL.md): turn your results into a story others can learn from.
- [research-source-finding](../../research/research-source-finding/SKILL.md): judge how trustworthy each story is.

## Credits
Written by [@nvminhtu](https://github.com/nvminhtu).
