---
name: social-x-reply
description: Write replies and quote posts on X (Twitter) that add something real, so bigger accounts' audiences visit your profile, using X Premium's reply prioritization by hand, never automated. Builds a list of 20–30 target accounts your buyers follow, a 20-minute daily reply session, five reply shapes (add a number, counter-example, screenshot, short how-to, honest question), a no-AI-slop check and a tracker. Use when someone asks "what should I reply on X", "how to get noticed by big accounts", "reply guy strategy", "use Premium reply boost", "draft a reply to this tweet", "write a quote post", "trả lời bài trên X", or pastes an X post and wants a reply.
license: MIT
metadata:
  category: social
  difficulty: beginner
  time: "Setup 20 min · 20 min/day"
  version: 1.0.0
  author: nvminhtu
---

# X Replies: Get Seen Under Bigger Posts

> A target list, a 20-minute daily session and five reply shapes that send profile visits, not "great post!".

## Goal
For a small account, a good reply under a big post is often seen by more people than your own post. X Premium
puts subscribers' replies higher in the thread ("reply prioritization", bigger on higher tiers, per
[About X Premium](https://help.x.com/en/using-x/x-premium)). In X's open-source ranker a predicted reply carries
weight 5 and a reply between accounts that follow each other gets a 15 boost
([param.rs](https://github.com/xai-org/x-algorithm/blob/main/home-mixer/params/param.rs), checked 2026-10-11). So
conversations are the cheapest reach a solo dev has, as long as each reply is worth reading.

## When to use
- You post on X and have under ~5,000 followers.
- You pay for Premium and want to use the reply prioritization you bought.
- Someone in your niche asked a question your product or experience can answer.
- **Not for:** your own daily posts → [social-x-growth](../social-x-growth/SKILL.md). Profile and pinned post
  that turn visits into trials → [social-x-profile-funnel](../social-x-profile-funnel/SKILL.md).

## Inputs
- The product fact bank from [social-x-growth](../social-x-growth/SKILL.md) (true, dated facts).
- 20–30 accounts your *buyers* follow (template: [reply-targets.md](../../templates/reply-targets.md)).
- The text of the post you want to reply to (copy it; don't scrape X).

## Steps
1. **Build the target list (20 min, once).** Mix: 10 bigger builders in your niche, 10 accounts your buyers read
   (reviewers, newsletters, communities), 5–10 peers your size you reply to often (mutual follows get the reply boost).
   Turn on notifications for 5 of them so you see posts in the first hour.
2. **Daily session (20 min).** Open the list, pick 5–10 fresh posts (under ~2 hours old), reply with one of the shapes:

   | Shape | Example opening |
   |---|---|
   | Add a number | "Same here: 9% trial → paid on a $4/mo Mac app, up from 3% after…" |
   | Counter-example | "Didn't work for us: we tried X, got Y, because Z." |
   | Screenshot | "Here's what that looks like in practice:" + image |
   | Short how-to | "The 2-step version: 1) … 2) …" |
   | Honest question | "How did you handle <specific thing>? We got stuck on it." |

3. **Mention your product only when it answers the post**, once, plainly: "I built a tool for this (it's mine): link".
   Most replies should have no link.
4. **Quote post** when you have a full take (a lesson, a disagreement with data). Quotes are weighted 5 like replies
   and live on your own profile.
5. **Reply back** to everyone who answers you; that's where follows come from.
6. **Never automate** replies, likes or follows. X's [automation rules](https://help.x.com/en/rules-and-policies/x-automation)
   ban automated replies based on keyword searches and scripting the website.
7. **Track weekly:** replies written, replies that got answered, profile visits (X analytics). Drop targets whose
   audience never visits your profile; add new ones.

## Prompt (copy-paste)
Works in Claude, ChatGPT, Gemini, Cursor. Replace everything in `{{ }}`.

````text
You help me write replies on X like a real indie developer, not a bot. Never invent experiences, numbers or
features that are not in my fact bank. No "Great post", "This!", "100%", em dashes, emoji chains or hashtags.

The post I'm replying to (author + full text): {{...}}
Why I'm replying: {{add data / disagree / ask / my product answers this}}
My fact bank: {{...}}
My product (only if relevant): {{name · one line · link with utm_source=x&utm_medium=reply}}

Give me 3 replies, each under 280 characters, each a different shape (number, counter-example, screenshot,
how-to, honest question). The first sentence must make sense on its own. Mention my product only if it directly
answers the post, once, with "I built this". Then say which one you'd post and why, and what screenshot to attach.
````

## Example output

> **Illustrative example.** Fictional product and numbers.

Post: *"Indie devs: what actually moved your paywall conversion?"*

1. **Number:** "Showing the user's own usage on the paywall. 'You saved 1,431 clips this week' took our Mac app
   from 3% to 9% trial → paid. Small sample (212 trials)."
2. **Counter-example:** "Annual-first pricing did nothing for us. Monthly-first converted better on a $4 utility;
   people wanted to try one month before trusting a tiny app."
3. **Honest question:** "Did you test the paywall before or after the first 'aha' moment? We moved ours after the
   first saved item and it changed everything, curious if that holds for games."

Pick: #1. It's the most specific and invites "how did you count that?" replies. Attach the paywall screenshot.

## Common mistakes
- **Generic praise.** It earns nothing and reads as a bot, Premium badge or not.
- **Link in every reply.** People mute you (mute weight −58.8). Link only when it answers the question.
- **Replying to posts that are a day old.** Posts leave For You after 48 hours; the conversation is over.
- **Only big accounts.** Peers your size reply back, follow back and share; mutual replies get the biggest boost.
- **Arguing to win.** A disagreement with data is great; a fight brings blocks and reports, the biggest penalties.

## Related skills
- [social-x-growth](../social-x-growth/SKILL.md): the daily post rotation these replies sit next to.
- [social-x-profile-funnel](../social-x-profile-funnel/SKILL.md): where the profile visits land.
- [social-credible-posting](../../../skills/social/social-credible-posting/SKILL.md): the trust rules for every claim.

## Credits
Written by [@nvminhtu](https://github.com/nvminhtu). Sources: [About X Premium](https://help.x.com/en/using-x/x-premium),
[X automation rules](https://help.x.com/en/rules-and-policies/x-automation),
[xai-org/x-algorithm](https://github.com/xai-org/x-algorithm) (checked 2026-10-11).
