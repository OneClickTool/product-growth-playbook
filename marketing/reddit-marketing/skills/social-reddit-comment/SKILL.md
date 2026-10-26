---
name: social-reddit-comment
description: Write Reddit answers that get upvoted and bring the right people to your profile, without breaking subreddit rules. Picks one of six answer shapes (direct fix, steps, honest comparison, first-hand experience, product answer, clarifying question), runs a five-check test on whether to mention your own product, adds a natural disclosure line, keeps the 1-in-10 self-promotion ratio per subreddit, and logs the answer in a thread tracker. Use when someone pastes a Reddit thread and asks "how should I answer this", "can I mention my app here", "write a Reddit comment", "reply to this r/macapps question", "is there an app that… thread", "my Reddit comments get no upvotes", "trả lời thread Reddit", or wants daily Reddit answers for a product.
license: MIT
metadata:
  category: social
  difficulty: beginner
  time: "5 min per answer · 15 min/day"
  version: 1.0.0
  author: nvminhtu
---

# Reddit Answers That Earn Trust

> Paste a thread, get one answer in the right shape, a clear yes/no on mentioning your product, and a log line.

## Goal
On Reddit, answers do most of the marketing: they're read for years, they build karma in the subreddits where you'll
post later, and good ones send readers to your profile. This skill writes one answer at a time, specific enough to
be the top comment, and only mentions your product when it truly answers the question.

## When to use
- You found a thread where someone asks for something your product does, or something you know first-hand.
- You want to know whether a product mention is allowed and wise here.
- Your answers get ignored or removed and you want to see why.
- **Not for:** writing a full post → [launch-reddit-posting](../../../../skills/launch/launch-reddit-posting/SKILL.md)
  and [06-post-variants.md](../../docs/06-post-variants.md). Finding threads → [04-finding-threads.md](../../docs/04-finding-threads.md).

## Inputs
- The thread: subreddit, title, the question, and the top 2–3 existing answers.
- The subreddit's promotion rule (from its [wiki page](../../../../docs/subreddits/README.md) or rules page).
- Your product facts: what it does, price, platform, privacy, and what it does **not** do.
- How many of your recent comments in that subreddit mentioned your products (from your
  [thread tracker](../../templates/thread-tracker.md)).

## Steps
1. **Read the question twice.** Write down what they actually asked in one line, and what they already tried.
2. **Check what's there.** If the top answer is already complete, either add what's missing (a step, a number, a
   gotcha) or skip the thread.
3. **Pick one shape** ([05-comment-playbook.md](../../docs/05-comment-playbook.md)): direct fix · steps · honest
   comparison · first-hand experience · product answer · clarifying question.
4. **Run the five checks** before mentioning your product: it answers the exact question; the comment is useful
   without it; the subreddit allows it; you're under 1 in 10 product mentions there; you'll say it's yours. Any
   "no" → no mention.
5. **Write it:** answer in the first line, specifics (menu paths, versions, sizes, prices), short paragraphs, your
   own voice. If mentioning the product, put it last with a disclosure line, and link only if the rules allow, with
   `?utm_source=reddit&utm_medium=comment&utm_campaign=<subreddit>`.
6. **Post it by hand**, check it logged out after 10 minutes, and log it in the thread tracker.
7. **Come back once** that day to answer follow-up questions.

## Prompt (copy-paste)
Works in Claude, ChatGPT, Gemini, Cursor. Replace everything in `{{ }}`.

````text
You write Reddit answers for me, an indie developer. Sound like a helpful person who knows the topic, not a brand.
Never invent features, numbers or experiences I didn't give you; write <CHECK> where you'd need a fact.

Subreddit: r/{{name}}   Its promotion rule: {{e.g. "no self-promotion" / "allowed in comments if disclosed" / unknown}}
Thread title: {{...}}
The question (paste): {{...}}
Top existing answers (short): {{...}}
My product: {{name · what it does · price · platform · privacy · what it does NOT do · landing URL}}
My recent comments in this subreddit: {{N}}, of which {{M}} mentioned my products.

1. In one line, restate what they actually need.
2. Pick ONE shape (direct fix, steps, honest comparison, first-hand experience, product answer, clarifying question)
   and say why.
3. Run these checks and answer yes/no for each: answers the exact question · useful without my product ·
   subreddit allows it · under 1 in 10 product mentions after this one · I'll disclose it's mine.
   Mention my product only if all are yes.
4. Write the answer: first line is the answer; specifics; short paragraphs; no "Great question", no emoji, no
   em dashes, no marketing words. If mentioning my product, put it last with a disclosure line; add a link only if
   the rule allows, with utm_source=reddit&utm_medium=comment&utm_campaign={{name}}.
5. Give me one line for my thread tracker: date · subreddit · shape · product mentioned yes/no.
````

## Example output

> **Illustrative example.** Fictional products (Clipnest, Copydeck, TinyClip) and subreddit rule.

Thread (r/macapps, promotion allowed in comments if disclosed): *"Copydeck vs TinyClip vs something else? I mostly
need image search."*

1. Need: a clipboard manager that can search **inside images**.
2. Shape: **honest comparison**, because they asked to compare.
3. Checks: answers it ✔ · useful without mine ✔ · allowed if disclosed ✔ · 1 of 9 after this ✔ · disclose ✔ → mention.
4. Answer:
   > For image search specifically: check whether the app does text recognition on copied images, most don't.
   > Copydeck is the most polished but subscription-only. TinyClip is free and fast, but I don't believe it searches
   > inside images <CHECK>.
   > Disclosure: I make Clipnest, which does OCR on copied images, free for 50 clips. Try the free tiers of two and
   > see which you keep using.
5. Tracker: 2026-10-12 · r/macapps · comparison · yes (disclosed)

## Common mistakes
- **Leading with the product.** The answer has to stand without it, or it reads as an ad and gets removed.
- **Hiding that it's yours.** "I found this great app" about your own app breaks Reddit Rule 5 and ends accounts.
- **Answering 20 threads with the same text.** Repeated content is spam under Reddit's rules; write each answer for
  that thread.
- **Generic answers.** "There are many apps for this" earns nothing. Steps, names, prices, versions.
- **DMing the person afterwards.** Unsolicited messages are spam. Let them come to your profile.

## Related skills
- [09-comment-guide.md](../../docs/09-comment-guide.md): the full guide this skill follows (sorting, hidden
  filters, worked examples, checklist).
- [social-reddit](../social-reddit/SKILL.md): the router for every Reddit job.
- [launch-reddit-posting](../../../../skills/launch/launch-reddit-posting/SKILL.md): posts, subreddits by product
  type, the rules script.
- [social-credible-posting](../../../../skills/social/social-credible-posting/SKILL.md): the proof ladder behind
  every claim.

## Credits
Written by [@nvminhtu](https://github.com/nvminhtu). Sources: [Reddit Rules](https://redditinc.com/policies/reddit-rules),
[Reddit Help: Spam](https://support.reddithelp.com/hc/en-us/articles/360043504051-Spam) (checked 2026-10-12).
