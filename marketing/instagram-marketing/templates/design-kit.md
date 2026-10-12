# Design kit (fill once, reuse on every post)

Copy this file to your product repo as `marketing/instagram/design-kit.md` and fill it in. Every slide is built
from these values, so the grid looks like one brand. Sizes are explained in
[docs/04-image-flow.md](../docs/04-image-flow.md#step-5--build-on-the-design-kit-once-then-0-min).

````markdown
# Design kit · {{brand}}

## Canvas
- Carousel / single: 1080 × 1440 (3:4). Safe margin 80 px.
- Reel / Story: 1080 × 1920 (9:16). No text in top 250 px or bottom 350 px.
- Reel cover: 1080 × 1920, key content inside the middle 1080 × 1440.

## Colors (contrast ≥ 4.5 : 1 for text)
| Role | Hex | Use |
|---|---|---|
| Background | {{#FAF6EE}} | All slides |
| Text | {{#1F2A44}} | Titles, body |
| Accent | {{#C8643F}} | Numbers, step badges, the one word that matters |
| Product accents | {{product A #…}} · {{product B #…}} | Only on that product's posts |

## Type
- Title: {{font}}, Bold, 96–120 px, max 8 words, line-height 1.05
- Body: {{font}}, Regular, 44–52 px, max 25 words
- Small (footer, counter): 28–32 px

## Layouts
- **A · Hook / title:** title top third, screenshot or illustration below, counter `1/8` bottom-right.
- **B · Step:** big step number in accent (`3`), one line of body, screenshot in a device frame.
- **C · Number / quote:** one number or sentence centred on accent color, source + date small below.
- **D · End card:** ask (`Send this to…`), path (`Free for 2 folders → link in bio`), app icon, handle.

## Footer (every slide)
`@{{handle}}` bottom-left · `N/M` bottom-right · 28 px · text color at 60 % opacity.

## Image rules
- Real screenshots first, in a device frame; demo data only.
- AI images only for backgrounds / illustrations, style: {{one-sentence style lock}}.
- No other app's watermark, no logos you don't own.

## Files
`marketing/instagram/NN-<slug>/NN-<slug>-sMM.png` · Reel: `NN-<slug>.mp4` + `NN-<slug>-cover.png`
````

Tools that do the job (none required): Canva or Figma templates for layouts A–D; Keynote / PowerPoint at
1080 × 1440 exported as PNG; or HTML/CSS slides rendered to PNG if you prefer code. Screen recording: macOS
`⇧⌘5`, iOS Control Center screen recording, Android's built-in recorder.
