# Instagram Marketing for Indie Devs

**Make one honest image post at a time that strangers send to a friend, then walk the people who care from the
post to your website in one tap.** Every rule here is labelled: **Official** (Instagram / Meta's own pages or
Mosseri's own posts), **Reported** (press coverage of an Instagram announcement), or **Practice** (worked for
others, test it yourself). Facts and sources: [reference/instagram-facts.md](reference/instagram-facts.md).

```text
image post (carousel / Reel / single)  →  reach (non-followers)  →  send / save  →  profile visit
        →  bio link or Story link sticker  →  landing (utm_source=instagram)  →  trial / email  →  paid
```

## One command

```text
/social-instagram post <fact>   → one post built with the 10-step image flow (slides, caption, alt text, link path)
/social-instagram week          → next week's 5 posts + 3 Story sequences from your fact bank
/social-instagram month         → the 30-day plan, day by day
/social-instagram profile       → name field, bio, 5 links with UTM, highlights, 3 pinned posts
/social-instagram story <post>  → a 3-frame Story that sends a post's readers to your site
/social-instagram numbers       → weekly numbers, the weakest step, what to fix
/social-instagram risk          → what cuts reach (originality, watermarks, bait, automation)
```

Router skill: [social-instagram](skills/social-instagram/SKILL.md). Installed as a plugin the command is
`/product-growth-hack:social-instagram post`; or copy `skills/social-instagram*` into `~/.claude/skills/`.

## The image flow (the core of this kit)

Ten steps from one true fact to a post that earns impressions and website visits:
[docs/04-image-flow.md](docs/04-image-flow.md) · skill [social-instagram-image-flow](skills/social-instagram-image-flow/SKILL.md).

```text
1 pick ONE fact → 2 pick the format → 3 write the hook slide → 4 script the slides → 5 build on the design kit
→ 6 make the visuals (real screenshots first) → 7 export + check → 8 caption, ≤5 hashtags, alt text
→ 9 the link path (bio · Story sticker · DM) → 10 publish, answer, reshare to Story, measure
```

## Start in 3 steps
1. **Today (45 min):** switch to a professional account and set up the profile →
   [docs/02-profile-setup.md](docs/02-profile-setup.md).
2. **Once (60 min):** build the design kit (colors, fonts, 3 slide layouts) → [templates/design-kit.md](templates/design-kit.md),
   and a [fact bank](../x-marketing/templates/fact-bank.md) per product (the same one the X kit uses).
3. **Every week (2–3 h):** 5 posts + 3 Story sequences with [social-instagram-growth](skills/social-instagram-growth/SKILL.md),
   or copy [posts/week-01-starter.md](posts/week-01-starter.md). Daily routine: [flow/daily-flow.md](flow/daily-flow.md).

## What's in this folder

| Folder | What's inside |
|---|---|
| [docs/](docs/) | The Instagram flow, one topic per file (below) |
| [reference/](reference/) | [Facts with sources and dates](reference/instagram-facts.md) · [research log 2026-10-12](reference/research-2026-10-12-instagram-survey.md) |
| [skills/](skills/) | [**social-instagram** (router)](skills/social-instagram/SKILL.md) · [image flow](skills/social-instagram-image-flow/SKILL.md) · [growth](skills/social-instagram-growth/SKILL.md) |
| [flow/](flow/) | [Daily / weekly / monthly routine](flow/daily-flow.md) · [Instagram → website funnel and UTM map](flow/website-funnel.md) |
| [templates/](templates/) | [Design kit](templates/design-kit.md) · [carousel brief](templates/carousel-brief.md) · [post file](templates/post-file.md) · [Story sequence](templates/story-sequence.md) · [weekly numbers](templates/weekly-numbers.md) |
| [posts/](posts/) | Ready to copy: [product rotation](posts/product-rotation.md), [week 1](posts/week-01-starter.md), [30-day plan](posts/plan-30-days.md) |

## Docs, in reading order
1. [Strategy: why images, and what Instagram is for an indie dev](docs/01-strategy.md)
2. [Profile setup checklist](docs/02-profile-setup.md)
3. [How Instagram ranks posts, in plain words](docs/03-how-instagram-ranks.md)
4. [The image flow: 10 steps from a fact to a post](docs/04-image-flow.md)
5. [Post formats: 12 kinds and the weekly rotation](docs/05-post-formats.md)
6. [Stories and the link path to your website](docs/06-stories-and-links.md)
7. [Metrics and stop rules](docs/07-metrics-and-stop-rules.md)
8. [Rules and risks](docs/08-rules-and-risks.md)

## Five things to remember
- Watch time, likes and **sends** are the top signals; sends matter most for reaching people who don't follow you
  (Reported, Mosseri, Jan 2025). Make posts people DM to a friend: checklists, before/after, honest numbers.
- Post your own work. Reposts, watermarks from other apps and "mostly text" Reels get less reach (Official).
- Links in captions don't work. The path to your site is **bio link → Story link sticker → DM** (Official / Reported).
- Five hashtags at most, and they help less than a clear caption with the words people search (Reported, Dec 2025).
- UTM on every link, or you'll never know whether Instagram sends visitors.

## Keep it current
- Monthly: re-check [reference/instagram-facts.md](reference/instagram-facts.md) against
  [Instagram's blog](https://about.instagram.com/blog) and [the Creators site](https://creators.instagram.com/), and update dates.
- New research goes in `reference/research-YYYY-MM-DD-<topic>.md`.

<sub>The products in `posts/` are made by the maintainer of this repo and are marked as such.</sub>
