# 07 · Metrics and stop rules

Read every number **per reach**, the way Mosseri suggested (Reported, Jan 2025). Totals grow with luck; rates show
whether the post was good.

## Per post (at +48 h, from Insights)

| Metric | Formula | What it tells you |
|---|---|---|
| Reach | — | How far it went |
| Non-follower share | non-follower reach ÷ reach | Did the rankers test it on strangers? (Explore / Reels) |
| **Sends per 1k reach** | shares ÷ reach × 1000 | The growth signal for non-followers |
| Saves per 1k reach | saves ÷ reach × 1000 | Was it useful enough to keep? |
| Likes per 1k reach | likes ÷ reach × 1000 | Did followers like it? |
| Swipe-through / watch | carousel: reach on last slide ÷ first; Reel: avg watch time ÷ length | Did the hook and the script hold? |
| Profile visits | — | Did the post make people curious about you? |
| External link taps | from profile activity | Did the profile convert? |
| Landing visits | GA4, `utm_source=instagram`, by `utm_content` | Did the visit actually happen? |

## Per week (Sunday, 10 min) → [templates/weekly-numbers.md](../templates/weekly-numbers.md)

```text
reach → profile visits → link taps → landing visits → trials / emails → paid
```
Find the **weakest arrow** and fix only that next week:

| Weak arrow | Fix |
|---|---|
| Low reach, low non-follower share | Hooks (step 3), format fit (step 2), originality / watermark ([03](03-how-instagram-ranks.md)) |
| Reach OK, few sends / saves | Make posts more useful or more "send to a friend" (checklists, before/after) |
| Sends OK, few profile visits | Give a reason to open the profile: name the product on the last slide, "full list in my bio link" |
| Profile visits OK, few link taps | Bio (02), link 1 matches the post, Highlights with link stickers |
| Link taps OK, few landing visits | Broken / slow link on mobile, wrong page, missing UTM |
| Landing visits OK, few trials | Landing page and offer, not Instagram |

## Stop rules (Practice)
- **Format:** after 4 posts of a format, drop it if its sends + saves per 1k reach is below your average for the
  other formats. Keep the top 2 formats; try 1 new format each month.
- **Product:** after 4 weeks, if a product's posts bring 0 landing visits, move it to Stories only.
- **Channel:** after 8 weeks with tracked links, if Instagram sends < 5 % of landing visits **and** no trials, cut
  to 1 Reel a week recycled from X / TikTok and spend the time on the channel that does.
- **Never** chase a metric by buying followers, engagement pods or follow/unfollow ([08](08-rules-and-risks.md)).

## Baseline first
Before changing anything, write down the last 28 days (Insights → Overview): views, reach, % non-followers,
profile visits, link taps. Every target is "better than my baseline", not a number from a blog.
