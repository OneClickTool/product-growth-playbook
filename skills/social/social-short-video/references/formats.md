# Short-video format catalog

17 formats to test against each other. Each one has an id you can put in the post file (`format: <id>`) so results
can be compared per format. **Automation** says how much an AI agent plus a video tool can do without you filming:

- **Auto**: the agent writes the script and a render spec; a code-based video tool (for example Remotion) builds the
  file from your real screen recording, licensed stock clips and free music. You only review and post.
- **Half**: the file can be built automatically, but one piece only exists inside the app (a trending sound, a Stitch).
- **Manual**: needs your face, your voice, or an in-app feature.

| # | `format` | What it looks like | Audio | Automation | Fits |
|---|---|---|---|---|---|
| 1 | `silent-demo` | Real screen recording, zoom + big caption per step, no voice | free music | Auto | any app, extension, SaaS |
| 2 | `pain-hook` | 2–3 s of licensed stock footage of someone frustrated at a computer, then the product fixes it | free music | Auto | utilities, productivity |
| 3 | `before-after` | The mess → one tap → clean, hard cut or split screen | free music | Auto | utilities, templates |
| 4 | `satisfying` | Smooth motion (files flying into folders, a counter going down), loops cleanly | soft music / app sounds | Auto | cleaners, organizers, games |
| 5 | `loop-text` | 5–9 s, one line + one shot, end frame = start frame so it replays | free music | Auto | anything with one clear result |
| 6 | `challenge` | "Clean my Mac in 30 seconds", countdown on screen, real result at the end | free music | Auto | speed / effort savers |
| 7 | `race` | Split screen with timers: doing it by hand vs the product, times measured for real | free music | Auto (needs a real recording of the manual way) | utilities |
| 8 | `photo-carousel` | 5–8 text slides on stock or app stills; TikTok photo mode or a slideshow video | free or trending | Auto | tips, lists, myths |
| 9 | `how-to` | "How to <do X> on <platform> in 3 steps", the exact search phrase as the first caption | AI or real voice | Auto (AI voice) | anything people search for |
| 10 | `hot-take` | "Stop <common bad habit>", then the better way | AI or real voice | Auto (AI voice) | tools that replace a manual habit |
| 11 | `genz-voice` | Cuts every 1–2 s, word-by-word captions, a spoken hook in under 3 s | voice + music | Auto (AI voice) | consumer apps, games |
| 12 | `pov` | "POV: you …" text over a relatable screen moment | trending sound | Half (sound added in the app) | consumer apps, games |
| 13 | `trend-remix` | This week's trend format recreated with your own footage, or a Stitch / Duet | trending sound | Half / Manual | anything, when a trend fits |
| 14 | `listicle` | "3 <platform> apps I use every day", yours plus real ones, said honestly | voice | Half (filming other apps) | utilities |
| 15 | `dev-story` | "I built this because …", one real decision, real numbers or none | voice / face | Manual | indie makers |
| 16 | `green-screen` | You talking over a screenshot: your store page, a Reddit thread, a review | voice / face | Manual | any |
| 17 | `reply-comment` | Video reply to a real comment, showing the answer in the product | voice | Manual (in-app feature) | once you have comments |

## Footage and music you may use

| Source | OK? | Note |
|---|---|---|
| Your own screen recordings and phone footage | yes | the core of every format |
| Stock clips from Pexels / Pixabay | yes | both licenses allow commercial use without credit; don't resell the raw file. Keep a `SOURCES.md` with link + download date |
| Free music from Pixabay Music or the YouTube Audio Library | yes | check each track's license; some tracks are registered with Content ID, keep the link as proof |
| Trending sounds and songs on TikTok / Instagram | only inside the app | promotional posts usually have to use the Commercial Music Library; never bake a copyrighted song into the file |
| Other creators' viral videos | **no** | downloading and re-uploading someone else's video breaks copyright and the platforms' originality rules, even if it fits your topic. Use Stitch / Duet (the creator allowed it and gets credit) or recreate the format with your own footage |
| AI avatars / AI voices | yes, labeled | TikTok asks you to label realistic AI-generated content; a real face usually builds more trust for story formats |

## A/B naming

Put `test: <topic>-<date>` and `variant: A | B | C` in each post of one test. Same topic and call to action, only the
format (or only the hook) changes. Post on different days at the same hour; after 24 h log views, average watch time,
% of viewers still watching at 3 s, link clicks and installs.
