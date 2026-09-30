---
name: case-study-write-your-own
description: Turn your own launch, ASO test, pricing change or growth experiment into an honest, reusable case study with context, baseline, what you did, before/after numbers, what failed and lessons, following a template that others (and your future self) can learn from and that can be contributed to this repo. Use when an experiment or launch has finished, when writing a build-in-public post, when sharing results with a team, or when someone asks "write a case study", "document my results", "launch retrospective", or "post-mortem for my app".
license: MIT
metadata:
  category: case-study
  difficulty: beginner
  time: 45-60 min
  version: 1.0.0
  author: nvminhtu
---

# Write Your Own Case Study

> In under an hour you will have a one-page case study with real numbers, one you can reuse as a build-in-public
> post and contribute to this repo.

## Goal
Capture what you did and what happened while it's fresh: the context, the numbers and the lessons. You avoid repeating
mistakes, and others can learn from real data instead of guesses.

## When to use
- A launch, ASO update, pricing change or channel test has run long enough to judge (usually 2–4 weeks).
- You're writing a build-in-public or Indie Hackers post.
- You want to contribute a real example to this repo.
- **Not for:** studying other people's results → [case-study-success-story-analysis](../case-study-success-story-analysis/SKILL.md).

## Inputs
- What you changed, and when (dates).
- Numbers **before** and **after**, over the same length of time (downloads, conversion, revenue, ratings…).
- Anything else that happened at the same time (a feature, a holiday, a mention somewhere).
- `assets/case-study-template.md` from this skill.

## Steps
1. **Write the TL;DR last, but put it first.** Three lines: what you did, the key number, the lesson.
2. **Context (5 min).** Product, platform, price model, stage, and the **baseline** numbers before the change.
3. **Goal and hypothesis (5 min).** "We believed that *X* would improve *metric* because *reason*."
4. **What you did (10 min).** Dated steps, specific enough to repeat. Link the skill you used from this repo.
5. **Results (10 min).** A before/after table over **equal time windows**. Include the metrics that got worse, too.
6. **Honesty check (5 min).** List confounders: other changes, seasonality, press, small sample sizes.
   Say how confident you are (high / medium / low).
7. **What worked, what didn't, what you'd do differently (10 min).** Be specific. "Captions helped" is too vague;
   "Screenshot 1 with the outcome caption lifted conversion from 3.1% to 4.0%" is useful.
8. **Share it.** Keep it in your research folder, adapt it into a post ([launch-post-writing](../../launch/launch-post-writing/SKILL.md)),
   and consider contributing it (below).

### Contributing a case study to this repo
- Open a pull request adding `case-studies/YYYY-MM-<short-name>.md` based on the template, or open an issue and a
  maintainer will add it with credit to you.
- **Real numbers only.** You can anonymize the product name, round the numbers, or show percentages, but say that you did.
- Link the skills you used. Your case study becomes the real example for that skill.

## Prompt (copy-paste)
Replace everything in `{{ }}`.

````text
You are an editor helping me write an honest growth case study. Use only the facts I give you.

What I changed and when: {{dated steps}}
Product context: {{product, platform, price model, stage}}
Numbers before (dates): {{...}}   Numbers after (same-length window, dates): {{...}}
Other things that happened in the same period: {{...}}
What I think worked / didn't: {{...}}

Write the case study with these sections: TL;DR (3 lines) · Context and baseline · Goal and hypothesis ·
What we did (dated) · Results (before/after table, equal windows, include metrics that got worse) ·
Confounders and confidence (high/medium/low) · What worked · What didn't · What I'd do differently ·
Skills used. Keep it under 600 words. Don't add numbers I didn't give you. Mark gaps as TODO.
````

## Example output

> **Illustrative example.** A fictional case, shown for format. Replace with your real one.

**TL;DR:** We rewrote the first 3 App Store screenshots around outcomes instead of features. Store conversion went from
3.1% to 4.0% over 4 weeks. Captions that name the outcome beat captions that list features.

| Metric (28 days) | Before (1–28 Aug) | After (4 Sep–1 Oct) | Change |
|---|---|---|---|
| Product page views | 12,400 | 12,900 | +4% |
| Conversion rate | 3.1% | 4.0% | +0.9 pts |
| Downloads | 384 | 516 | +34% |
| Day-7 retention | 22% | 21% | ≈ flat |

**Confounders:** a small iOS update shipped on 10 Sep (bug fixes only). No press. **Confidence:** medium.
**Skills used:** [aso-screenshot-strategy](../../aso/aso-screenshot-strategy/SKILL.md).

## Common mistakes
- **Unequal time windows,** such as comparing 7 days before with 30 days after.
- **Only reporting wins.** Metrics that got worse are part of the lesson, and they build trust.
- **No baseline.** "We got 500 downloads" means nothing without "we used to get 380".
- **Claiming causation from one noisy week.** State the confidence level and the confounders.

## Related skills
- [case-study-success-story-analysis](../case-study-success-story-analysis/SKILL.md): read other people's stories the same way.
- [research-doc-organization](../../research/research-doc-organization/SKILL.md): where to keep your case studies.
- [launch-post-writing](../../launch/launch-post-writing/SKILL.md): turn the case study into a post.

## Credits
Written by [@nvminhtu](https://github.com/nvminhtu).
