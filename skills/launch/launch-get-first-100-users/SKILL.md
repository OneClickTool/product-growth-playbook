---
name: launch-get-first-100-users
description: Plan and run the manual outreach that gets a new product its first 100 real users, with a named target list, personal message templates, a channel plan and a tracking sheet. Use when a product just launched or has fewer than 100 users, or when someone asks "how do I get my first users", "nobody is signing up", "I launched and got no traffic", or "how do I find beta users".
license: MIT
metadata:
  category: launch
  difficulty: beginner
  time: 60 min to plan, then 30 min/day
  version: 1.0.0
  author: nvminhtu
---

# Get Your First 100 Users

> In an hour you will have a list of 100 specific people or places, three message templates and a daily routine.
> In 2–4 weeks of following it you should have your first 100 users.

## Goal
Get the first 100 users by hand, one conversation at a time, and learn *why* each one signed up.
At this stage what you learn from them is worth more than the number.

## When to use
- You just launched, or you have fewer than ~100 users.
- Ads, SEO or ASO aren't working yet because nobody knows the product exists.
- **Not for:** products that already have steady organic sign-ups. Use channel-specific skills instead.

## Inputs
- A one-sentence description of **who** has the problem, specific enough to find them
  ("freelance designers who send invoices monthly", not "small businesses").
- The product must be usable today: a live link, a TestFlight or closed-test invite, or a store listing.
- Your own network: contacts, followers, communities you already belong to.

## Steps
1. **Write the "who" and the "where" (10 min).** List 10 places where these people already talk about the problem:
   subreddits, Discord and Slack groups, Facebook groups, forums, hashtags, newsletters, meetups,
   people who publicly complained about a competitor. Be specific (`r/freelance` beats "Reddit").
2. **Build a list of 100 (20 min, finish during the week).** Mix three rings:
   - **Ring 1:** 20–30 people you know who have the problem.
   - **Ring 2:** 30–40 people who publicly described the problem: posts, reviews of competitors, questions.
   - **Ring 3:** 3–5 communities where you will post and answer questions, not just drop a link.
   Put them in a sheet: `name | where found | what they said | contacted | replied | signed up | activated | notes`.
3. **Write three messages (15 min).** Use the templates below. Personal and short. Ask for feedback,
   not for a favour, and mention the specific thing they said.
4. **Daily routine (30 min/day).** Send 10 personal messages. Answer 3 questions in communities *without* linking,
   unless someone asks. Reply to everyone who replied yesterday.
5. **Onboard people by hand.** For the first 20 users, offer a 15-minute call or a personal walkthrough.
   Watch where they get stuck. Fix the top issue each week.
6. **Ask for the next user.** After someone gets value, ask: "Who else do you know who has this problem?"
   One referral each doubles your list.
7. **Review weekly.** Which ring and which channel produced **activated** users (not just sign-ups)? Double down there
   and drop what produced nothing after 2 weeks.

This is Paul Graham's "Do Things That Don't Scale" applied: manual recruiting is how most products get their start.

## Prompt (copy-paste)
Replace everything in `{{ }}`.

````text
You are helping me get my first 100 users by hand.

Product: {{what it does, link}}
Who has the problem (be specific): {{target user}}
The problem in their words: {{quotes from reviews, posts, conversations}}
My network: {{communities I'm in, audience size, notable contacts}}
Current users: {{number}}

1. List 15 specific places where these people discuss the problem (exact subreddit / group / forum names,
   hashtags, newsletters). For each, note its self-promotion rules if they are commonly known, and how to add
   value there without linking.
2. Give me 5 search queries I can use to find individuals who publicly described this problem.
3. Write 3 short outreach messages (under 80 words each):
   a) to someone I know, b) to a stranger who posted about the problem (reference their post),
   c) a community post that asks for feedback and shares a lesson, with the link only at the end.
   No hype, no "revolutionary". Ask for feedback, not favours.
4. A 14-day routine: daily actions, targets, and what to measure.
````

## Example output

> **Illustrative example.** Fictional product and numbers, shown for format.

*Invoicely Lite*, invoicing for freelance designers. 14 days, 30 min/day.

| Ring / channel | Contacted | Signed up | Activated (sent 1 invoice) |
|---|---|---|---|
| Ring 1: designer friends | 25 | 14 | 9 |
| Ring 2: people complaining about late payments on X | 60 | 11 | 6 |
| Ring 3: r/freelance feedback post | 1 post | 38 | 12 |
| Ring 3: design Discord, answering invoicing questions | 12 answers | 9 | 5 |
| Referrals from activated users | — | 17 | 11 |
| **Total** | | **89** | **43** |

Stranger message that worked best:
> Hi Mai, saw your post about chasing a client for 60 days 😩 I'm building a tiny invoicing tool for freelance
> designers that sends polite automatic reminders. Would you try it and tell me what's missing? Free while in beta.

## Common mistakes
- **Posting a link and leaving.** Communities ignore or ban drive-by links. Give an answer or a lesson first.
- **Mass-messaging templates.** A message that could go to anyone gets answered by no one. Reference something the person said.
- **Counting sign-ups instead of activated users.** 100 sign-ups who never used it teach you nothing.
- **Waiting for the product to be "ready".** If it solves the core problem, start recruiting now and polish with feedback.

## Related skills
- [launch-post-writing](../launch-post-writing/SKILL.md): write the community and launch posts.
- [launch-pre-launch-checklist](../launch-pre-launch-checklist/SKILL.md): make sure tracking is in place first.
- [monetization-pricing-strategy](../../monetization/monetization-pricing-strategy/SKILL.md): once people use it, decide what to charge.

## Credits
Written by [@nvminhtu](https://github.com/nvminhtu). Inspired by Paul Graham,
[Do Things That Don't Scale](https://paulgraham.com/ds.html) (2013).
