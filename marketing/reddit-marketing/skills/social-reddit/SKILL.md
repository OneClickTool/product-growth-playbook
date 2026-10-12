---
name: social-reddit
description: The single entry point for Reddit marketing. Reads what you type after /social-reddit (today, find, reply, post, rules, profile, numbers, risk, start) and runs the right skill or doc from the Reddit marketing kit and the main library (launch-reddit-posting, the subreddit wiki, research-where-users-ask), so you don't have to remember which one to open. Comments first, posts later, always disclosed. Use when someone types "/social-reddit", "reddit", "what do I answer on Reddit today", "find threads about my app", "reply to this Reddit thread", "write a post for r/macapps", "subreddit rules", "set up my Reddit profile", "Reddit numbers", "my Reddit post got removed", "shadowban", "hôm nay trả lời gì trên Reddit", "đăng Reddit", or pastes a Reddit thread and asks what to do.
license: MIT
metadata:
  category: social
  difficulty: beginner
  time: "1 min to route, then the target's time (15 min/day routine)"
  version: 1.0.0
  author: nvminhtu
---

# Reddit: One Command, the Right Skill

> Type `/social-reddit <what you want>` and get sent to the one Reddit skill or doc that does it.

## Goal
Reddit marketing for a small product is mostly answering questions well and posting rarely, in each subreddit's own
format. The pieces live in several places: this kit, [launch-reddit-posting](../../../../skills/launch/launch-reddit-posting/SKILL.md)
and the [subreddit wiki](../../../../docs/subreddits/README.md). This router maps a short command to the right one,
runs it, and tells you the next command.

## When to use
- You want a fixed set of short commands for every day: `today`, `reply`, `post`, `numbers`.
- You pasted a Reddit thread and want to know whether and how to answer.
- **Not for:** other channels → [growth](../../../../skills/growth/SKILL.md) or the
  [marketing hub](../../../README-marketing-social.md).

## Inputs
- The command word and what it needs (a thread for `reply`, a subreddit for `post` and `rules`, a topic for `find`).
- Once: your product (one line, who for, price, platform, privacy facts, landing URL), 3–5 target subreddits, and
  your problem words ([04-finding-threads.md](../../docs/04-finding-threads.md)).

## Steps
1. **Read the first word** and route with this table. No command word: match the question to the closest row; still
   unclear, show the table and ask.

   | Command | Aliases | Runs | You get |
   |---|---|---|---|
   | `today` | day, hôm nay | [flow/daily-flow.md](../../flow/daily-flow.md) | 2–3 threads to answer, and the post if it's your post day |
   | `find <topic>` | search, where | [04-finding-threads.md](../../docs/04-finding-threads.md) + [research-where-users-ask](../../../../skills/research/research-where-users-ask/SKILL.md) | Subreddits, 5 saved searches, F5Bot keywords |
   | `reply <thread>` | answer, comment, trả lời | [social-reddit-comment](../social-reddit-comment/SKILL.md) | An answer in the right shape + mention-the-product yes/no |
   | `post <sub> [variant]` | write, đăng | [06-post-variants.md](../../docs/06-post-variants.md) + [launch-reddit-posting](../../../../skills/launch/launch-reddit-posting/SKILL.md) step 3 | One post file written to that subreddit's rules |
   | `rules <sub>` | flair, allowed? | [docs/subreddits](../../../../docs/subreddits/README.md) page, else `fetch_subreddit_rules.py` | Promo allowed? day, flair, title format, karma minimum |
   | `profile` | bio, links | [02-profile-setup.md](../../docs/02-profile-setup.md) | Bio line, social links with UTM, what to pin |
   | `numbers` | stats | [07-metrics-and-stop-rules.md](../../docs/07-metrics-and-stop-rules.md) + [weekly numbers](../../templates/weekly-numbers.md) | Weekly table, weakest step, what to change |
   | `risk` | removed, banned, shadowban | [08-rules-and-risks.md](../../docs/08-rules-and-risks.md) | What happened, what's allowed, what to do now |
   | `start` | setup, bắt đầu | [README](../../README-Reddit-Marketing.md) "Start in 3 steps" | Profile → comments-only weeks → first post |

2. **Run the target** with what the user gave: load the target `SKILL.md` and follow it, or read the doc and answer
   from it with links.
3. **Keep the kit's rules in every output:** say you're the developer; product in at most 1 of 10 comments per
   subreddit; one post per subreddit per month; never the same text twice; no DMs to people who didn't ask; no
   automation; UTM `utm_source=reddit` on every link; no invented numbers.
4. **End with the next command**, e.g. after `today` → "`/social-reddit reply` + paste each thread"; on Sunday →
   "`/social-reddit numbers`".

## Prompt (copy-paste)
Works in Claude, ChatGPT, Gemini, Cursor. Replace everything in `{{ }}`.

````text
You are my Reddit marketing assistant for a small software product. Route my request to one job and do it:
today = 2–3 threads to answer today from my subreddits and searches (+ the weekly post if today is my post day)
find = where people ask about my topic: subreddits (buyers vs builders), 5 searches, alert keywords
reply = an answer to the pasted thread in one shape (direct fix, steps, comparison, experience, product answer,
        question), and a yes/no on mentioning my product with the reason
post = one post for the named subreddit in a variant it allows (showcase, build story, lesson, comparison, feedback,
       deal, weekly-thread drop, tutorial, milestone, AMA), following its rules
profile = bio line, social links with UTM, what to pin
numbers = read my weekly table and name the weakest step (answers → removals → visits → trials → paid)
Rules: I'm the developer and say so; product in at most 1 of 10 comments per subreddit; never invent numbers,
users or features; no DMs, no automation, no vote requests; links only where the subreddit allows, with
utm_source=reddit&utm_medium=comment|post|profile&utm_campaign=<subreddit>. Sound like a person, no AI phrasing.

My request: {{today | find <topic> | reply <thread text> | post <subreddit> | profile | numbers <table>}}
My product: {{name · one line · who for · price · platform · privacy facts · landing URL}}
My subreddits (and rules I know): {{...}}
Today is: {{weekday, date}}

Say which job you picked in one line, do it, then tell me the next request I should make.
````

## Example output

> **Illustrative example.** Fictional product.

Input: `/social-reddit reply` + *r/MacOS: "Any way to see clipboard history on Mac?"*

Routed to **reply** ([social-reddit-comment](../social-reddit-comment/SKILL.md)). Shape: **product answer**, because
the question asks for an app and r/MacOS allows answers that name apps (no promo posts).

> macOS doesn't keep clipboard history, so you need an app. Look for one that stores history only on your Mac and
> lets you exclude password managers. Disclosure: I made one (Clipnest, free for 50 clips), but any of them does this.

Mention product: **yes**, it answers the exact question; 1 of your last 12 comments in r/MacOS mentioned it. Next:
`/social-reddit today` for the rest of today's threads.

## Common mistakes
- **Starting with `post`.** New accounts get removed. Two weeks of `today` + `reply` first.
- **Running `post` for the same text in five subreddits.** That's spam by Reddit's definition. One subreddit, one
  variant, its own words.
- **Asking the agent to post or DM for you.** It drafts; you post by hand.

## Related skills
- [social-reddit-comment](../social-reddit-comment/SKILL.md): answers worth upvoting.
- [launch-reddit-posting](../../../../skills/launch/launch-reddit-posting/SKILL.md): subreddits by product type,
  the rules script, title and body formulas.
- [social-x](../../../x-marketing/skills/social-x/SKILL.md): where Reddit readers go to check you out.

## Credits
Written by [@nvminhtu](https://github.com/nvminhtu). Sources: the docs in this kit,
[Reddit Rules](https://redditinc.com/policies/reddit-rules) and
[Reddit Help: Spam](https://support.reddithelp.com/hc/en-us/articles/360043504051-Spam) (checked 2026-10-12).
