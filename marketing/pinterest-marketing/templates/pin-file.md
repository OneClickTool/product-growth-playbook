# Pin file template

One file per pin set (one page), `marketing/pinterest/NN-<page-slug>.md` in the product's repo. Same frontmatter
fields as the other kits' post files (`where`, `stage`, `date`, `link`, `status`), plus Pinterest fields.

````markdown
---
where: Pinterest
page: {{https://your-site/page}}
terms: [{{main term}}, {{narrower term}}, {{problem term}}]
stage: share            # share | results | deal
date: {{YYYY-MM-DD}}
status: planned         # planned | scheduled YYYY-MM-DD | posted YYYY-MM-DD <pin URLs> | skipped
---
# {{NN}} — Pinterest · {{page title}}

> Promise of the page in one line: {{...}}. Check before posting: {{price, platform, "free" is true}}.

## Pin 1 · {{P01–P08 variant}}
- Board: {{board name}}
- Image: {{headline on the image}} · {{what the picture shows}} · file `{{pin-NN-1.png}}` (1000 × 1500)
- Title: {{term first, ≤ 100 chars, first 40 carry it}}
- Description: {{1–2 sentences, terms said naturally, call to action}}
- Link: {{page}}?utm_source=pinterest&utm_medium=pin&utm_campaign={{page-slug}}&utm_content={{variant}}

## Pin 2 · {{variant}}
{{same fields}}

## Result after 30 days
| Pin | Impressions | Saves | Outbound clicks | Visits (UTM) | Signups |
|---|---|---|---|---|---|
| 1 | | | | | |
````
