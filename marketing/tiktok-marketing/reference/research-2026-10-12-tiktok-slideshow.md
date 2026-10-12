# Research log · 2026-10-12 · TikTok slideshow marketing for indie apps

## Questions
1. What is the "TikTok slideshow" process people say drives installs, and where did it come from?
2. Which numbers are real (with a source) and which are hype?
3. What skills, repos and tools exist to run it, and which are worth using?
4. What do TikTok's API and policies allow?

## Sources read

| Source | Type | What we took |
|---|---|---|
| [TikTok Content Posting API: photo post reference](https://developers.tiktok.com/doc/content-posting-api-reference-photo-post) | Official docs | `media_type: PHOTO`, post modes, 35 images, title/description limits, rate limits, unaudited = private only, `is_aigc` → [tiktok-photo-post-api.md](tiktok-photo-post-api.md) |
| [Integrity and Authenticity](https://www.tiktok.com/safety/en/policies-and-engagement/integrity-authenticity), [Branded Content Policy](https://www.tiktok.com/legal/page/global/bc-policy/en), [Commercial Content Disclosure](https://ads.tiktok.com/help/article/about-the-content-disclosure-setting-for-creators) | Official policy | Multi-account, automation, fake engagement and disclosure rules → [docs/07](../docs/07-rules-and-risks.md) |
| [gameplaydev Substack: Larry step-by-step](https://gameplaydev.substack.com/p/how-his-openclaw-agent-larry-got) | Secondary, quotes the founder | Hooks with view counts, costs, failures, setup → [case study](../case-studies/2026-02-oliver-henry-larry-snugly.md) |
| [Stack Junkie: Larry skill deep dive](https://www.stack-junkie.com/blog/how-to-automate-tiktok-marketing-with-openclaw-larry-skill-deep-dive) | Third party | 6-slide skeleton, decision table, warm-up practice |
| [Larry on ClawHub](https://clawhub.ai/OllieWazza/larry) | Skill listing | Text rules, safe zones, hook thresholds, posting defaults, file layout |
| [Luminary Lane: from Larry to Lane](https://www.luminarylane.app/blog/from-larry-to-lane/) | Vendor analysis | Where DIY agents break (drift, auth, single channel) |
| [Postiz: automate TikTok slideshows](https://postiz.com/blog/automate-tiktok-slideshow), [Postiz: Quran app case](https://postiz.com/blog/automate-tiktok-slideshow-marketing-ai-agents-postiz) | Vendor | Hook-mining prompt, render specs, 3-slide case → [case study](../case-studies/2026-04-postiz-quran-app-three-a-day.md) |
| [MrrStory: Alex Nguyen](https://www.mrrstory.com/stories/from-0-to-370k-users-using-tiktok-app-store-seo), [Starter Story summary (Vix)](https://finance.biggo.com/podcast/fbb0f4aa8eac0d9b), [Yahoo Finance (Candle)](https://finance.yahoo.com/news/yc-founders-pivoted-5-times-170051223.html), [Building Afrika](https://buildingafrika.substack.com/p/3-types-of-content-that-convert-on) | Interviews | Other founders → [notes](../case-studies/2026-other-founders-slideshow-notes.md) |
| GitHub API (2026-10-12) for ~15 repos | Data | Stars, licence, last push → [tools-and-repos.md](tools-and-repos.md) |
| Vendor guides (makeviral, reelbase, socialrails, verticalflair, instacarousel) | Vendor | Only to cross-check slide counts and canvas sizes |

## Findings
1. **The process went viral in Feb–Mar 2026** through Oliver Henry's "Larry" (OpenClaw agent) story and Greg Isenberg's
   podcast. It's a loop: research → 6 slides with a locked scene → draft via API → human adds sound and publishes →
   analytics + revenue → rewrite hooks/CTA.
2. **The hook explains most of the variance.** Same pipeline: 147K–234K views for "person + doubt → showed them"
   hooks; under 3K for feature or self-focused hooks.
3. **Cost per post is tiny** (~$0.50 reported), which makes many tests cheap. That, not a secret algorithm boost,
   is the "wild" part.
4. **Measure to revenue.** Both the Larry loop and Vix tie content to purchases, not views.
5. **The API supports photo posts** but not sound choice, and unaudited apps can only post privately, so everyone
   ends with a human publish step.
6. **Repos:** the most-starred open slideshow generator is `athcagithub/SlideSmith` (335★, licence not declared);
   the original Larry skill is free on ClawHub (MIT-0); `jorge-dev/swipekit` (MIT) is the only one focused on
   *finding* formats that work in a niche.

## Not verified (don't quote as fact)
- "Slideshows get 5× more reach than video" and "TikTok has been pushing photo mode since early 2026": vendor blogs,
  no data.
- "TikTok detects Midjourney images in 0.5 s and downranks them"; "API posts from server IPs are penalised": Postiz
  blog, no data.
- "Warm up a new account 7–14 days": practice from the Larry skill, not a TikTok rule.
- Larry's MRR: $588, $670 and $714 appear in different places; 8M views in one week mixes X article views with TikTok.
- Best posting times; slide-1 swipe-through targets like "70%".

## Output of this research
Docs [01–07](../docs/), [case studies](../case-studies/README.md), [templates](../templates/), skills
[social-tiktok-slideshow](../skills/social-tiktok-slideshow/SKILL.md) and
[social-tiktok-slideshow-loop](../skills/social-tiktok-slideshow-loop/SKILL.md).
