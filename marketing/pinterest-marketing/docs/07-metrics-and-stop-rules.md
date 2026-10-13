# 07 · Metrics and stop rules

Template: [templates/weekly-numbers.md](../templates/weekly-numbers.md). 10 minutes every Sunday, a real review monthly.

## What to track (and where)
Metric definitions from [Pinterest Help: Analytics](https://help.pinterest.com/en/business/article/pinterest-analytics).

| Metric | Means | Where | What it tells you |
|---|---|---|---|
| Impressions | Times your pins were on screen | Pinterest Analytics | Search is showing you (keywords work) |
| Saves | Times people saved your pin to a board | Pinterest Analytics | The image is worth keeping |
| Pin clicks | Clicks that open the pin close-up | Pinterest Analytics | The image raises interest |
| Outbound clicks | Actions that lead off Pinterest to your link | Pinterest Analytics | The promise is worth a visit |
| Visits `utm_source=pinterest` | Sessions on your site | GA4 / Plausible, by `utm_campaign` and `utm_content` | Which page and variant |
| Signups / trials / installs | Email, trial, install from those visits | Your analytics, checkout, store | Whether Pinterest brings **buyers** |

UTM pattern: `utm_source=pinterest&utm_medium=pin|profile&utm_campaign=<page>&utm_content=<variant>`.

## Stop and fix rules
- **Impressions near zero after 30 days:** the words are wrong or too broad. Redo the [keyword sheet](../templates/keyword-sheet.md),
  rename boards to search terms, put the term first in the title.
- **Impressions but few saves or clicks:** the image. Bigger headline, clearer result, less text; try another variant.
- **Pin clicks but few outbound clicks:** the pin promises something it doesn't show how to get. Add "free template",
  "steps inside", or a clearer call to action.
- **Outbound clicks but the visitors leave:** the page doesn't match the pin. Same headline at the top of the page,
  the promised thing first, the app second.
- **Visits but no signups:** no email box or no reason to give one. Offer the template or checklist by email.
- **90 days, steady pinning, still no outbound clicks worth counting:** Pinterest isn't the channel for this product.
  Keep the pins (they cost nothing) and move the time; see the [fit test](01-strategy.md#fit-test-yes-test-or-no).
