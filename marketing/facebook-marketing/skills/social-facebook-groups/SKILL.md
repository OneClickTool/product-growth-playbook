---
name: social-facebook-groups
description: Get users from Facebook groups without spam, bans or burning your name. Finds 10–20 groups where your buyers ask for tools (by job, platform, profession, local language, competitor), scores them on activity, questions and promo rules, saves the rules, then writes answers that help first and mention your product only after a 5-check test, and one rule-checked post per group per month (how-to, before → after, free thing, feedback request, build story) with an admin message when the rules are silent and a UTM link per group. Use when someone says "which Facebook groups should I join", "post my app in a Facebook group", "answer this Facebook group question", "can I mention my app in this group", "my group post was declined", "Facebook groups marketing", "đăng app lên group Facebook", "tìm group Facebook", or pastes a group thread or rules.
license: MIT
metadata:
  category: social
  difficulty: beginner
  time: "1 hour to set up, then 15–20 min/day"
  version: 1.0.0
  author: nvminhtu
---

# Facebook Groups: Find, Answer, Post

> Five groups that fit, a daily answer habit, and one welcome post a month per group, each tracked by UTM.

## Goal
Groups are where non-developer buyers ask each other for tools. This skill picks the groups worth your time,
keeps you inside each group's rules and Meta's spam policy, and turns real questions into answers that bring
profile visits and signups, so admins approve your rare posts instead of removing them.

## When to use
- Your buyers are non-developers, local, or a hobby / job community, and you want them from Facebook.
- You have a thread or a group's rules and want to know what you may post.
- **Not for:** deciding if Facebook fits at all → [social-facebook](../social-facebook/SKILL.md) `fit`. Page and
  profile setup → [02-page-and-profile-setup.md](../../docs/02-page-and-profile-setup.md). Running your own group →
  [06-your-own-group.md](../../docs/06-your-own-group.md).

## Inputs
- Product facts you can prove: name, one line, price, platform, what's free, site URL, buyers' language.
- For answers: the thread text and the group's rules. For posts: the group's rules and what you've done there.
- Your [group tracker](../../templates/group-tracker.md) (or start one).

## Steps
1. **Find 10–20 groups** with five searches: the job, the platform, the profession or hobby, the local language,
   competitor names ([04-groups-playbook.md](../../docs/04-groups-playbook.md)).
2. **Score and join 5.** Activity (posts this week), questions asking for tools, promo rule, language. Paste each
   rule set into the tracker with today's date. Answer entry questions honestly.
3. **Answer 2–3 threads a day.** Answer the question fully first, add what you know from building, name other tools
   when they fit better. Run the 5-check test; mention the product with "I made it" only if all five pass:
   asked for a tool · useful without a click · rules allow · disclosed · not mentioned in this group this week.
4. **Post once per group per month, after 2+ weeks of answers.** Pick an allowed format
   ([05-post-formats.md](../../docs/05-post-formats.md)); first line in the group's words, no product name; "I made
   <product>" in the post; a real question at the end. Rules silent → send the admin message first.
5. **Link with UTM** where links are allowed:
   `<page>?utm_source=facebook&utm_medium=group&utm_campaign=<group-slug>&utm_content=<F-code>`. Save a
   [post file](../../templates/post-file.md).
6. **Track.** Every mention and post goes in the tracker; Sunday numbers in
   [weekly numbers](../../templates/weekly-numbers.md). After 30 days keep the top 3 groups, drop the bottom 2.

## Prompt (copy-paste)
Works in Claude, ChatGPT, Gemini, Cursor. Replace everything in `{{ }}`.

````text
You help me, an indie maker, get users from Facebook groups without spam. Write in {{language}}, plain and
specific, like a helpful member, not a brand. Never invent features, numbers, reviews or "free" claims; write
<CHECK> where you need a fact. Never suggest like/share-gating ("comment YES for the link"), tagging strangers,
cold messages, posting the same text in many groups, or bought engagement.

My product: {{name · one line · who for · price · platform · what's free · site URL}}
Job: {{find | reply | post}}

If find: give 10–20 Facebook group searches across: the job my product does, my platform, my buyers' profession or
hobby, local-language terms, competitor names. Then a scoring table I fill in: activity, tool questions, promo
rule, language, verdict (join / watch / skip).

If reply: here is the thread {{thread text}} and the group rules {{rules}}.
1. Write a full answer to the question first (steps, the free way, other tools if better).
2. Run the 5-check test and show each check: they asked for a tool or a one-step fix / useful without a click /
   rules allow a mention / I disclose I made it / not mentioned in this group in the last week ({{yes/no}}).
3. Only if all 5 pass, add one line: "I made {{product}} for this; it <does the last step>. <price>." plus the link
   {{URL}}?utm_source=facebook&utm_medium=group&utm_campaign={{group-slug}}&utm_content=f01 if links are allowed.

If post: here are the group rules {{rules}} and what I've done there {{weeks of answers, admin contact}}.
1. Say whether a post is allowed now, in a promo thread, or only with admin OK. If admin OK is needed, write the
   message to the admin (3 sentences, polite, what I'll share and where).
2. Pick one format: how-to, before→after, free thing, feedback request, build story, short video, poll.
3. Write the post: first line in the group's words with no product name; body; "I made {{product}}"; link with UTM
   (utm_content = format code) if allowed; a real question at the end.
4. Output it as a Markdown post file with frontmatter: where, format, rules_checked, admin_ok, date, link, status: planned.
````

## Example output

> **Illustrative example.** Fictional product, group and thread.

Thread in "Mac for Beginners": *"I copied an address, then copied a phone number, and the address is gone. Is
there a way to get it back?"*

Answer:
*"Sadly macOS only keeps the last thing you copied, so the address is gone unless it's still in the app you
copied it from (try Cmd+Z there). For next time: Spotlight won't help, but a clipboard history app will. Maccy is
free and open source; Raycast has one built in. I made Clipnest ($9, Mac) for the same problem; it keeps 30 days
of copies and lets you search them. Any of the three will do it."*

| Check | Result |
|---|---|
| Asked for a tool or one-step fix | Yes ("is there a way") |
| Useful without a click | Yes: Cmd+Z tip, two free options |
| Rules allow a mention | Yes: rule 4 "mention your own apps only when relevant, say you made them" |
| Disclosed | Yes: "I made Clipnest" |
| Not mentioned here this week | Yes |

No link in the answer (rule 5: links only in the Sunday thread). Tracker: `mac-for-beginners`, mention 1.

## Common mistakes
- **Joining 30 groups and posting on day one.** Most groups remove links from new members. Answer for 2 weeks first.
- **One text, many groups.** Rewrite for each group's language and question, one group a day at most.
- **Only answering when the product fits.** Then everyone sees a salesperson. Most answers should never mention it.
- **"DM me for the link."** It looks like a scam and moves the chat where admins can't see. Link where allowed, or none.
- **Arguing after a removal.** Read the rule, thank the admin, ask what's allowed, wait a month.
- **No `utm_campaign` per group.** Without it you can't tell the group that brings buyers from the one that brings likes.

## Related skills
- [social-facebook](../social-facebook/SKILL.md): the router for every Facebook job.
- [research-where-users-ask](../../../../skills/research/research-where-users-ask/SKILL.md): where the questions are, by country.
- [social-credible-posting](../../../../skills/social/social-credible-posting/SKILL.md): tone, proof and disclosure.
- [social-reddit-comment](../../../reddit-marketing/skills/social-reddit-comment/SKILL.md): the same answer-first method on Reddit.

## Credits
Written by [@nvminhtu](https://github.com/nvminhtu). Sources:
[Meta Community Standards: Spam](https://transparency.meta.com/policies/community-standards/spam/),
[Reducing the distribution of problematic content](https://transparency.meta.com/enforcement/taking-action/lowering-distribution-of-problematic-content),
[Social Media Examiner on Admin Assist](https://www.socialmediaexaminer.com/facebook-admin-assist-streamline-your-facebook-group-content-management/)
(checked 2026-10-13), and the [community posting](../../../../skills/growth/action/06-community-posting.md) step.
