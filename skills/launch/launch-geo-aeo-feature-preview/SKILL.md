---
name: launch-geo-aeo-feature-preview
description: Use GEO (generative engine optimization) and AEO (answer engine optimization) to promote features you haven't built yet. Turns real user questions into honest feature preview pages with design mockups and a design review log, written so Google AI Overviews, ChatGPT search, Perplexity, Copilot and Claude can find, quote and cite them, then tracks daily traffic, AI referrals and waitlist sign-ups to decide build / rework / drop (with a script). Includes a learning guide to GEO and AEO from official docs and research. Use when someone says "GEO", "AEO", "AI SEO", "get cited by ChatGPT", "show up in AI Overviews", "LLM optimization", "promote a feature before building it", "validate a feature with a landing page", "coming soon page for a feature", "mockup page SEO", "fake door test", or wants to judge demand by daily traffic growth before writing code.
license: MIT
metadata:
  category: launch
  difficulty: intermediate
  time: 2-3 h setup + 10 min/day
  version: 1.0.0
  author: nvminhtu
---

# GEO & AEO for Feature Previews

> In an afternoon you will have 1–3 honest preview pages for features you're designing, set up so search and AI
> engines can cite them, plus a daily log that tells you after 28 days which feature to build.

## Goal
Find out which features people want **before** you build them, by publishing one preview page per feature (problem,
mockups, design decisions, waitlist) that answers real questions well enough to be found in Google and quoted by AI
assistants. The finished output is: the pages, a tracking setup, and a build / rework / drop call per feature
backed by your own traffic and sign-up numbers.

New to GEO and AEO? Read the [learning guide](references/geo-aeo-learning-guide.md) first (40 min). It covers the
terms, how AI answers pick sources, what Google, OpenAI, Perplexity, Anthropic and Bing officially say, the GEO
research, crawler setup and how to read daily numbers.

## When to use
- You have mockups or a design review, no code yet, and want demand evidence before building.
- You want the product to show up in AI answers ("best app for…", "how do I…") from day one.
- You have a site (even a one-page one) where you can publish pages and edit robots.txt.
- **Not for:** a live product that needs store installs → [aso-keyword-research](../../aso/aso-keyword-research/SKILL.md).
  Finding the questions in the first place → [research-where-users-ask](../../research/research-where-users-ask/SKILL.md).
  A full launch checklist → [launch-pre-launch-checklist](../launch-pre-launch-checklist/SKILL.md).

## Inputs
- 1–3 features you are designing, each with at least one mockup (Figma export, screenshot of a prototype).
- Notes from your design review: decisions, what you cut, open questions.
- 10+ real questions or complaints about the problem (threads, reviews, autocomplete). No questions → do
  [research-where-users-ask](../../research/research-where-users-ask/SKILL.md) first.
- Access to your site, Google Search Console, Bing Webmaster Tools and GA4 (all free).
- A waitlist form ([email-list-and-deliverability](../../email/email-list-and-deliverability/SKILL.md) if you have none).

## Steps
1. **Set up measurement before publishing (30 min).** This is day 0 of your log; without a baseline you can't tell
   growth from noise.
   - Verify the site in [Google Search Console](https://search.google.com/search-console) and [Bing Webmaster Tools](https://www.bing.com/webmasters) (Bing has an *AI Performance* report of Copilot citations).
   - In GA4, add a custom channel **"AI assistants"** above *Referral* (regex in the
     [guide, section 8](references/geo-aeo-learning-guide.md#8-measuring-it-day-by-day)), and a key event on the
     waitlist form with the feature name.
   - Copy [assets/daily-traffic-log.csv](assets/daily-traffic-log.csv) (the rows in it are illustrative; delete them) and log the last 7 days as baseline.
2. **Open the door to crawlers (10 min).** robots.txt allows `Googlebot`, `Bingbot`, `OAI-SearchBot`,
   `PerplexityBot`, `Claude-SearchBot`; training bots (`GPTBot`, `ClaudeBot`, `Google-Extended`) are your choice.
   Check your host's bot protection doesn't block them. Pages must be in the sitemap and not `noindex`.
3. **Pick the question per feature (20 min).** From your collected questions, choose the one **main question** per
   feature and 4–6 sub-questions (pricing, platform, "vs X", "does it…"). These are your H1 and H2s. Write them in
   the users' words, not your feature name. Before writing, ask ChatGPT (search on), Perplexity and Google the main
   question and note who is cited: that's your competition and your outreach list.
4. **Write one preview page per feature (40 min each).** Use the
   [template](references/feature-preview-page-template.md): status line ("In design · not available yet"), a
   40–60 word short answer, question H2s with the answer first, labelled mockups, a "vs. today" table with cited
   facts, the design decisions from your review, what it won't do, an FAQ, and **one** action (waitlist or vote).
   Add owned facts: a number from a prototype test, a quote from your designer or a tester (real, with permission).
5. **Run the honesty check (5 min).** No Download / Buy / Trial buttons, no reviews or user counts you don't have,
   every image labelled *Design mockup*, no near-duplicate pages per keyword. These break Google's spam policies
   (misleading functionality, doorway, scaled content) and the FTC reviews rule; see the
   [guide, section 6](references/geo-aeo-learning-guide.md#6-geo-before-the-product-exists).
6. **Publish and get indexed (15 min).** Link each page from the home page or a `/roadmap` page, submit the sitemap,
   request indexing in Search Console (URL Inspection) and Bing (URL Submission). Write the publish date in the log.
7. **Build presence in 3 places in week 1 (60 min).** AI engines cite other sites too. Answer 3–5 real threads
   where the question lives (link only where it helps, disclose it's yours), post a 30-second mockup walk-through with
   captions, and list the product in 1–2 directories that already show up for the question. UTM-tag every link.
8. **Log daily, read weekly (10 min/day, 15 min/week).** Each day add visits by page and source plus sign-ups.
   Each week run the prompt check (5 prompts × 3 runs × ChatGPT, Perplexity, Google; record "mentioned 1/3") and:
   ```bash
   python3 scripts/traffic_trend.py daily-traffic-log.csv --start 2026-10-01
   ```
   It compares the latest 7 days with the 7-day baseline, splits search / AI / social / direct, shows the 7-day
   rolling average and sign-ups per 100 visits per page. Change one thing per page per week and log the date.
9. **Decide at day 28.** Per feature: **build** (traffic growing and people sign up), **rework the page** (flat
   traffic: the question or short answer is off), **rethink the feature** (traffic but no sign-ups), or **drop**.
   The script's thresholds (3 visits/day minimum, +10% vs baseline, 2 sign-ups per 100 visits) are this repo's
   starting rules of thumb, not industry benchmarks: tune them to your niche. Email the waitlist the decision.

## Prompt (copy-paste)
Works in Claude, ChatGPT, Gemini, Cursor. Replace everything in `{{ }}`. Attach mockups if the tool accepts images.

````text
You are a GEO/AEO editor for a small software team. We are promoting a feature we have NOT built yet.
Write an honest feature preview page that search engines and AI assistants (Google AI Overviews, ChatGPT search,
Perplexity, Copilot) can find, quote and cite.

Product: {{product, platform, who it's for}}
Feature: {{name + one line}}
Status: in design, target {{month year}}
Real user questions (verbatim, with links where public): {{10+ questions}}
Design review notes: {{decisions, what we cut, open questions}}
Mockups: {{list what each mockup shows}}
Facts we own: {{prototype test numbers, quotes with names and permission; or "none yet"}}
What people use today: {{competitors / workarounds, with source links}}
Waitlist URL: {{url}}

Do this:
1. Pick the ONE main question for the H1 and 4-6 sub-questions for H2s, in the users' words. Explain the choice in 2 lines.
2. Write the page in Markdown:
   - Status line at the top: "In design · not available yet", target month, last updated date, author.
   - "The short answer": 40-60 words that make sense on their own.
   - Each H2 is a question; the first sentence under it answers it directly.
   - A comparison table vs. what people use today, with every outside fact linked to its source.
   - "Design decisions so far" from the review notes, and "What it won't do (yet)".
   - FAQ (availability, price, platform), then one call to action: join the waitlist or vote.
   - Mark every image "Design mockup".
3. Rules: no Download/Buy/Trial buttons, no invented reviews, numbers, users or logos; if a fact is missing, write
   {{TODO: fact}} instead of guessing. No keyword stuffing. Write for a person first.
4. After the page, list: the title tag (under 60 chars), meta description (~150 chars), 5 prompts I should check
   weekly in AI assistants, and 3 places (threads, directories) where I should answer this question this week.
````

## Example output

> **Illustrative example.** Fictional product and made-up numbers to show the format.

*Snapsort*, a Mac photo organizer in design. Feature: batch rename. Page `/features/batch-rename`:

> **Status: In design · not available yet.** Planned for Feb 2027. Last updated 1 Oct 2026 by Linh, product designer.
>
> **The short answer.** Batch Rename will rename hundreds of photos on a Mac by date, place or camera in one step.
> Unlike Finder's rename, it shows every new file name before applying it and can undo the whole batch.
>
> **Can I rename photos by the date they were taken on Mac?** Yes, that's the default pattern…

Daily log, day 28, from `traffic_trend.py`:

| Page | Visits (last 7 d) | vs. baseline | AI visits | Sign-ups / 100 visits | Call |
|---|---|---|---|---|---|
| /features/batch-rename | 73 | +480% | 7 | 5.5 | Build: keep designing, interview 5 waitlist people |
| /features/smart-albums | 41 | +270% | 5 | 4.9 | Keep the page; test a sharper short answer |
| /features/cloud-sync | 9 | +12% | 0 | 0.0 | Rethink: people don't search for this |

Prompt check, week 4: "best app to batch rename photos on Mac", Perplexity: mentioned 1/3 (cited page:
/features/batch-rename); ChatGPT 0/3 (cites two Reddit threads → answer those).

## Common mistakes
- **"Download now" on a feature that doesn't exist.** It's misleading functionality to Google and to people. The
  only action is waitlist, vote or feedback.
- **Judging after 3 days.** New pages take days to weeks to be indexed and longer to be cited. Read the 7-day average
  and decide at day 28.
- **Changing five things at once.** One change per page per week, dated in the log, or you'll never know what worked.
- **Writing feature-name H2s ("Introducing SmartSort™").** Nobody asks that. Use the questions people type.
- **Only your own site.** AI answers lean on Reddit, reviews and directories. Without presence, you get read but
  not recommended.
- **Ignoring sign-ups.** Traffic says people look; sign-ups per 100 visits say they want it. Build on the second.
- **Trusting the AI-visits number as total.** Some assistants send no referrer; that traffic hides in *Direct*.

## Related skills
- [research-where-users-ask](../../research/research-where-users-ask/SKILL.md): collect the real questions first.
- [research-source-finding](../../research/research-source-finding/SKILL.md): cite facts you can trust on the page.
- [social-build-in-public](../../social/social-build-in-public/SKILL.md): share the mockups and design decisions as you go.
- [email-beta-program](../../email/email-beta-program/SKILL.md): turn the waitlist into beta testers when you build.
- [launch-pre-launch-checklist](../launch-pre-launch-checklist/SKILL.md): once a feature wins and has a date.

## Credits
Written by [@nvminhtu](https://github.com/nvminhtu). Sources: Google Search Central
([AI features and your website](https://developers.google.com/search/docs/appearance/ai-features),
[spam policies](https://developers.google.com/search/docs/essentials/spam-policies)),
[OpenAI crawlers](https://developers.openai.com/api/docs/bots), [Perplexity crawlers](https://docs.perplexity.ai/guides/bots),
[Anthropic crawlers](https://support.claude.com/en/articles/8896518-about-claude-s-web-crawler),
[Bing AI Performance](https://blogs.bing.com/webmaster/February-2026/Introducing-AI-Performance-in-Bing-Webmaster-Tools-Public-Preview),
Aggarwal et al., [GEO: Generative Engine Optimization](https://arxiv.org/abs/2311.09735) (KDD 2024), the
[FTC reviews rule](https://www.ftc.gov/news-events/news/press-releases/2024/08/federal-trade-commission-announces-final-rule-banning-fake-reviews-testimonials),
and the MIT-licensed `ai-seo` skill in [coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills).
Checked 18 Oct 2026; re-check the official pages each quarter.
