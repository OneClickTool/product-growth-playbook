# 04 · Slide design: sizes, safe zones, text, keeping the scene the same

## Size
| Option | When | Source |
|---|---|---|
| 1024×1536 portrait (2:3) | Generating with gpt-image; this is a native size | [Larry case](../case-studies/2026-02-oliver-henry-larry-snugly.md) |
| 1080×1920 (9:16) | Designing in Canva/Figma or rendering with a script | [Postiz guide](https://postiz.com/blog/automate-tiktok-slideshow) and other third-party guides |

Never landscape: in the Larry case, 1536×1024 images showed black bars and hurt engagement. All slides in one post
should be the same size. Use JPG or WebP; one third-party API doc says TikTok doesn't take PNG for photo posts through
its service, so convert if an upload fails.

## Safe zones (portrait)
TikTok draws its own UI on top of the image. From the Larry skill rules:

```text
┌──────────────────────┐
│  top 10%: keep clear  │  status bar, "Following | For You"
│                      │
│  ▼ text centred ~28% │  ← hook / slide text lives here
│    from the top      │
│                      │
│                      │  right edge: like/comment/share buttons
│                      │
│  bottom 20%: clear    │  caption, sound name, username
└──────────────────────┘
```

Early Larry posts put text too high (hidden by the status bar), too small, and on long lines that got squashed.

## Text
| Rule | Value |
|---|---|
| Font size | Scale with word count: ~7.5% of image width for short lines, ~6.5% medium, ~5% long (Larry skill) |
| Line length | 4–6 words, 3–4 lines per slide |
| Colour | White text with a dark outline or shadow, or white on a 50%-ish dark overlay |
| Font | One bold sans-serif. TikTok's own "Classic" text style is the native look |
| Text per slide | One idea. Two ideas = two slides |

Example render settings from the Postiz pipeline (1080×1920): 80 px side padding, line height 1.2, sizes 88 / 72 /
64 / 56 px, black overlay at 52% opacity, shadow 75% black, 12 px blur, 4 px Y offset.

## Keep the scene the same on every slide
The biggest giveaway of an AI slideshow is a room that changes between slides (window moves, bed resizes). Fix:

1. Write one **locked scene** paragraph: size, camera angle, window and door positions, furniture sizes, floor,
   ceiling, light direction.
2. Paste it **word for word** into all 6 prompts.
3. Change only the style line: wall colour, bedding, decor, lamps.
4. Add "iPhone photo, realistic lighting, natural imperfections, no text, no watermark, no logo".
5. Reject any image where the locked parts moved. Regenerate that one slide only.

Best of all: use the **real output of your own app** (the same model your app uses), so what viewers see is what they
get after installing. Oliver Henry used the same image model as Snugly for this reason.

## Images you may use
- Your app's own output, your own photos, or images from a model whose terms let you use them commercially.
- Stock with a commercial licence (Pexels, Pixabay, Unsplash). Pinterest images belong to someone else; "aesthetic
  background" packs scraped from Pinterest are not licensed for ads. Use them only if you have the rights.
- Never someone else's slideshow, even with the text changed.
- Realistic AI images of people or places need TikTok's AI-generated label: [07](07-rules-and-risks.md#ai-generated-images).
