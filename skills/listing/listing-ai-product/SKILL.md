---
name: listing-ai-product
description: List a small AI product where AI users look (AI tool directories, the GPT Store, agent-skill directories like skills.sh and awesome lists, Claude Code plugin marketplaces, the MCP Registry), in three levels (1 get listed, 2 get found, 3 grow), with which directories still have free submission, how agent skills get indexed, and what makes an AI listing trustworthy. Use when launching an AI tool, a custom GPT, an agent skill or plugin, or an MCP server, or when someone asks "where do I list my AI tool", "free AI directories", "publish a GPT", "how do I get my skill on skills.sh", or "list my MCP server".
license: MIT
metadata:
  category: listing
  niche: AI tools, GPTs, agent skills, MCP servers
  difficulty: beginner → intermediate (3 levels)
  time: "Level 1: 1-2 h · Level 2: 1-2 h · Level 3: ongoing"
  version: 1.0.0
  author: nvminhtu
---

# AI Product Listing (AI tools · GPTs · Agent skills · MCP)

> AI users discover tools through directories, AI app stores and GitHub. List in the channels that match your
> product type, and prove it works with a demo.

## Goal
Get an AI product listed where people look for that *type* of AI product. A SaaS AI tool, a custom GPT, an agent
skill and an MCP server each have their own directories.

## When to use
- Launching an AI web tool, a custom GPT, an agent skill/plugin, or an MCP server.
- **Not for:** general launch platforms → [listing-free-directories](../listing-free-directories/SKILL.md) (do those too).

## Inputs
- The product type (web tool, custom GPT, agent skill/plugin, MCP server) and its link or repo.
- A 30-second demo with a real input → output, pricing, and one line about what happens to user data.

## Where to list, by product type

**AI web tools / SaaS**

| Directory | Free option? (checked 2026-09-30, may change) | Link |
|---|---|---|
| There's An AI For That | Free submission with a review queue reported, paid featuring | [theresanaiforthat.com](https://theresanaiforthat.com/) |
| Futurepedia | Free submission reported, featured placements paid | [futurepedia.io](https://www.futurepedia.io/) |
| Future Tools | Free submission form reported (curated) | [futuretools.io](https://www.futuretools.io/) |
| Toolify | Free basic tier reported | [toolify.ai](https://www.toolify.ai/) |
| Uneed, TinyLaunch, Product Hunt | Free options | → [listing-free-directories](../listing-free-directories/SKILL.md) |
| More directories | Community-maintained list | [best-of-ai/ai-directories](https://github.com/best-of-ai/ai-directories) |

Many AI directories charge to submit or to skip the queue. Check the price before filling the form, and skip paid ones
until the free channels have worked.

**Custom GPTs**

| Where | How | Link |
|---|---|---|
| GPT Store (ChatGPT) | Set the GPT to "Everyone" / publish to the store. Needs an eligible ChatGPT plan and a completed **builder profile** (verified domain or billing name) | [Sharing and publishing GPTs](https://help.openai.com/en/articles/8798878-building-and-publishing-a-gpt) |

**Agent skills and plugins** (Claude Code, Codex, Cursor, Gemini CLI…)

| Where | How | Link |
|---|---|---|
| skills.sh | No publish step: a public GitHub repo with `SKILL.md` files shows up once people install it with `npx skills add owner/repo` | [skills.sh](https://skills.sh/) · [vercel-labs/skills](https://github.com/vercel-labs/skills) |
| Claude Code plugin marketplace | Add `.claude-plugin/marketplace.json` to your repo. Users run `/plugin marketplace add owner/repo` (this repo does exactly that) | [Claude Code docs](https://docs.claude.com/en/docs/claude-code/plugin-marketplaces) |
| Awesome lists | Pull request, e.g. [VoltAgent/awesome-agent-skills](https://github.com/VoltAgent/awesome-agent-skills) | GitHub |

**MCP servers**

| Where | How | Link |
|---|---|---|
| Official MCP Registry | Publish server metadata with the registry's CLI | [registry.modelcontextprotocol.io](https://registry.modelcontextprotocol.io/) |
| Awesome MCP lists | Pull request | search GitHub `awesome mcp servers` |

## Steps

### Level 1: Get listed
1. **Name your type (1 min):** web tool, GPT, skill/plugin or MCP server. Use the matching table.
2. **Prepare the AI listing kit (45 min):** one-sentence use case ("Turns meeting audio into action items"), **a
   30-second demo video or GIF with a real input → output**, 3 screenshots, pricing (free / freemium / paid),
   which model(s) it uses if relevant, and a privacy note (what happens to user data or prompts).
3. **Submit to 3–5 free places** from your table, plus Level 1 of [listing-free-directories](../listing-free-directories/SKILL.md).
4. **For skills/plugins:** make installation one command (`npx skills add owner/repo`, `/plugin marketplace add owner/repo`)
   and put it at the top of the README.

### Level 2: Get found
1. **Pick precise categories** ("meeting notes", "SEO writing"), not just "AI".
2. **Show real outputs.** Before/after examples beat claims. AI directories are full of lookalikes.
3. **Be where AI users ask:** r/ChatGPT, r/ClaudeAI, r/LocalLLaMA, tool-specific Discords → [research-where-users-ask](../../research/research-where-users-ask/SKILL.md).
4. **GitHub topics** for skills and MCP servers (`agent-skills`, `claude-skills`, `mcp-server`) make the repo discoverable.

### Level 3: Grow
- **Update listings when models or features change.** Stale AI listings lose trust fast.
- **Comparison pages** ("X vs Y") on your site, and "alternative to" entries on AlternativeTo.
- **Case studies with real results** → [case-study-write-your-own](../../case-study/case-study-write-your-own/SKILL.md).
- **Paid featuring only after** you know your free-channel conversion rate.

## Prompt (copy-paste)
Replace everything in `{{ }}`.

````text
You are an AI product launch advisor. Help me list my AI product.

Product: {{what it does}}   Type: {{web tool / custom GPT / agent skill or plugin / MCP server}}
Repo or URL: {{...}}   Pricing: {{...}}   Models used: {{...}}   Data handling: {{...}}

1. Pick the 5-8 best places to list it for my type (AI directories, GPT Store, skills.sh, Claude Code plugin marketplace,
   awesome lists, MCP Registry, general launch platforms). Say which are free and remind me to verify the current pricing.
   Never claim a directory is free if you're not sure.
2. Write the AI listing kit: one-sentence use case, a 100-word description, 5 precise categories/tags, a shot list for a
   30-second demo (real input → output), and a privacy line.
3. For skills/plugins/MCP: the one-line install command and a README opening.
4. A 2-week submission schedule.
````

## Example output

> **Illustrative example.** Fictional product, shown for format.

*growth-skills* (a set of Claude/Codex agent skills on GitHub) → Level 1: `.claude-plugin/marketplace.json` + an `npx skills add`
line in the README (skills.sh indexes it on install), and a PR to an awesome agent-skills list. Level 2: GitHub topics
`agent-skills, claude-skills`, plus a post in r/ClaudeAI with a 30-second demo of one skill producing a keyword list.

## Common mistakes
- **"AI-powered everything" descriptions.** Say the one job it does, and show it.
- **Paying for featured spots first.** Free channels tell you whether the listing converts at all.
- **No privacy statement.** AI users want to know where their prompts and files go.
- **Skills that need a 10-step install.** Make it one command.

## Related skills
- [listing-free-directories](../listing-free-directories/SKILL.md): general free launch platforms.
- [listing-dev-plugin](../listing-dev-plugin/SKILL.md): if your AI product is an editor plugin.
- [case-study-competitor-teardown](../../case-study/case-study-competitor-teardown/SKILL.md): study the top AI tools in your category.

## Credits
Written by [@nvminhtu](https://github.com/nvminhtu). Sources: OpenAI Help, [Sharing and publishing GPTs](https://help.openai.com/en/articles/8798878-building-and-publishing-a-gpt);
[vercel-labs/skills](https://github.com/vercel-labs/skills); directory free tiers per their own sites and roundups
([ai-directories list](https://github.com/best-of-ai/ai-directories)). AI directories change pricing often, so verify before submitting.
