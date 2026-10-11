# Open-source X repos and skills worth knowing

Stars and last push from the GitHub API on **2026-10-11**. Stars measure popularity, not quality; read a repo's
code and licence before installing it, and never give a third-party tool your X password.

## Source of truth

| Repo | Stars | Licence | Why it matters |
|---|---|---|---|
| [xai-org/x-algorithm](https://github.com/xai-org/x-algorithm) | 33.6k | Apache-2.0 | The current For You ranker: weights, filters, visibility labels. Updated monthly-ish (last push 2026-10-09) |
| [twitter/the-algorithm](https://github.com/twitter/the-algorithm) | 74.0k | AGPL-3.0 | The 2023 Scala-era release. Historical; don't quote its numbers as current |

## Skills you can install in Claude Code / Codex

| Repo | Stars | Licence | What it does | Watch out |
|---|---|---|---|---|
| [coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills) | 54.1k | MIT | Large marketing skill set; `social`, `copywriting`, `launch`, `pricing`, `paywalls` are useful next to this skill | General marketing, not X-specific |
| [sergebulaev/x-skills](https://github.com/sergebulaev/x-skills) | 124 | MIT | 9 X skills: tweets and threads in your voice, hook extraction, replies and quotes, a weekly plan, AI-tell stripping, approve before publish | Publishing goes through a third-party service (Publora); trend data via Apify (paid) |
| [aaaronmiller/create-viral-content](https://github.com/aaaronmiller/create-viral-content) | 71 | none listed | Hooks, headlines and formatted posts for X, Reddit, LinkedIn, TikTok | No licence: you may read it, not reuse its text |
| [yamz8/x-thread-skill](https://github.com/yamz8/x-thread-skill) | 4 | MIT | Turns a technical project into a short human-sounding thread | Small and young |
| [PHY041/claude-skill-twitter](https://github.com/PHY041/claude-skill-twitter) | 5 | MIT | Growth, keyword monitoring, content strategy | Scrapes X while bypassing Cloudflare; scripting the X website breaks X's [automation rules](https://help.x.com/en/rules-and-policies/x-automation). Read-only ideas, don't run the scraper on your main account |
| [ceoguy/x-algorithm-skill](https://github.com/ceoguy/x-algorithm-skill) | 1 | MIT | Pre-flight checklist built from the open-source ranker | Very new; check its claims against the weights in [x-algorithm-and-premium-facts.md](x-algorithm-and-premium-facts.md) |

## Lists

- [BehiSecc/awesome-claude-skills](https://github.com/BehiSecc/awesome-claude-skills) (10.2k stars): curated list
  with a social media section. Check each entry's licence and whether it automates actions on X.

## How to pick
1. Want drafts in your voice with an approval step → `sergebulaev/x-skills`, plus this skill's fact bank so drafts stay true.
2. Want broader marketing (pricing, paywall, landing copy) → `coreyhaines31/marketingskills`.
3. Want to understand reach → read `xai-org/x-algorithm` README yourself; it's written for non-engineers too.
4. Skip anything that auto-replies, auto-DMs, auto-follows or scrapes the website.
