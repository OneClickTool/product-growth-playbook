---
name: launch-pre-launch-checklist
description: Build a dated, owner-assigned pre-launch checklist for an app, SaaS, game, AI tool or browser extension, covering store and legal requirements, tracking, landing page, audience warm-up and launch-day assets. Use when a launch is 2-6 weeks away, when someone asks "what do I need before launching", "am I ready to launch", "launch checklist", or when a store submission keeps getting rejected for missing items.
license: MIT
metadata:
  category: launch
  difficulty: beginner
  time: 45-60 min
  version: 1.0.0
  author: nvminhtu
---

# Pre-launch Checklist

> In under an hour you will have a checklist with a date and an owner on every line, counting back from launch day.

## Goal
Make sure nothing that blocks or wastes launch day is left to the last 48 hours: store rejections, missing
analytics, an empty waitlist, or no post ready to publish.

## When to use
- Launch is 2–6 weeks away. Less than 2 weeks still works: cut to the *Blockers* column.
- You have launched before and something went wrong on the day.
- **Not for:** finding users after launch → [launch-get-first-100-users](../launch-get-first-100-users/SKILL.md).

## Inputs
- Product type and where it ships: App Store, Google Play, web, Chrome Web Store…
- Launch date, or the earliest realistic date.
- Who is on the team and how many hours a week each person has.
- Where your audience already hangs out: communities, newsletters, social accounts.

## Steps
1. **Fix the date and work backwards (5 min).** Write the launch date, then mark T-28, T-14, T-7, T-2, T-1, T-0.
   Anything that depends on someone else (store review, beta testers, a partner) goes early.
2. **Blockers first (15 min).** These stop the launch if they are missing. Check the ones that apply:
   - **Google Play, new personal developer account:** a closed test with at least **12 testers opted in for
     14 continuous days** before you can apply for production access. Start this at T-28 or earlier.
   - **App Store:** App Privacy details, a privacy policy URL, a support URL, screenshots for every
     required device size, and review notes with a demo login if the app needs sign-in. Leave 2–3 days of buffer
     for review, plus time for one rejection.
   - **Google Play:** Data safety form, privacy policy, content rating questionnaire, target audience.
   - **Chrome Web Store:** a single-purpose description, a justification for every permission, and a privacy policy
     if you handle user data.
   - **Web / SaaS:** terms, privacy policy, a working payment flow in live mode, and transactional email that
     doesn't land in spam.
3. **Measurement (10 min).** Before launch, decide the 3 numbers you will look at on day 1 and day 7
   (for example: visits, sign-ups/installs, activated users). Make sure the events fire, crash reporting is on, and every
   link you post carries a UTM tag (`?utm_source=reddit&utm_campaign=launch`). You can't measure a launch afterwards.
4. **Warm up an audience (10 min to plan, then weekly).** Pick one: a waitlist on the landing page, a TestFlight /
   closed-test group, or build-in-public posts. A launch to zero warm people is a launch to nobody.
   Aim to have **the first 50 people who will try it on day one** identified by name or email.
5. **Prepare launch-day assets (10 min to list).** Landing page, store listing, 3–5 screenshots or a short demo video,
   one launch post per channel ([launch-post-writing](../launch-post-writing/SKILL.md)), an FAQ with answers to the
   5 objections you expect, and a support inbox someone watches.
6. **Assign and date every line.** Every line gets an owner and a T-date. Anything without both won't get done.
   Save it as `LAUNCH.md` in the product's repo, next to the code, so you and your AI agent work from the same list.
7. **Dry run at T-2.** Install from the store build or production URL on a clean device or browser profile.
   Sign up, pay (test mode if possible), get the email, and click every launch link.

## Prompt (copy-paste)
Replace everything in `{{ }}`.

````text
You are a launch manager for small software teams. Build my pre-launch checklist.

Product: {{what it is, who it is for}}
Ships on: {{App Store / Google Play / web / Chrome Web Store / other}}
Developer account status: {{e.g. new personal Google Play account, existing Apple account}}
Launch date: {{date}}   Today: {{date}}
Team and weekly hours: {{names + hours}}
Audience today: {{followers, waitlist size, communities I'm in}}

Output a table with columns: Task | Why it matters | Owner | Due (T-minus days and real date) | Blocker? (Y/N)
Rules:
- Start with store and legal blockers for my platforms. Flag anything that needs lead time
  (store review, closed testing periods, external approvals) and schedule it first.
- Include tracking: 3 launch metrics, events to verify, UTM links per channel.
- Include audience warm-up so that 50 named people are ready to try it on launch day.
- Include a T-2 dry run from a clean device / browser profile.
- If the date is not realistic, say so and propose the earliest realistic date.
Only include tasks for my platforms. Keep it under 30 lines.
````

## Example output

> **Illustrative example.** Fictional product, dates made up to show the format.

*Tabsy*, a Chrome extension that groups tabs by project. Launch Tue 3 Nov, today 6 Oct (T-28).

| Task | Owner | Due | Blocker |
|---|---|---|---|
| Rewrite permission justifications (`tabs`, `storage`) and single-purpose text | Tu | T-21 (13 Oct) | Y |
| Privacy policy page on the landing site | Tu | T-21 (13 Oct) | Y |
| Submit to Chrome Web Store as unlisted, then fix review notes | Tu | T-14 (20 Oct) | Y |
| Events: install, first group created, day-7 active; UTM per channel | An | T-10 (24 Oct) | N |
| Waitlist form + 2 build-in-public posts per week | An | from T-28 | N |
| DM 50 people from the r/productivity and Discord lists | Tu | T-7 → T-1 | N |
| Show HN + Reddit posts drafted and reviewed | An | T-3 (31 Oct) | N |
| Dry run: install from the store on a new Chrome profile, click every link | Tu | T-2 (1 Nov) | Y |

## Common mistakes
- **Leaving store requirements to launch week.** Closed-testing periods and review rejections cost days you can't win back.
- **"We'll add analytics later."** The launch spike is the one moment you can't recreate.
- **A checklist with no owners.** Shared tasks belong to nobody.
- **Launching on a date you announced but can't hit.** Moving the date a week costs less than a broken launch.

## Related skills
- [launch-post-writing](../launch-post-writing/SKILL.md): write the posts for launch day.
- [launch-product-hunt-launch](../launch-product-hunt-launch/SKILL.md): if Product Hunt is one of the channels.
- [listing-app-store](../../listing/listing-app-store/SKILL.md) / [listing-google-play](../../listing/listing-google-play/SKILL.md): every store field, step by step.
- [aso-keyword-research](../../aso/aso-keyword-research/SKILL.md): get the store listing right before submitting.

## Credits
Written by [@nvminhtu](https://github.com/nvminhtu). Requirements from Google Play Console Help
("App testing requirements for new personal developer accounts"), App Store Connect Help ("Submit an app"),
and Chrome Web Store Program Policies. Re-check them before each launch, because they change.

**Tools (made by the maintainer at [OneClickTool](https://oneclicktool.app/?utm_source=github&utm_medium=skill&utm_campaign=growth-playbook&utm_content=launch-pre-launch-checklist)):** launching several products at once?
[ShotMatic](https://shotmatic.app/?utm_source=github&utm_medium=skill&utm_campaign=growth-playbook&utm_content=launch-pre-launch-checklist) (Mac) shows every repo's next steps, blockers and uncommitted changes on
one screen, and reopens the right Claude session. [Markdown Viewer](https://oneclicktool.app/macos/markdown-viewer?utm_source=github&utm_medium=skill&utm_campaign=growth-playbook&utm_content=launch-pre-launch-checklist) (free) reads
a folder of `LAUNCH.md` and plan files at a glance.
