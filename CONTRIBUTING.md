# Contributing

Thanks for helping! This repo gets better with every real-world lesson people add.

## Ways to help
- **Improve a skill:** fix something that's wrong, add a missing step, or add a common mistake you've actually made.
- **Share a real example:** numbers from your own launch, ASO test or pricing change. Anonymize them if you need to.
- **Write a new skill:** first check the [roadmap](ROADMAP.md)
  and open issues, then open a *Skill request* issue so nobody duplicates work.
- **Test a skill:** run it on your product and leave feedback with the *Skill feedback* issue template.

## Adding a skill
1. Copy [SKILL_TEMPLATE.md](SKILL_TEMPLATE.md) to `skills/<area>/<area>-<task>/SKILL.md`.
   The folder name must equal the `name` field.
2. Put templates in `assets/`, long reference material in `references/`, and helper scripts in `scripts/`.
   Scripts must use the standard library only.
3. Add the skill to:
   - the `skills` list in [.claude-plugin/marketplace.json](.claude-plugin/marketplace.json)
   - the area's `README.md` table
   - the router table in [skills/growth/SKILL.md](skills/growth/SKILL.md)
   - the root [README.md](README.md)
4. Run `python3 scripts/validate_skills.py` and fix anything it reports.
   To eyeball how your new `SKILL.md` links to the others, open the `skills/` folder in
   [Markdown Viewer](https://oneclicktool.app/macos/markdown-viewer?utm_source=github&utm_medium=contributing&utm_campaign=growth-playbook&utm_content=link-map) and look at its link map (free, Mac, made by the maintainer).
5. Open a PR and complete the checklist.

## Definition of done
- [ ] `name` matches the folder. `description` says what the skill does **and when to use it** (≤ 1024 chars).
- [ ] Has every section: Goal · When to use · Inputs · Steps · Prompt · Example output · Common mistakes · Related skills.
- [ ] At least one copy-paste prompt, fenced with four backticks.
- [ ] The example output is real, or starts with an **Illustrative example** label.
- [ ] A reader can finish it in ≤ 1 hour and ends up with a concrete output.
- [ ] Every step is a concrete action. No generic tips.
- [ ] You ran it with at least one AI assistant on a real product.
- [ ] `SKILL.md` ≤ 500 lines. Validator passes.

## Style
- English, plain words, short sentences. Write for someone smart but new to the topic.
- Give numbers and limits (character counts, time frames, thresholds) and cite the source.
- If you mention your own product, say it's yours. At most one mention per skill, and only where it genuinely helps.

## Using an AI to write a skill
Welcome. [CLAUDE.md](CLAUDE.md) / [AGENTS.md](AGENTS.md) tell the agent the rules. You're still responsible
for every claim, so check the facts and test the prompt yourself.

## Review
Maintainers aim to respond within 48 hours. Please run `python3 scripts/validate_skills.py` before opening a PR; PRs that fail it will be sent back.
By contributing you agree that your contribution is licensed under the [MIT License](LICENSE) and that you
follow the [Code of Conduct](CODE_OF_CONDUCT.md).
