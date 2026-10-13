---
name: social-pinterest
description: The single entry point for Pinterest marketing. Reads what you type after /social-pinterest (today, keywords, pin, boards, profile, numbers, fit, risk, start) and runs the right skill or doc from the Pinterest marketing kit, so you don't have to remember which one to open. Pins link to a page on your own site, made fresh each week, written for Pinterest search. Use when someone types "/social-pinterest", "pinterest", "should I use Pinterest for my app", "make pins for this page", "Pinterest keywords", "name my Pinterest boards", "set up Pinterest business account", "claim my website on Pinterest", "Pinterest numbers", "my link is blocked on Pinterest", "pin cho app", "làm Pinterest", or pastes a page URL and asks for pins.
license: MIT
metadata:
  category: social
  difficulty: beginner
  time: "1 min to route, then the target's time (≈1 hour/week batch)"
  version: 1.0.0
  author: nvminhtu
---

# Pinterest: One Command, the Right Skill

> Type `/social-pinterest <what you want>` and get sent to the one Pinterest skill or doc that does it.

## Goal
Pinterest marketing for a small product is mostly picking search terms people really type, having a page that
serves each one, and making fresh tall pins for those pages every week. The pieces live in this kit's docs, templates
and [social-pinterest-pin](../social-pinterest-pin/SKILL.md). This router maps a short command to the right one, runs
it, and tells you the next command.

## When to use
- You want a fixed set of short commands for the weekly batch: `today`, `pin`, `numbers`.
- You aren't sure Pinterest fits your product and want a yes / test / no.
- **Not for:** other channels → [growth](../../../../skills/growth/SKILL.md) or the
  [marketing hub](../../../README-marketing-social.md).

## Inputs
- The command word and what it needs (a page URL for `pin`, a topic for `keywords`, a table for `numbers`).
- Once: your product (one line, who for, price, platform, site URL) and 3 pages worth landing on.

## Steps
1. **Read the first word** and route with this table. No command word: match the question to the closest row; still
   unclear, show the table and ask.

   | Command | Aliases | Runs | You get |
   |---|---|---|---|
   | `today` | week, batch, hôm nay | [flow/weekly-flow.md](../../flow/weekly-flow.md) | This week's 2–3 pages, 5–10 pins to make, the schedule |
   | `keywords <topic>` | search, terms, từ khoá | [04-keywords-and-boards.md](../../docs/04-keywords-and-boards.md) + [keyword sheet](../../templates/keyword-sheet.md) | 3 terms per page, where to check them, trend notes |
   | `pin <page URL>` | pins, make, làm pin | [social-pinterest-pin](../social-pinterest-pin/SKILL.md) | 3–5 different pins for that page, in a pin file |
   | `boards` | board | [04-keywords-and-boards.md](../../docs/04-keywords-and-boards.md) + [board plan](../../templates/board-plan.md) | 5–10 board names and descriptions |
   | `profile` | setup, claim, bio | [02-profile-setup.md](../../docs/02-profile-setup.md) | Business account, claim method, name, about, website with UTM |
   | `numbers` | stats | [07-metrics-and-stop-rules.md](../../docs/07-metrics-and-stop-rules.md) + [weekly numbers](../../templates/weekly-numbers.md) | Weekly table, weakest step, what to change |
   | `fit` | worth it?, nên không | [01-strategy.md](../../docs/01-strategy.md) fit test | Yes / test 90 days / no, with the signals |
   | `risk` | blocked, suspended, spam | [08-rules-and-risks.md](../../docs/08-rules-and-risks.md) | What happened, what's allowed, what to do now |
   | `start` | bắt đầu | [README](../../README-Pinterest-Marketing.md) "Start in 3 steps" | Fit → profile → first 9 pins |

2. **Run the target** with what the user gave: load the target `SKILL.md` and follow it, or read the doc and answer
   from it with links.
3. **Keep the kit's rules in every output:** a new image for every pin, no re-saving the same pin; every pin links to
   a real page that delivers the promise; UTM `utm_source=pinterest` on every link; no unapproved automation, no
   bought engagement; never present an AI image as a real photo or customer; no invented numbers.
4. **End with the next command**, e.g. after `fit` = yes → "`/social-pinterest profile`"; after `pin` →
   "`/social-pinterest pin` for the next page"; on Sunday → "`/social-pinterest numbers`".

## Prompt (copy-paste)
Works in Claude, ChatGPT, Gemini, Cursor. Replace everything in `{{ }}`.

````text
You are my Pinterest marketing assistant for a small software product. Route my request to one job and do it:
fit = yes / test 90 days / no for Pinterest, using: can one tall image show the result, do my buyers plan things,
      do I have pages worth landing on, does the topic show up in Pinterest search
keywords = 3 search terms per page (main, narrower, problem), where to check them (autocomplete, Trends), seasonality
pin = 3–5 different pins for the page (variants: result, before/after, how-to steps, checklist, list of ideas,
      comparison, template preview, short video): image brief, title with the term first (first 40 chars carry it),
      1–2 sentence description, best board, link with UTM
boards = 5–10 boards named after search terms, each with a 1–2 sentence description
profile = business account, how to claim my site, display name, about line, website link with UTM
numbers = read my weekly table and name the weakest step (impressions → saves → outbound clicks → visits → signups)
Rules: new image for every pin, never re-save the same pin; link to a real page that delivers the promise; never
invent numbers, users or features (write <CHECK>); no automation or bought engagement; don't present AI images as
real photos; links use utm_source=pinterest&utm_medium=pin&utm_campaign=<page>&utm_content=<variant>.

My request: {{fit | keywords <topic> | pin <page URL + what the page offers> | boards | profile | numbers <table>}}
My product: {{name · one line · who for · price · platform · site URL}}
My pages worth landing on: {{URL · what it offers}}

Say which job you picked in one line, do it, then tell me the next request I should make.
````

## Example output

> **Illustrative example.** Fictional product.

Input: `/social-pinterest fit` — *Clipnest, a Mac clipboard manager, $9; site has a landing page and two how-to
posts ("Mac clipboard history", "Mac keyboard shortcuts cheat sheet").*

Routed to **fit** ([01-strategy.md](../../docs/01-strategy.md)).

| Signal | Answer |
|---|---|
| One tall image shows the result? | Partly: a shortcuts cheat sheet does, a clipboard list less so |
| Buyers plan things? | Students and remote workers setting up a Mac: yes |
| Pages worth landing on? | Yes: the cheat sheet is printable |
| Shows up in search? | `<CHECK>` type "mac shortcuts" into Pinterest search and note suggestions |

Verdict: **test for 90 days**, built around the cheat sheet page (P04 checklist, P03 how-to), not the landing page.
Next: `/social-pinterest profile`.

## Common mistakes
- **Pinning the App Store link.** Strangers on Pinterest want the thing they searched for. Link a page that gives it.
- **Saving one pin to ten boards in a day.** Repetitive saving is spam under Pinterest's rules. New image, best board.
- **Judging after two weeks.** Pinterest is slow. Decide at 90 days, from outbound clicks and signups.
- **Asking the agent to post with a bot.** It drafts; you schedule with Pinterest's own tools or an approved scheduler.

## Related skills
- [social-pinterest-pin](../social-pinterest-pin/SKILL.md): the pins for one page.
- [social-instagram-image-flow](../../../instagram-marketing/skills/social-instagram-image-flow/SKILL.md): the same
  facts as carousels; re-cut to 2:3 for Pinterest.
- [social-tiktok-slideshow](../../../tiktok-marketing/skills/social-tiktok-slideshow/SKILL.md): slides that also
  work as a pin set.

## Credits
Written by [@nvminhtu](https://github.com/nvminhtu). Sources: the docs in this kit,
[Pinterest Community Guidelines](https://policy.pinterest.com/en/community-guidelines),
[Pinterest Help: product specs](https://help.pinterest.com/en/business/article/pinterest-product-specs) and
[Pinterest Help: Trends](https://help.pinterest.com/en/business/article/pinterest-trends) (checked 2026-10-13).
