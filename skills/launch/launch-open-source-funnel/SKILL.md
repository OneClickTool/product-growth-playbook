---
name: launch-open-source-funnel
description: Use a free, open-source GitHub repo as the front door to a product: pick a model (open core, free tool → paid app, free CLI → hosted service, free template or playbook → paid product, sponsorware), decide what stays free forever, add honest hand-off points (README, docs, in-tool tips, release notes) that move users to a paid product or an email list, and measure which repo visitors become users with UTM links and GitHub traffic. Use when someone asks "how do I market with a free GitHub repo", "open source as marketing", "free repo to get customers", "open core model", "how do I monetize my open-source project", "turn GitHub stars into users", "lead magnet repo", "marketing GitHub repos free", "kéo khách bằng free repo", or has a repo with stars but no business behind it.
license: MIT
metadata:
  category: launch
  difficulty: intermediate
  time: "2-3 h to set up · 30 min per release"
  version: 1.0.0
  author: nvminhtu
---

# Open-Source Funnel: Free Repo In, Users Out

> A clear line between what's free and what's paid, 3–4 honest hand-off points in the repo, and links that show
> how many GitHub visitors become users or customers.

## Goal
A useful free repo earns trust before you ask for anything: developers and AI agents find it, try it in minutes, and
remember who made it. Stars alone don't pay the bills, though. This skill connects the repo to something
that does: a paid product, a hosted version, or at least an email list, without making the free part worse.

## When to use
- You have (or plan) a public repo that solves a real problem, and a product or service behind it.
- The repo gets stars and traffic, but you can't tell whether any of it turns into users or revenue.
- You want a marketing channel that costs time, not ad money, and keeps working after launch.
- **Not for:** getting the first stars → [launch-github-repo-seeding](../launch-github-repo-seeding/SKILL.md) (do that first
  or alongside). Publishing a plugin to a marketplace → [listing-dev-plugin](../../listing/listing-dev-plugin/SKILL.md).

## Inputs
- The repo (or the idea for it) and the product it should lead to.
- Who uses the repo: developers, vibe coders using AI agents, designers, makers…
- Your licence choice, or a willingness to pick one. See [choosealicense.com](https://choosealicense.com/).
- A landing page or store page for the paid product, and an email signup page.

## Steps
1. **Pick the model** that matches what you actually sell:

   | Model | Free repo | What people pay for (or join) | Works when |
   |---|---|---|---|
   | **Open core** | The full core tool | Team, cloud, enterprise or pro features | The core is useful alone; paid features matter to companies |
   | **Free tool → paid app** | A CLI, library or script | A polished app (Mac, iOS, web) doing the same job with a UI | Many users want the result without the terminal |
   | **Free CLI → hosted** | Self-hostable code | Hosting, backups, updates done for you | Running it yourself is a real chore |
   | **Free content → product** | A playbook, templates, skills, an awesome list | A related tool, course or service | The content shows expertise in the problem your product solves |
   | **Sponsorware / donations** | Everything | Sponsors get early access or nothing at all | You have a big, grateful user base; income is usually small |

2. **Write the free-forever line.** In the README, say plainly what is free and will stay free, and what isn't.
   Never move a free feature behind a paywall later without a long notice: it's the fastest way to lose the
   community (and invites a fork). If the licence allows commercial reuse, accept that someone may host it too.
3. **Add 3–4 hand-off points** where a user naturally needs the next step. Each one tells them what they get:
   - **README:** a short "Want X without Y? → [Product]" section after the quick start. Not a banner on top.
   - **Docs:** on the pages where the free tool hits its limit (scale, UI, team use), a one-line pointer.
   - **In the tool:** an optional, rare tip in the CLI output or app ("Tip: the hosted version backs this up
     automatically → link"), one that's easy to switch off. Never nag on every run.
   - **Releases:** release notes and a "subscribe to updates" link (email list → [strategy-product-as-funnel](../../strategy/strategy-product-as-funnel/SKILL.md)).
4. **Make the repo easy for AI agents too.** Many users now arrive through Cursor, Claude Code or Codex. A clear
   README, an `AGENTS.md`, and one-line install help agents set it up correctly, and agents surface the README's
   links to the user.
5. **Tag every link.** Add `?utm_source=github&utm_medium=readme&utm_campaign=<repo>&utm_content=<spot>` to each
   hand-off link, so your analytics show which spot works. Note GitHub *Insights → Traffic* (referrers and popular
   content, last 14 days only) every week.
6. **Give back visibly.** Answer issues quickly, credit contributors, ship small releases. The repo's reputation is
   the marketing, and a paid product next to a neglected repo looks like bait.
7. **Review monthly** in `growth/open-source-funnel.md`: repo visitors → hand-off clicks → sign-ups/installs → paid,
   per hand-off spot. Keep what converts; remove links nobody clicks.

## Prompt (copy-paste)
Works in Claude, ChatGPT, Gemini, Cursor. Replace everything in `{{ }}`.

````text
You are an open-source maintainer who also runs a profitable product. You keep the free part genuinely useful
and never suggest bait-and-switch, nagware, or hiding that a link is commercial.

Repo: {{name, what it does, stars, monthly visitors if known}}
Licence: {{MIT / Apache-2.0 / GPL / not chosen}}
Users: {{developers / vibe coders / designers / ...}}
The product it should lead to: {{what, price, link}} (or "not built yet")
My email list / updates page: {{link or none}}

1. Recommend the best model (open core, free tool → paid app, free CLI → hosted, free content → product,
   sponsorware) and explain why in 3 sentences.
2. Write the "free forever" paragraph for my README.
3. Write the copy for 3–4 hand-off points (README section, docs pointer, optional in-tool tip, release-notes
   line), each with a UTM-tagged link using utm_source=github and utm_content=<spot>.
4. Suggest one AGENTS.md section so AI agents install and use the repo correctly.
5. Give me a monthly review table: visitors, clicks per spot, sign-ups, paid.
````

## Example output

> **Illustrative example.** A fictional repo and numbers.

*`pdf-squeeze`: MIT-licensed CLI that compresses PDFs. Product: a $12 Mac app with drag-and-drop and batch folders.*

**Free forever:** "The CLI is MIT licensed and will stay free and fully featured. The Mac app is a paid, separate
product for people who prefer a window to a terminal."

| Hand-off spot | Copy | Clicks / month | Paid |
|---|---|---|---|
| README, after quick start | "Prefer drag-and-drop? There's a Mac app → link" | 410 | 23 |
| Docs: "batch folders" page | "Batch watch-folders are built into the Mac app" | 95 | 9 |
| CLI tip (once per 30 runs, `--no-tips` to hide) | "Tip: the Mac app does this from Finder" | 60 | 2 |
| Release notes | "Get release emails" | 140 sign-ups | — |

## Common mistakes
- **Crippling the free version** so people have to pay. Developers notice, and the stars stop.
- **A sales banner at the top of the README.** Show the value first; the hand-off goes after the quick start.
- **Untagged links.** Without UTM you'll never know if the repo sells anything.
- **Changing the licence suddenly** to block competitors. It breaks trust and often triggers a fork; decide early.
- **Nagging in the tool.** One rare, switch-off-able tip is fine; a message every run gets the repo uninstalled.
- **A neglected repo next to a polished paid product.** It reads as bait. Keep both alive or say the repo is archived.

## Related skills
- [launch-github-repo-seeding](../launch-github-repo-seeding/SKILL.md): get the first real stars and users.
- [strategy-product-as-funnel](../../strategy/strategy-product-as-funnel/SKILL.md): the same give-first idea across all your products.
- [strategy-contrarian-marketing](../../strategy/strategy-contrarian-marketing/SKILL.md): a free repo is one of the best "side doors".
- [listing-ai-product](../../listing/listing-ai-product/SKILL.md): if the repo is an agent skill or MCP server.

## Credits
Written by [@nvminhtu](https://github.com/nvminhtu). Licence guidance: [choosealicense.com](https://choosealicense.com/)
(by GitHub). Traffic data: GitHub repository *Insights → Traffic*.
