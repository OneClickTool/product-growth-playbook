---
name: social-instagram
description: One command for the Instagram marketing kit. Routes `/social-instagram post · week · month · profile · story · numbers · risk · engine · creators · hooks · network` to the right Instagram skill or doc - one image post built with the 10-step image flow, next week's 5 posts and 3 Story sequences, the 30-day plan, profile setup with UTM bio links and Highlights, a 3-frame Story with a link sticker, the Sunday numbers check, what cuts reach, the 8-engine Operator plan, the creator program, hook tests or the niche account network. Use when someone types /social-instagram, says "Instagram", "IG", "Insta", "what do I post on Instagram today", "Instagram plan", "Instagram for my app", "đăng Instagram", "quy trình Instagram", "làm bài Instagram", or doesn't know which Instagram skill to use.
license: MIT
metadata:
  category: social
  difficulty: beginner
  time: 1 min to route
  version: 1.0.0
  author: nvminhtu
---

# /social-instagram: One Command for Instagram

> Type one word, get the right Instagram flow: a post, a week, a month, the profile, a Story, the numbers, the risks, or the Operator engine.

## Goal
The Instagram kit has four skills and eleven docs. This router reads the command (or the question), opens the right
one, asks only for the inputs that one needs, and returns a finished result in the same format every time.

## When to use
- Someone types `/social-instagram <command>` or asks anything about Instagram for their product.
- **Not for:** X → [social-x](../../../x-marketing/skills/social-x/SKILL.md). TikTok / Shorts only →
  [social-short-video](../../../../skills/social/social-short-video/SKILL.md).

## Inputs
- The command (below). If none is given, ask one question: "A post, the week, or the profile?"
- Whatever the routed skill lists as its inputs (product, fact bank, screenshots, landing URL).

## Steps
1. **Read the command** and route:

   | Command | Opens | Returns |
   |---|---|---|
   | `post <fact or product>` | [social-instagram-image-flow](../social-instagram-image-flow/SKILL.md) | One post: format, 5 hooks, slide script or shot list, caption, alt text, Story, UTM links, post file |
   | `week` | [social-instagram-growth](../social-instagram-growth/SKILL.md) step 4–5 | 5 posts + 3 link Stories + 2 Stories, bio link 1 per day |
   | `month` | [posts/plan-30-days.md](../../posts/plan-30-days.md) (or build one with the growth skill) | 30 days, day by day, with weekly checks |
   | `profile` | [docs/02-profile-setup.md](../../docs/02-profile-setup.md) | Name field, bio, 5 links with UTM, Highlights, pins |
   | `story <post>` | [docs/06-stories-and-links.md](../../docs/06-stories-and-links.md) + [template](../../templates/story-sequence.md) | 3 frames with poll and link-sticker text + URL |
   | `numbers` | [docs/07-metrics-and-stop-rules.md](../../docs/07-metrics-and-stop-rules.md) + [template](../../templates/weekly-numbers.md) | Filled weekly numbers, weakest arrow, one fix, keep/drop |
   | `risk` | [docs/08-rules-and-risks.md](../../docs/08-rules-and-risks.md) | What in the user's plan cuts reach, and the fix |
   | `flow` | [docs/04-image-flow.md](../../docs/04-image-flow.md) | The 10-step card |
   | `engine` | [social-instagram-engine](../social-instagram-engine/SKILL.md) | Operator week across 8 engines, budget, kill rules |
   | `creators` | [social-instagram-creators](../social-instagram-creators/SKILL.md) | Creator queries, DMs, deal tiers, brief, tracker |
   | `hooks <idea>` | [docs/11-hook-bank.md](../../docs/11-hook-bank.md) + [templates/hook-tests.md](../../templates/hook-tests.md) | 3 hooks (pain / number / before-after) for one body |
   | `network` | [docs/09, engine 3](../../docs/09-growth-engine.md#engine-3--owned-niche-network-24-accounts) | Niche account topics, bio disclosure, 14 first posts |

2. **Ask only for missing inputs** of that route, in one message.
3. **Run it** and return the result in the route's format. Every number must come from the user's facts or carry
   `<NUMBER?>`.
4. **End with the next command** (e.g. after `post`: "`/social-instagram story 03-tidybox-downloads` in 1–3 h").

## Prompt (copy-paste)
Works in Claude, ChatGPT, Gemini, Cursor. Replace everything in `{{ }}`.

````text
You run my Instagram kit. Command: {{post | week | month | profile | story | numbers | risk | flow | engine | creators | hooks | network}} {{argument}}.
My products (pitch · who for · offer today · landing URL · slug): {{...}}
Fact bank: {{...}}
Rules: never invent numbers, users, reviews or results; no URL in captions (say "link in bio"); max 5 hashtags;
real screenshots before AI images; every link has utm_source=instagram, utm_medium (bio|story|dm),
utm_campaign=<slug>, utm_content=<post-id>; at most one offer post in five.
Do the command:
- post: the 10-step image flow for one post, ending with the post file.
- week: 5 posts (Mon teach carousel, Wed demo Reel, Thu send-able carousel, Fri single/behind the scenes,
  Sun tips/tour/numbers/offer) + Story sequences on Mon, Wed, Sat + bio link 1 per day.
- profile: name field, 3-line bio, up to 5 bio links with UTM, Highlights, 3 pins.
- story: 3 frames (tease / proof + poll / path + link sticker text + URL).
- numbers: from my numbers {{...}}, the funnel reach → profile → link tap → landing → trial → paid, the
  weakest arrow, one fix, formats to keep / drop / try.
- risk: what in my plan {{...}} could cut reach or the account, and what to do instead.
- engine: next week across 8 engines (factory, hook lab, niche accounts, creators, collabs, DM, paid on winners,
  search) for my budget and hours, with kill rules.
- creators: queries to find micro-creators, DM 1 + follow-up, deal tiers, brief, tracker.
- hooks: 3 hooks (pain / number / before-after, ≤ 8 words) for the same body.
- network: 2-4 niche account topics, bio disclosure line, 14 first posts (80% value, 20% product).
End with the next command I should run.
````

## Example output

> **Illustrative example.** Fictional product.

`/social-instagram story 03-tidybox-downloads` →

```text
1 tease: share post 03 — "New: clean Downloads in one scan"
2 proof: 5 s clip, 214 duplicates found → Trash — poll "Is your Downloads a mess?" Yes / Very
3 path: "Free for 2 folders ↓" — sticker "Get Tidybox"
  https://tidybox.example/?utm_source=instagram&utm_medium=story&utm_campaign=tidybox&utm_content=03-tidybox-downloads
Next: add frame 3 to the "Tidybox" Highlight · at +48 h run /social-instagram numbers
```

## Common mistakes
- Running `week` without a fact bank: the plan fills with generic tips. Build the fact bank first.
- Skipping `profile`: posts send visits to a profile that doesn't say what you make.
- Using `post` for every idea and never `numbers`: you can't tell which format works.

## Related skills
- [social-instagram-image-flow](../social-instagram-image-flow/SKILL.md) · [social-instagram-growth](../social-instagram-growth/SKILL.md)
- [social-x](../../../x-marketing/skills/social-x/SKILL.md): the same router idea for X.

## Credits
Written by [@nvminhtu](https://github.com/nvminhtu). Facts and sources: [reference/instagram-facts.md](../../reference/instagram-facts.md).
