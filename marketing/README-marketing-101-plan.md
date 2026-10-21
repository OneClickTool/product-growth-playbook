# Plan: a "101" tips page for every channel kit

> **Status: in progress.** The X page exists ([x-marketing/docs/00-101-tips.md](x-marketing/docs/00-101-tips.md),
> 100 tips); the other kits are planned. Back to the
> [marketing hub](README-marketing-social.md).

## Why

The kits teach a method (strategy → profile → posting → numbers). That's the long read. What people also want, and
what they share, is the short stuff: **one-line, do-this-today tips** from someone who has used the channel.
"Don't change your profile photo on X, you lose the Premium checkmark until it's reviewed again." You read it in
5 seconds and it saves you a week.

A **101** page is that layer: the channel's daily tips, each one line, each labelled by how sure we are.

## What a 101 tip is

One tip = one bullet with four parts:

```text
- **<Label>** · <Do / Don't, one line> — <why, one line>. <source link or link to the kit doc that explains it>
```

| Part | Rule |
|---|---|
| Label | Same scale as the X seed: **Help** (official help/policy page) · **Code** (open-source ranker) · **Statement** (said by staff/owner) · **Real** (seen on the maintainer's account, small base) · **Practice** (common among builders, unproven: "test it") |
| Do / Don't | An action someone can take today, not a principle. Starts with a verb. |
| Why | The mechanism or the risk, one line. No numbers unless sourced. |
| Source | **Help / Code / Statement need a link.** Policies, limits and prices must cite the official page (repo rule). Practice tips link to the kit doc that explains them, or say "unverified". |

Two example tips, written to the format:

- **Help** · Don't change your profile photo, display name or @handle while on Premium — the blue checkmark goes
  away until X reviews the account again ([About X Premium](https://help.x.com/en/using-x/x-premium)).
- **Practice** · Reply under promoted posts (X ads) in your niche with a useful, on-topic answer — an ad is paid
  to reach many people, so a good reply under it can be seen by them too. Unverified: no X source; test it for two
  weeks and compare impressions on those replies with your normal ones. Never spam ads: blocks and reports hurt
  the account.

## Where it lives

One file per kit, first in `docs/` so beginners open it first:

```text
marketing/<channel>-marketing/docs/00-101-tips.md
```

Inside, the same sections for every channel (skip one if it has no tips yet):

1. Profile & account (bio, photo, name changes, verification, link in bio)
2. Posting (format, length, timing, frequency)
3. Reach (what the feed/ranker rewards, small hacks like the ad-reply one)
4. Replies, comments & DMs
5. Links & selling
6. Paid features (Premium, Boost, ads) — only what the official page says, plus labelled Practice tips
7. Rules & bans (what gets you limited, removed or banned)
8. Stop believing (myths with no evidence)

Start at **30 tips per kit**, grow toward 101 as the maintainer and contributors find more. Each tip that the kit
already explains links to that doc instead of repeating it.

## Rollout

| Order | Page | Seed | Notes |
|---|---|---|---|
| 1 · **urgent** | **Short video 101** (TikTok · YouTube Shorts · Instagram Reels · Facebook Reels) | [social-short-video](../skills/social/social-short-video/SKILL.md), [tiktok-marketing/](tiktok-marketing/README-TikTok-Marketing.md) docs and case studies, Reels notes in the [Instagram](instagram-marketing/README-Instagram-Marketing.md) and [Facebook](facebook-marketing/README-Facebook-Marketing.md) kits | First because short vertical video is the channel closest to money for **apps and games**: video → profile → link → store → install → paid. One page, not four (see below) |
| 2 | X ✅ | [docs/00-101-tips.md](x-marketing/docs/00-101-tips.md) | Done 2026-10-21: 100 tips in the 8 sections; `reference/tips-and-tricks.md` is now a one-line pointer |
| 3 | Instagram (non-Reels: carousels, Stories, DMs) | `docs/`, research survey | Reels tips live in Short video 101; link to it |
| 4 | Reddit | `docs/`, subreddit rules | Most tips are "Rules & bans": karma, self-promo ratio, shadowban signs |
| 5 | Facebook (groups, Page) | `docs/04-groups-playbook.md` | Reels tips live in Short video 101; link to it |
| 6 | Pinterest | `docs/` | Claimed site, 2:3, keyword tips |
| 7 | Medium | `docs/` | Canonical link, Boost, publications |

### Short video 101 first: one page, four platforms, tips that turn views into money

**Why one page.** Makers film one vertical video and post it to TikTok, Shorts, Reels and Facebook Reels. Most tips
(hook in the first 1–2 seconds, one format repeated, the money path after the view) are the same everywhere; what
differs is the platform's rules and features. So: shared tips first, then one short section per platform.

```text
marketing/README-marketing-short-video-101.md      (planned)
  1. Shared: hook · format · editing · posting · link path · install → paid · rules
  2. TikTok (video + photo-mode slideshows)
  3. YouTube Shorts
  4. Instagram Reels
  5. Facebook Reels
  6. Games: where tips differ from apps
```

Every tip is also tagged with the step of the money path it fixes, so a reader with "views but no installs" jumps
straight to the right tips:

```text
hook → video / slides → post → profile / link → store page → install → paywall / IAP / ads → paid
```

| Step | Kinds of tips to collect (each still needs a label and source) |
|---|---|
| Hook | Person + doubt hooks vs feature hooks (TikTok case studies); game-moment hooks (a fail, a near-win, a level) |
| Video / slides | One repeatable format from social-short-video; TikTok slideshow: same scene across 6 slides, last slide shows the app / game |
| Post | Cross-posting the same video: watermarks, re-uploads and "original content" rules per platform (official sources only) |
| Profile / link | Where a clickable link is allowed on each platform and for which accounts (official help pages); one UTM per platform: `utm_source=tiktok|youtube|instagram|facebook` |
| Store page | First screenshot matches the video's result; links to the ASO skills |
| Install → paid | Read installs from App Store Connect / Play Console; "installs high, paid low" = paywall / IAP / ad placement, not the video |
| Rules & bans | Disclosing your own product, AI-content labels, spam signals on new accounts, per platform (official sources only) |

Per-platform sections hold only what is different: length limits, link options, remix / duet / collab features,
watermark and repost rules, and each platform's own monetization program for creators. Every limit or policy cites
the platform's help page and the date it was checked. Any number from a case study stays labelled as self-reported.

## Daily use (planned, after at least 3 kits have a 101 page)

- Each channel router skill gets a `101` mode, e.g. `/social-x 101`: picks one tip you haven't used, says what to do
  today and how to check it worked (and, for Practice tips, what to compare after two weeks).
- Tips double as content: a "<Channel> tip" post is useful to other makers and builds trust. The mode can draft one
  post per tip in the kit's post format.
- A tip that a test proves or disproves gets its label updated (Practice → Real, or moved to "Stop believing"), with
  the date.

## Done when (per kit)

- [ ] `docs/00-101-tips.md` (or `README-marketing-short-video-101.md`) exists with ≥ 30 tips in the 8 sections
- [ ] Every tip has a label; every Help / Code / Statement tip has a link; no invented numbers
- [ ] Kit README links it at the top ("New here? Read the 101 first")
- [ ] Hub table below gets a ✅ for the kit
- [ ] `python3 scripts/validate_skills.py` prints `OK`

| Kit | 101 page |
|---|---|
| Short video (TikTok · Shorts · Reels · FB Reels) | planned · **next, urgent** |
| X | ✅ [100 tips](x-marketing/docs/00-101-tips.md) |
| Instagram (non-Reels) | planned |
| Reddit | planned |
| Facebook (groups, Page) | planned |
| Pinterest | planned |
| Medium | planned |
