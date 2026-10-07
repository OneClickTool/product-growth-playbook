---
name: social-short-video
description: Get users from short vertical video (TikTok, Instagram Reels, YouTube Shorts) by making fewer videos that each have a better chance to spread. Picks one repeatable format for your product type (app, game, extension, SaaS, AI tool), writes hooks for the first 1-2 seconds, scripts 15-45 second videos you can film on a phone or as a screen recording, tests 3 formats against each other, then repeats only the winner and reposts it across platforms. Includes 17 formats (which ones an AI agent can render from a screen recording, stock clips and free music) and a script-to-video pipeline. Covers disclosure rules for promoting your own product and how to send viewers to an install or sign-up. Use when someone asks "how do I market my app on TikTok", "make a viral video for my app", "TikTok for indie developers", "Reels or Shorts for my product", "faceless app videos", "video viral trên TikTok", "làm ít mà viral nhiều", "AI làm video tự động", "auto render short video", or wants short-video growth without posting 3 times a day.
license: MIT
metadata:
  category: social
  difficulty: beginner
  time: "Setup 60 min · each video 30-60 min · 3-week test"
  version: 1.1.0
  author: nvminhtu
---

# Short Video: Fewer Videos, More Reach

> One video format that fits your product, 10 hooks, 3 scripts to test, and a rule for when to repeat a winner
> and when to drop a format.

## Goal
Short-video platforms show each new video to a small test audience first and show it to more people if they
watch and react. You don't need to post daily to win. You need a **format** that makes strangers watch to the end,
then the discipline to repeat it with small changes. This skill helps you find that format in 3 weeks with
about 9 videos, then spend your time only on the format that works.

## When to use
- Your product can be **shown** in seconds: a visible result, a before/after, a game moment, a satisfying action.
- You've posted a few videos with low views and don't know what to change.
- You want a channel that can produce a sudden spike (a momentum signal for
  [strategy-spend-and-timing](../../strategy/strategy-spend-and-timing/SKILL.md)).
- **Not for:** text posts on X, Threads or Facebook → [social-credible-posting](../social-credible-posting/SKILL.md).
  A one-off launch video for Product Hunt → [launch-product-hunt-launch](../../launch/launch-product-hunt-launch/SKILL.md).

## Inputs
- A phone, and a screen recorder for app/web demos (iOS and macOS have one built in; Android has one on most devices).
- The product's **"wow moment"**: the second where a user sees the result.
- A landing link that works on mobile, with a UTM tag, or a store link.
- 3 hours a week for 3 weeks.

## The rules you must follow
- **Say when a video promotes something.** TikTok's [Branded Content Policy](https://www.tiktok.com/legal/page/global/bc-policy/en)
  asks you to turn on the content disclosure setting for promotional content. Instagram and YouTube have similar
  paid-promotion labels ([YouTube paid product placements](https://support.google.com/youtube/answer/154235)).
  Promoting **your own** product is allowed; hiding it isn't. In the US, the FTC's
  [Disclosures 101](https://www.ftc.gov/business-guidance/resources/disclosures-101-social-media-influencers) applies to
  anyone paid or gifted to post about your product.
- **No fake engagement.** Bought views, follower trades and comment pods break each platform's rules (see the
  [TikTok Community Guidelines](https://www.tiktok.com/community-guidelines/en)) and the platform's ranking learns
  from fake viewers who don't care about your product.
- **Use sounds you have the rights to.** Business accounts usually get a smaller, commercially cleared music library.
  Free music (Pixabay Music, YouTube Audio Library) can go into the file; trending songs are added only inside the app.
- **Never re-upload someone else's video**, even a viral one that fits your topic perfectly. Use licensed stock clips
  (Pexels, Pixabay) for the "frustrated person" moment, Stitch / Duet inside the app, or recreate the trend with your own
  footage. Sources and licenses: [references/formats.md](references/formats.md#footage-and-music-you-may-use).

## Steps
1. **Pick your format family (10 min).** Choose the one that shows your wow moment fastest. The full list of 17
   formats, with which ones an AI agent can render for you, is in [references/formats.md](references/formats.md):

   | Product | Formats that usually fit | The first 2 seconds show… |
   |---|---|---|
   | Utility app / extension | Before → after · "Stop doing X manually" · speed run of a boring task | The annoying "before" or the finished "after" |
   | Indie game | Satisfying clip · fail/win moment · "I made this game, can you beat it?" | The most dramatic frame of gameplay |
   | SaaS / AI tool | Real input → real output · "I asked [tool] to…" · a problem-solved screen recording | The output on screen |
   | Template / design | Transformation (blank → finished) · "steal my setup" | The finished result |
   | Builder story | "Day N of building X" · "I made $X from a tiny app" (only with real numbers) | The number or the product, not your face saying hi |

2. **Write 10 hooks** for that format. A hook is the first line on screen *and* the first thing said. Make them
   specific and visual:
   - "This button saves me 20 minutes every morning."
   - "Your Mac can do this and nobody told you."
   - "I built a game where you lose if you blink."
   - "POV: you finally stopped [annoying thing]."
   Avoid "Hey guys, today I want to show you…": that's the classic first 2 seconds that make people scroll.
3. **Script 3 videos, one per format** (15–45 seconds each):
   `Hook (0–2 s) → problem shown (2–6 s) → product does it (6–20 s) → result + one-line CTA (last 3 s)`.
   Text on screen for every line (many people watch without sound). One idea per video.
4. **Film in batches, or render.** Record all 3 in one session: screen recording + a phone shot of a real hand or real
   screen if you can, since real-looking footage often reads as more native than polished ads. Edit in any free
   editor; captions on. For the **Auto** formats (silent demo, pain hook, before/after, satisfying, loop, challenge,
   race, carousel), let an agent write a render spec next to the script and build the file with a code-based video
   tool: [references/auto-render.md](references/auto-render.md). Tag each post `format:`, and for a test `test:` +
   `variant: A|B|C`, so results line up per format.
5. **Post and test (3 weeks, ~9 videos).** Week 1: one video per format. Weeks 2–3: two more of each, changing only
   the hook. Post the same video to TikTok, Reels and Shorts (remove other platforms' watermarks). Write the
   disclosure and one specific CTA in the caption: "Free on the App Store, link in bio".
6. **Read the numbers that matter.** For each video log: views, **average watch time / % watched to the end**,
   shares, profile visits, link clicks, installs (UTM or store campaign link). Views alone don't count; a
   video with fewer views but many link clicks is the better one.
7. **Keep the winner, kill the rest.** After 9 videos, keep the format with the best watch-through and clicks.
   From now on, make **only that format**, 2–3 per week, with a new hook or new example each time. If a video
   suddenly gets 5–10× your usual views, make 3 close variations within 72 hours while the audience is warm.
8. **Turn viewers into owned users.** Link to a page that captures something lasting (install, account, email),
   not just your homepage. → [strategy-product-as-funnel](../../strategy/strategy-product-as-funnel/SKILL.md).

## Prompt (copy-paste)
Works in Claude, ChatGPT, Gemini, Cursor. Replace everything in `{{ }}`.

````text
You are a short-video strategist for indie apps and games. You value watch-through and installs over views.
No fake engagement, no misleading claims, and always remind me to disclose promotional content.

Product: {{what it is, platform, price}}
Who it's for: {{...}}
The wow moment (what the user sees when it works): {{...}}
What I can film: {{screen recording / phone footage / my face / gameplay}}
Videos I've posted and their results: {{views, watch time, clicks, or "none yet"}}

1. Pick the 3 best formats for this product from: silent demo, pain hook (licensed stock clip of the problem),
   before/after, satisfying, loop, challenge, race, photo carousel, how-to, hot take, Gen Z voice-over, POV,
   trend remix, listicle, dev story, green screen, reply to a comment. Prefer formats I can render without filming
   if I say so. Say why each fits.
2. Write 10 hooks (on-screen text + spoken line), each under 12 words, specific and visual.
3. Write one 15–45 second script per format, with a timeline:
   hook (0–2s) → problem (2–6s) → product (6–20s) → result + CTA. Include on-screen text for every line.
4. Give me a 3-week posting plan (~9 videos) and a log table with: views, % watched to end, shares, profile
   visits, link clicks, installs.
5. Write the rule for keeping one format and dropping the others.
6. For each script, list the footage: my screen-recording scenes, licensed stock clips (Pexels / Pixabay) and free
   music. Never suggest re-uploading other creators' videos or baking a copyrighted song into the file.
````

## Example output

> **Illustrative example.** Numbers are made up to show the format.

*Menu-bar app that cleans messy copied text on macOS.*

| Format | Video | Views | % watched to end | Link clicks | Installs |
|---|---|---|---|---|---|
| Before → after | "Pasting from PDFs is broken. Watch." | 2,400 | 41% | 38 | 12 |
| Stop doing X | "Stop retyping text from screenshots" | 9,800 | 22% | 15 | 3 |
| Speed run | "Cleaning 10 messy pastes in 8 seconds" | 1,100 | 55% | 21 | 9 |

**Verdict:** keep *before → after* (best clicks and installs per view). The *stop doing X* video got the most views but
few installs: the wrong viewers. Next 2 weeks: 6 before → after videos with different source apps (PDF, Slack, email).

## Common mistakes
- **Judging by views.** Views without watch-through or clicks are an audience that won't install.
- **A slow start.** Logos, intros and greetings in the first 2 seconds cost you most of the viewers.
- **Changing everything every video.** Change one thing (the hook) so you learn what works.
- **Posting daily, burning out in 2 weeks.** 2–3 good videos a week for months beats 30 rushed ones.
- **Hiding that it's your product.** Disclose it; "I made this" is also a stronger hook than pretending to be a fan.
- **Sending viewers to a desktop-only page.** They're on a phone. Link to the store or a mobile page.
- **Borrowing a viral clip.** Re-uploading someone else's video gets the post taken down and the account struck. Use a
  licensed stock clip of the same feeling, or Stitch / Duet in the app.
- **Automating the wrong formats.** Auto-render is great for demos and before/after; story and reply formats still
  need a real person.

## Related skills
- [social-build-in-public](../social-build-in-public/SKILL.md): the "day N of building" format as a weekly habit.
- [strategy-spend-and-timing](../../strategy/strategy-spend-and-timing/SKILL.md): what to do when one video takes off.
- [aso-screenshot-strategy](../../aso/aso-screenshot-strategy/SKILL.md): the same wow moment, for your store page.
- [launch-quick-download-wins](../../launch/launch-quick-download-wins/SKILL.md): other low-effort channels.

## Credits
Written by [@nvminhtu](https://github.com/nvminhtu). Rules: [TikTok Branded Content Policy](https://www.tiktok.com/legal/page/global/bc-policy/en),
[TikTok Community Guidelines](https://www.tiktok.com/community-guidelines/en), [FTC Disclosures 101](https://www.ftc.gov/business-guidance/resources/disclosures-101-social-media-influencers)
(checked 2026-10-02). Platforms don't publish their ranking formulas, so this skill relies on what you can measure.
