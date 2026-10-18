# Tools for the daily X flow

Which step of the day each tool is for: [a-day-on-x.md](a-day-on-x.md).

Rule for every tool: it may help you **write, schedule, record and measure**. It may not reply, like, follow or DM
for you, or script the X website ([X automation rules](https://help.x.com/en/rules-and-policies/x-automation)).
Check each tool's current X support and price yourself; they change.

## Built into X

| Tool | Use it for | Tier |
|---|---|---|
| X composer (web) | Write, schedule your own posts, polls | All |
| X analytics | Impressions, profile visits, link clicks per post | Check your account |
| Edit post | Fix typos within 1 hour | Basic and up |
| Long posts | Saturday how-tos | Basic and up |
| Media Studio (studio.x.com) | Keep demo clips to reuse | Premium and up |
| X Pro | Several live columns (targets list, mentions, search) for the reply session | Premium+ |
| Lists (free) | A private list of reply targets; open it each morning | All |

Source for tiers: [About X Premium](https://help.x.com/en/using-x/x-premium).

## Outside tools (free or common)

| Need | Options | Note |
|---|---|---|
| Write with an agent | [Claude Code](https://claude.com/claude-code) / [Codex](https://openai.com/codex/) + `/social-x` from [../skills/](../skills/), [sergebulaev/x-skills](https://github.com/sergebulaev/x-skills) | Keep the approve-before-post step |
| Schedule (if not using X's own) | Tools that post via the official X API, e.g. [Buffer](https://buffer.com), [Typefully](https://typefully.com) | Scheduling your own original posts is allowed; skip "auto-engage" features |
| Reply-target list | [X Lists](https://help.x.com/en/using-x/x-lists) (private), [X Pro](https://pro.x.com) columns (Premium+) | Open it at 08:05 and 17:35 |
| Niche groups | [X Communities](https://help.x.com/en/using-x/communities) | Read the rules before posting |
| Demo captions / trims | iMovie, [CapCut](https://www.capcut.com), [Descript](https://www.descript.com) | 10–30 s, captions burned in |
| Screen recording (Mac) | ⇧⌘5 screenshot toolbar, QuickTime | 10–30 s, captions on |
| Screen recording (iPhone / Android) | Built-in screen recorder | Crop status bar personal info |
| UTM links | [Google Campaign URL Builder](https://ga-dev-tools.google/campaign-url-builder/) | Or follow the pattern in [resources/README.md](../resources/README.md) |
| App Store install source | App Store Connect campaign links (`pt`, `ct`) | See which posts drive installs |
| Analytics | GA4, Plausible, or your store's dashboard | Filter `utm_source=x` |
| Ranker updates | Watch [xai-org/x-algorithm](https://github.com/xai-org/x-algorithm) releases | Monthly check |

## Tools the maintainer builds

> Disclosure: these are made by the maintainer of this repo. Free ones are free; paid ones say so.

| Tool | Use in this flow | Status |
|---|---|---|
| [Promo Desk](https://oneclicktool.app/macos/promo-desk?utm_source=github&utm_campaign=growth-playbook&utm_content=x-marketing) | Mac app that reads your repo's launch posts as a checklist by date; an X tab (Today / Week / Replies / copy buttons) is planned | In development, $9.99 once |
| [Markdown Everywhere](https://oneclicktool.app/desktop/markdown-everywhere?utm_source=github&utm_campaign=growth-playbook&utm_content=x-marketing) | Open this `x-marketing/` folder (and your post files) as a table to read and copy | Free, Mac & Windows |
| [TapRec](https://github.com/nvminhtu/taprec#readme) | Record Android app demos for Monday posts, trim and caption them | Free, Android |
| [Reel Desk](https://oneclicktool.app/desktop/reeldesk?utm_source=github&utm_campaign=growth-playbook&utm_content=x-marketing) | Script → hook → post for short videos you can reuse on X | In development |
