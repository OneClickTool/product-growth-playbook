# Contributing

Thanks for helping! This repo gets better with every real-world lesson people add.
**You don't need to code**, and you don't need to have contributed to open source before.

## How this repo works (in 30 seconds)
- A **skill** is one Markdown file (`SKILL.md`) that teaches one growth task: goal, steps, a copy-paste AI prompt,
  and an example. Skills live in `skills/<area>/<skill-name>/`.
- **Areas** group skills: `research`, `case-study`, `listing`, `aso`, `launch`, `monetization`. Each area has a `README.md` listing its skills.
- **Playbooks** (`playbooks/`) chain several skills into a route, like a 6-week launch.
- Everything is plain text, so you can edit it right on GitHub.

## Pick how you want to help

| Time | What | How |
|---|---|---|
| 2 min | Star the repo | ⭐ at the top of the page |
| 5 min | Report what worked or didn't | Open a [Skill feedback](https://github.com/OneClickTool/product-growth-playbook/issues/new?template=skill-feedback.yml) issue |
| 10 min | Fix a typo, a broken link or an outdated rule | Open the file on GitHub → ✏️ *Edit* → *Propose changes* (GitHub makes the fork and PR for you) |
| 15 min | Add a community, source or tool to a list | Same ✏️ edit, e.g. the map in [research-where-users-ask](skills/research/research-where-users-ask/SKILL.md) |
| 30 min | Share a real example with numbers | Write a [case study](skills/case-study/case-study-write-your-own/SKILL.md), edit a skill's *Example output*, or open an issue and we'll add it with credit |
| 1–2 h | Write a new skill | Follow the guide below. Check the [roadmap](ROADMAP.md) for skills nobody has claimed |

Not sure? Ask in [Discussions](https://github.com/OneClickTool/product-growth-playbook/discussions). No question is too basic.

## Your first edit on GitHub (no tools needed)
1. Open the file you want to change on github.com.
2. Click the ✏️ pencil (*Edit this file*).
3. Make your change. The *Preview* tab shows how it will look.
4. Scroll down, write one line about what you changed, and click **Propose changes**, then **Create pull request**.
5. We'll review it within about 48 hours, and may suggest small edits. That's normal, not a rejection.

## Writing a new skill (step by step)
1. **Claim it.** Open a *Skill request* issue (or comment on an existing one) so nobody writes the same skill twice.
2. **Copy the template.** Create `skills/<area>/<area>-<task>/SKILL.md` from [SKILL_TEMPLATE.md](SKILL_TEMPLATE.md).
   The folder name must equal the `name` field, e.g. `skills/aso/aso-competitor-audit/SKILL.md`.
3. **Fill every section.** Goal · When to use · Inputs · Steps · Prompt · Example output · Common mistakes · Related skills.
   Look at [aso-keyword-research](skills/aso/aso-keyword-research/SKILL.md) as a model.
4. **Test it.** Run the prompt in an AI assistant on a real product. Does the output match your *Example output*?
5. **List it.** Add the skill to the area `README.md`. If you can, also add it to
   [.claude-plugin/marketplace.json](.claude-plugin/marketplace.json), the router in
   [skills/growth/SKILL.md](skills/growth/SKILL.md) and the root [README.md](README.md). If you can't, maintainers will.
6. **Check it (optional, needs Python 3).** Run `python3 scripts/validate_skills.py`. It checks names, sections and links.
   If you can't run it, just open the PR and we'll run it for you.
7. **Open a pull request** and tick the checklist.

Tip: to see how your skill links to the others, open the `skills/` folder in
[Markdown Viewer](https://oneclicktool.app/desktop/markdown-viewer?utm_source=github&utm_medium=contributing&utm_campaign=growth-playbook&utm_content=link-map)
(free, Mac, made by the maintainer) and look at the link map.

## When is a skill "done"?
- [ ] `name` matches the folder. `description` says what the skill does **and when to use it** ("Use when…").
- [ ] Every section is there, with at least one copy-paste prompt fenced with four backticks (` ```` `).
- [ ] The example is real, or starts with `> **Illustrative example.**`
- [ ] Someone new to the topic can finish it in about an hour and ends up with something concrete.
- [ ] Every step is an action ("Write 20 seed keywords"), not advice ("Think about keywords").
- [ ] Facts like store rules, limits and prices link to an official source.

## Style
- English, plain words, short sentences. Write for someone smart but new to the topic.
- Numbers beat adjectives: "30 characters", "2–4 weeks", "at least 12 testers".
- Mentioning your own product is fine if it genuinely helps: say it's yours, once, at the end.

## Using an AI to write or edit
Welcome. [CLAUDE.md](CLAUDE.md) / [AGENTS.md](AGENTS.md) give the agent the rules. You're still responsible for every
claim, so check the facts and test the prompt yourself.

## The fine print
By contributing you agree that your contribution is licensed under the [MIT License](LICENSE) and that you follow the
[Code of Conduct](CODE_OF_CONDUCT.md). Contributors are credited in the skill's `author` field and its *Credits* section.
