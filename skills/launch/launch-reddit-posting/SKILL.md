---
name: launch-reddit-posting
description: Share a product on Reddit without getting removed or banned. Pick the right subreddits for your product type (macOS app, iOS, Android, browser extension, SaaS, dev tool or open source, indie game, AI tool, Notion template, Windows app), pull each subreddit's current rules with a script, write a post in the format Reddit rewards (title formulas, body template, first comment), follow a posting schedule that builds karma instead of burning the account, and get more users from fewer posts (a quality bar, the post types that convert, and a monthly rhythm of 2-4 strong posts plus useful comments). Use when posting on Reddit, "which subreddit should I post my app in", "r/macapps post", "how to promote on Reddit without getting banned", "Reddit self-promotion rules", "my Reddit post got removed", "how to get users from Reddit with few posts", "which Reddit posts bring signups", or planning a Reddit launch.
license: MIT
metadata:
  category: launch
  difficulty: beginner
  time: "Setup 30-45 min · each post 30 min · ongoing 15 min/day"
  version: 1.2.0
  author: nvminhtu
---

# Reddit Posting by Product Type

> In 45 minutes you'll have 5–8 subreddits that fit your product, their current rules in one file, and a first post
> written in the format each one accepts.

## Goal
Get real users from Reddit, which works for indie products when the post follows the subreddit's rules and helps the
reader. Most failed Reddit launches are removed by a moderator or a bot before anyone reads them: wrong subreddit,
wrong day, a missing flair, a new account, or a link with no story.

## When to use
- You're about to share a product, an update or a milestone on Reddit.
- A post was removed, or got no comments, and you don't know why.
- You need to know which subreddits fit a macOS app vs an extension vs a game.
- **Not for:** the core launch story and the other channels (HN, X, LinkedIn) →
  [launch-post-writing](../launch-post-writing/SKILL.md). Finding where users ask for tools (research, not posting) →
  [research-where-users-ask](../../research/research-where-users-ask/SKILL.md).

## Inputs
- A Reddit account that has commented in your target subreddits before. A brand-new account posting a link is the
  most common reason for an automatic removal.
- What the product is, the platform, the price (free / freemium / paid / free trial), and one link.
- A 20–60 second demo GIF or video, or 2–4 screenshots.
- The story: why you built it, one real number or moment.
- Python 3 to run `scripts/fetch_subreddit_rules.py`, or 10 minutes to read the rules pages by hand.

## Reddit-wide rules (apply in every subreddit)
From the [Reddit Rules](https://redditinc.com/policies/reddit-rules) (checked 2026-10-01):
- **Rule 2:** take part authentically in communities where you have a personal interest, **don't spam**, and don't
  manipulate content (no vote rings, no asking friends to upvote, no extra accounts). Breaking it can get posts
  removed and the account suspended.
- **Rule 5:** be authentic, don't mislead. **Say you're the developer.** "I found this cool app…" posts about your own
  product are the classic way to get banned.

From Reddit Help ([Spam](https://support.reddithelp.com/hc/en-us/articles/360043504051-Spam),
[keeping spam out of a community](https://support.reddithelp.com/hc/en-us/articles/28012014962580-How-do-I-keep-spam-out-of-my-community)):
- Promotion is **not spam by itself**. Spam is repeated or unsolicited posting: the same content mass-posted for
  exposure, mass private messages, bots or AI tools posting for you, masked links.
- **Each subreddit decides how much promotion it allows.** Some ban it completely. Others use a **10% rule**: at most
  1 in 10 of your posts and comments in that community may promote your own work. Read the rules before every first post (step 2).

## Steps

### Step 1: Pick subreddits by product type
Choose 1–2 from **Showcase** (they allow sharing what you made) and 2–4 from **Audience** (where users are, usually
stricter: weekly threads, specific days, or value-first posts only). Developer subreddits are for *how you built it*,
not for users.

| Product | Showcase (sharing allowed, check format) | Audience (strict, read the rules) | Developers (build story only) |
|---|---|---|---|
| **macOS app** | r/macapps | r/MacOS · r/mac · r/apple | r/SwiftUI · r/swift · r/iOSProgramming |
| **iOS app** | r/iosapps · r/AppHookup (deals: free or discounted) | r/iphone · r/ios · r/shortcuts (if it supports Shortcuts) | r/iOSProgramming · r/SwiftUI |
| **Android app** | r/androidapps | r/Android | r/androiddev |
| **Browser extension** | r/chrome_extensions | r/chrome · r/firefox · r/browsers | r/webdev |
| **Windows app** | r/software | r/Windows11 · r/windows | r/csharp, r/dotnet (stack-specific) |
| **SaaS / web app** | r/SideProject · r/IMadeThis · r/alphaandbetausers | Your users' niche (e.g. r/freelance, r/smallbusiness) | r/SaaS · r/indiehackers · r/microsaas · r/EntrepreneurRideAlong |
| **Dev tool / CLI / open source** | r/coolgithubprojects · r/opensource · r/selfhosted (self-hostable) | r/commandline · r/vscode · language subs (r/Python, r/javascript, r/reactjs) | r/programming · r/webdev |
| **Indie game** | r/playmygame · r/WebGames (browser) · r/IndieGaming | r/indiegames · genre subs (e.g. r/incremental_games) | r/IndieDev · r/gamedev · r/godot · r/Unity3D |
| **AI tool / agent / MCP** | r/SideProject | r/ChatGPT · r/ClaudeAI · r/LocalLLaMA (local models) · r/ChatGPTPro | r/AI_Agents · r/mcp · r/OpenAI · r/artificial |
| **Notion / Obsidian / sheet template** | r/Notion (check its promo rules) | r/productivity · r/ObsidianMD · r/excel · r/googlesheets | — |

#### macOS in detail
Mac users on Reddit are picky and generous at the same time: they try small utilities, and they ask about price,
privacy and native-ness straight away. In order:
1. **r/macapps:** the main showcase for Mac apps. Run the script, check whether it requires a post template or flair,
   and follow it exactly.
2. **r/SwiftUI or r/swift:** a "how I built X in SwiftUI" post with code or a technical lesson. The product link goes at the end.
3. **r/MacOS / r/mac / r/apple:** only as a genuinely useful tip ("how to …"), or in their weekly/self-promo thread
   if they have one. Don't post a bare app link.
4. **Off Reddit, same week:** MacUpdate, AlternativeTo → [listing-mac-app](../../listing/listing-mac-app/SKILL.md).

What Mac readers check in the comments: native (SwiftUI/AppKit) or Electron, price model (one-time vs subscription),
privacy (offline? telemetry?), macOS version, App Store or direct download, and Apple Silicon. **Answer these in the post.**

### Step 2: Get the current rules (10 min)
Rules, flairs and promo days change every few months, so don't trust a copy, including this skill.

```bash
python3 scripts/fetch_subreddit_rules.py macapps MacOS SwiftUI SideProject -o subreddit-rules.md
```

`--all` fetches every subreddit in the table above. Keep `subreddit-rules.md` in your project. For each subreddit,
fill one row of the checklist in `assets/reddit-post-plan.md`:

- [ ] Self-promotion allowed? Only in a weekly/megathread? Only on a certain day?
- [ ] Required **flair** or **title tags** (e.g. `[Free]`, `[iOS]`, `[Showoff Saturday]`)?
- [ ] Required content: price, platform, "I'm the developer", demo, source link?
- [ ] Ratio rule (how much of your activity may be self-promotion)? Account age/karma minimum?
- [ ] Banned: link-only posts, waitlists, surveys, referral links, AI-written posts, landing pages without a product?

If the script can't reach Reddit (blocked network), open `https://old.reddit.com/r/<name>/about/rules` and the
pinned posts by hand.

**Save a profile per subreddit, once.** Copy `assets/subreddit-profile.md` to `r-<Name>.md` for each subreddit: the
one rule that matters most, link rule, flair, title format, what readers want, the date you checked and the source.
Rules belong to the subreddit, not to your product, so keep these files in one shared folder and reuse them for every
product you post. Re-check a profile when it's older than 60 days. Never fill one from memory.

### Step 3: Write the post
Write **one post per request**: "a post for r/A about X" gives one file, written against r/A's profile. Note the date
you asked for it and the request in one line at the top of the file. The list of posts then reads in the order you
asked (post 1 → r/A, post 2 → r/B…), and each one shows which rules shaped it.

**Title formulas** (pick one, keep it plain, no emoji, no ALL CAPS):
- *Made-a-thing:* `I made [what it is] that [does one specific thing] for [who]`
- *Problem-first:* `I was tired of [specific annoyance], so I built [name]`
- *Lesson:* `[N] [weeks/users/$] in: what I learned building [what]` (best for builder and developer subreddits)
- *Deal* (deal subreddits only): follow the exact tag format from the rules.

**Body template**

```text
[1–2 lines: the problem, specific, in your own words]

[What it does, 3–5 bullets. Concrete verbs, no adjectives like "powerful" or "seamless"]

[Demo GIF / screenshot]

Details:
- Price: [free / $X one-time / $X per month, free trial N days]
- Platform: [macOS 14+, Apple Silicon + Intel / iOS 17+ / Chrome …]
- Privacy: [works offline, no account, no tracking — only if true]
- I'm the developer. [One line about you: solo, side project, how long]

[A specific question: "Would you use X or Y?", "What's missing for your workflow?"]

[Link, unless the rules say to put it in a comment]
```

**First comment** (post it yourself within a minute): the build story or technical detail in 3–5 lines, and what's
next on the roadmap. It gives early readers something to reply to.

### Step 4: Post, then stay (the first 2 hours matter most)
1. **Timing:** post when the subreddit's audience is awake. For US-heavy subreddits that's US morning. Check the
   promo day in the rules.
2. **One subreddit per day**, not all at once. Cross-posting the same text everywhere in an hour looks like spam
   to both moderators and filters.
3. **Reply to every comment for the first 2 hours.** Thank people for criticism, fix bugs they report, and say so.
4. If it's removed, read the removal reason, fix it, and **message the moderators politely** to ask. Don't repost
   without asking.
5. Log it in `assets/reddit-post-plan.md`: subreddit, date, upvotes, comments, signups/installs (use a UTM link).

### Step 5: Build the account (15 min/day, ongoing)
- Comment usefully in your subreddits for 1–2 weeks before your first post: answer questions, recommend other
  people's tools.
- Keep self-promotion a small share of your activity (many subreddits have a ratio rule).
- Come back with **updates that are news**: a big version, a milestone with numbers, an honest lesson. Not the same
  post again.

### Step 6: Fewer posts, more users (the monthly rhythm)
One strong post in the right subreddit usually brings more users than ten average ones, and it doesn't use up the
community's patience. Aim for **2–4 high-effort posts a month in total**, plus daily useful comments.

**Quality bar: post only if you can tick all five.**
- [ ] It would still be upvoted **with the link removed**: the story, lesson or demo is worth reading on its own.
- [ ] It has one specific thing: a number, a before/after, a mistake, a technical detail.
- [ ] The demo (GIF/video/screenshot) is in the post, not behind the link.
- [ ] It answers the obvious questions (price, platform, privacy, "why not X?") before they're asked.
- [ ] You'll be online for the next 2 hours.

**Post types ranked by users per post** (watch your own numbers, but start here):

| Type | Where | Why it converts |
|---|---|---|
| **Answering a "looking for a tool that…" thread** | Wherever users ask ([research-where-users-ask](../../research/research-where-users-ask/SKILL.md)) | The reader already wants the tool; say you're the developer |
| **"I made X" with a demo** | One showcase subreddit | Clear, visual, invites feedback |
| **Lesson or how-to** with the product mentioned once | Builder/developer subreddits | Gets saved and searched for months |
| **Milestone with real numbers** (1–2 months later) | Builder subreddits, or the same showcase if allowed | A new story, not a repost |
| **Deal / free promo code** | Deal subreddits only, in their format | Spikes installs, fewer long-term users |

**Measure per post:** upvotes, comments, link clicks (UTM) and sign-ups or installs. After 3–4 posts, the best type and
subreddit are obvious: repeat that type with a new story, and stop the ones that bring upvotes but no users.

## Prompt (copy-paste)
Replace everything in `{{ }}`. Paste the rules you fetched in step 2.

````text
You are a Reddit-savvy indie developer who has launched products without getting banned.

Product: {{name, what it does, who it's for}}
Type and platform: {{macOS app / iOS / Android / extension / SaaS / dev tool / game / AI tool / template}}
Price: {{...}}   Link: {{...}}   Demo: {{GIF/video yes/no}}
Story: {{why I built it, one real number or moment}}
My Reddit account: {{age, karma, subreddits I already comment in}}
Rules of the subreddits I'm considering (pasted from the subreddits' rules pages, or my saved r-<Name>.md profiles):
{{paste here}}

1. From these subreddits, pick the best 3–5 for my product type and order them (showcase first). For each, say
   whether I may post now, only in a weekly thread, only on a certain day, or should only comment for now,
   quoting the rule that decides it.
2. For each chosen subreddit, write: a title (in its required format/flair), the body (problem, 3–5 concrete
   bullets, price, platform, privacy, "I'm the developer", one specific question), and my first comment.
   Different wording for each subreddit, not copy-paste.
3. List the questions commenters will probably ask (for a Mac app: native or Electron, price model, privacy, macOS
   version, App Store or direct) and a short honest answer for each.
4. Give a 7-day schedule: one subreddit per day, best time, and what to do in the first 2 hours.
5. Check each post against this bar and rewrite it if it fails: worth upvoting with the link removed, one specific
   number or lesson, demo in the post, obvious questions answered. Then suggest a monthly rhythm of 2-4 posts
   (which post types, which subreddits) plus where to answer "looking for a tool" threads.
Never suggest vote manipulation, multiple accounts or hiding that I'm the developer.
````

## Example output

> **Illustrative example.** A fictional app. The rules quoted here are invented for format; use your own fetched rules.

*Menu-bar clipboard manager for macOS, $9 one-time, 14-day trial, SwiftUI, offline.*

| Day | Subreddit | Type | Title |
|---|---|---|---|
| Tue | r/macapps | Showcase (follows its template) | I made a tiny clipboard manager that lives in the menu bar and never touches the network |
| Thu | r/SwiftUI | Developer | What I learned building a menu-bar app in SwiftUI (MenuBarExtra pitfalls + code) |
| Sat | r/MacOS | Audience (weekly thread only) | Short comment in the self-promo thread linking the r/macapps post |

Body for r/macapps (excerpt):
> I copy 50+ things a day and kept losing the one from 10 minutes ago. Existing tools wanted an account or a subscription.
> - ⌘⇧V opens the last 200 items, type to search
> - Pin snippets, skip passwords from password managers automatically
>
> Price: $9 one-time, 14-day trial · macOS 14+, Apple Silicon and Intel · offline, no telemetry · I'm the solo developer.
> What would make you switch from your current clipboard tool?

## Common mistakes
- **Posting from a new account with no comments.** Filters often remove it silently. Build history first.
- **Same text in 10 subreddits in one hour.** Write per subreddit, one per day.
- **Missing flair or title tag.** The automatic moderator removes it, and you never find out why.
- **Link first, no story.** Reads as an ad and gets downvoted.
- **Hiding that you're the developer.** It's found out quickly and hurts the product's name.
- **Arguing with critics.** Thank them, fix what's real, and reply with what you changed.
- **Asking for upvotes anywhere.** It's vote manipulation under Reddit's rules.
- **Trusting an old rules list** (including the table in this skill). Re-run the script before you post.
- **Writing the post before opening the subreddit's profile.** Title format, flair and link rule decide whether it
  survives the first minute; check them first, not after.
- **Posting often instead of posting well.** Ten weak posts spend the community's goodwill; three strong ones build it.

## Related skills
- [launch-post-writing](../launch-post-writing/SKILL.md): the core story, and versions for HN, X and LinkedIn.
- [launch-quick-download-wins](../launch-quick-download-wins/SKILL.md): Reddit is one of 16 quick channels.
- [listing-mac-app](../../listing/listing-mac-app/SKILL.md): the Mac directories to use the same week.
- [research-where-users-ask](../../research/research-where-users-ask/SKILL.md): find threads where people ask for your tool, and answer there.

## Credits
Written by [@nvminhtu](https://github.com/nvminhtu). Site-wide rules: [Reddit Rules](https://redditinc.com/policies/reddit-rules) and Reddit Help ([Spam](https://support.reddithelp.com/hc/en-us/articles/360043504051-Spam)).
Subreddit rules are not copied here on purpose: they change often, so `scripts/fetch_subreddit_rules.py` pulls the
current ones from each subreddit's own rules page.
