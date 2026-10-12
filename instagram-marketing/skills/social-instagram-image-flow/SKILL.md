---
name: social-instagram-image-flow
description: Build one Instagram post (carousel, Reel, single image or Story) from one true product fact with a 10-step image flow made to raise impressions from non-followers and send visits to your website. Picks the format that fits the fact, writes 5 hooks for the first slide, scripts every slide (one idea, 25 words max, the image proves the text), applies a fixed design kit (1080x1440 carousels, 1080x1920 Reels and Stories, safe zones), puts real screenshots before AI images, then writes the search-friendly caption, up to 5 hashtags, alt text and the link path (bio link, Story link sticker, keyword to DM) with UTM tags. Use when someone asks "make an Instagram carousel for my app", "Instagram image post that drives website traffic", "more impressions on Instagram", "how to get website visits from Instagram", "làm hình Instagram", "carousel Instagram cho app", "tăng impression Instagram", "kéo traffic từ Instagram về web", or has a product fact and needs a finished post.
license: MIT
metadata:
  category: social
  difficulty: beginner
  time: "Design kit 60 min once · 45-90 min per post"
  version: 1.0.0
  author: nvminhtu
---

# Instagram Image Flow: One Fact → One Post That Brings Visits

> A finished Instagram post (slides or Reel shot list, caption, alt text, Story sequence and UTM links) built from
> one real fact in 10 checkable steps.

## Goal
Instagram shows a new post to some followers and a test group of strangers, and widens it when people swipe to the
end, save it and **send** it to friends (Instagram's own ranking explainer; Mosseri named watch time, likes and sends
as the top signals in Jan 2025). Most dev posts fail at the first slide or have no path to the website, because
caption links can't be tapped. This skill makes every post pass both tests: a hook that stops the scroll, and one
planned tap from the post to your landing page.

## When to use
- You have a product with something visible (a screen, a before/after, a result card) and one fact to show.
- Your Instagram posts get some reach but no profile visits or website visits.
- You want an agent to produce the slide texts, image list, caption and links for a designer (or you) to build.
- **Not for:** planning the whole week or month → [social-instagram-growth](../social-instagram-growth/SKILL.md).
  Finding a video format across TikTok / Reels / Shorts → [social-short-video](../../../skills/social/social-short-video/SKILL.md).

## Inputs
- One fact from your fact bank (true, dated, with a visible result) and the product slug.
- The product's landing URL, offer (free tier / trial / price, as the store says today) and audience in their words.
- Your design kit ([templates/design-kit.md](../../templates/design-kit.md)) or permission to use the defaults.
- Real screenshots or a screen recording made with demo data.

## Steps
1. **Fact.** One sentence with a noun you can photograph. Numbers must be real and dated; otherwise `<NUMBER?>`.
2. **Format.** Process / checklist → carousel 6–10 slides; before/after → carousel 3–5 or Reel 7–15 s; motion →
   Reel 7–30 s; a single striking result → one 3:4 image; a link for today → 3-frame Story. A new Reel format goes
   out as a Trial Reel first. Never a mostly-text Reel (shown less, Official).
3. **Hook.** Write 5 hooks (pain in their words · number + result · before/after label · "settings you never
   changed" · yes-question · honest limit), pick one: ≤ 8 words, one image of the problem.
4. **Script.** Fill [templates/carousel-brief.md](../../templates/carousel-brief.md): slide 1 hook, 2 why it matters,
   3–6 one step each, 7 result/proof, 8 ask + path. ≤ 25 words a slide, the image proves the words, only slide 8
   asks.
5. **Design kit.** 1080 × 1440 for carousels/singles, 1080 × 1920 for Reels/Stories; 80 px margin; Reels/Stories keep
   text out of the top 250 px and bottom 350 px (Practice); 2 type sizes; layouts A (hook), B (step), C (number),
   D (end card).
6. **Visuals.** Real screenshots in device frames first, then your own diagrams; AI images only for backgrounds or
   illustrations, never fake UI or fake results. No other app's watermark. No personal data.
7. **Export + check.** Same size for every slide, checked on a phone; Reel 1080 × 1920 with sound and a cover whose
   middle 3:4 works on the grid; files named `NN-<slug>-sMM.png`.
8. **Caption.** Line 1 ≤ 125 characters with the words buyers search; steps one per line; the ask (send / save);
   the path ("→ link in bio"); 3–5 specific hashtags (cap is 5, Reported Dec 2025). Alt text on every slide.
9. **Link path.** Bio link 1 = this product with `utm_source=instagram&utm_medium=bio&utm_campaign=<slug>&utm_content=<post-id>`;
   a 3-frame Story with the link sticker 1–3 h later ([templates/story-sequence.md](../../templates/story-sequence.md)),
   saved to a Highlight; keyword → DM only if the DM delivers exactly what was promised.
10. **Publish + measure.** Answer every comment in the first hour; Story at +1–3 h; Trial Reel decision at +24 h; at
   +48 h log reach, non-follower %, sends and saves per 1k reach, profile visits, link taps and landing visits by
   `utm_content` ([templates/weekly-numbers.md](../../templates/weekly-numbers.md)).

Full version with examples and the one-card checklist: [docs/04-image-flow.md](../../docs/04-image-flow.md).

## Prompt (copy-paste)
Works in Claude, ChatGPT, Gemini, Cursor. Replace everything in `{{ }}`.

````text
You are my Instagram post editor. I'm an indie developer. Build ONE Instagram post from ONE fact, following the
10-step image flow below. Plain words, specific, no hype. Never invent features, numbers, users, reviews or
results that are not in my facts; write <NUMBER?> where one is missing and list it at the end.

Product: {{name}} · {{one-line pitch}} · offer today: {{free tier / trial / price}}
Landing URL: {{url}}   Product slug: {{slug}}   Post id: {{NN-slug}}
Audience, in their words: {{e.g. "my Mac is always full"}}
The fact (dated): {{fact}}
Other facts I allow you to use: {{3-10 facts}}
Screenshots / clips I have: {{list}}
Design kit: {{paste mine, or "use defaults: 1080x1440, bg #FAF6EE, text #1F2A44, accent #C8643F"}}

Do these steps and show the output of each:
1 FACT: restate it in one sentence with a noun that can be photographed.
2 FORMAT: choose carousel / Reel / single / Story and say why in one line (process→carousel, before/after→carousel
  or short Reel, motion→Reel, one result→single). If Reel and the format is new for me, say "post as Trial Reel".
  Never propose a Reel that is mostly text.
3 HOOK: 5 hooks (pain, number+result, before/after, settings-you-never-changed, yes-question), each ≤ 8 words, and
  the image for each. Star the best and say why.
4 SCRIPT: a table: slide # · layout (A hook / B step / C number / D end card) · text ≤ 25 words · exact image to
  show (which screenshot, cropped to what) · alt text. Slide 1 hook, 2 why it matters, middle one point each,
  second-last proof, last = ask (send or save) + path ("→ link in bio"). Product name at most once before the
  last two slides. For a Reel give a second-by-second shot list instead (result in second 0-1, end card last 2 s).
5-7 PRODUCTION NOTES: for each slide, what to capture, how to frame it, and anything to blur. If an illustration
  is needed, write one image prompt: no text, no UI, no logos, my palette, empty space where the title goes,
  portrait 3:4. Never an AI image that imitates my app's screen.
8 CAPTION: line 1 ≤ 125 characters with the search words a buyer types; then the steps one per line; the ask; the
  path; 3-5 specific hashtags (no #explore #reels #fyp). No URL in the caption.
9 LINKS: the bio URL and the Story URL with utm_source=instagram, utm_medium=bio|story, utm_campaign={{slug}},
  utm_content={{NN-slug}}; and the 3-frame Story (tease / proof + poll / path + link-sticker text).
10 CHECKLIST: every number and claim I must verify, every screenshot that needs demo data, and what to log at +48 h.
Finally, output the post file in this frontmatter: where, stage, date, link, status, kind, format, slides, trial,
day, product, aim.
````

## Example output

> **Illustrative example.** Fictional product ("Tidybox", a Mac cleaner) with made-up facts; not a real post.

**2 FORMAT:** carousel, 8 slides: a process with a before/after, and people save and send clean-up lists.

**3 HOOK (starred):** `Your Downloads has 3 copies of every PDF.` + a screenshot of `report (1).pdf, report (2).pdf…`

**4 SCRIPT (excerpt):**

| # | Layout | Text | Image |
|---|---|---|---|
| 1 | A | Your Downloads has 3 copies of every PDF. | Finder list with `(1)`, `(2)` copies |
| 3 | B | **1** One scan finds exact duplicates, even across folders. | Tidybox result list |
| 5 | B | **3** Big and old files are flagged, never pre-selected. | Flagged rows, unticked |
| 6 | B | **4** Everything goes to Trash. Undo for 7 days. | Undo button |
| 8 | D | Send this to someone whose Mac is full. Free for 2 folders → link in bio. | App icon + handle |

**8 CAPTION line 1:** `How to find duplicate files on a Mac and clean Downloads in one scan` · hashtags
`#macapps #macos #macbook #productivitytips`

**9 LINKS:** `https://tidybox.example/?utm_source=instagram&utm_medium=bio&utm_campaign=tidybox&utm_content=01-tidybox-downloads`

## Common mistakes
- **Logo on slide 1.** Nobody stops for a logo. Show the problem.
- **A wall of text as a Reel.** "Mostly text" Reels are shown less; put text ideas in a carousel.
- **URL in the caption.** It isn't tappable. Say "link in bio" and update bio link 1.
- **Reposting your TikTok with its watermark.** Watermarked Reels get less reach to non-followers. Export the original.
- **AI screenshots of your own app.** That's a fake result. Use real screenshots with demo data.
- **30 hashtags.** The cap is 5 and hashtags matter less than a caption with search words.
- **No Story after the post.** The Story link sticker is where most taps to the website come from (Practice); skip it
  and the post's readers have no one-tap path.

## Related skills
- [social-instagram-growth](../social-instagram-growth/SKILL.md): the weekly plan, profile and numbers around these posts.
- [social-instagram](../social-instagram/SKILL.md): one command for the whole Instagram kit.
- [social-short-video](../../../skills/social/social-short-video/SKILL.md): find the Reel format that works.
- [social-credible-posting](../../../skills/social/social-credible-posting/SKILL.md): the proof rules every slide follows.
- [aso-screenshot-strategy](../../../skills/aso/aso-screenshot-strategy/SKILL.md): the same "one benefit per frame" rule for store screenshots.

## Credits
Written by [@nvminhtu](https://github.com/nvminhtu). Sources: [Instagram Ranking Explained](https://about.instagram.com/blog/announcements/instagram-ranking-explained),
[link sticker for everyone](https://about.instagram.com/blog/announcements/expanding-sharing-links-in-stories-to-everyone),
[alt text help](https://help.instagram.com/503708446705527), and the press reports listed in
[reference/instagram-facts.md](../../reference/instagram-facts.md) (all checked 2026-10-12).
