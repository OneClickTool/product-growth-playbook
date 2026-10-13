---
name: social-medium
description: The single entry point for Medium marketing. Reads what you type after /social-medium (fit, start, write, mirror, pubs, profile, numbers, risk) and runs the right skill or doc from the Medium marketing kit, so you don't have to remember which one to open. Reader-first articles, product at most once and disclosed, canonical links to your own blog, publications before Boost. Use when someone types "/social-medium", "medium", "should I post on Medium", "is Medium worth it for my app", "write a Medium article", "republish my blog on Medium", "canonical link Medium", "which Medium publication", "Medium Boost", "Medium Partner Program", "my Medium story got no views", "Medium suspended", "có nên viết Medium không", "đăng bài Medium".
license: MIT
metadata:
  category: social
  difficulty: beginner
  time: "1 min to route, then the target's time (3–4 h/week or 15 min/post in mirror mode)"
  version: 1.0.0
  author: nvminhtu
---

# Medium: One Command, the Right Skill

> Type `/social-medium <what you want>` and get sent to the one Medium skill or doc that does it.

## Goal
Medium works for a small product when it publishes useful long articles, mirrors your own blog with canonical links,
and gets into the right publications. The pieces live in several docs of this kit. This router maps a short command
to the right one, runs it, and tells you the next command.

## When to use
- You're deciding whether Medium is worth your time for this product.
- You want a fixed set of short commands for the weekly routine: `write`, `mirror`, `numbers`.
- **Not for:** other channels → [growth](../../../../skills/growth/SKILL.md) or the
  [marketing hub](../../../README-marketing-social.md). SEO pages on your own site →
  [intent pages](../../../../skills/growth/action/04-listings-and-intent-pages.md).

## Inputs
- The command word and what it needs (a topic or real question for `write`, a blog URL for `mirror`).
- Once: your product (one line, who for, price, platform, landing URL), whether you have a blog, and your topics.

## Steps
1. **Read the first word** and route with this table. No command word: match the question to the closest row; still
   unclear, show the table and ask.

   | Command | Aliases | Runs | You get |
   |---|---|---|---|
   | `fit` | worth it?, có nên | [01-strategy.md](../../docs/01-strategy.md) fit check | Good / medium / weak for this product, and why |
   | `start` | setup, bắt đầu | [README](../../README-Medium-Marketing.md) "Start in 3 steps" | Profile → import 2–3 posts → first article |
   | `write <topic>` | article, viết | [social-medium-article](../social-medium-article/SKILL.md) | Title, outline, draft, product-mention test, topics, UTM link |
   | `mirror <url>` | import, canonical | [04-canonical-and-republishing.md](../../docs/04-canonical-and-republishing.md) | Import steps, canonical check, new title/intro for Medium |
   | `pubs <topic>` | publication, boost | [06-publications-and-boost.md](../../docs/06-publications-and-boost.md) + [tracker](../../templates/publication-tracker.md) | How to find and vet 3–5 publications, a pitch |
   | `profile` | bio, about | [02-profile-setup.md](../../docs/02-profile-setup.md) | Bio, about page, link with UTM, featured story |
   | `numbers` | stats | [07-metrics-and-stop-rules.md](../../docs/07-metrics-and-stop-rules.md) + [weekly numbers](../../templates/weekly-numbers.md) | Weekly table, weakest step, what to change |
   | `risk` | suspended, no views | [08-rules-and-risks.md](../../docs/08-rules-and-risks.md) | What likely happened, what's allowed, what to do now |

2. **Run the target** with what the user gave: load the target `SKILL.md` and follow it, or read the doc and answer
   from it with links.
3. **Keep the kit's rules in every output:** the article is useful without the product; product at most once in the
   body, disclosed in the same sentence; one UTM link at the end (`utm_source=medium`); canonical only to the user's
   own original; human-written (AI help disclosed); no invented numbers, users or quotes.
4. **End with the next command**, e.g. after `fit` = good → "`/social-medium start`"; after `write` →
   "`/social-medium pubs <topic>`"; on Sunday → "`/social-medium numbers`".

## Prompt (copy-paste)
Works in Claude, ChatGPT, Gemini, Cursor. Replace everything in `{{ }}`.

````text
You are my Medium marketing assistant for a small software product. Route my request to one job and do it:
fit = is Medium worth it for this product (good / medium / weak) and why, based on who buys it and what they read
write = one reader-first article: type (how-to, fix, comparison, build story, lesson, deep dive, checklist, case
        study), title + subtitle, first 3 lines, outline, draft, 5 topics, one UTM link at the end
mirror = steps to republish my blog post on Medium with a canonical link, plus a new title and intro for Medium
pubs = how to find and vet 3–5 active publications for my topic, and a short pitch
profile = bio, about page, link with UTM, which story to feature
numbers = read my weekly table and name the weakest step (read ratio → distribution → visits → trials → paid)
Rules: the article must be useful if my product didn't exist; mention my product at most once in the body, as one
option, with "I make this" in the same sentence; never invent numbers, users, quotes or features (write <CHECK>);
links use utm_source=medium&utm_medium=article|profile&utm_campaign=<slug>. Sound like a person, no AI phrasing.

My request: {{fit | write <topic or real question> | mirror <blog URL> | pubs <topic> | profile | numbers <table>}}
My product: {{name · one line · who for · price · platform · landing URL}}
My blog: {{URL or "none"}}   My topics: {{...}}

Say which job you picked in one line, do it, then tell me the next request I should make.
````

## Example output

> **Illustrative example.** Fictional product.

Input: `/social-medium fit` + *"Clipnest, a $9 clipboard manager for Mac, buyers are Mac power users."*

Routed to **fit** ([01-strategy.md](../../docs/01-strategy.md)). Verdict: **medium**. Mac power users do search
"how to see clipboard history on Mac", and a tutorial on Medium can rank and be linked from your Reddit answers. But
most buyers decide on Reddit, X and the Mac App Store, so Medium is a support channel: mirror mode (import each blog
post, 15 minutes) plus one tutorial a month. Next: `/social-medium start`.

## Common mistakes
- **Writing about the product.** "Introducing Clipnest 2.0" gets no distribution. Write the tutorial; the product is
  one line.
- **Copying the blog post without a canonical link.** Use `mirror`; it sets it for you.
- **Expecting Medium to pay the bills.** Income comes only from paying members' reading time; treat it as a bonus.
- **Asking the agent to publish for you.** It drafts; you publish by hand.

## Related skills
- [social-medium-article](../social-medium-article/SKILL.md): one article from topic to published.
- [social-credible-posting](../../../../skills/social/social-credible-posting/SKILL.md): the proof ladder behind every
  claim.
- [social-reddit](../../../reddit-marketing/skills/social-reddit/SKILL.md): where the real questions for your
  articles come from.

## Credits
Written by [@nvminhtu](https://github.com/nvminhtu). Sources: the docs in this kit,
[Medium Rules](https://policy.medium.com/medium-rules-30e5502c4eb4),
[Help: Distribution](https://help.medium.com/hc/en-us/articles/360006362473) and
[Help: Set a canonical link](https://help.medium.com/hc/en-us/articles/360033930293-Set-a-canonical-link) (checked 2026-10-13).
