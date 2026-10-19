---
name: social-facebook
description: The single entry point for Facebook marketing. Reads what you type after /social-facebook (today, groups, reply, post, page, own-group, numbers, fit, risk, start) and runs the right skill or doc from the Facebook marketing kit, so you don't have to remember which one to open. Groups first (answer, then one rule-checked post a month), a Page and profile that look real, your own group later, UTM on every link. Use when someone types "/social-facebook", "facebook", "should I use Facebook for my app", "which Facebook groups", "post my app in a Facebook group", "Facebook page setup", "my post was declined in a group", "Facebook link limit", "start a Facebook group for my users", "Facebook numbers", "làm Facebook", "đăng group Facebook", or pastes a group post and asks how to answer.
license: MIT
metadata:
  category: social
  difficulty: beginner
  time: "1 min to route, then the target's time (15–20 min/day)"
  version: 1.0.0
  author: nvminhtu
---

# Facebook: One Command, the Right Skill

> Type `/social-facebook <what you want>` and get sent to the one Facebook skill or doc that does it.

## Goal
Facebook marketing for a small product is mostly finding the groups where your buyers ask for tools, answering
there every day, posting rarely and by the rules, and having a profile and Page that look real when people click
through. The pieces live in this kit's docs, templates and
[social-facebook-groups](../social-facebook-groups/SKILL.md). This router maps a short command to the right one,
runs it, and tells you the next command.

## When to use
- You want a fixed set of short commands for the daily habit: `today`, `reply`, `post`, `numbers`.
- You aren't sure Facebook fits your product and want a yes / test / no.
- **Not for:** paid Meta ads (not covered by this kit); other channels → [growth](../../../../skills/growth/SKILL.md)
  or the [marketing hub](../../../README-marketing-social.md). Instagram → [social-instagram](../../../instagram-marketing/skills/social-instagram/SKILL.md).

## Inputs
- The command word and what it needs (a thread for `reply`, a group + its rules for `post`, a table for `numbers`).
- Once: your product (one line, who for, price, platform, site URL, language of your buyers).

## Steps
1. **Read the first word** and route with this table. No command word: match the question to the closest row; still
   unclear, show the table and ask.

   | Command | Aliases | Runs | You get |
   |---|---|---|---|
   | `today` | daily, hôm nay | [flow/weekly-flow.md](../../flow/weekly-flow.md) | Today's 2–3 threads to answer, this week's one post, if any |
   | `groups <topic>` | find, tìm group | [social-facebook-groups](../social-facebook-groups/SKILL.md) step 1–2 | 10–20 groups to search for, scored on fit, activity, rules |
   | `reply <thread>` | answer, trả lời | [social-facebook-groups](../social-facebook-groups/SKILL.md) step 3 | One answer, 5-check test result, with or without the product |
   | `post <group + rules>` | đăng bài | [social-facebook-groups](../social-facebook-groups/SKILL.md) step 4 + [05-post-formats.md](../../docs/05-post-formats.md) | One post in an allowed format, admin message if needed, a post file |
   | `page` | profile, setup | [02-page-and-profile-setup.md](../../docs/02-page-and-profile-setup.md) | Profile intro, Page name, bio, cover, pinned post, links with UTM |
   | `own-group` | my group, cộng đồng | [06-your-own-group.md](../../docs/06-your-own-group.md) | Name, description, rules, entry questions, first 30 days |
   | `numbers` | stats | [07-metrics-and-stop-rules.md](../../docs/07-metrics-and-stop-rules.md) + [weekly numbers](../../templates/weekly-numbers.md) | Weekly table, weakest step, what to change |
   | `fit` | worth it?, nên không | [01-strategy.md](../../docs/01-strategy.md) fit test | Yes / test 30 days / no, with the signals |
   | `risk` | declined, removed, blocked | [08-rules-and-risks.md](../../docs/08-rules-and-risks.md) | What happened, what's allowed, what to do now |
   | `start` | bắt đầu | [README](../../README-Facebook-Marketing.md) "Start in 3 steps" | Fit → profile + Page → 5 groups joined |

2. **Run the target** with what the user gave: load the target `SKILL.md` and follow it, or read the doc and answer
   from it with links.
3. **Keep the kit's rules in every output:** answer before you mention; say "I made it"; follow each group's rules
   and ask the admin when they're silent; one post per group per month at most; never the same text in many groups;
   no like/share-gating or engagement bait; no cold messages, no scraping, no bought engagement; UTM
   `utm_source=facebook` on every link; no invented numbers; write in the group's language.
4. **End with the next command**, e.g. after `fit` = yes → "`/social-facebook page`"; after `groups` →
   "`/social-facebook reply` on today's threads"; on Sunday → "`/social-facebook numbers`".

## Prompt (copy-paste)
Works in Claude, ChatGPT, Gemini, Cursor. Replace everything in `{{ }}`.

````text
You are my Facebook marketing assistant for a small software product. Route my request to one job and do it:
fit = yes / test 30 days / no for Facebook, using: are my buyers non-developers, are there active groups for the
      job my product does, do those groups ask for tools, do their rules allow any promotion, can I write their language
groups = 10–20 group searches (job, platform, profession/hobby, local language, competitor), and how to score each
      (activity, questions, promo rule, language)
reply = a full answer to the thread first; then the 5-check test (they asked for a tool / useful without a click /
      rules allow / I say I made it / not mentioned in this group this week); product line only if all 5 pass
post = one post in a format the group allows (how-to, before→after, free thing, feedback request, build story,
      short video, poll); first line in the group's words with no product name; "I made X" in the post; a real
      question at the end; an admin message if the rules don't say
page = profile intro, Page name/bio/cover/pinned post, links with UTM
own-group = name after the job, description, 5–7 rules, 2–3 entry questions, first 30 days
numbers = read my weekly table and name the weakest step (answers → reactions → profile visits → clicks → signups)
Rules: never like/share-gate or bait; never the same text in many groups; no cold messages; never invent numbers,
users or features (write <CHECK>); write in the group's language; links use
utm_source=facebook&utm_medium=group|page|profile&utm_campaign=<group-slug>&utm_content=<format>.

My request: {{fit | groups <topic> | reply <thread text + group rules> | post <group + rules> | page | own-group | numbers <table>}}
My product: {{name · one line · who for · price · platform · site URL · buyers' language}}

Say which job you picked in one line, do it, then tell me the next request I should make.
````

## Example output

> **Illustrative example.** Fictional product.

Input: `/social-facebook fit` — *Shopnote, an iPhone app for small online sellers in Vietnam to track orders and
customer addresses, free with Pro 99,000₫/month.*

Routed to **fit** ([01-strategy.md](../../docs/01-strategy.md)).

| Signal | Answer |
|---|---|
| Buyers are non-developers? | Yes: small sellers on Facebook and Shopee |
| Active groups for the job? | `<CHECK>` search "bán hàng online", "chủ shop", "quản lý đơn hàng" and note posts this week |
| They ask for tools? | Likely ("app nào quản lý đơn…"); confirm by reading a month of posts |
| Rules allow promotion? | Varies: many seller groups have a promo day; save each rule set |
| Language | Vietnamese: yes |

Verdict: **yes, as the main channel**, answers in Vietnamese seller groups first, own group "Chủ shop online dùng
iPhone" after 20 users. Next: `/social-facebook page`.

## Common mistakes
- **Starting with the Page.** A new Page reaches almost no one. Start in groups; the Page is where they check you.
- **Posting the same text in ten groups.** Admins see it, members report it, Meta counts very high frequency as spam.
- **"Comment YES for the link."** That's engagement gating. Put the link in the post or comment, or don't.
- **Hiding that you made it.** One honest "I made this" keeps you welcome; one exposed fake review ends it.
- **Asking the agent to post or DM with a bot.** It drafts; you post by hand or with Meta's own scheduler.

## Related skills
- [social-facebook-groups](../social-facebook-groups/SKILL.md): find, answer and post in groups.
- [social-credible-posting](../../../../skills/social/social-credible-posting/SKILL.md): the proof ladder behind every claim.
- [social-instagram](../../../instagram-marketing/skills/social-instagram/SKILL.md): the visual side of the same Meta account.
- [social-reddit-comment](../../../reddit-marketing/skills/social-reddit-comment/SKILL.md): the same answer-first method on Reddit.

## Credits
Written by [@nvminhtu](https://github.com/nvminhtu). Sources: the docs in this kit,
[Meta Community Standards: Spam](https://transparency.meta.com/policies/community-standards/spam/),
[Reducing the distribution of problematic content](https://transparency.meta.com/enforcement/taking-action/lowering-distribution-of-problematic-content)
and [TechCrunch on the link test](https://techcrunch.com/2025/12/17/facebook-is-testing-a-link-posting-limit-for-professional-accounts-and-pages)
(checked 2026-10-13).
