# TikTok Slideshow Marketing for Indie Apps

> Part of [Marketing & Social](../README-marketing-social.md): every channel kit and how they link to each other.

**Post 6-image photo-mode slideshows about a human moment your product creates, send them to TikTok as drafts, add a
sound by hand, publish, and let the numbers decide which hook to repeat.** This is the "Larry loop" that took one
indie dev's apps from near zero to a few hundred dollars of MRR in a week (self-reported, see the
[case study](case-studies/2026-02-oliver-henry-larry-snugly.md)), written down so anyone can run it, with or without an
AI agent.

```text
research niche → write hook → 6 slides (same scene) → draft to TikTok → add sound + publish
      ↑                                                                          │
      └──── keep / retest / drop the hook  ←  views · saves · profile visits · installs · paid
```

## Why slideshows (and why people call it "wild")
- **Cheap per post.** Six images and six short lines. The reported API cost was about $0.50 per post
  ($0.25 with batch generation) and ~60 seconds of human time ([case study](case-studies/2026-02-oliver-henry-larry-snugly.md)).
- **Many shots on goal.** 1–3 posts a day is realistic, so you find a winning hook in days, not months.
- **No face, no filming.** The format is text over pictures. That fits apps where the result is visual
  (rooms, faces, outfits, food, before/after, a game moment) and founders who won't be on camera.
- **The hook is the whole game.** In the Larry data, hooks about *another person + doubt → shown the result → changed
  their mind* got 147K–234K views; hooks about the app or its features got under 3K.

What's **not** proven: claims like "slideshows get 5× the reach of video" come from vendor blogs without data.
See [reference/research-2026-10-12-tiktok-slideshow.md](reference/research-2026-10-12-tiktok-slideshow.md#not-verified-dont-quote-as-fact).

## Start in 3 steps
1. **Today (60 min):** read [docs/01](docs/01-what-a-slideshow-is.md) and [docs/02](docs/02-the-slideshow-loop.md),
   then run [`social-tiktok-slideshow`](skills/social-tiktok-slideshow/SKILL.md) to get 10 hooks and your first 3
   slideshows (slides, image prompts, caption).
2. **This week:** use the account like a normal viewer first ([docs/07](docs/07-rules-and-risks.md#new-accounts)),
   then post 1–3 slideshows a day by hand or from drafts. Log every post in [templates/post-log.csv](templates/post-log.csv).
3. **Every Sunday (20 min):** run [`social-tiktok-slideshow-loop`](skills/social-tiktok-slideshow-loop/SKILL.md) on
   the log. It tells you which hooks to scale, keep, retest or drop, and which slide to fix (hook or CTA).

## What's in this folder

| Folder | What's inside |
|---|---|
| [docs/](docs/) | The method, one topic per file (below) |
| [case-studies/](case-studies/README.md) | [Larry × Snugly](case-studies/2026-02-oliver-henry-larry-snugly.md) (the reference case) · [3 posts a day for a Quran app](case-studies/2026-04-postiz-quran-app-three-a-day.md) · [other founders using slideshows](case-studies/2026-other-founders-slideshow-notes.md) |
| [reference/](reference/) | [Research log with sources](reference/research-2026-10-12-tiktok-slideshow.md) · [skills, repos and tools](reference/tools-and-repos.md) · [TikTok photo-post API facts](reference/tiktok-photo-post-api.md) |
| [templates/](templates/) | [Hook bank](templates/hook-bank.md) · [one slideshow post](templates/slideshow-post.md) · [post log (CSV)](templates/post-log.csv) |
| [skills/](skills/README.md) | [**social-tiktok-slideshow**](skills/social-tiktok-slideshow/SKILL.md) (make the posts) · [**social-tiktok-slideshow-loop**](skills/social-tiktok-slideshow-loop/SKILL.md) (read the numbers, with a script) |

## Docs, in reading order
1. [What a TikTok slideshow is, and which products it fits](docs/01-what-a-slideshow-is.md)
2. [The slideshow loop, step by step](docs/02-the-slideshow-loop.md)
3. [Hooks: the formula, what worked, what flopped](docs/03-hooks.md)
4. [Slide design: sizes, safe zones, text, keeping the scene the same](docs/04-slide-design.md)
5. [Posting: drafts, sound, captions, cadence](docs/05-posting.md)
6. [Metrics and the decision table](docs/06-metrics-and-decisions.md)
7. [Rules and risks: AI labels, ad disclosure, many accounts, automation](docs/07-rules-and-risks.md)

## Five things to remember
- Write about a **person and a moment**, not your app. The app name goes on the CTA slide and in the caption.
- **Same scene on all 6 slides.** Lock the room / face / object description; change only the style.
- **Drafts, then a sound by hand.** The API can't pick trending audio; that last 60 seconds is yours.
- **Measure to money.** Views alone lie. High views + no installs = fix the CTA; few views + good installs = fix the hook.
- **Label AI images and disclose that you're promoting your own app.** It's TikTok's rule and it protects the account.

## Keep it current
- Monthly: re-check the [Content Posting API photo reference](https://developers.tiktok.com/doc/content-posting-api-reference-photo-post),
  [Community Guidelines](https://www.tiktok.com/community-guidelines) and [Branded Content Policy](https://www.tiktok.com/legal/page/global/bc-policy/en);
  update [reference/](reference/) with the date.
- New research goes in `reference/research-YYYY-MM-DD-<topic>.md`. New cases go in `case-studies/`.
