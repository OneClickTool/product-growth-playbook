---
name: launch-post-writing
description: Write launch posts that fit each channel's culture and rules (Show HN, Reddit, X/Twitter thread, LinkedIn, Indie Hackers, community groups), leading with a story or lesson instead of an ad. Use when announcing a product, a major update or a milestone, or when someone asks "write my launch post", "Show HN post", "how do I post on Reddit without getting banned", or "announce my app".
license: MIT
metadata:
  category: launch
  difficulty: beginner
  time: 30-45 min
  version: 1.0.0
  author: nvminhtu
---

# Launch Post Writing

> In 30–45 minutes you will have one core story and a version of it for each channel, ready to post.

## Goal
Write posts people read to the end because they are useful or interesting, and click because they want to,
not because you told them to.

## When to use
- Launch day, a major version, or a milestone ("100 paying users, here's what worked").
- A post you already published flopped and you want to know why.
- **Not for:** paid ads or store listing copy → [aso-title-subtitle-optimization](../../aso/aso-title-subtitle-optimization/SKILL.md).

## Inputs
- What the product does, who it's for, and a link people can try (ideally without signing up).
- **The story:** why you built it, a real number or moment, what surprised you.
- The channels you'll post in, and each one's rules (read the sidebar or rules page of every community).

## The one structure that works everywhere
1. **Hook:** a specific problem, number or moment. ("I waited 94 days for a $2,400 invoice.")
2. **Story or insight:** what you tried, what you learned. This is the part people share.
3. **What you built:** one or two sentences, concrete.
4. **What's different:** the one thing that isn't true of the alternatives.
5. **Ask:** a specific question you want feedback on. The link goes here, at the end.

## Channel rules

| Channel | Format | Must know |
|---|---|---|
| **Show HN** | Title `Show HN: <Name> – <what it does>`, plain text, link to the product | For things people can try. Make it easy: no signup wall if possible. Technical detail and honest limits do well, marketing language does badly. Stay and answer comments. |
| **Reddit** | Story/lesson post, link at the end or in a comment if the sub prefers | Every subreddit has its own self-promotion rules. Read them first ([launch-reddit-posting](../launch-reddit-posting/SKILL.md) picks subreddits by product type and fetches their rules). Many only allow promotion on specific days or threads. Post from an account with real history in that community. |
| **X / Twitter** | Thread: hook tweet → 4–7 tweets → link in the last tweet | The first tweet must stand alone. A screenshot or 15-second demo video beats text. |
| **LinkedIn** | 1,000–1,300 characters, short lines, lesson-first | The first 2 lines show before "…see more". Put the link in the post or first comment. |
| **Indie Hackers / communities** | Milestone or lesson post with real numbers | Numbers and transparency (revenue, what failed) get engagement. |

## Steps
1. **Write the core story once (15 min)** using the 5-part structure. Around 150–250 words.
2. **Adapt per channel (15 min)** using the table. Change the hook and length, not the facts.
3. **Remove hype.** Delete "revolutionary", "game-changer", "excited to announce", and every exclamation mark except one.
4. **Check the rules** of every community one more time. Add UTM tags to every link.
5. **Post and stay.** Block 2 hours after each post to reply to every comment. Early replies drive most of the reach.

## Prompt (copy-paste)
Replace everything in `{{ }}`.

````text
You are a launch copywriter who writes like a builder, not a marketer.

Product: {{what it does, who it's for}}
Link: {{URL}}   Can people try it without signing up? {{yes/no}}
My story: {{why I built it, a real moment or number, what I learned}}
What's different from alternatives: {{one thing}}
Channels: {{e.g. Show HN, r/SaaS, X, LinkedIn}}

1. Write a core story (150-250 words): hook with a specific moment or number → insight → what I built →
   what's different → a specific feedback question. Link only at the end.
2. Adapt it for each channel:
   - Show HN: title in the "Show HN: Name – what it does" format + a plain first comment with technical
     details and honest limitations.
   - Reddit: a lesson-first post; remind me to check the subreddit's self-promotion rules.
   - X: a 5-7 tweet thread, first tweet must stand alone, link in the last tweet.
   - LinkedIn: 1,000-1,300 characters, first two lines must make people click "see more".
3. No hype words (revolutionary, game-changer, excited to announce). Max one exclamation mark per post.
````

## Example output

> **Illustrative example.** Fictional product, shown for format.

**Show HN title:** `Show HN: Invoicely Lite – invoices that send polite payment reminders for you`

**X hook tweet:**
> I waited 94 days for a $2,400 invoice.
> Not because the client was shady. Because I hated writing "just following up" emails.
> So I built a tool that writes them for me. Here's what 3 months of automatic reminders did to my payment times 🧵

## Common mistakes
- **Starting with the product name.** Nobody cares yet. Start with the problem or the moment.
- **The same post pasted everywhere.** Each community notices, and moderators remove it.
- **Link first, story never.** It reads as an ad, gets downvoted, and in many subreddits gets removed.
- **Posting and leaving.** Unanswered comments kill reach in the first hour.

## Related skills
- [launch-product-hunt-launch](../launch-product-hunt-launch/SKILL.md): the Product Hunt version of launch day.
- [launch-get-first-100-users](../launch-get-first-100-users/SKILL.md): personal outreach alongside public posts.

## Credits
Written by [@nvminhtu](https://github.com/nvminhtu). Show HN rules from Hacker News'
[Show HN guidelines](https://news.ycombinator.com/showhn.html). Always read each subreddit's rules before posting.
