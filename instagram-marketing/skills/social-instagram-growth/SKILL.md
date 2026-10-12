---
name: social-instagram-growth
description: Grow on Instagram as an indie developer and turn reach into website visits and first customers. Sets up the profile once (professional account, searchable name field, 3-line bio, up to 5 bio links with UTM, Highlights that keep Story links alive, 3 pinned posts), then plans each week as 5 image posts (3 carousels, 1 Reel, 1 single image) from 12 formats plus Story sequences with a link sticker, built with the 10-step image flow. Follows what Instagram says it ranks (watch time, likes and sends per reach, originality), tests formats with Trial Reels, and runs a Sunday check that finds the weakest step from reach to paid. Use when someone asks "how do I grow on Instagram as a developer", "Instagram marketing for my app", "plan my Instagram posts for the week", "get website traffic from Instagram", "Instagram content plan for SaaS", "kế hoạch Instagram", "quy trình Instagram marketing", "tăng traffic web từ Instagram", or wants a weekly Instagram system.
license: MIT
metadata:
  category: social
  difficulty: beginner
  time: "Setup 90 min · 2-3 h/week batching · 20 min/day"
  version: 1.0.0
  author: nvminhtu
---

# Instagram Growth: Weekly Image Posts → Website Visits

> A profile that converts, a week of image posts and Stories planned from your real product facts, and a Sunday
> check that tells you which step to fix.

## Goal
Most indie devs either skip Instagram or post app screenshots with a caption URL nobody can tap. What works is a
small, steady set of image posts strangers want to save and send, a profile that says what you make, and one
planned tap from each post to your website. This skill sets that up once, then keeps it to one batching session a
week and 20 minutes a day.

## When to use
- Your product has a visible result (consumer app, Mac utility, game, template) and buyers who aren't developers.
- You post on Instagram but reach stays with followers, or reach grows and website visits don't.
- You already post on X or TikTok and want Instagram from the same facts without reposting.
- **Not for:** building one post in detail → [social-instagram-image-flow](../social-instagram-image-flow/SKILL.md).
  Video-only strategy across TikTok / Reels / Shorts → [social-short-video](../../../skills/social/social-short-video/SKILL.md).
  Developer-only buyers → [social-x-growth](../../../x-marketing/skills/social-x-growth/SKILL.md) first.

## Inputs
- Products: one-line pitch, who it's for, offer as the store shows it today, landing URL.
- A fact bank per product (10–20 true, dated facts) — the [X kit's template](../../../x-marketing/templates/fact-bank.md) works.
- Real screenshots / screen recordings with demo data; your design kit ([templates/design-kit.md](../../templates/design-kit.md)).
- Access to Instagram Insights (professional account) and an analytics tool that reads UTM tags (GA4 or similar).

## Steps
1. **Baseline (10 min).** Write down the last 28 days from Insights: views, reach, % non-followers, profile visits,
   external link taps. Every target is "better than this".
2. **Profile (45 min, once)** → [docs/02-profile-setup.md](../../docs/02-profile-setup.md): professional account,
   search-engine setting on, Account Status clean, name field with search words, 3-line bio, bio links with
   `utm_source=instagram&utm_medium=bio`, one Highlight per product with a link-sticker frame, 3 pinned posts.
3. **Design kit (60 min, once):** canvas sizes, 3 colors, 2 type sizes, layouts A–D, footer. Then nobody designs from zero.
4. **Plan the week (15 min, Sunday)** with the rotation in [docs/05-post-formats.md](../../docs/05-post-formats.md):

   | Day | Post | Story |
   |---|---|---|
   | Mon | Carousel: how-to or checklist (teach) | Reshare + link sticker |
   | Tue | — | Behind the scenes / poll |
   | Wed | Demo Reel (Trial Reel if the format is new) | Reshare + link sticker |
   | Thu | Carousel: before/after or mistakes (send-able) | — |
   | Fri | Single result image or behind the scenes | Question sticker |
   | Sat | — | What shipped + link sticker |
   | Sun | Tips / tour / numbers / offer (max one offer a week) | — |

   One product per post; each product at least every 2 weeks; never the same format for the same product two weeks running.
5. **Make the posts (90–120 min)** with the [image flow](../../docs/04-image-flow.md): fact → format → hook →
   script → kit → visuals → export → caption + alt text → link path. One post file each
   ([templates/post-file.md](../../templates/post-file.md)).
6. **Every day (20 min)** → [flow/daily-flow.md](../../flow/daily-flow.md): publish, set bio link 1 to today's
   product, answer every comment in the first hour, Story with link sticker at +1–3 h and save it to the Highlight,
   3–5 real comments on accounts your buyers follow.
7. **Sunday numbers (10 min)** → [templates/weekly-numbers.md](../../templates/weekly-numbers.md): reach →
   profile visits → link taps → landing visits (GA4, `utm_source=instagram`, by `utm_content`) → trials → paid.
   Fix the weakest arrow only ([docs/07](../../docs/07-metrics-and-stop-rules.md)).
8. **Monthly:** keep the 2 best formats (sends + saves per 1k reach), drop the weakest, try one new one; refresh
   pins and Highlights; check Account Status; re-check [reference/instagram-facts.md](../../reference/instagram-facts.md).
9. **Recycle winners:** a carousel above your average becomes next week's Reel and an X post. Same fact, new cut.

## Prompt (copy-paste)
Works in Claude, ChatGPT, Gemini, Cursor. Replace everything in `{{ }}`.

````text
You are my Instagram content planner. I'm an indie developer selling my own products. Plain words, specific, no
hype. Never invent features, numbers, users, reviews or results not in my fact bank; write <NUMBER?> and list it.

Products (pitch · who for · offer today · landing URL · slug):
{{...}}
Fact bank (true, dated facts per product):
{{...}}
Screenshots / clips I have: {{...}}
Last week's posts (format id + product) and their sends/saves per 1k reach: {{... or "first week"}}
Baseline (28 days): {{views, reach, % non-followers, profile visits, link taps}}

Plan next week:
1. Five posts on Mon, Wed, Thu, Fri, Sun using this rotation: Mon teach carousel (I01 how-to / I03 checklist),
   Wed demo Reel (I07; say "Trial Reel" if the format is new for me), Thu send-able carousel (I02 before/after /
   I05 mistakes), Fri single result (I10) or behind the scenes (I08), Sun I04 tips / I06 tour / I09 numbers /
   I12 offer. At most one I12 offer post. One product per post; don't repeat last week's format for the same product.
2. For each post: format id, product, the one fact used, 3 hook options (≤ 8 words) with the image for each,
   the slide-by-slide script (≤ 25 words per slide, image that proves it, alt text) or a Reel shot list, caption
   (line 1 ≤ 125 characters with search words, ask, "link in bio" path, 3-5 specific hashtags, no URL), and the
   bio + Story URLs with utm_source=instagram, utm_medium=bio|story, utm_campaign=<slug>, utm_content=<NN-slug>.
3. Three Story sequences (Mon, Wed, Sat), 3 frames each: tease / proof + poll / path + link-sticker text.
4. Two Stories without links for Tue and Fri (behind the scenes, question sticker).
5. Which bio link should be #1 on each day.
6. A checklist of every number, claim and screenshot I must verify, and what to log at +48 h per post.
Never suggest buying followers, engagement pods, follow/unfollow, reposting others' content, or "comment to get"
on more than one post a week.
````

## Example output

> **Illustrative example.** Fictional products (Tidybox, a Mac cleaner; Pinlog, an iPhone places app) and made-up facts.

| Day | Format | Product | Hook | Path |
|---|---|---|---|---|
| Mon | I03 checklist, 9 slides | Tidybox | `7 things filling your Mac right now` | Bio link 1 = Tidybox · Story + sticker |
| Wed | I07 demo Reel 12 s (Trial Reel) | Pinlog | `My week, as a recap card` | Story + sticker "Join the waitlist" |
| Thu | I02 before/after, 4 slides | Tidybox | `Downloads: before → after one scan` | Bio |
| Fri | I08 behind the scenes, 5 slides | Pinlog | `Why it has no account and no servers` | Bio |
| Sun | I12 offer, 5 slides | Tidybox | `Free for 2 folders. Here's what Pro adds.` | Bio · DM keyword `CLEAN` |

**Sunday check (made-up):** reach up, sends per 1k reach highest on Thu's before/after, profile visits flat → the
weak arrow is post → profile. Fix: name the product and "link in bio" on the last slide of every carousel.

## Common mistakes
- **Posting every day without a path.** Reach with no bio link 1 / Story sticker is reach you can't use.
- **Screenshots without a story.** A bare UI screenshot has no hook; show the problem first, then the result.
- **Only selling.** More than one offer post in five reads as an ad; sends and saves drop.
- **Cross-posting TikToks with the watermark.** Less reach to non-followers. Export the original.
- **Reading totals, not rates.** Compare sends and saves per 1k reach; a lucky post hides a weak format.
- **No UTM.** Without `utm_source=instagram` and `utm_content`, you can't tell which post sent the buyer.

## Related skills
- [social-instagram-image-flow](../social-instagram-image-flow/SKILL.md): build each post in 10 steps.
- [social-instagram](../social-instagram/SKILL.md): one command for the Instagram kit.
- [social-short-video](../../../skills/social/social-short-video/SKILL.md): find the Reel format that works.
- [social-build-in-public](../../../skills/social/social-build-in-public/SKILL.md): the weekly "what shipped" Story as a habit.
- [strategy-product-as-funnel](../../../skills/strategy/strategy-product-as-funnel/SKILL.md): move followers to an email list you own.

## Credits
Written by [@nvminhtu](https://github.com/nvminhtu). Sources: [Instagram Ranking Explained](https://about.instagram.com/blog/announcements/instagram-ranking-explained),
[Add a website to your profile](https://help.instagram.com/362497417173378),
[link sticker for everyone](https://about.instagram.com/blog/announcements/expanding-sharing-links-in-stories-to-everyone),
and press reports in [reference/instagram-facts.md](../../reference/instagram-facts.md) (checked 2026-10-12).
