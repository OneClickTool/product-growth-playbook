# Skills, repos and tools for TikTok slideshows

Checked 2026-10-12 with the GitHub API and the listing pages. Stars and dates change; licences matter if you fork.
None of these are made by the maintainer of this repo. **Read a skill's `SKILL.md` and scripts before installing it**:
several want API keys and post to your account.

## Agent skills (install into Claude Code / OpenClaw / Codex)

| Skill | Where | Licence | What it does | Use it when |
|---|---|---|---|---|
| **larry** (Oliver Henry) | [ClawHub](https://clawhub.ai/OllieWazza/larry) | MIT-0 | The original: competitor research, gpt-image slides, node-canvas text, Postiz drafts, analytics + RevenueCat loop, daily report. Scripts: `generate-slides.js`, `post-to-tiktok.js`, `check-analytics.js`, `daily-report.js` | You want the full agent loop and have Node 18+, an OpenAI key and Postiz |
| **openquok-tiktok-slideshow** | [Ratimon/openquok-monorepo](https://github.com/Ratimon/openquok-monorepo) (`agent/`), also on [ClawHub](https://clawhub.ai/ratimon/openquok-tiktok-slideshow) | AGPL-3.0 (repo) | Larry-style pipeline wired to OpenQuok, an open-source scheduler you can self-host | You'd rather self-host the scheduler |
| **tiktok-slideshow-creator** | [mathiasbarea/tiktok-slideshow-creator](https://github.com/mathiasbarea/tiktok-slideshow-creator) | not declared | 6-slide packages from an account profile + campaign brief: prompts, overlay text, caption, ready-to-publish folder. No posting | You only want the content files, organised per account/campaign |
| **slideshow-kit** | [TheMattBerman/slideshow-kit](https://github.com/TheMattBerman/slideshow-kit) | MIT | Brand-DNA-driven carousel generation; routes into concept and styled-carousel workflows | Branded carousels for TikTok and Instagram |
| **vyral-tiktok-slideshow-skill** | [Meliwat/vyral-tiktok-slideshow-skill](https://github.com/Meliwat/vyral-tiktok-slideshow-skill) | — | Planning board for slideshow scripts | Planning only |
| Larry forks | e.g. [plunderandriffle/larry-tiktok-engine](https://github.com/plunderandriffle/larry-tiktok-engine), [satoshistackalotto/skills](https://github.com/satoshistackalotto/skills) (archive of ClawHub skills incl. `tiktok-app-marketing`) | varies | Copies / variants of Larry | Prefer the original listing |

## Apps and repos (run locally)

| Repo | ★ | Licence | What it does |
|---|---|---|---|
| [athcagithub/SlideSmith](https://github.com/athcagithub/SlideSmith) | 335 | not declared | Local dashboard: an AI (via OpenRouter) writes on-brand slideshows → review queue → slides rendered in the browser → post-bridge schedules and posts → analytics. No image-gen cost (text over gradients / library images) |
| [jorge-dev/swipekit](https://github.com/jorge-dev/swipekit) | 4 | MIT | Local MCP server + CLI: uses your own Chrome to measure accounts in a niche (views, slideshow %, slides per post, posts/week, spikes) and read winning posts slide by slide. Research only, no posting |
| [gitroomhq/postiz-app](https://github.com/gitroomhq/postiz-app) | 37K | AGPL-3.0 | Open-source scheduler with an agent CLI/MCP; the posting layer Larry used. Cloud or self-host |
| [Ratimon/openquok-monorepo](https://github.com/Ratimon/openquok-monorepo) | 82 | AGPL-3.0 | Open-source scheduler with CLI, MCP and API |
| [tylerprogramming/social-studio](https://github.com/tylerprogramming/social-studio) | 2 | — | Carousels, slideshows and Reels, local, bring your own keys |

## Posting layer (paid services)
Postiz (cloud), post-bridge, Publer, Upload-Post, Zernio, bundle.social. Before paying, check: TikTok **photo** posts
(not only video), draft / inbox mode, and analytics access. Some only post video to TikTok
([Make community thread](https://community.make.com/t/post-to-tiktok-using-zernio-only-allow-videos-not-tiktok-photo-carousels/112267)).

## Hosted slideshow generators
SlideReels, SlideStorm, ReelFarm-style tools: faster to start, no feedback loop to your revenue. Fine for a first
month; switch to your own loop once you know your winning hook formula.

## Image models mentioned in the cases
gpt-image-1.5 (Larry: chosen because Snugly uses it, so slides match the app), Gemini image model (Quran app case).
Check each model's commercial-use terms.

## Picking one
- **Just want posts this week, no code:** the [social-tiktok-slideshow](../skills/social-tiktok-slideshow/SKILL.md)
  prompt + Canva/TikTok's editor.
- **Want an agent to make the slides:** larry (ClawHub) or tiktok-slideshow-creator, posting by hand.
- **Want a dashboard:** SlideSmith.
- **Don't know what format works in your niche:** swipekit first.
