# Ready-made short-video pipelines to follow

Open-source repos that already turn a script into a finished short, one genre at a time. Study how they split the
work (one rule file per genre, reusable blocks, a publish log), then build the same thing for **your** formats from
[formats.md](formats.md) with the pipeline in [auto-render.md](auto-render.md).

Last checked: 2026-10-07. Check again every month: open the repo's commit list and add new genres or blocks below.

## video-mkt-agents (HyperFrames)

[TuNa-eTech/video-mkt-agents](https://github.com/TuNa-eTech/video-mkt-agents) · a copy to watch:
[nvminhtu/video-mkt-agents](https://github.com/nvminhtu/video-mkt-agents) · last upstream commit 2026-06-12.

An agent workflow that goes **Markdown script → TTS voice → word-by-word captions (Whisper) → HTML/CSS composition →
MP4**, rendered with [HyperFrames](https://github.com/hyperframes/hyperframes) (HTML + GSAP timelines instead of
React). Vertical 1080×1920 for TikTok / Reels / Shorts, horizontal 1920×1080 for YouTube.

### Genres (one rule file each)

Each genre has its own rule file in `.agents/rules/`: tone, length, voice, language, and a research step that must
happen before the script. One workflow (`.agents/workflows/create-video.md`) reads whichever rule you pick.
Several rule files are written in Vietnamese; the structure is the useful part.

| Rule file | Genre | Length | Research step before the script | Closest `format` here |
|---|---|---|---|---|
| `app-promo.md` | Introduce or review a mobile app | 30–60 s | Read the store page, download the real screenshots | `silent-demo`, `listicle` |
| `ai-tips.md` | AI tips for creators | 50–65 s | A surprising number for the hook + a real before/after | `how-to`, `hot-take` |
| `ai-news.md` · `ai-news-youtube.md` | AI news and analysis | 45–60 s | The news source and what changed | `genz-voice`, `photo-carousel` |
| `book-debates.md` | A debate taken from a popular book | 45–60 s | Pick the book and the line most likely to start comments | `hot-take` |
| `debt-payoff-x.md` | Personal finance education for one app | 30–60 s | The money problem the viewer has | `pain-hook`, `how-to` |
| `youtube-landscape.md` | Long-form 16:9 explainers | 2–10 min | Outline before recording | (long-form, not a short) |
| `_template.md` | Start a new genre | — | — | — |

### Blocks you can reuse

`templates/blocks/` holds whole scenes, `templates/components/` small effects. Copy the **idea** into your own
video tool, not the file (see the license note below).

| Block | Use it for |
|---|---|
| `hook-pop` | The first 2 seconds: one line that pops in |
| `fake-imessage` | A chat bubble conversation (label it as a re-enactment) |
| `vs-comparison-table` · `neobrutalism-ai-comparison` | You vs. the old way, or tool A vs. tool B |
| `line-chart-drop` · `number-counter` | A number that changes (only real, measured numbers) |
| `neobrutalism-breaking-news` · `neobrutalism-news-card` | News-style headline card |
| `vertical-roadmap` | Steps 1-2-3 of a how-to |
| `swipe-up` | The closing call to action |
| `text-marker` · `text-glitch` · `moving-grid` · `neobrutalism-window` | Emphasis, background and window frames |

### Helpers worth copying as an idea

- **`video-history`**: a small database of what was posted where, checked before each upload so the same video is
  not posted twice to one account.
- **`tiktok-cover`**: the cover image is an HTML page screenshotted at 1080×1920, so the cover matches the video's
  fonts and colors.
- **`stop-slop`**: a pass that removes predictable AI phrasing from scripts before they are voiced.
- **`website-to-hyperframes`** and **`remotion-to-hyperframes`**: start a video from a website, or port a Remotion
  composition.

### Before you use it

- **License.** The README says MIT, but the repo has no LICENSE file (checked 2026-10-07). Read and learn from it;
  ask the author before copying files into your own repo.
- **Uploads.** The repo includes a headless-browser TikTok uploader. Automated posting through a browser can break a
  platform's terms; post through the official app or an approved scheduler instead
  (see [auto-render.md](auto-render.md#what-stays-manual)).
- **Voice cloning.** Clone only your own voice. AI voice still needs the promotion disclosure from the
  [main skill](../SKILL.md#the-rules-you-must-follow).
- **Same rules as every other format.** Real screens only, real numbers only, licensed music and stock only.

## Add a repo to this list

Open a PR with one more `##` section in the same shape: link, last commit date, genres, reusable parts, license and
"before you use it" notes. Only repos you have opened yourself, with the date you checked.
