# 01 · What a TikTok slideshow is, and which products it fits

## The format
A **photo-mode post** is a swipeable carousel of still images with text on them, plus a sound. It's a different post
type from a video made of photos: you either pick *Photo* in the TikTok app before choosing images, or post through
the Content Posting API with `media_type: PHOTO` ([official reference](https://developers.tiktok.com/doc/content-posting-api-reference-photo-post)).
A video that happens to contain photos is not swipeable.

| Fact | Value | Source |
|---|---|---|
| Max images per photo post (API) | 35 | [TikTok photo-post API](https://developers.tiktok.com/doc/content-posting-api-reference-photo-post) |
| Title / description length (API) | 90 / 4,000 UTF-16 runes | same |
| Images are sent as | Public URLs from a domain you verified (`PULL_FROM_URL`) | same |
| Slides used in the reference case | 6, portrait 1024×1536 | [case study](../case-studies/2026-02-oliver-henry-larry-snugly.md) |
| Canvas many tools export | 1080×1920 (9:16) | Third-party guides, see [04](04-slide-design.md) |

## Why it can spread fast
- Each post is cheap, so you can test many **hooks** (the line on slide 1) quickly. Finding the hook is most of the work.
- A viewer swipes on purpose. Each swipe is attention you earned, and a good last slide sends them to your profile.
- No camera, no voice, no editing timeline. A solo founder can ship 1–3 posts a day.

## Which products fit
It works when the product makes a **visible result** or a **moment between people**. Rule of thumb from the
[Stack Junkie teardown](https://www.stack-junkie.com/blog/how-to-automate-tiktok-marketing-with-openclaw-larry-skill-deep-dive):
there must be a before/after contrast to show.

| Fits well | Why | Slide 3–4 shows |
|---|---|---|
| AI room / outfit / hair / makeup / photo apps | Result is a picture | The same scene in new styles |
| Fitness, food, habit, study apps | Progress over time, lists of tips | Before → after, a plan, a checklist |
| Relationship, manifestation, faith, journaling apps | Emotional quotes on aesthetic backgrounds | The quote or message the app gives |
| Casual games | A funny or satisfying moment | Screenshots of the moment, a "level 1 vs level 50" |
| Utility apps, extensions | Only if the "before" pain is visual | The messy before, the clean after |

Weak fit: B2B dashboards, developer tools, anything whose value is invisible in a still image. Use
[social-credible-posting](../../../skills/social/social-credible-posting/SKILL.md) or
[social-short-video](../../../skills/social/social-short-video/SKILL.md) (screen-recording formats) instead.

## Slideshow vs. the short-video skill
| | Slideshow (this kit) | Short video ([social-short-video](../../../skills/social/social-short-video/SKILL.md)) |
|---|---|---|
| Unit of work | 6 images + 6 lines | 15–45 s clip |
| Volume | 1–3 a day | ~3 a week |
| Best for | Visual results, emotions, lists | Live demos, game play, screen recordings |
| AI does | Images, text, caption, analysis | Script, render from your recordings |

Run both if you like; they share the same hook rules.
