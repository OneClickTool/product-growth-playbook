# 06 · Stories and the link path to your website

On Instagram a website visit happens in four places only. Plan which one each post uses.

| Path | Tappable? | Lives | Label |
|---|---|---|---|
| **Bio links** (up to 5) | Yes | Until you change them | Official (website) / Reported (5 links) |
| **Story link sticker** | Yes | 24 h, forever in a Highlight | Official (all accounts except new / rule-breaking ones) |
| **DM** (you send the link) | Yes | In their inbox | Practice |
| Caption URL | **No** (plain text) | — | Practice; clickable caption links are only a Meta Verified test (Reported) |
| Paid boost button | Yes, while the ad runs | Campaign | Out of scope here |

## The 3-frame Story that sends a post's readers to your site

Post it 1–3 hours after the feed post. Template: [templates/story-sequence.md](../templates/story-sequence.md).

| Frame | What's on it | Sticker |
|---|---|---|
| 1 · Tease | The post's hook slide shared to Story (tap-through to the post) + `New post: the 20-second Downloads clean-up` | — |
| 2 · Proof | One real screenshot or a 5 s screen clip of the result | Poll: `Is your Downloads folder a mess?` Yes / Very |
| 3 · Path | One line: `Free for 2 folders. Try it ↓` + app icon | **Link sticker**, text `Get Tidybox`, URL with `utm_medium=story&utm_content=<post-id>` |

Then **add frame 3 (or all three) to the product's Highlight**, so the link keeps working on the profile.

Rules (Practice): one link per Story sequence; the sticker text says what happens (`Get the free app`, not `Link`);
put the sticker in the middle third, above the reply bar.

## Keyword → DM (for posts that get comments)
- On the last slide and in the caption: `Comment CLEAN and I'll send you the link.`
- Answer by hand, or with a tool that uses Meta's official messaging API. The DM must contain **only** what was
  promised + the UTM link (`utm_medium=dm`). Don't promise a "free guide" you don't have.
- Don't use it on every post; "comment to get" on everything reads as bait ([08](08-rules-and-risks.md)).
- Meta's rules: one private reply per comment, within 7 days; automated messages only inside 24 h of the person's
  last message (Official, [facts](../reference/instagram-facts.md#growth-levers-checked-2026-10-12)). Full flow,
  saved replies and tracking: [social-instagram-dm](../skills/social-instagram-dm/SKILL.md) (`/social-instagram dm <post>`).

## Bio link rotation
- Link 1 = the product of **today's** post. Change it when you publish; change it back to the hero product after
  3 days.
- Each bio link has its own `utm_campaign`, and `utm_content=<post-id>` while a post is fresh, so you can see which
  post sent the visit.

## Highlights as a mini landing page
Order: `Start` (who you are, what you make, 3 frames) · one Highlight per product (demo frame, proof frame, link
frame) · `Free` (everything free, with links). Refresh the link frames when prices or URLs change.

## UTM pattern
```text
https://<site>/<product>?utm_source=instagram&utm_medium=<bio|story|dm|reel>&utm_campaign=<product-slug>&utm_content=<post-id>
```
Post id = the post file's `NN-<slug>` ([templates/post-file.md](../templates/post-file.md)). Full map and the GA4
report to read it: [flow/website-funnel.md](../flow/website-funnel.md).
