# 05 · Posting: drafts, sound, captions, cadence

## Draft first, publish by hand
Both public cases send slideshows to TikTok as **drafts** and publish from the phone:
- The API cannot choose a TikTok sound. Trending or fitting audio is added in the app.
- You get a last look at each post (wrong text, warped image, missing app name).
- It keeps a human in the loop, which matters for TikTok's automation rules ([07](07-rules-and-risks.md)).

Ways to get a draft onto the phone:

| Route | How | Notes |
|---|---|---|
| Manual | AirDrop / save images, open TikTok → + → Photo → pick 6 → text → save draft | Zero setup |
| TikTok API, `MEDIA_UPLOAD` | Your app sends photos to the user's inbox; they finish in TikTok | Needs a TikTok developer app, verified URL prefix, app version ≥ 31.8. Max 5 pending shares per 24 h. [Facts](../reference/tiktok-photo-post-api.md) |
| TikTok API, `DIRECT_POST` with `SELF_ONLY` | Posts privately, you change privacy later | Unaudited API clients can **only** post privately |
| Scheduler (Postiz, post-bridge, Publer, …) | Their TikTok integration + their API/CLI | Monthly fee; check the plan includes TikTok photo posts and drafts |

## Sound
- Pick a sound from TikTok's library inside the app. On a **business account** you only get the commercially cleared
  library; that's the one to use when promoting your own product.
- Lo-fi / ambient fits educational and quote slideshows; trending sounds help discovery but can feel off-topic. Test
  both, log which one you used.

## Caption
- 2–4 sentences that continue the story from slide 1, name the app once, and end with a soft action.
- The first line is what people see before "more"; make it the useful line.
- At most 5 hashtags (both cases). Mix 2 niche tags and 1–2 broad ones. No banned or unrelated trending tags.
- Every caption different. Review the first batch for repeated phrasing; templated captions read as spam.
- Links in captions aren't clickable. Put one tracked link in your bio and say "link in bio".

```text
My landlord has a strict "no changes" rule. I ran our living room through Snugly and showed her three versions.
She picked the green one and said I can paint. Link in bio if you want to try your room.
#roomdecor #smallapartment #interiordesign #renterfriendly
```
(Illustrative caption in the style the case describes, not the real one.)

## Cadence and timing
| Phase | Posts/day | Notes |
|---|---|---|
| Week 1 (after the account is warm) | 1 | Learn the tools; get 7 data points |
| Weeks 2–3 | 2–3 | Test 3+ hook formulas side by side |
| After a winner | 3 (+ variations of the winner) | Larry suggested 7:30, 16:30, 21:00 in the audience's time zone |

Posting times above are one agent's defaults, not TikTok data. Use your audience's time zone and check TikTok
analytics → Followers → activity once you have followers.

## Bio
- One line: who it's for + what they get. One tracked link (store or landing) with `utm_source=tiktok`.
- If you run the app's own account, the name and avatar match the app; if it's your personal account, say you made it.
