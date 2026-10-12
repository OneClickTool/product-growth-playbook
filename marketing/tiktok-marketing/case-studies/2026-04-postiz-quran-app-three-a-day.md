# Three 3-slide posts a day for a small Quran AI app

**Who:** a developer known as "ashen", as told by Postiz (the scheduler vendor).
**Product:** a vibe-coded iOS Quran AI app.
**Channel:** TikTok slideshows, 3 slides each, 3 posts a day, scheduled for a whole month (April 2026).
**Seen:** 2026-10-12 in [Postiz's write-up](https://postiz.com/blog/automate-tiktok-slideshow-marketing-ai-agents-postiz).

> Vendor story with small, self-reported numbers. Useful because it shows a **different shape** from the Larry case:
> fewer slides, emotional quotes instead of before/after, and a month batched in advance.

## What they did
- **Format:** 3 slides. Hook (introduce the idea, make them swipe) → expansion (a verse quote on an anime-style
  background, with an AI-written explanation) → resolution (emotional pull or CTA).
- **Volume:** 3 posts a day (09:00, 12:00, 17:00 EST), ~63 images a week, all of April scheduled ahead.
- **Tools:** an AI agent following a reusable skill file; Postiz API/MCP for scheduling; Gemini image model for
  backgrounds; a ~$50 Android phone controlled over Wi-Fi with ADB to pick audio and publish each draft five minutes
  after its slot.
- **Rules they kept:** warm up the account ~3 days first; drafts, not direct posts; max 5 hashtags; each caption unique
  and under 1,000 characters; review the first batch for formulaic wording; ~1 hour a month to restock the library.

## Numbers (as reported)
| Metric | Value |
|---|---|
| Downloads | 100+ |
| Likes | 1,000+ |
| Cost | Postiz API access quoted at $29/month (vendor price on their page) |

The post also shows another account's posts at 5.6M, 7.2M and 4.9M views. **That is not this app's result.**

## What's worth copying
- Quote / emotional slideshows are a second proven *shape* for apps whose value is a feeling, not a picture.
- 3 slides is enough when the payoff is one message.
- Batch a month, then spend your time on the numbers.

## What to be careful about
- Driving the TikTok app on a phone with ADB to publish is automation of the app itself; TikTok's rules ban
  automated account operation at scale ([docs/07](../docs/07-rules-and-risks.md)). Publishing by hand is the safe default.
- 100 downloads from three posts a day for a month is modest. The case shows the workflow, not a breakout.
- Religious content: be respectful and accurate; AI explanations of scripture should be checked by someone qualified.
