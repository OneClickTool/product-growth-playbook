---
name: social-pinterest-pin
description: Make 3–5 different Pinterest pins for one page of your site that people search for and click through. Picks the page's search terms (main, narrower, problem), chooses a different variant per pin (result, before/after, how-to steps, checklist, list of ideas, comparison, template preview, short video), writes a 2:3 image brief, a title with the term in the first 40 characters, a short description, the best board and a UTM link, and saves it all as a pin file. Use when someone says "make pins for this page", "Pinterest pin for my app", "write Pinterest titles and descriptions", "pin ideas for my template", "my pins get impressions but no clicks", "làm pin Pinterest", or pastes a URL and asks for Pinterest content.
license: MIT
metadata:
  category: social
  difficulty: beginner
  time: "20 min per page (plus image making)"
  version: 1.0.0
  author: nvminhtu
---

# Pinterest Pins for One Page

> Paste one page, get 3–5 fresh pins that each say the search term, show the result and link back with UTM.

## Goal
On Pinterest, one useful page fed by several different pins does better than one pin saved many times, and it
stays within Pinterest's rule against repetitive content. This skill turns one page into a small, varied pin set,
written for the words people search, ready to make and schedule.

## When to use
- You have a page worth landing on (how-to, free template, checklist, comparison, landing with a clear demo).
- Your pins get impressions but few outbound clicks and you want new variants.
- **Not for:** deciding if Pinterest fits at all → [social-pinterest](../social-pinterest/SKILL.md) `fit`. Board names
  and keyword research for a whole topic → [04-keywords-and-boards.md](../../docs/04-keywords-and-boards.md).

## Inputs
- The page: URL, its promise in one line, what's on it (steps, template, download, price).
- 1–3 search terms from your [keyword sheet](../../templates/keyword-sheet.md), or the topic to find them.
- Your boards ([board plan](../../templates/board-plan.md)).
- Product facts you can prove (price, platform, "free" is really free).

## Steps
1. **One promise.** Write the page's promise in one line. If the page doesn't deliver it in the first screen, fix the
   page first.
2. **Three terms.** Main, narrower, problem ([04-keywords-and-boards.md](../../docs/04-keywords-and-boards.md)).
   Check them in Pinterest search autocomplete.
3. **Pick 3–5 variants**, all different ([06-pin-variants.md](../../docs/06-pin-variants.md)): at least one that shows
   the result (P01/P02/P07) and one that teaches (P03/P04).
4. **Brief each image** at 1000 × 1500: headline (3–7 words, the term or the result), what the picture shows, small
   detail line, name or domain small ([05-pin-design.md](../../docs/05-pin-design.md)).
5. **Write the text:** title starts with a term and carries the promise in the first 40 characters (≤ 100);
   description 1–2 sentences with 1–2 related terms said naturally and a plain call to action.
6. **Board and link:** the most specific board; link
   `<page>?utm_source=pinterest&utm_medium=pin&utm_campaign=<page-slug>&utm_content=<variant>`.
7. **Save the [pin file](../../templates/pin-file.md)**, make the images, schedule them on different days.
8. **After 30 days**, fill the result table; the variant with the most outbound clicks gets 2 new siblings.

## Prompt (copy-paste)
Works in Claude, ChatGPT, Gemini, Cursor. Replace everything in `{{ }}`.

````text
You write Pinterest pins for me, an indie developer. Plain, specific words, no hype, no emoji walls, no hashtags
lists. Never invent features, numbers, reviews or "free" claims I didn't give you; write <CHECK> where you need a fact.

Page: {{URL}}
What the page gives the reader: {{promise in one line + what's on it}}
Product facts: {{name · price · platform · what's free}}
Search terms (if known): {{main · narrower · problem}}  If not known, propose 3 and tell me to check them in
Pinterest search autocomplete.
My boards: {{list}}

1. Restate the page's promise in one line. If the page can't deliver it in the first screen, say so.
2. Give 3 terms: main, narrower, problem.
3. Make {{3–5}} pins, each a DIFFERENT variant from: result, before/after, how-to steps, checklist/printable, list of
   ideas, comparison, template preview, short video. At least one shows the result, one teaches.
   For each pin give:
   - Variant
   - Image brief for 1000x1500 (2:3): headline on the image (3–7 words), what the picture shows, small detail
     line, where the name/domain sits (small)
   - Title: starts with a term, promise within the first 40 characters, max 100
   - Description: 1–2 sentences, 1–2 related terms said naturally, a plain call to action, max 500 characters
   - Board: the most specific one from my list
   - Link: {{URL}}?utm_source=pinterest&utm_medium=pin&utm_campaign={{page-slug}}&utm_content=<variant>
4. Output everything as a Markdown pin file with frontmatter: where, page, terms, stage, date, status: planned.
````

## Example output

> **Illustrative example.** Fictional product, page and terms.

Page: `example.com/mac-shortcuts-cheat-sheet` — a free printable of 40 Mac shortcuts; Clipnest ($9) is mentioned
at the end for clipboard history.

Promise: *every Mac shortcut you'll use daily, on one printable page.* Terms: `mac keyboard shortcuts` (main) ·
`mac shortcuts cheat sheet printable` (narrower) · `how to be faster on mac` (problem).

| # | Variant | Image headline | Title | Board |
|---|---|---|---|---|
| 1 | P04 checklist | "Mac shortcuts cheat sheet" | Mac shortcuts cheat sheet: 40 keys, free printable | Mac Keyboard Shortcuts |
| 2 | P03 how-to | "Be faster on Mac in 5 shortcuts" | How to be faster on Mac: 5 shortcuts to learn first | Mac Productivity Tips |
| 3 | P02 before → after | "Copy, copy, copy… and lose it" → "Every copy, kept" | Mac clipboard history: stop losing what you copied | Mac Productivity Tips |

Pin 1 description: *A one-page printable of the 40 Mac keyboard shortcuts you'll use every day, grouped by task.
Free to download and print.*
Link: `example.com/mac-shortcuts-cheat-sheet?utm_source=pinterest&utm_medium=pin&utm_campaign=mac-shortcuts-cheat-sheet&utm_content=p04`

## Common mistakes
- **Five pins, one image.** That's the same pin five times. Different variant, different picture.
- **Brand first in the title.** `Clipnest: …` wastes the 40 characters that show. Term first.
- **A promise the page doesn't keep.** "Free printable" that needs a $9 purchase loses the click and the trust.
- **Tiny text.** If the headline can't be read at thumbnail size, it isn't a headline.
- **No UTM.** Without `utm_content` you can't tell which variant brings signups.

## Related skills
- [social-pinterest](../social-pinterest/SKILL.md): the router for every Pinterest job.
- [aso-screenshot-strategy](../../../../skills/aso/aso-screenshot-strategy/SKILL.md): one image, one message.
- [social-credible-posting](../../../../skills/social/social-credible-posting/SKILL.md): the proof behind every claim.

## Credits
Written by [@nvminhtu](https://github.com/nvminhtu). Sources:
[Pinterest Help: product specs](https://help.pinterest.com/en/business/article/pinterest-product-specs),
[Pinterest Business: creative best practices](https://business.pinterest.com/creative-best-practices/),
[Pinterest Community Guidelines](https://policy.pinterest.com/en/community-guidelines) (checked 2026-10-13).
