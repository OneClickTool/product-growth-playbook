---
name: research-source-finding
description: Find trustworthy sources for a product or growth question (official docs and policies, real data, real users, then articles), search them efficiently with search operators, and record each source with a date and a confidence level. Use when researching a market, a store rule, a competitor or a pricing question, when someone asks "where do I find data on X", "is this still true", "find sources for", or before writing any skill, plan or decision that depends on facts.
license: MIT
metadata:
  category: research
  difficulty: beginner
  time: 30-45 min
  version: 1.0.0
  author: nvminhtu
---

# Source Finding

> In 30–45 minutes you will have 5–10 sources for one question, ranked by how much you can trust them,
> each with a link, a date and a one-line summary.

## Goal
Answer questions with evidence you can point to, not with the first blog post Google shows. Know which source
wins when two disagree.

## When to use
- Before a decision that depends on facts: a price, a store rule, a market's size, a launch channel.
- When a "fact" you found has no date or no source.
- **Not for:** finding what users say about software → [research-where-users-ask](../research-where-users-ask/SKILL.md).
  Storing what you find → [research-doc-organization](../research-doc-organization/SKILL.md).

## Inputs
- **One** clear question, written as a sentence. ("What is Apple's commission on subscriptions for a new small developer?")
- Why you need it, and how exact the answer has to be.

## The source ladder (trust top to bottom)

| Level | What | Examples |
|---|---|---|
| 1. Official | The platform or company that makes the rule | [App Store Review Guidelines](https://developer.apple.com/app-store/review/guidelines/), [App Store Connect Help](https://developer.apple.com/help/app-store-connect/), [Play Console Help](https://support.google.com/googleplay/android-developer/), [Chrome Web Store docs](https://developer.chrome.com/docs/webstore/), pricing pages |
| 2. Data | Numbers you can check yourself | [Google Trends](https://trends.google.com/), store charts and search autocomplete, your own analytics, public company reports |
| 3. Real users | What people actually say and do | Reviews, forums, Reddit, [Hacker News](https://news.ycombinator.com/), communities → [research-where-users-ask](../research-where-users-ask/SKILL.md) |
| 4. Practitioners | People who did it and share numbers | Indie Hackers posts, founder blogs, conference talks, industry reports that show their method |
| 5. Articles | Summaries by others | Blog posts, listicles, AI answers. Use them to **find** level 1–4 sources, never as the final source |

When sources disagree, the higher level wins. When sources on the same level disagree, the newer one wins.

## Steps
1. **Write the question and its "good enough" bar (5 min).** Exact number? A range? Yes or no?
2. **Go to level 1 first (10 min).** Search the official site directly: `site:developer.apple.com subscription commission`.
3. **Use search operators (10 min).**
   - `site:reddit.com "alternative to notion"`: search one site.
   - `"exact phrase"`: only pages with that phrase.
   - `intitle:pricing` / `inurl:changelog`: words in the title or URL.
   - `filetype:pdf "state of"`: reports.
   - `before:2026-01-01` / `after:2025-06-01`: limit by date (Google).
   - `-word`: exclude results.
4. **Check every source (5 min).** Who wrote it? When (no date means low trust)? Is it first-hand? Does a second
   source agree?
5. **Record it (5 min).** For each source: link, date published, date you checked, level (1–5), and a one-line
   summary. Use `assets/sources-template.md` from [research-doc-organization](../research-doc-organization/SKILL.md).
6. **Write the answer with confidence.** High (level 1–2, two sources agree), medium (level 3–4, or one source),
   low (level 5 only, or sources disagree). Say which one it is.

## Prompt (copy-paste)
Replace everything in `{{ }}`. Works best in an AI assistant with web search turned on.

````text
You are a careful research assistant. Answer this question with sources I can verify.

Question: {{one sentence}}
Why I need it / how exact: {{...}}
Region / platform / date that matters: {{e.g. US App Store, as of this month}}

Rules:
- Rank sources: 1 official (the platform or company itself), 2 data, 3 real users, 4 practitioners with numbers,
  5 articles. Prefer level 1-2. Use level 5 only to find better sources.
- For each source give: title, link, publish date, level, and a one-line summary of what it says.
- If you can't find a source for a claim, say "no source found". Never invent a link or a number.
- End with: the answer, confidence (high / medium / low) and why, and what would change the answer.
Also give me 5 search queries (with operators like site:, "", intitle:, before:) I can run myself.
````

## Example output

> **Illustrative example.** Shows the format. Check the current numbers yourself before relying on them.

**Question:** What does Apple take from a new indie developer's subscription revenue?

| # | Source | Level | Published / checked | Says |
|---|---|---|---|---|
| 1 | App Store Small Business Program page | 1 | — / 2026-09-30 | 15% for developers under $1M proceeds a year |
| 2 | App Store Review Guidelines 3.1.2 | 1 | 2026-06 / 2026-09-30 | Subscription rules; no rate |
| 3 | r/iOSProgramming thread "SBP approval took 2 days" | 3 | 2026-03 / 2026-09-30 | Enrolment is quick in practice |

**Answer:** 15% if you enrol in the Small Business Program (otherwise 30%, dropping to 15% after a subscriber's
first year). **Confidence: high** (two level-1 sources).

## Common mistakes
- **Trusting AI answers or listicles as the source.** They are level 5. Follow them to the original.
- **No dates.** Store rules and prices change every year. A source without a date is a guess.
- **Stopping at the first answer** that matches what you hoped to find.
- **Keeping sources in browser tabs.** Tabs disappear. Write them down (step 5).

## Related skills
- [research-doc-organization](../research-doc-organization/SKILL.md): where to store what you find.
- [research-where-users-ask](../research-where-users-ask/SKILL.md): level-3 sources, meaning what real users say.
- [research-review-mining](../research-review-mining/SKILL.md): turn reviews into evidence.

## Credits
Written by [@nvminhtu](https://github.com/nvminhtu). Search operators from Google Search Help ("Refine web searches").
