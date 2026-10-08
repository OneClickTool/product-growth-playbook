---
name: research-where-users-ask
description: Map and monitor the places where people ask for software recommendations, look for apps, utilities, extensions and alternatives, and share experiences with tools (subreddits, Q&A sites, alternative directories, forums, Hacker News, review sites, Vietnamese tech forums), with ready-made search queries and free alerts. Use when validating an idea, finding a niche, finding where to launch or answer questions, or when someone asks "where do people look for apps like mine", "where do users ask for software", "find alternatives to X threads", or "which communities should I join".
license: MIT
metadata:
  category: research
  difficulty: beginner
  time: 45-60 min
  version: 1.1.0
  author: nvminhtu
---

# Where Users Ask About Software

> In under an hour you will have a list of the 8–12 places where *your* users ask for tools, the exact threads to
> read, search queries you can reuse, and free alerts for new questions.

## Goal
Find the conversations where people say "I need an app that…", "what do you use for…", or "X is too expensive, any
alternative?". Those threads show real problems, the words people use, which competitors they mention, and where
to show up later (without spamming).

## When to use
- Validating an idea before building.
- Looking for a niche: what do people keep asking for and not finding?
- Choosing launch channels → [launch-post-writing](../../launch/launch-post-writing/SKILL.md).
- **Not for:** mining reviews of a specific competitor → [research-review-mining](../research-review-mining/SKILL.md).

## Inputs
- Your product or idea in one sentence, and its platform (Mac, Windows, iOS, Android, web, browser extension).
- 2–5 competitors or tools people currently use.
- The language and country of your users.

## The map: where people ask

**General "what software should I use"**

| Place | Good for | Link |
|---|---|---|
| r/software | Any desktop software recommendation | [reddit.com/r/software](https://www.reddit.com/r/software/) |
| Software Recommendations (Stack Exchange) | Precise requirement-based questions | [softwarerecs.stackexchange.com](https://softwarerecs.stackexchange.com/) |
| AlternativeTo | "Alternative to X", with likes and comments | [alternativeto.net](https://alternativeto.net/) |
| Ask HN | Developers and technical users asking what they use | [news.ycombinator.com/ask](https://news.ycombinator.com/ask) |
| Product Hunt | New tools, maker Q&A, "alternatives" pages | [producthunt.com](https://www.producthunt.com/) |
| Quora | Long-tail "best app for…" questions | [quora.com](https://www.quora.com/) |

**By platform**

| Platform | Places |
|---|---|
| Mac | [r/macapps](https://www.reddit.com/r/macapps/) · [MacRumors Forums](https://forums.macrumors.com/) · [MacUpdate](https://www.macupdate.com/) (user reviews) |
| Windows | [r/software](https://www.reddit.com/r/software/) · [r/Windows11](https://www.reddit.com/r/Windows11/) |
| iPhone / iPad | [r/iosapps](https://www.reddit.com/r/iosapps/) · [r/iphone](https://www.reddit.com/r/iphone/) · [r/AppHookup](https://www.reddit.com/r/AppHookup/) (deals, people comment on apps) |
| Android | [r/androidapps](https://www.reddit.com/r/androidapps/) · [XDA Forums](https://xdaforums.com/) |
| Browser extensions | [r/chrome_extensions](https://www.reddit.com/r/chrome_extensions/) · [r/chrome](https://www.reddit.com/r/chrome/) |
| Self-hosted / open source | [r/selfhosted](https://www.reddit.com/r/selfhosted/) · [r/opensource](https://www.reddit.com/r/opensource/) · [Lobsters](https://lobste.rs/) |
| Privacy-focused tools | [Privacy Guides forum](https://discuss.privacyguides.net/) · [r/privacy](https://www.reddit.com/r/privacy/) |

**By job or audience**

| Audience | Places |
|---|---|
| Productivity / notes / tasks | [r/productivity](https://www.reddit.com/r/productivity/) · [r/ObsidianMD](https://www.reddit.com/r/ObsidianMD/) · [r/Notion](https://www.reddit.com/r/Notion/) |
| AI tools | [r/ChatGPT](https://www.reddit.com/r/ChatGPT/) · [r/LocalLLaMA](https://www.reddit.com/r/LocalLLaMA/) · [r/ClaudeAI](https://www.reddit.com/r/ClaudeAI/) |
| Founders / SaaS buyers | [r/SaaS](https://www.reddit.com/r/SaaS/) · [r/Entrepreneur](https://www.reddit.com/r/Entrepreneur/) · [Indie Hackers](https://www.indiehackers.com/) |
| IT / sysadmins | [Spiceworks Community](https://community.spiceworks.com/) · [r/sysadmin](https://www.reddit.com/r/sysadmin/) |
| Business software buyers | [G2](https://www.g2.com/) · [Capterra](https://www.capterra.com/) (reviews + "alternatives" pages) |
| Vietnamese users | [Tinhte.vn](https://tinhte.vn/) · [VOZ](https://voz.vn/) · Facebook groups for your niche (search the group name + "phần mềm" / "app") |

Communities come and go, and rules change. Open each one and read its rules and recent posts before you rely on it.

## Steps
1. **Pick 8–12 places (10 min).** Take the general rows, your platform row and your audience row from the map.
   Add any niche forums or Discord servers your competitors mention on their sites.
2. **Search each one with the query bank (20 min).** Replace `X` with a competitor and `job` with what your product does:
   - `"alternative to X"` · `"X alternative"` · `"X is too expensive"` · `"switched from X"`
   - `"app for job"` · `"is there an app that"` · `"looking for a tool"` · `"what do you use for job"`
   - Across Reddit: `site:reddit.com "alternative to X"`. In a subreddit, use its own search sorted by *Top → Past year*.
   - Vietnamese: `"phần mềm" job` · `"app nào" job` · `"thay thế X"`.
3. **Save the best 15–20 threads (15 min).** For each: link, date, the question in the user's words, the tools
   people recommended, and the complaint behind the question. Store them in a research note
   ([research-doc-organization](../research-doc-organization/SKILL.md)).
4. **Look for patterns (10 min).** Which problem comes up again and again? Which competitor gets recommended, and
   which one gets complaints? Which exact words do people use? Those are your keywords and your landing-page headline.
5. **Set up free alerts (5 min).** [F5Bot](https://f5bot.com/) emails you when a keyword appears on Reddit or Hacker
   News. Google Alerts works for forums and blogs. Add your product name, competitors, and 2–3 "alternative to" phrases.
6. **Watch for event-driven waves (10 min).** A cheap new device, an OS end-of-support date or a popular product
   shutting down creates a crowd of new users at once. They rarely search "best apps for…". They search
   "how to <task> on <device>" or "<old product> alternative". Check Google Trends → *Related queries → Rising* for
   the event's name, and Google autocomplete for `<device> how to`, `how to <task> on <device>`. Each rising query is
   a question to answer (a help page, a short video) and, if the answer is "the OS can't do it well", a product.
7. **Participate the right way.** Answer questions helpfully, and mention your product only when it genuinely fits,
   saying that you made it. Follow each community's self-promotion rules. Many ban links from new accounts.

## Prompt (copy-paste)
Works best with web search turned on. Replace everything in `{{ }}`.

````text
You are a user-research assistant. Find where people ask for and talk about software like mine.

My product: {{one sentence}}   Platform: {{Mac / Windows / iOS / Android / web / extension}}
Competitors / current tools: {{2-5}}
Users' language + country: {{e.g. English, US; Vietnamese, VN}}

1. List the 10 best places (subreddits, Q&A sites, forums, directories, review sites, communities) where these users
   ask for recommendations or share experiences with tools like mine. For each: link, why it fits,
   and its self-promotion rules if known. Only list places you are confident exist. Mark uncertain ones.
2. Give me 15 search queries using operators (site:, "exact phrase") built from my competitors and my product's job,
   including "alternative to", "switched from", "is there an app that" patterns. Add local-language queries if needed.
3. If you can browse: find 10 real threads from the last 12 months. For each: link, date, the question in the
   user's words, what people recommended, and the underlying complaint. Never invent a link.
4. Summarize patterns: the top 3 unmet needs, the words users use, and the competitors that get praise vs complaints.
````

## Example output

> **Illustrative example.** Fictional product and threads, shown for format.

*Product:* a Mac menu-bar app that shows a checklist from pasted text. *Competitors:* Things, Todoist, Apple Reminders.

| Place | Thread (paraphrased) | Asked for | Recommended | Complaint behind it |
|---|---|---|---|---|
| r/macapps | "Lightweight to-do in the menu bar, no account?" | Menu bar, no sign-up | Reminders, Taska | Todoist needs an account |
| AlternativeTo | Things alternatives (comments) | Cheaper, one-time purchase | TickTick | Things is iOS + Mac, paid separately |
| Ask HN | "What do you use for daily checklists?" | Plain text, fast | text files, Obsidian | Apps are too heavy for simple lists |

**Pattern:** "no account", "menu bar", "just paste text" appear in 11 of 18 threads. That becomes the headline.

## Common mistakes
- **Drive-by self-promotion.** Posting your link in every "recommend an app" thread gets you banned and remembered badly.
- **Reading only the top answer.** The complaints are in the replies ("I tried X but…").
- **Old threads.** Software changes fast. Prefer the last 12 months and check dates.
- **Searching only "best apps for X".** First-time users type "how to …" questions. Track those too.
- **Counting upvotes as market size.** Threads show problems and words, not how many people will pay.

## Related skills
- [research-review-mining](../research-review-mining/SKILL.md): go deep on competitors' reviews.
- [research-doc-organization](../research-doc-organization/SKILL.md): store threads and patterns.
- [launch-get-first-100-users](../../launch/launch-get-first-100-users/SKILL.md): turn these places into your first users.
- [aso-keyword-research](../../aso/aso-keyword-research/SKILL.md): user words make good keywords.

## Credits
Written by [@nvminhtu](https://github.com/nvminhtu). Found a great community that's missing? Open a PR and add it to the map.
