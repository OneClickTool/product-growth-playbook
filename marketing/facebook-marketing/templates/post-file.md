# Post file template

One file per post, `marketing/facebook/NN-<slug>.md` in the product's repo. Same frontmatter fields as the other
kits' post files (`where`, `stage`, `date`, `link`, `status`), plus Facebook fields.

````markdown
---
where: Facebook · {{group name | Page | profile}}
format: {{F01–F08}}
rules_checked: {{YYYY-MM-DD}}        # date you re-read the group's rules
admin_ok: {{yes | not needed | asked YYYY-MM-DD}}
stage: share            # share | results | deal
date: {{YYYY-MM-DD}}
link: {{https://your-site/page}}?utm_source=facebook&utm_medium={{group|page|profile}}&utm_campaign={{group-slug}}&utm_content={{F-code}}
status: planned         # planned | posted YYYY-MM-DD <post URL> | declined | removed | skipped
---
# {{NN}} — Facebook · {{group or Page}} · {{one-line topic}}

> Check before posting: {{price, platform, "free" is true}} · disclosure line present · link allowed here.

## Text
{{first line: the problem or result in the group's words, no product name}}

{{body: steps / story / images described}}

{{"I made <product>" + link if allowed}}

{{a real question to invite comments}}

## Images / video
{{file names, what each shows}}

## Result after 7 days
| Reactions | Comments | Clicks (UTM) | Signups | Admin / member feedback |
|---|---|---|---|---|
| | | | | |
````
