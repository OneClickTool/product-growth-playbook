---
name: aso-keyword-research
description: Build a prioritized App Store / Google Play keyword list for an app and turn it into a ready-to-paste title, subtitle and 100-character keyword field. Use when launching a new app, when downloads from search are flat, when localizing a listing, or when someone asks "what keywords should my app target", "ASO keywords", "fill the keyword field", or "why doesn't my app show up in search".
license: MIT
metadata:
  category: aso
  difficulty: beginner
  time: 45-60 min
  version: 1.0.0
  author: nvminhtu
---

# ASO Keyword Research

> In under an hour you will have a scored keyword sheet and a title, subtitle and keyword field you can paste
> into App Store Connect (or a title and short description for Google Play).

## Goal
Pick the handful of search terms your app can realistically rank for *now*, and place them where the store
actually indexes them. A new app does better ranking #3 for a narrow term than #180 for a broad one.

## When to use
- Before the first release, or before a big listing update.
- Search installs are flat even though the app itself is good.
- Adding a new country or language.
- **Not for:** writing the title copy itself → [aso-title-subtitle-optimization](../aso-title-subtitle-optimization/SKILL.md).
  Visuals → [aso-screenshot-strategy](../aso-screenshot-strategy/SKILL.md).

## Inputs
- A one-paragraph description of the app and who it is for.
- 3–5 direct competitors (store links).
- 20–50 competitor reviews (1–3★ and 5★), which show the words real users use.
- Optional: keyword popularity and difficulty from any ASO tool. Apple Search Ads shows popularity for free
  once you have an account. Astro, AppFigures, AppTweak and Sensor Tower show both.
  With no tool you can still do steps 1–3 and 5–6 and use store autocomplete as the popularity signal.

## Where the stores read keywords

| Field | App Store | Google Play |
|---|---|---|
| Title / app name | 30 chars, strongest weight | 30 chars, strongest weight |
| Subtitle / short description | Subtitle 30 chars, indexed | Short description 80 chars, indexed |
| Keyword field | 100 chars, comma-separated, **hidden**, indexed | none |
| Long description | **not** indexed for search | 4,000 chars, **indexed** (natural language, no stuffing) |
| In-app purchase names | indexed | indexed |

On iOS each word only needs to appear **once** across title, subtitle and keyword field. The store combines
them into phrases, so "habit" in the title plus "tracker" in the keywords can rank for "habit tracker".

## Steps

1. **Seed list (10 min).** Write 20–30 words and phrases a user would type *before they know your app
   exists*: the problem ("stop procrastinating"), the job ("track water"), the category noun ("planner"),
   the audience ("for adhd"). Pull at least 5 of them word-for-word from competitor reviews.
2. **Expand (10 min).** Type each seed into the App Store / Play search box and write down every
   autocomplete suggestion. Add the words from competitors' titles and subtitles. Aim for 60–100 candidates.
3. **Cut for relevance (5 min).** Score each 1–5: *would someone who typed this be happy to find my app?*
   Drop everything below 3. Drop competitor brand names (Apple rejects them) and filler words: `app`, `free`,
   `the`, `and`, and your category name (you are already indexed for it).
4. **Measure (10 min).** For each survivor, record *popularity* (search volume) and *difficulty*
   (how strong the top 10 results are). With no tool, open the search results: if the top 5 apps each have
   more than 10k ratings, treat the keyword as hard for a new app.
5. **Score and pick (5 min).** `score = relevance × popularity ÷ difficulty` (any consistent scale).
   Sort. For an app with fewer than ~100 ratings, favour **long-tail** terms (low difficulty, relevance 5)
   over the highest popularity.
6. **Place (10 min).**
   - Title: brand + the single most valuable phrase.
   - Subtitle: the next 1–2 phrases, written for humans (it shows in search results).
   - Keyword field: everything else, as **single words**, comma-separated, **no spaces**, no words that
     already appear in the title or subtitle, no plurals of words you already have.
     `scripts/pack_keywords.py` does this packing and dedup for you.
   - Google Play: put the phrases in the title and short description, and use each target phrase 2–4 times
     naturally in the long description.
7. **Track (ongoing).** Record your rank for the top 10 keywords now, and again 2 and 4 weeks after the
   update goes live. Replace keywords where you are still outside the top 50 after 4 weeks.

Use `assets/keyword-sheet.csv` as the working sheet.

## Prompt (copy-paste)
Paste into Claude, ChatGPT, Gemini or Cursor. Replace everything in `{{ }}`.

````text
You are an App Store Optimization specialist. Help me research keywords for my app.

App: {{one-paragraph description, who it is for, main features}}
Store(s): {{App Store / Google Play / both}}   Country + language: {{e.g. US English}}
Competitors: {{3-5 app names or links}}
Words users use in competitor reviews: {{paste 20-50 review snippets}}
Current ratings count: {{number}}
Keyword data (optional): {{paste popularity / difficulty export, or "none"}}

Do this, in order:
1. Seed list: 25 phrases a user would search BEFORE knowing my app exists (problem, job, audience, category).
   Mark which ones come from the reviews.
2. Expand to 60+ candidates using likely store autocomplete variations and competitor titles/subtitles.
3. Score each 1-5 for relevance and drop anything below 3. Drop brand names and the words:
   app, free, the, and, my category name.
4. For each survivor estimate popularity (1-5) and difficulty (1-5). If I gave data, use it instead.
   Say clearly which numbers are estimates.
5. score = relevance * popularity / difficulty. Return a table sorted by score.
   Because I have {{ratings}} ratings, favour low-difficulty long-tail terms.
6. Propose:
   - Title (max 30 chars, incl. brand "{{brand}}")
   - Subtitle (max 30 chars, readable by humans)
   - iOS keyword field (max 100 chars, single words, comma-separated, no spaces,
     no word repeated from title/subtitle)
   - Google Play short description (max 80 chars)
   Show the character count for each.
7. List the 10 keywords I should track, and what would make you swap each one out after 4 weeks.
````

## Example output

> **Illustrative example.** Fictional app, numbers made up to show the format. Replace with a real case.

App: *Sipwell*, a water-intake reminder for office workers · US English · 40 ratings.

| Keyword | Rel | Pop | Diff | Score | Placement |
|---|---|---|---|---|---|
| water reminder | 5 | 4 | 3 | 6.7 | title |
| drink water tracker | 5 | 3 | 2 | 7.5 | subtitle ("drink", "tracker") + title ("water") |
| hydration | 5 | 3 | 3 | 5.0 | subtitle |
| water log | 4 | 2 | 1 | 8.0 | "log" in subtitle + "water" in title |
| daily water intake | 5 | 2 | 2 | 5.0 | keywords ("daily", "intake") |
| water tracker | 5 | 5 | 5 | 5.0 | already covered by title + subtitle words |
| habit tracker | 2 | 5 | 5 | 2.0 | dropped (relevance) |

Output of `scripts/pack_keywords.py`:

```text
Title    ( 23/30): Sipwell: Water Reminder
Subtitle ( 29/30): Drink Tracker & Hydration Log
Keywords ( 98/100): daily,intake,hydrate,bottle,cup,goal,health,alert,ounce,ml,fluid,sip,office,work,body,thirst,glass
Did not fit: schedule, electrolyte, caffeine
```

Four weeks later: #4 for "water log", #11 for "drink water tracker", still outside the top 100 for
"hydration". So the next update tests "electrolyte" and "caffeine" in place of the weakest keyword-field words.

## Common mistakes
- **Chasing the biggest keyword.** "water tracker" is worth nothing if you rank #150. Win narrow terms first;
  ratings and downloads then lift you on broad ones.
- **Spaces and repeats in the keyword field.** `water, reminder` wastes a character per comma, and repeating
  "water" (already in the title) wastes 6. Every character is one more word you could rank for.
- **Plurals and duplicates.** Apple matches most singular/plural forms, so pick one.
- **Stuffing the Google Play description.** A keyword in every sentence reads as spam and can get the
  listing rejected. Use each target phrase 2–4 times, naturally.
- **Never re-checking.** Rankings take 1–4 weeks to settle. Keyword research is a loop you run every
  update, not a one-time task.

## Related skills
- [aso-title-subtitle-optimization](../aso-title-subtitle-optimization/SKILL.md): turn the chosen phrases into copy that converts.
- [aso-screenshot-strategy](../aso-screenshot-strategy/SKILL.md): the visuals people see next to your title.
- [growth](../../growth/SKILL.md): pick the next skill for your stage.

## Credits
Written by [@nvminhtu](https://github.com/nvminhtu). Field limits from Apple's App Store Connect help
("Product page") and Google Play Console help ("Store listing"). Check both before a release, because
limits do change.
