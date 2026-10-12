---
name: social-x-daily
description: Plans one day on X (Twitter) for an indie dev who promotes 3–5 products and spends the rest of the time earning reach, follows and trust. Picks today's product slot from a weekly rotation (one product a day at most), writes the two posts (one product or tip, one non-promo), the first-reply UTM link, a three-session reply plan (big accounts, peers, buyer sources) and an hour-by-hour checklist sized to 25, 60 or 120 minutes, with a ramp-up so the account doesn't get a reach label. Use when someone asks "what do I post on X today", "daily X plan", "X routine", "how much should I promote vs. just engage", "grow followers and trust on X", "lịch đăng X hôm nay", "1 ngày trên X làm gì", or types "/social-x today".
license: MIT
metadata:
  category: social
  difficulty: beginner
  time: "5 min to plan · 25–120 min to run"
  version: 1.1.0
  author: nvminhtu
---

# X Daily: Today's Posts, Replies and Checklist

> In 5 minutes: today's two posts written, links ready, and the reply sessions on a clock.

## Goal
Turn the weekly mix (each of your 3–5 products once a week, everything else non-promo) into one concrete day.
Selling every day trains people to scroll past or mute; in X's open-source ranker a mute or "not interested" costs
far more than a like earns ([03-how-x-ranks-posts.md](../../docs/03-how-x-ranks-posts.md)). Talk posts and replies
build the audience the product posts land on.

## When to use
- Every morning, or the night before.
- You promote 3–5 products and want a fixed share of promo vs. talk.
- **Not for:** writing the whole week at once → [social-x-growth](../social-x-growth/SKILL.md); drafting one reply →
  [social-x-reply](../social-x-reply/SKILL.md).

## Inputs
- Your [product rotation](../../templates/product-rotation.md): 3–5 products, offer as the store says it, hooks, links.
- Your [fact bank](../../templates/fact-bank.md) and a list of talk ideas (filled example in `posts/talk-bank.md`).
- Today's weekday, how many minutes you have, which week of the ramp-up you're in, and which products were already
  posted this week.

## Steps
1. **Pick the product slot.** One product today at most; skip any already posted this week. Default rotation:
   Mon reach product (free, loud problem) · Tue hero · Wed second reach · Thu second hero · Fri none (poll) ·
   Sat story / in development · Sun weekly numbers + one ask for the hero.
2. **Write post 1 (08:00).** Product day: demo or lesson that gives something on its own, offer exactly as the store
   says, link in the **first reply** with `utm_source=x&utm_medium=reply&utm_campaign=<slug>&utm_content=<date>`.
   No-product day: the strongest talk post.
3. **Write post 2 (17:30, at least 4 hours later).** Always talk: a tip people would send, a question or poll, a take
   you'd defend, a build-log line, or an honest dated number. Never a second product.
4. **Plan the reply sessions** (Premium ranks subscribers' replies higher, per
   [About X Premium](https://help.x.com/en/using-x/x-premium)):

   | Session | When | Who | Replies |
   |---|---|---|---|
   | 1 | right after post 1 | bigger accounts in your niche, posts < 2 h old | 5–7 |
   | 2 | lunch | peers your size (they reply and follow back) | 3 |
   | 3 | after post 2 | buyer sources: reviewers, newsletters, communities | 5 |

   At most one reply with a product link all day, only where it answers the post, with "I built this".
5. **Set the clock to your buyers.** The times above are your buyers' local time. Living in Vietnam and selling to
   the US? Post 1 lands around 19:00–21:00 ICT (US East Coast morning); check X analytics after 2 weeks.
6. **Size to the time budget.** 25 min: post 1 + session 1. 60 min: everything. 120 min: same posts, more replies and
   record next week's demo; never more posts.
7. **Apply the ramp-up.** Week 1: 1 post, 5 replies, ≤ 3 follows. Week 2: 1–2 posts, 8–10 replies. Week 3: 2 posts,
   13–15 replies. Week 4+ and under 1,000 followers: 2 posts, 20–30 replies (about 70% of your X time on replies,
   [06-reply-playbook.md](../../docs/06-reply-playbook.md#under-1000-followers-70-replies-30-posts)). No profile photo / name / handle change during a ramp-up week
   ([08-rules-and-risks.md](../../docs/08-rules-and-risks.md)).
8. **Output the checklist** with times, and end with: "Tonight: answer replies, follow 3–5 people you replied to,
   add one line to the fact bank."

## Prompt (copy-paste)
Works in Claude, ChatGPT, Gemini, Cursor. Replace everything in `{{ }}`.

````text
Plan my day on X. I promote 3–5 products and want everything else to build reach, follows and trust.

Today: {{weekday, date}} · time I have: {{25 / 60 / 120}} min · ramp-up week: {{1 / 2 / 3 / 4+}}
Followers: {{number}} · my timezone: {{e.g. ICT, UTC+7}} · my buyers' timezone: {{e.g. US Eastern}}
My niche and buyers: {{...}}
Products (slot · name · one line · offer exactly as the store says · link · posted this week? y/n): {{...}}
Fact bank (true, dated): {{...}}
Talk ideas I like: {{optional}}

Rules: at most one product post today, and none already posted this week. Post 2 is never a product.
Under 1,000 followers, about 70% of my time goes to replies; give post times in my timezone, timed for my buyers' morning.
Product links only in the first reply, with utm_source=x&utm_medium=reply&utm_campaign=<slug>&utm_content={{date}}.
Never invent numbers, users or features; leave <…> where I must add a real number. Under 280 characters unless it's
a Saturday long post. No hashtags, em dashes, emoji chains or "game-changer".

Give me:
1. Post 1 (time, text, what to attach, first reply)
2. Post 2 (time, text, what to attach)
3. Three reply sessions: who to look for, how many, and two example reply openers for my niche
4. An hour-by-hour checklist sized to my time and ramp-up week
5. One line: which product goes tomorrow
````

## Example output

> **Illustrative example.** Fictional product.

**Tue, 60 min, ramp-up week 3.** Product slot: hero, *ClipKeep* (not posted this week).

1. **08:00 · post 1:** "Copied something an hour ago and lost it to the next ⌘C? ClipKeep keeps your last 200
   clips, searchable. Free, Pro $4.99 once." Attach a 12 s clip. First reply: `…/clipkeep?utm_source=x&utm_medium=reply&utm_campaign=clipkeep&utm_content=2026-10-13`
2. **17:30 · post 2 (talk):** "Mac tip: ⌥⌘V moves files in Finder instead of copying them."
3. **Replies:** 6 under Mac/productivity accounts · 3 peers · 5 newsletters. Openers: "The 2-step version: …",
   "Didn't work for me: …".
4. **Checklist:** 07:30 answer overnight · 08:00 post 1 · 08:05 session 1 · 12:30 answers + peers · 17:30 post 2 +
   session 3 · 21:30 answers, 4 follows, fact-bank line.
5. **Tomorrow:** second reach product.

## Common mistakes
- **Two product posts in one day** "because it's launch week". Pin the launch post instead.
- **Talk posts about growth hacking** when your buyers aren't marketers. Talk about their problems.
- **Posting 1 and 2 an hour apart.** Posts close together from one author get decayed in feeds.
- **Doubling everything on a good day.** The jump itself can trigger a reach label; follow the ramp-up.

## Related skills
- [social-x](../social-x/SKILL.md): the router; `/social-x today` runs this skill.
- [social-x-reply](../social-x-reply/SKILL.md): during the reply sessions.
- [social-x-growth](../social-x-growth/SKILL.md): the weekly batch the day pulls from.

## Credits
Written by [@nvminhtu](https://github.com/nvminhtu). Day guide: [flow/a-day-on-x.md](../../flow/a-day-on-x.md).
Sources: [About X Premium](https://help.x.com/en/using-x/x-premium),
[xai-org/x-algorithm](https://github.com/xai-org/x-algorithm) (checked 2026-10-11).
