# UTM convention (one table for every channel)

One rule for every link you post, so GA4 can say which channel brought the visit. Checked 2026-10-19 against
[GA4 default channel group](https://support.google.com/analytics/answer/9756891).

## The rule

| Parameter | Holds | Format | Example |
|---|---|---|---|
| `utm_source` | The site or list the click came from | lowercase, one word | `x`, `reddit`, `instagram`, `newsletter` |
| `utm_medium` | The placement on that site | lowercase, one word | `post`, `reply`, `bio`, `comment`, `email` |
| `utm_campaign` | What you promote | lowercase-hyphens | `habit-launch`, `v2-release` |
| `utm_content` | (optional) which variant | lowercase-hyphens | `hook-a`, `slide-6` |

No spaces, no capitals, no `@` or `/`. GA4 treats `Reddit` and `reddit` as two sources: values are case sensitive,
and Google recommends lowercase and always setting `utm_source`, `utm_medium` and `utm_campaign`
([URL builders](https://support.google.com/analytics/answer/10917952)). Tag only links that live **outside** your
site, never your own menu or footer.

## What the channel kits in this repo use

These values come from the channel kits (`marketing/*/docs/07-metrics-and-stop-rules.md` and their posts). Keep
using them so old and new links match.

| Channel | `utm_source` | `utm_medium` values used | Kit |
|---|---|---|---|
| X | `x` | `post`, `reply`, `bio` | [x-marketing](../../../../marketing/x-marketing/docs/07-metrics-and-stop-rules.md) |
| Instagram | `instagram` | `bio`, `story`, `dm`, `creator` | [instagram-marketing](../../../../marketing/instagram-marketing/docs/07-metrics-and-stop-rules.md) |
| Reddit | `reddit` | `comment`, `post`, `profile` | [reddit-marketing](../../../../marketing/reddit-marketing/docs/07-metrics-and-stop-rules.md) |
| Facebook | `facebook` | `group`, `page`, `profile` | [facebook-marketing](../../../../marketing/facebook-marketing/docs/07-metrics-and-stop-rules.md) |
| Pinterest | `pinterest` | `pin`, `profile` | [pinterest-marketing](../../../../marketing/pinterest-marketing/docs/07-metrics-and-stop-rules.md) |
| Medium | `medium` | `article`, `profile` | [medium-marketing](../../../../marketing/medium-marketing/docs/07-metrics-and-stop-rules.md) |
| TikTok | `tiktok` | `video` | [growth action step 1](../../../growth/action/01-measure-first.md) |
| Your other products | `extension` (or product type) | `crosspromo` | [growth action step 1](../../../growth/action/01-measure-first.md) |
| Email | `newsletter` | `email` | — |
| GitHub | `github` | `readme`, `skill`, `area`, `playbook`, `funding` | this repo's own links |
| YouTube | `youtube` | `video`, `shorts`, `description` | — (no kit yet) |

## Why some of these land in "Unassigned" (and the fix)

GA4's default channel group looks at `utm_medium` first. Organic Social matches mediums like `social`,
`social-network`, `social-media`, `sm`; Email matches `email`, `e-mail`, `e_mail`; Referral matches `referral`,
`app`, `link`. Organic Social and Email can also match on the **source** if it's on Google's own list of social
sites or email sources. Anything that matches no rule is **Unassigned**.

So a link like `utm_source=x&utm_medium=reply` is only "Organic Social" if Google's source list knows `x`. Don't
assume; check:

1. Reports → Acquisition → **Traffic acquisition** → filter *Session default channel group* = `Unassigned`.
2. Add the secondary dimension *Session source / medium*. Any of your tagged links in that list?

If yes, **don't rewrite links you already posted**. Add a custom channel group instead (Admin → Data display →
Channel groups → Create new), copy the default rules, and add near the top:

| New channel | Condition |
|---|---|
| Organic Social (tagged) | *Session source* exactly matches one of `x`, `reddit`, `instagram`, `facebook`, `pinterest`, `medium`, `tiktok` |
| Cross-promo | *Session medium* exactly matches `crosspromo` |

Rules are checked top to bottom; the first match wins. If you also use the "AI assistants" channel from
[launch-geo-aeo-feature-preview](../../../launch/launch-geo-aeo-feature-preview/SKILL.md), put it in the same custom
group, above *Referral*.

For brand-new channels you can instead put the placement in `utm_content` and use `utm_medium=social`, so the
default group works with no custom rules. Pick one approach and write it in your tracking plan with the date.
