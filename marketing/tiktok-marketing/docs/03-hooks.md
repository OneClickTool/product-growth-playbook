# 03 · Hooks: the formula, what worked, what flopped

Slide 1 does most of the work. In the reference case, the same app, images and posting setup produced 234K views
with one hook and 879 with another. Change the hook before you change anything else.

## Real data (Snugly, Feb 2026, self-reported by Oliver Henry)
Source: [gameplaydev Substack step-by-step](https://gameplaydev.substack.com/p/how-his-openclaw-agent-larry-got).

| Hook | Views | Shape |
|---|---|---|
| "My landlord said I can't change anything so I showed her what AI thinks it could look like" | 234,000 | person + doubt → showed → changed |
| "I showed my mum what AI thinks our living room could be." | 167,000 | person + showed |
| "My landlord wouldn't let me decorate until I showed her these." | 147,000 | person + doubt → showed |
| "The difference between $500 and $5000 taste" | 2,671 | abstract idea |
| "Why does my flat look like a student loan" | 905 | self-focused joke |
| "See your room in 12+ styles before you commit" | 879 | feature list |

**Pattern:** the winners are a tiny story with a second person who doubts, and a reveal. The losers talk about the
product, the problem in general, or a feature. Per the same write-up, formula posts cleared ~50K and most reached
100K, while other posts struggled to reach 10K.

## The formula
```text
[another person] + [doubt / rule / conflict] + "so I showed them" + [what the app made] (+ they changed their mind)
```

Adapt it to your product. These are **starting points to test**, not proven results:

| Product | Hook to test |
|---|---|
| Room / decor AI | "My mum said our kitchen was hopeless so I showed her this" |
| Outfit / hair / makeup preview | "My sister said bangs would ruin my face so I showed her these first" |
| Fitness / habit | "My doctor said 10 minutes a day won't change anything. Day 1 vs day 60" |
| Language / study | "My teacher said I'd never pass. Here's the plan I used instead" |
| Relationship / LDR | "My friends said long distance never works. What we do every Sunday" |
| Faith / quotes / journaling | "I couldn't sleep, so I asked for a verse about worry" |
| Casual game | "My boyfriend said this level was impossible so I recorded it" |
| Budget / finance app | "My partner said we can't save on our salary so I showed him this" |

## Rules
- **A person and a moment, not your app.** Your app name never appears on slide 1.
- **Write the reaction, not a label.** "She asked for the link" beats "AI room makeover".
- **Short lines.** 4–6 words per line, 3–4 lines on the slide, line breaks by hand (Larry skill rules).
- **No emoji on the slide** if you render text with a script: canvas libraries often can't draw them.
- **Specific nouns.** "landlord", "mum", "my Dad's garage", not "someone", "a room".
- **Don't open with** "Did you know", "Here are 5 tips", "POV" with nothing after it, or a feature name.
- **Steal the shape, not the post.** Copy the structure of hooks you find in step 1 of the loop; never reuse someone's
  slides or images.

## Building a hook bank
Keep every hook with its numbers in [templates/hook-bank.md](../templates/hook-bank.md). Postiz's guide calls ~100
logged hooks a valuable asset (vendor claim, but the logic holds: winners turn into formulas, losers stop you
repeating mistakes). For each hook log: date, hook, formula, person, emotion, views, saves, profile visits, installs.

## Mining hooks from viral slideshows (manual)
1. Search TikTok with the words your user would type ("small bedroom ideas", "glow up", "study plan").
2. Open the top 20 slideshows from the last 30 days. Skip accounts with one lucky hit.
3. Write down only slide 1 text, slide count and views.
4. Ask an AI: *"For each hook: why it works (curiosity / pain / surprise / relatability), its structure, and 3
   variations for {{my product}} under 12 words, each with a person and a moment."*
