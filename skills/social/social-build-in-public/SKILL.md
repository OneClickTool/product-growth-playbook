---
name: social-build-in-public
description: Share the building of your product in public every week (progress, numbers, decisions, failures) so an audience grows alongside the product and is ready on launch day. Sets what to share and what to keep private, a 30-minute weekly update template, a monthly numbers post, milestone and launch-countdown posts, where to post (X, Threads, Indie Hackers, LinkedIn, a newsletter), and how to move followers to an email list you own. Use when someone asks "should I build in public", "what should I post while building", "how do I grow an audience before launch", "weekly update template", "share my MRR publicly", "build in public on X", "how to get followers as an indie developer", or wants launch-day users without paid ads.
license: MIT
metadata:
  category: social
  difficulty: beginner
  time: "Setup 30 min · 30 min/week"
  version: 1.0.0
  author: nvminhtu
---

# Build in Public: Grow the Audience With the Product

> A share/don't-share list, a weekly update you can write in 30 minutes, and a plan that turns followers into
> email subscribers before launch day.

## Goal
Most launches fail because nobody is waiting. Building in public fixes that by making the work itself the content:
each week, a short honest update. After a few months you have people who watched the product grow, trust you,
and show up when you launch. It costs 30 minutes a week, not a marketing budget.

## When to use
- You're building something and have 4+ weeks until launch, or you're live and want a steady trickle of attention.
- You're a solo builder or a small team, comfortable sharing numbers and mistakes.
- **Not for:** writing one credible post → [social-credible-posting](../social-credible-posting/SKILL.md).
  Products where secrecy matters (a client project, a patentable idea, a clone-able niche with no moat).

## Inputs
- One account on 1–2 platforms where your users or fellow builders are.
- A simple way to see your weekly numbers (store dashboard, analytics, payment provider).
- An email signup page (waitlist or newsletter) → [email-list-and-deliverability](../../email/email-list-and-deliverability/SKILL.md).

## Steps
1. **Decide what you share (and what you never share).** Write it down once:

   | Share | Keep private |
   |---|---|
   | Weekly progress, screenshots, decisions and why | Users' personal data, emails, names (unless they agree) |
   | Numbers you're comfortable with: users, revenue range or exact, conversion | API keys, dashboards with private info visible, bank details |
   | Mistakes and what you learned | Anything under NDA or a client's business |
   | Tools and stack | Exact niche keywords or data that lets anyone clone you in a weekend (your call) |

2. **Pick 1–2 places and a day.** Builders follow builders on X, Threads, [Indie Hackers](https://www.indiehackers.com/)
   and LinkedIn. Your *users* might be elsewhere; cross-post a user-friendly version there. Same day every week, so
   people come back.
3. **Write the weekly update (30 min) with this template:**

   ```text
   Week {{N}} of building {{product}}: {{one-line headline: the most interesting thing}}

   Shipped: {{1–3 bullets, with a screenshot or GIF}}
   Numbers: {{users / sign-ups / revenue this week vs last}}
   Learned: {{one lesson, specific}}
   Stuck on / question: {{one real question for readers}}
   Next week: {{one goal}}
   ```

   The question at the end is what gets replies, and replies are where relationships start.
4. **Post a monthly numbers post** (rung 3–4 of the proof ladder in
   [social-credible-posting](../social-credible-posting/SKILL.md)): a chart or dashboard screenshot, what moved it,
   what didn't work. These are the posts people save and share.
5. **Mark milestones** (first user, first $1, 100 users, first review, a rejection you fixed) with a short story
   post, not just a number.
6. **Move followers to an owned list.** Every 3–4 updates, end with: "I send the full update + early access by email
   once a month: {{link}}". On launch day, email first, then post. → [strategy-product-as-funnel](../../strategy/strategy-product-as-funnel/SKILL.md)
7. **Run a launch countdown** in the last 2 weeks: beta invites for followers, a "launch day is {{date}}" post,
   and ask people to *try it on day 1 and reply with feedback*, never to upvote in a coordinated way (most launch
   sites ban that; see [launch-product-hunt-launch](../../launch/launch-product-hunt-launch/SKILL.md)).
8. **Review monthly:** followers gained, replies per post, email sign-ups from social, launch-day users from your
   audience. If replies are near zero after 8 weeks, change the platform or the question you ask, not the honesty.

## Prompt (copy-paste)
Works in Claude, ChatGPT, Gemini, Cursor. Replace everything in `{{ }}`.

````text
You help indie builders write build-in-public updates that are honest and short. Never invent progress or numbers.

Product: {{what, who for}}
Week number: {{N}}   Platform: {{X / Threads / Indie Hackers / LinkedIn}}
This week, raw notes: {{what I shipped, numbers, problems, anything interesting}}
Last week's numbers: {{...}}
Things I don't want to share: {{...}}
Email signup link: {{...}}

1. Find the most interesting thing in my notes and turn it into a one-line headline.
2. Write the weekly update using: headline, Shipped, Numbers (vs last week), Learned, Stuck on / question, Next week.
   Under 150 words for X/Threads (as a short thread if needed), up to 300 for Indie Hackers/LinkedIn.
3. Suggest the screenshot or GIF to attach.
4. Write one specific question for readers that invites useful replies.
5. If this is week 4, 8, 12…, add a one-line invitation to my email list.
````

## Example output

> **Illustrative example.** Fictional product and numbers.

> **Week 7 of building Tabby (tab manager for Chrome): the "save session" button doubled day-2 retention**
>
> Shipped: one-click "save all tabs as a session" (GIF below), dark mode
> Numbers: 312 users (+48), day-2 retention 38% (was 19%), $0 revenue (paid tier comes in week 10)
> Learned: users didn't want *more* features, they wanted one they could trust not to lose their tabs
> Stuck on: pricing. $3/month or $19 lifetime for a tab manager?
> Next week: sync across devices, behind a waitlist
>
> I send a longer monthly update + early access by email: tabby.example/updates

## Common mistakes
- **Only posting when there's good news.** The weeks where something broke are the ones people remember.
- **Talking only to other builders.** Fun, but they won't be your users. Add posts for the people who'll use it.
- **Leaking private data in screenshots.** Crop emails, customer names and keys before posting.
- **No owned list.** Followers belong to the platform; an email list belongs to you.
- **Stopping after launch.** The audience you built wants to see what happens next. That's more weeks of content.

## Related skills
- [social-credible-posting](../social-credible-posting/SKILL.md): the trust rules behind each post.
- [social-short-video](../social-short-video/SKILL.md): "day N of building" as a video format.
- [email-beta-program](../../email/email-beta-program/SKILL.md): turn followers into beta testers.
- [launch-pre-launch-checklist](../../launch/launch-pre-launch-checklist/SKILL.md): plan the countdown weeks.

## Credits
Written by [@nvminhtu](https://github.com/nvminhtu).
