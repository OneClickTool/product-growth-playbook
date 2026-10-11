---
name: social-x
description: The single entry point for X (Twitter) marketing. Reads what you type after /social-x (today, week, month, reply, drop, check, profile, promo, talk, numbers, premium, risk) and runs the right X skill or doc from the X marketing kit, so you don't have to remember which one to open. Use when someone types "/social-x", "x", "twitter", "what do I do on X today", "plan my X week", "reply to this tweet", "fix my X profile", "promote my app on X", "post ideas for X", "X numbers", "is Premium worth it", "label on my X account", "is this revenue screenshot fake", "is this a scam", "hôm nay đăng gì trên X", "lên lịch X", "trả lời tweet", or just pastes an X post and asks what to do.
license: MIT
metadata:
  category: social
  difficulty: beginner
  time: "1 min to route, then the target skill's time"
  version: 1.1.0
  author: nvminhtu
---

# X: One Command, the Right Skill

> Type `/social-x <what you want>` and get sent to the one X skill or doc that does it.

## Goal
The X kit has several skills, a day guide, post banks and templates. This router maps a short command (or a plain
question) to the right one, runs it, and tells you the next command, so the daily routine is "type, copy, post".

## When to use
- You don't remember which X skill does what.
- You want a fixed set of short commands for every day: `today`, `reply`, `week`, `numbers`.
- **Not for:** other channels (Reddit, email, launch) → the main router [growth](../../../skills/growth/SKILL.md).

## Inputs
- The command word, and anything it needs (a pasted post for `reply`, a product name for `promo`).
- Once, kept in your repo: a [fact bank](../../templates/fact-bank.md) and a
  [product rotation](../../templates/product-rotation.md) for the 3–5 products you promote.

## Steps
1. **Read the first word** and route with this table. If there's no command word, match the question to the
   closest row; if it's still unclear, show the table and ask which one.

   | Command | Aliases | Runs | You get |
   |---|---|---|---|
   | `today` | day, hôm nay, daily | [social-x-daily](../social-x-daily/SKILL.md) | Today's 2 posts, reply plan and checklist by the hour |
   | `week` | batch, plan, tuần | [social-x-growth](../social-x-growth/SKILL.md) | 7–14 posts for next week from your fact bank |
   | `reply <post>` | trả lời, quote | [social-x-reply](../social-x-reply/SKILL.md) | 3 replies in different shapes + which to post |
   | `profile` | bio, pin, banner | [social-x-profile-funnel](../social-x-profile-funnel/SKILL.md) | Bio, link, pinned demo, weekly funnel check |
   | `promo <product>` | sell, quảng cáo | [templates/product-rotation.md](../../templates/product-rotation.md) → [social-x-growth](../social-x-growth/SKILL.md) | 3 hooks, demo shot list, when a reply may link |
   | `talk` | ideas, chém gió | [flow/a-day-on-x.md](../../flow/a-day-on-x.md) mix + filled bank in `posts/` | 5 non-promo posts: tip, question, take, build log |
   | `month` | 30 days, plan | [docs/04-premium-30-day-plan.md](../../docs/04-premium-30-day-plan.md) + the day-by-day example in `posts/plan-30-days.md` | 4 weeks, day by day, with weekly checks and stop signs |
   | `drop <post>` | link, what are you building | [06 · "What are you building?" posts](../../docs/06-reply-playbook.md#what-are-you-building-posts-drop-your-link-or-not) | 6-check yes/no, then a reply worth reading without the link |
   | `numbers` | stats, analytics | [docs/07-metrics-and-stop-rules.md](../../docs/07-metrics-and-stop-rules.md) + [templates/weekly-numbers.md](../../templates/weekly-numbers.md) | Weekly table, weakest link in the chain, what to change |
   | `premium` | blue check | [docs/04-premium-30-day-plan.md](../../docs/04-premium-30-day-plan.md) | Keep / drop Premium from your own numbers |
   | `risk` | label, ban, shadowban | [docs/08-rules-and-risks.md](../../docs/08-rules-and-risks.md) | What's allowed, what triggers labels, what to do now |
   | `check <screenshot / account>` | fake, scam, real? | [reference/fake-proof-and-scams.md](../../reference/fake-proof-and-scams.md) | Screenshot + source checks, scam patterns, a verdict with how sure |
   | `start` | setup, bắt đầu | [README](../../README-X-Marketing.md) "Start in 3 steps" | Profile → fact bank → first day |

2. **Run the target** with what the user gave. Load the target `SKILL.md` and follow its steps and prompt; for a
   doc, read it and answer from it with links.
3. **Keep the kit's rules in every output:** nothing automated (posting by hand or via a scheduler for your own
   posts only), no invented numbers, at most one product post a day, link in the first reply with UTM.
4. **End with the next command** the user will need, e.g. after `today` → "`/social-x reply` + paste a post during
   your reply session"; on Sunday → "`/social-x numbers`, then `/social-x week`".

## Prompt (copy-paste)
Works in Claude, ChatGPT, Gemini, Cursor. Replace everything in `{{ }}`.

````text
You are my X (Twitter) marketing assistant. Route my request to one job and do it:
today = today's two posts + reply plan + hourly checklist (max one product post, the rest non-promo)
week = 7–14 posts for next week from my fact bank
reply = 3 replies to the pasted post, different shapes (number, counter-example, screenshot, how-to, question)
profile = bio, link, pinned post, banner
promo = 3 hooks + 10–30 s demo shot list for one product + when a reply may include the link
talk = 5 non-promo posts (tip, question, take, build log, honest number) for my niche
numbers = read my weekly numbers, name the weakest step (impressions → profile visits → link clicks → trials)
Rules: never invent numbers, users or features; no automation of replies, likes, follows or DMs; product links in
the first reply with utm_source=x; no "great post", em dashes, emoji chains or hashtags.

My request: {{today | week | reply <post> | profile | promo <product> | talk | numbers <table>}}
My niche and buyers: {{...}}
My 3–5 products (name · one line · offer as the store says · link): {{...}}
My fact bank: {{...}}
Today is: {{weekday, date}} · time I have: {{25 / 60 / 120 min}}

Say which job you picked in one line, do it, then tell me the next request I should make.
````

## Example output

> **Illustrative example.** Fictional product.

Input: `/social-x reply` + *"Mac devs: what's your setup for knowing when a long build is done?"*

Routed to **reply** ([social-x-reply](../social-x-reply/SKILL.md)).

1. **How-to:** "`caffeinate -i make build && say done`. Mac stays awake, and talks when it's finished."
2. **Question:** "Do you also want it to ping you when it fails halfway, or only at the end?"
3. **Product (it answers the post):** "I built a small menu bar app that does this for AI agents (it's mine): ‹link›"

Pick #1, no link: it's a tip people can copy. Next: `/social-x today` to see what's left of today's plan.

## Common mistakes
- **Skipping the router and asking for "a viral tweet".** You get generic posts. Start with `today` or `week`, which
  use your fact bank.
- **Running `promo` every day.** One product post a day at most, each product once a week; the rest is `talk`.
- **Asking the agent to post or reply for you.** It drafts; you post by hand ([X automation rules](https://help.x.com/en/rules-and-policies/x-automation)).

## Related skills
- [social-x-daily](../social-x-daily/SKILL.md): the plan for today.
- [social-x-growth](../social-x-growth/SKILL.md) · [social-x-reply](../social-x-reply/SKILL.md) ·
  [social-x-profile-funnel](../social-x-profile-funnel/SKILL.md).
- [growth](../../../skills/growth/SKILL.md): the router for every other channel.

## Credits
Written by [@nvminhtu](https://github.com/nvminhtu). Sources: the docs in this kit,
[X automation rules](https://help.x.com/en/rules-and-policies/x-automation) (checked 2026-10-11).
