# 07 · Metrics and stop rules

Template: [templates/weekly-numbers.md](../templates/weekly-numbers.md). 10 minutes every Sunday.

## What to track (and where)

| Metric | Where | What it tells you |
|---|---|---|
| Views and reads per story | Medium story stats | Whether the title and first lines work (reads ÷ views) |
| Member reading time, earnings | Partner Program dashboard | Whether paying members read to the end |
| Followers gained | Medium audience stats | Whether readers want more from you |
| Accepted by a publication? Boosted? | Story page, publication emails | Whether editors rate the work |
| Site visits `utm_source=medium` | GA4 / Plausible, by `utm_campaign=<article-slug>` | Which article sends people |
| Trials / installs / signups from Medium | Store or checkout, same UTM | Which article sends **buyers** |
| Google clicks to the Medium story | Medium stats (external referrers) | Whether it ranks |

UTM pattern: `utm_source=medium&utm_medium=article|profile|newsletter&utm_campaign=<article-slug>`.

## Stop and fix rules
- **Read ratio low** (most viewers don't read): the title promises something the first lines don't deliver. Rewrite
  the first 3 lines.
- **Reads but no site visits:** the last paragraph doesn't give a reason to click. Link to a page that continues the
  article (a free template, the exact feature), not the home page.
- **Visits but no trials:** the landing page doesn't match the article. Send them to the matching feature page.
- **A story isn't distributed beyond your network:** check it against [08](08-rules-and-risks.md): too promotional,
  AI writing, or link-heavy.
- **8 articles, 0 publication acceptances:** your pitches are product stories. Switch to types 1–3 in
  [05](05-article-playbook.md).
- **10 weeks, under ~20 site visits from Medium in total and no follower growth:** Medium isn't where your buyers
  read. Keep importing your blog posts with canonical links (5 minutes each) and move the writing time to your main
  channel.
