---
name: launch-github-repo-seeding
description: Seed a new open-source GitHub repository from 0 to its first real stars, users and contributors, in three levels (1 make the repo worth starring, 2 seed it with your own circle and the ecosystem of bigger repos, 3 keep it growing), with legitimate tricks (awesome lists, GitHub topics, integrations with popular projects, "alternative to X", good first issues) and a clear line on what GitHub bans (bought or exchanged stars). Covers how to reach classic developers and "vibe coders" who build with AI tools and rarely browse GitHub. Use when someone asks "how do I get GitHub stars", "promote my open-source repo", "seed a repository", "get my repo on GitHub trending", "get listed in awesome lists", "market a GitHub project", "my community wants to grow a repo", or "how do vibe coders find tools on GitHub".
license: MIT
metadata:
  category: launch
  difficulty: beginner
  time: "Level 1: 2-3 h · Level 2: 1 week · Level 3: 1 h/week"
  version: 1.0.0
  author: nvminhtu
---

# GitHub Repo Seeding

> A repo that converts visitors into stars, a one-week seeding plan with your own circle and bigger repos'
> ecosystems, and a weekly habit that keeps it growing, with no fake stars.

## Goal
Take a new public repository from zero to its first 100 **real** stars, users and one or two outside contributors.
Stars matter because they are social proof: they decide whether the next visitor trusts the repo, whether it shows
up in GitHub search and trending, and whether an awesome list accepts it. Only real stars keep doing that.

## When to use
- You're a solo builder or the owner of a group or community (Facebook group, Discord, company team) and want to put
  a repo on the map.
- The repo is public and works, but it has fewer than ~50 stars and nobody outside your circle has found it.
- **Not for:** publishing a VS Code / JetBrains / Obsidian plugin to its store → [listing-dev-plugin](../../listing/listing-dev-plugin/SKILL.md).
  Agent skills, GPTs and MCP servers → [listing-ai-product](../../listing/listing-ai-product/SKILL.md). Writing the
  Show HN or Reddit post itself → [launch-post-writing](../launch-post-writing/SKILL.md).

## Inputs
- The repo URL and a one-sentence "what it does for whom" ("Turns any Figma frame into a SwiftUI view").
- 3–5 bigger, well-known repos your project **works with or replaces** (the ecosystem you can plug into).
- Who you already reach: group size, followers, colleagues, newsletter, other repos you own.
- Who the users are: classic developers (use git daily), vibe coders (build with Cursor, Claude Code, Lovable,
  Bolt, v0, Replit…), or both.

## First, the line you don't cross
GitHub's [Acceptable Use Policies](https://docs.github.com/en/site-policy/acceptable-use-policies/github-acceptable-use-policies)
(section 4, *Spam and Inauthentic Activity*) prohibit rank abuse such as automated starring or following, fake accounts,
coordinated inauthentic activity, markets for inauthentic activity, and engagement bought with rewards or give-aways.
Researchers have found millions of suspected fake stars ([He et al., StarScout, arXiv 2412.13459](https://arxiv.org/abs/2412.13459)),
and detection tools now flag them, so bought stars can get the repo hidden and the account restricted.

| ✅ Allowed | ❌ Not allowed |
|---|---|
| Asking people who **tried** the repo to star it if it helped | Buying stars, "star-for-star" exchange groups, sock-puppet accounts |
| Telling your group about the repo and asking for honest feedback | Asking your group to all star at 9:00 to "hit trending" |
| A "⭐ if this saved you time" line in the README | Giveaways, credits or tokens in exchange for stars |
| Answering an issue in a big repo when your tool genuinely solves it | Pasting your link into dozens of unrelated issues and PRs |

**Group owners:** your members are your best first users, not a star farm. Ask them to *use* it and report one bug.
The stars that follow are real, and the issues they open make the repo look alive.

## Level 1: make the repo worth starring (2–3 hours)
Visitors decide in seconds. Fix these before you send anyone.

| # | Item | What good looks like |
|---|---|---|
| 1 | **Name + About line** | Searchable words, not only a brand: `swiftui-figma-export`, About: "Export Figma frames to SwiftUI views". Add the website field |
| 2 | **Topics** | Up to 20 per repo, lowercase with hyphens, ≤ 50 chars ([docs](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/classifying-your-repository-with-topics)). Use the **same topics the big repos in your ecosystem use**, so you appear on those topic pages |
| 3 | **README top screen** | One sentence, a GIF or screenshot of the result, and the install command, all above the fold |
| 4 | **30-second quick start** | Copy-paste install + one command that shows a result. If it needs 10 steps, it gets 0 stars |
| 5 | **Social preview image** | 1280×640 px, PNG/JPG/GIF under 1 MB ([docs](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/customizing-your-repositorys-social-media-preview)). This is what shows when the link is shared on X, Slack, Facebook or Discord |
| 6 | **Trust signals** | LICENSE, a release tag, a CHANGELOG, CI badge, recent commits. Empty repos with one commit look abandoned |
| 7 | **Community files** | CONTRIBUTING.md, issue templates, 3–5 issues labelled `good first issue`, Discussions turned on |
| 8 | **Vibe-coder path** | A section "Use it with your AI agent": one line to paste into Cursor / Claude Code / Codex, plus `npx`, a Claude Code plugin or an MCP config if it fits. An AGENTS.md so agents set it up correctly |
| 9 | **One-click try** | A "Deploy to Vercel/Netlify" button, "Open in GitHub Codespaces" badge or a live demo link, for people who never clone |
| 10 | **A soft star ask** | One line near the end: "If this saved you time, a ⭐ helps others find it." Not a banner, not a popup |

## Level 2: seed it (one week)
Do these in order. Each step builds on the proof from the one before.

**Day 1–2: your own circle (the first 20–50 stars).**
1. Share it with the people who know you (group, colleagues, friends, past users) with a **specific ask**:
   "Try the quick start and tell me where you got stuck." People who used it star it on their own.
2. Pin it on your GitHub profile, add it to your profile README, bio and email signature.
3. Group owners: post a "build log" in the group (why you made it, a demo GIF, what help you need),
   and open a thread for feedback. Credit the people who report bugs in the release notes.

**Day 3–4: plug into bigger repos (the "ecosystem" trick).** Big repos have thousands of visitors a day. Be useful
inside their world instead of shouting next to it:
4. **Awesome lists.** Search GitHub for `awesome <your topic>`, pick 3–5 active lists (merged PRs in the last months),
   read each list's CONTRIBUTING and open one clean PR per list. Many lists require the project to be mature, with docs
   and some history. The main [sindresorhus/awesome](https://github.com/sindresorhus/awesome) index, for example, only
   accepts **lists** that are at least 30 days old and doesn't accept fully AI-generated PRs.
5. **Ecosystem and showcase pages.** Many large projects have a "Community", "Integrations", "Plugins", "Built with"
   or "Showcase" page in their docs or Discussions. Build a real integration, then ask to be listed there.
6. **"X for Y" and "alternative to X".** Name the relationship in the README: "A lightweight alternative to X",
   "Y plugin for Z". Add the repo on [AlternativeTo](https://alternativeto.net/) as an alternative to the big project.
7. **Contribute upstream.** Fix a real bug or doc gap in a big repo you depend on. Maintainers and watchers see
   your profile, which pins your repo. This is slow, but it builds a reputation that lasts.
8. **Answer questions where the big repo's users ask** (its issues, Discussions, Stack Overflow tag, subreddit, Discord):
   only when your tool actually solves the problem, and say you made it.

**Day 5–7: one public launch spike.**
9. Pick **one or two** places that fit your users and post on the same day, so the stars arrive together
   (GitHub trending is driven by recent star velocity; the exact algorithm isn't public):
   - Classic developers: Show HN, r/programming or a language subreddit, dev.to, Lobsters (invite-only), a language newsletter.
   - Vibe coders: X/Threads with a 30-second demo video, r/vibecoding, r/cursor, r/ClaudeAI, the Discords of the AI
     tool you integrate with, YouTube Shorts / TikTok "I built this with AI" demos.
   - Your region: local developer groups (for example Vietnamese dev Facebook groups and Viblo), in the local language.
   Posts → [launch-post-writing](../launch-post-writing/SKILL.md). Be online for the first 3 hours to answer everything.

## Level 3: keep it growing (1 hour a week)
- **Ship visibly.** Small releases with notes every 1–2 weeks. Each release is a reason to post again.
- **Answer every issue within a day** at the start. A fast, kind maintainer is the best marketing an open-source repo has.
- **Turn users into contributors:** label `good first issue` / `help wanted`, thank people by name, add an
  all-contributors table. Seasonal events like [Hacktoberfest](https://hacktoberfest.com/) bring new contributors,
  but the rules change every year, so read the current maintainer rules first.
- **Content that ranks outside GitHub:** a tutorial or "how I built it" post that links to the repo keeps sending visitors
  long after launch day.
- **Track** stars, clones and referrers weekly in *Insights → Traffic* (last 14 days only, so write them down).
  Keep the channels that send people who star **and** open issues.

## How to reach developers vs vibe coders
| | Classic developers | Vibe coders |
|---|---|---|
| Where they find tools | GitHub search and trending, HN, Reddit, newsletters, awesome lists | X, YouTube, TikTok, Discords of Cursor/Lovable/Bolt/Claude, "what are you building" threads, their AI agent |
| What convinces them | Clean code, docs, license, tests, benchmarks | A demo video of the result, "works in 1 prompt", a template they can remix |
| How they install | `git clone`, package manager | Paste a prompt into their agent, click Deploy, `npx`, a plugin or MCP one-liner |
| Do they star? | Yes, often right away | Less often. Ask **after** a success moment, and link directly to the repo |

Vibe coders do use GitHub, often without noticing: their agents clone repos, templates import from GitHub, and many
tools sync projects there. Make the repo **easy for an agent to use** (clear README, AGENTS.md, one-line install) and
give humans a demo they can watch in 30 seconds.

## Steps
1. Write the one-sentence pitch and list 3–5 big repos your project works with or replaces.
2. Do Level 1 items 1–10. Ask one person who has never seen the repo to follow the quick start while you watch.
3. Day 1–2: share with your circle and ask for **usage feedback**, not stars.
4. Day 3–4: open PRs to 3–5 awesome lists, ask for one ecosystem/showcase listing, add AlternativeTo.
5. Day 5–7: one launch spike in the 1–2 places where your users are. Answer everything.
6. From week 2: Level 3 habits, and a weekly note of stars, traffic referrers and new issues.

## Prompt (copy-paste)
Replace everything in `{{ }}`.

````text
You are an open-source growth coach who follows GitHub's Acceptable Use Policies (no bought, exchanged or
automated stars, no spam in other repos).

Repo: {{URL}}   What it does, for whom: {{one sentence}}
Big repos it works with or replaces: {{3-5 repos}}
Users: {{classic developers / vibe coders / both}}   Language/region: {{e.g. English + Vietnamese}}
Who I already reach: {{group size, followers, colleagues, other repos}}
Current state: {{stars, README quality, has demo GIF? install steps?}}

1. Audit the repo against: name + About line, topics (max 20, matching the big repos' topics), README top screen,
   30-second quick start, social preview 1280x640, trust signals, community files and good first issues,
   an "use it with your AI agent" section, one-click try, a soft star ask. List fixes in priority order.
2. Rewrite the README top screen (pitch, demo placeholder, install, agent one-liner).
3. Suggest 20 topics and 5 search queries to find active awesome lists and ecosystem/showcase pages for my big repos.
   Draft one awesome-list PR description (objective, no hype).
4. Write the message to my own circle that asks for usage feedback, not stars.
5. Pick 1-2 launch places that fit my users (developers vs vibe coders) and draft the post for each.
6. Give me a 7-day calendar and a weekly Level 3 routine. Flag anything that could break GitHub's rules or a
   community's self-promotion rules.
````

## Example output

> **Illustrative example.** Fictional repo and numbers, shown for format.

*figma2swiftui* (CLI + Claude Code plugin), owner of a 3,000-member iOS dev Facebook group.

| Day | Action | New stars (cumulative) |
|---|---|---|
| Before | Topics now match `figma`, `swiftui`, `ios`, `design-to-code`; demo GIF; "Use with Claude Code" one-liner | 4 |
| 1 | Build-log post in own group: "try it on one screen, tell me what broke" → 14 bug reports | 41 |
| 3 | PRs to 3 awesome lists (2 merged in a week); listed in a Figma plugin community thread | 63 |
| 4 | AlternativeTo: alternative to two paid design-to-code tools | 68 |
| 6 | Show HN (developers) + 40-second X video "Figma → SwiftUI in one prompt" (vibe coders) | 212 |
| 14 | Two releases, 3 outside PRs from `good first issue` | 287 |

**Keep:** own group (best bug reports), X video (most vibe-coder installs), awesome lists (steady trickle).
**Drop:** dev.to cross-post (few visits).

## Common mistakes
- **Buying or trading stars.** It breaks GitHub's policies, detection tools flag it, and it doesn't bring a single user.
- **Launching with a weak README.** You get one first impression per community. Fix Level 1 before any post.
- **Asking the group to "star this"** instead of "try this". You get stars that never come back, and no feedback.
- **Spamming big repos' issues with your link.** Maintainers block you and the community remembers.
- **Only reaching git users.** If vibe coders are your users, a demo video and an agent one-liner beat a perfect CONTRIBUTING.md.
- **Posting everywhere on different days.** One focused spike does more for trending than seven small ones.

## Related skills
- [launch-post-writing](../launch-post-writing/SKILL.md): the Show HN / Reddit / X posts for your launch spike.
- [listing-ai-product](../../listing/listing-ai-product/SKILL.md): if the repo is an agent skill, plugin or MCP server.
- [listing-dev-plugin](../../listing/listing-dev-plugin/SKILL.md): if it's an editor or tool plugin with its own store.
- [research-where-users-ask](../../research/research-where-users-ask/SKILL.md): find the threads and communities to answer in.
- [launch-get-first-100-users](../launch-get-first-100-users/SKILL.md): one-by-one outreach after the first stars.

## Credits
Written by [@nvminhtu](https://github.com/nvminhtu). Sources: GitHub,
[Acceptable Use Policies](https://docs.github.com/en/site-policy/acceptable-use-policies/github-acceptable-use-policies) (section 4);
GitHub Docs on [topics](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/classifying-your-repository-with-topics)
and [social preview images](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/customizing-your-repositorys-social-media-preview);
[sindresorhus/awesome](https://github.com/sindresorhus/awesome) PR requirements; He et al.,
"(Suspected) Fake Stars in GitHub" ([arXiv 2412.13459](https://arxiv.org/abs/2412.13459)); [Hacktoberfest](https://hacktoberfest.com/).
