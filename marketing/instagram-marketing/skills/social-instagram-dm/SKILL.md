---
name: social-instagram-dm
description: Turn Instagram comments and DMs into website visits - the only clickable path besides the bio link and the Story sticker. Builds the first-hour comment routine, a comment-keyword → DM flow ("Comment CLEAN and I'll send the checklist") with message 1, a button and message 2 carrying the link with utm_medium=dm, the Meta messaging rules it must follow (person starts the chat, 24-hour window, one private reply within 7 days of a comment, official API tools only), saved replies for the 5 questions people always ask, a Broadcast channel plan, and the clicks-per-flow-entry check. Use when someone asks "comment to DM", "ManyChat for Instagram", "comment keyword get link", "auto DM on Instagram", "how to send a link on Instagram", "Instagram DMs for my app", "broadcast channel", "trả lời comment Instagram", "comment nhận link", "inbox Instagram ra đơn", or gets comments but no website visits.
license: MIT
metadata:
  category: social
  difficulty: beginner
  time: "Setup 45 min · 10-20 min/day"
  version: 1.0.0
  author: nvminhtu
---

# Instagram DMs: Comments → Messages → Website Visits

> One post a week where people comment a word and get exactly what you promised in a DM, with a tracked link, plus a
> daily routine that answers every comment and question like a person.

## Goal
Links in feed captions don't click (Practice: how the app behaves). A DM link does. This skill sets up the DM path
from [docs/06](../../docs/06-stories-and-links.md) and engine 6 of [docs/09](../../docs/09-growth-engine.md#engine-6--dm-engine-the-click-machine)
so 1–2 posts a week send people straight to your landing page, inside Meta's messaging rules, and so you can see
which post sent them (`utm_medium=dm&utm_content=<post-id>`).

## When to use
- Posts get comments and saves, but link taps from the bio are low.
- You have something real to send: a checklist, a template, a free version, a waitlist.
- People keep asking the same questions in comments ("price?", "Windows?", "what app is this?").
- **Not for:** getting the post seen in the first place → [social-instagram-image-flow](../social-instagram-image-flow/SKILL.md).
  The Story link path → `/social-instagram story`. Influencer outreach DMs → [social-instagram-creators](../social-instagram-creators/SKILL.md).

## Inputs
- The post (id, slides, caption) and the **one thing** you'll send: a real checklist, file or page.
- Landing URL and slug for the UTM.
- The 5 questions people already ask about the product, with true answers (price as the store shows it today).
- Whether you'll answer by hand (fine under ~50 comments a post) or with a tool on Meta's official API.

## Steps
1. **First-hour routine (every post, 10 min).** Answer every comment with a real sentence, not an emoji. Answer
   questions in public (others read them), then offer the link in DM: "Sent you the link 👋". Pin the most useful
   comment. Feed ranking predicts comments and shares (Official, Instagram Ranking Explained).
2. **Saved replies for the 5 questions.** Write one true answer each (price, platform, privacy, free vs paid, "what
   app is this?"); store them as quick / saved replies in the Instagram inbox if your account has them (Practice:
   confirm in your app), or in a notes file. Edit each one to the person before sending.
3. **Pick the keyword post (1–2 a week).** A send-able carousel (checklist, mistakes, before/after) whose last slide
   promises something only the DM gives. One word, easy to type, tied to the post: `CLEAN`, `LIST`, `MAP`.
   ```text
   Last slide + caption line:  "Comment CLEAN and I'll DM you the 5-step checklist + the free app"
   ```
4. **Write the flow (3 messages max).**
   ```text
   Public reply (auto or by hand): "Sent 👋 check your DMs"
   Message 1 (private reply):       "Here you go 👋 Want the checklist and the free app link?"  [button: Send it]
   Message 2 (after they tap):      the checklist itself (real) + <landing>?utm_source=instagram&utm_medium=dm
                                    &utm_campaign=<slug>&utm_content=<post-id>
   ```
   Vendor benchmarks put clicks at ~18–25 % of people who enter a flow, and the link in message 2 after a button
   beat message 1 (Practice, vendor data). Message 2 must give exactly what the post promised.
5. **Follow Meta's messaging rules.** (Official, Meta developer docs, checked 2026-10-13)
   - The **person starts** the conversation (a DM, or a comment you answer with a private reply). No cold DMs from a tool.
   - A **private reply** to a comment is **one message**, sent within **7 days** of the comment.
   - After someone messages you, automated messages go inside the **24-hour** standard window; the **human agent**
     tag (up to 7 days) is for a real person answering, not for bots or promos.
   - Use a tool built on the official Instagram messaging API (Meta business partner), never a password-sharing bot.
6. **Broadcast channel.** Open one on the brand account; invite followers once from a Story. Post only what they'd
   want pushed: launches, betas, a discount window, a new free resource; at most 1–2 a week. It's one-to-many to
   people who joined (Official, Meta newsroom).
7. **Measure every Sunday.** Per keyword post: comments with the keyword (flow entries) → button taps → link clicks
   (from the tool) → landing sessions with `utm_medium=dm` and `utm_content=<post-id>` (GA4) → trials / emails.
   Clicks ÷ entries ≥ 15 % is fine; under 10 % → change message 1 or the button text, not the post (Practice, from
   [docs/09 dashboard](../../docs/09-growth-engine.md#the-operator-dashboard-sunday-20-min)). Log it in
   [templates/dm-flow.md](../../templates/dm-flow.md).

## Prompt (copy-paste)
Works in Claude, ChatGPT, Gemini, Cursor. Replace everything in `{{ }}`.

````text
You run Instagram comments and DMs for my product so they turn into website visits.
Product: {{name}} · {{one line}} · offer today (as the store shows it): {{...}} · landing: {{url}} · slug: {{slug}}.
The post: id {{post-id}} · format {{carousel/Reel}} · what it teaches: {{...}}.
What I can send for real in a DM: {{checklist / template / free version / waitlist}}.
Questions people already ask, with true answers: {{...}}.
Rules: never invent numbers, reviews or features; the DM gives exactly what the post promised; the person starts
the chat (comment or DM), one private reply per comment within 7 days, automated messages only inside 24 h of their
last message, no cold DMs, no fake urgency; every link has utm_source=instagram&utm_medium=dm&utm_campaign={{slug}}
&utm_content={{post-id}}.

Give me:
1. The keyword (one word) and the last-slide line + caption line that ask for it.
2. The public auto-reply, message 1 (≤ 25 words) with a button label, and message 2 with the real content and the
   link.
3. 5 saved replies (≤ 40 words each) for my questions, written to be edited per person.
4. 3 first-hour comment replies for the likely comment types (praise, doubt, question).
5. 2 Broadcast channel messages for this week (one value, one news), no hype.
6. The Sunday tracking row: entries, button taps, clicks, landing sessions, trials, clicks ÷ entries, and what to
   change if it's under 10 %.
````

## Example output

> **Illustrative example.** Fictional product (Tidybox, a Mac cleaner); no real results.

```text
Keyword: CLEAN
Last slide: "Comment CLEAN → I'll DM you the 5-step checklist + the free app"
Public reply: "Sent 👋 check your DMs"
Message 1: "Here's your Downloads checklist 👋 Want it plus the free Tidybox link?"   [Send it]
Message 2: "1 copies (1)(2)(3) · 2 old .dmg · 3 not opened in 90 days · 4 files 500 MB+ · 5 loose files.
            Tidybox finds all 5, free for 2 folders:
            https://tidybox.example/?utm_source=instagram&utm_medium=dm&utm_campaign=tidybox&utm_content=07-tidybox-checklist"
Saved reply · "Windows?": "Mac only for now (macOS 14+). I'll post here if that changes."
Sunday row: entries <N?> · taps <N?> · clicks <N?> · sessions <N?> · trials <N?> → clicks ÷ entries <%?>
```

## Common mistakes
- **Bait and switch.** "Comment LIST" then only a store link. Send the list; the link rides along.
- **Link in message 1.** Ask first, link after the tap; it reads as a conversation, not spam.
- **Keyword on every post.** 1–2 a week; the rest of the feed earns sends and saves on its own.
- **Copy-paste replies.** Saved replies are drafts; change the first line for the person.
- **Cold DMs or unofficial bots.** Outside Meta's rules; they risk the account's messaging and reach.
- **No `utm_content`.** You'll see `instagram / dm` in GA4 but not which post earned it.

## Related skills
- [social-instagram](../social-instagram/SKILL.md): `/social-instagram dm <post>` routes here.
- [social-instagram-image-flow](../social-instagram-image-flow/SKILL.md): the post the keyword lives on (step 9, the link path).
- [social-instagram-engine](../social-instagram-engine/SKILL.md): engine 6 among the 8 engines.
- [email-list-and-deliverability](../../../../skills/email/email-list-and-deliverability/SKILL.md): turn DM clicks into an email list you own.

## Credits
Written by [@nvminhtu](https://github.com/nvminhtu). Sources (checked 2026-10-13):
[Messenger Platform and IG Messaging API policy](https://developers.facebook.com/documentation/business-messaging/messenger-platform/policy) ·
[Instagram messaging API: send messages](https://developers.facebook.com/documentation/instagram-platform/instagram-api-with-instagram-login/messaging-api) ·
[Meta: Broadcast channels](https://about.fb.com/news//2023/02/instagram-broadcast-channels-creators-deepen-connections-with-followers/) ·
[Instagram Ranking Explained](https://about.instagram.com/blog/announcements/instagram-ranking-explained) ·
[Inrō glossary (vendor benchmark)](https://www.inro.social/glossary/dm-click-through-rate).
