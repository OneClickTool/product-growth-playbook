# Larry × Snugly: an AI agent posting TikTok slideshows for two indie apps

**Who:** Oliver Henry ([@oliverhenry on X](https://x.com/oliverhenry)), indie iOS developer.
**Products:** Snugly (AI room redesign) and Liply (lip filler preview), both iOS.
**Channel:** TikTok photo-mode slideshows, made by an OpenClaw agent he named "Larry".
**When:** Early 2026 (posts on X from about February 2026). Seen and summarised 2026-10-12.

> All numbers are **self-reported** by Oliver Henry in his X posts and article, or repeated by write-ups that quote
> him. Nobody has published the TikTok or RevenueCat dashboards. Different write-ups give different MRR figures.

## What they did
1. Ran an AI agent (OpenClaw with Claude) on an old gaming PC (NVIDIA 2070 Super, Ubuntu), talking to it on WhatsApp.
2. Gave it a TikTok skill file of 500+ lines: sizes, locked prompt templates, text rules, caption and hook formulas,
   and a log of every failure.
3. The agent researched competitor accounts in a browser, wrote hooks, generated 6 images with gpt-image-1.5 (the
   model Snugly itself uses), drew text on them, and uploaded each slideshow to TikTok as a **private draft** via the
   Postiz API.
4. Oliver opened TikTok, added a trending sound, pasted the caption and published: ~60 seconds per post.
5. The agent read TikTok analytics (via Postiz) and RevenueCat, logged every post, and rewrote weak hooks and CTAs.
6. Later he published the skill free on ClawHub ([larry](https://clawhub.ai/OllieWazza/larry), MIT-0) and launched a
   hosted version, LarryLoop.

## Numbers (as reported)
| Metric | Value | Source |
|---|---|---|
| Views, first ~5 days | 500K+ | [gameplaydev Substack](https://gameplaydev.substack.com/p/how-his-openclaw-agent-larry-got) |
| Top post | 234K views | same |
| Posts over 100K | 4 | same |
| Paying subscribers (both apps) | 108 | same |
| MRR | ~$588 (article body), $714 (article intro), $670 (Oliver on X later) | same; [Luminary Lane](https://www.luminarylane.app/blog/from-larry-to-lane/) |
| Views in a later week | 1M+ on TikTok; "8M" in one headline (that figure mixes in his X article's views) | [Oliver on X](https://x.com/oliverhenry/status/2031798300425244829), Luminary Lane |
| API cost per post | ~$0.50 (~$0.25 with OpenAI Batch API) | gameplaydev Substack |
| Human time per post | ~60 seconds | same |
| Agent time per post | 15–30 min | same |

## Hooks: what worked and what flopped
| Hook | Views |
|---|---|
| "My landlord said I can't change anything so I showed her what AI thinks it could look like" | 234,000 |
| "I showed my mum what AI thinks our living room could be." | 167,000 |
| "My landlord wouldn't let me decorate until I showed her these." | 147,000 |
| "The difference between $500 and $5000 taste" | 2,671 |
| "Why does my flat look like a student loan" | 905 |
| "See your room in 12+ styles before you commit" | 879 |

Formula: **[another person] + [conflict or doubt] → showed them AI → they changed their mind.** Details in
[docs/03-hooks.md](../docs/03-hooks.md).

## What went wrong first (and the fix)
| Problem | Fix |
|---|---|
| Local Stable Diffusion and DALL·E 3 images looked obviously AI | gpt-image-1.5 + "iPhone photo, realistic lighting" in prompts |
| Landscape images → black bars, less engagement | Portrait 1024×1536 only |
| Room changed between slides (window moved, bed resized) | One locked room description pasted into all 6 prompts |
| Text too small, too high (under the status bar), squashed long lines | Bigger font scaled to word count, text at ~28% from top, 4–6 words per line |
| CTA slide without the app name ("She's redecorating now. Snugly.") — even the podcast host asked what the app was called | Name the app clearly on the CTA slide and in the caption |
| Self-focused / feature hooks | The person + doubt formula |
| He was still checking every post by hand early on | Kept the human publish step; logged failures into the skill file |

## What's worth copying
- **The decision table** (high views + low installs = fix CTA; low views + good installs = fix hook).
- **Measure to revenue**, not views: RevenueCat in the loop told the agent which content made money.
- **Drafts + a human publish step**: the sound, a last check and a real person behind every post.
- **A failure log inside the skill**, so mistakes aren't repeated.
- **Use your own product's output** as the images, so the slideshow shows exactly what users get.

## What to be careful about
- Self-reported numbers, inconsistent MRR figures, and the author now sells a product built on the story.
- A critique from a competing vendor ([Luminary Lane](https://www.luminarylane.app/blog/from-larry-to-lane/)) lists
  where DIY agents break: one channel only, context drift over weeks, auth/token failures, infrastructure to run.
  Their angle is commercial, but the points are real: keep the rules in files, not in chat history.
- The images are AI. Label them ([docs/07](../docs/07-rules-and-risks.md#ai-generated-images)) and turn on the
  promotional-content disclosure.
- The format fits apps with a visual result. A dev tool won't get 200K views from it.

## Run it on your product (checklist)
- [ ] Your product has a visual before/after or an emotional moment ([docs/01](../docs/01-what-a-slideshow-is.md))
- [ ] 10 hooks in the person + doubt shape ([templates/hook-bank.md](../templates/hook-bank.md))
- [ ] Locked scene description, 6 portrait images from your own app's output
- [ ] App name on slide 5 and in the caption; one tracked link in bio
- [ ] Drafts → sound → publish, AI + promotional labels on
- [ ] Post log filled after 48–72 h; Sunday review with [social-tiktok-slideshow-loop](../skills/social-tiktok-slideshow-loop/SKILL.md)

## Sources
- [How his OpenClaw agent, Larry, got millions of TikTok views in one week (gameplaydev Substack)](https://gameplaydev.substack.com/p/how-his-openclaw-agent-larry-got)
- [OpenClaw TikTok Marketing: How the Larry Skill Works (Stack Junkie)](https://www.stack-junkie.com/blog/how-to-automate-tiktok-marketing-with-openclaw-larry-skill-deep-dive)
- [Larry skill on ClawHub](https://clawhub.ai/OllieWazza/larry)
- [The Startup Ideas Podcast: I let OpenClaw run my organic marketing (while I sleep)](https://podcasts.apple.com/nz/podcast/i-let-openclaw-run-my-organic-marketing-while-i-sleep/id1593424985?i=1000754066019)
- [Oliver Henry on X: LarryLoop announcement](https://x.com/oliverhenry/status/2035116107153997980)
- [Luminary Lane: 8M TikTok views, then it broke](https://www.luminarylane.app/blog/from-larry-to-lane/) (vendor analysis)
