# Instagram → website funnel and UTM map

How a stranger who sees one image ends up on your landing page, and how to prove it in analytics.

```text
 Explore / Reels / Feed / Google result
            │  (impression)
            ▼
   post: hook → slides → last slide "link in bio" / "Story has the link"
            │  (send · save · profile visit)
            ▼
   profile: name field + bio + Highlights + pinned 3
            │                      │
     bio link 1 (utm_medium=bio)  Highlight / Story link sticker (utm_medium=story)
            │                      │           keyword → DM (utm_medium=dm)
            ▼                      ▼                    ▼
   landing page for THAT product (same promise as the post, mobile-first)
            │
            ▼
   trial / email signup / store button   →   paid
```

## Make each step convert

| Step | Must have | Check |
|---|---|---|
| Post | Last slide names the product and the path in one line | Read slide 8 alone: is it clear where to go? |
| Profile | Name field with search words, 3-line bio, link 1 = the post's product | A stranger knows what you make in 5 s |
| Highlight | One per product, last frame with the link sticker | Tap it on a phone |
| Landing | Same words and image as the post's hook; loads fast on mobile; one button | Open the UTM link on 4G |
| Store / trial | The offer the post promised (free tier, trial length, price) | Matches the store today |

## UTM map

| Where | utm_medium | utm_campaign | utm_content |
|---|---|---|---|
| Bio link | `bio` | product slug | `<post-id>` while a post is fresh, else `profile` |
| Story link sticker | `story` | product slug | `<post-id>` or `hl-<highlight>` |
| Highlight frame | `story` | product slug | `hl-<product>` |
| DM after a keyword | `dm` | product slug | `<post-id>` |
| Reel / post (only if caption links are enabled for you) | `reel` / `post` | product slug | `<post-id>` |

`utm_source=instagram` always. Lowercase, no spaces. The post id is the post file's `NN-<slug>`.

## Reading it in GA4 (10 min, weekly)
Reports → Acquisition → Traffic acquisition → add the filter **Session source = instagram**, then add
**Session manual ad content** (`utm_content`) as a secondary dimension. That gives visits and conversions per post. If you
see sessions from `l.instagram.com` / `instagram.com` **without** UTM, a link somewhere is missing its tags: find
it (bio, an old Highlight) and fix it.

## Cross-channel
- Put the Instagram profile on your landing page footer, X bio's second line, GitHub profile and email signature
  ([X kit's cross-channel funnel](../../x-marketing/flow/cross-channel-funnel.md)); tag those links
  `utm_source=<that channel>` if they point to your site, not to Instagram.
- A carousel that wins on Instagram becomes an X post and a TikTok the next week. Same fact, new cut.
