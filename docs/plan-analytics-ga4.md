# Plan: 📊 Analytics area — learn Google Analytics 4 and use it to grow traffic

> **Status: phase 1 done, phases 2–4 planned.** Phase 1 skills exist in [skills/analytics/](../skills/analytics/README.md). This is the build plan for the skill area
> `skills/analytics/`, written so a maintainer can review it before any skill is created and an AI agent can
> execute it phase by phase. Tick boxes as work lands. Last updated: 2026-10-19.

## Why

- The router ([skills/growth/SKILL.md](../skills/growth/SKILL.md)) says *"SEO, retention, analytics… the repo doesn't
  cover it yet"*. Analytics is the gap every other area depends on: the channel kits each have a
  `07-metrics-and-stop-rules.md`, [launch-growth-stack-setup](../skills/launch/launch-growth-stack-setup/SKILL.md) sets
  up Firebase for apps, and [launch-geo-aeo-feature-preview](../skills/launch/launch-geo-aeo-feature-preview/SKILL.md)
  adds an "AI assistants" channel in GA4. Nothing teaches how to **read** GA4 and turn it into more traffic.
- "Traffic to the roof" only happens when you know which pages and channels already work and push those harder.
  Without that, makers post everywhere and guess.

## Goal of the area

A maker with a website, landing page, blog or web app goes from *"GA4 is installed, I never open it"* to a
**weekly loop**: read 5 numbers → find the one lever with the most upside → run one change → check it next week.

"Grow traffic" is defined so it can be measured (no vanity numbers):

| Measure | Why this one | GA4 API name (verify against the API schema when writing) |
|---|---|---|
| Sessions by channel | Where traffic comes from | `sessions` × `sessionDefaultChannelGroup` |
| Engaged sessions | Traffic that actually read or clicked | `engagedSessions`, `engagementRate` |
| Key events | Traffic that did the thing you want (sign-up, store click, lead, purchase) | `keyEvents` |
| Landing pages | Which page brought them in | `landingPagePlusQueryString` |
| Organic queries | What people searched to find you (Search Console, not GA4) | GSC `query`, `page`, `clicks`, `impressions`, `ctr`, `position` |

**Not for:** in-app analytics of mobile apps (Firebase → `launch-growth-stack-setup`), paid ads optimisation
(→ [08-paid-ads-gate](../skills/growth/action/08-paid-ads-gate.md)), store installs (→ ASO area).

## AI-agent-ready rules (apply to every skill in the area)

These make the skills safe and repeatable when an agent (Claude Code, Cursor, Codex…) runs them, not only a human.

1. **Description = trigger list.** Each `description` names the task and the phrases people type: "GA4 setup",
   "why did traffic drop", "which pages bring traffic", "weekly analytics report", "Search Console queries",
   "grow website traffic", "key events", "UTM".
2. **Exact API names.** Every metric and dimension is written with its GA4 Data API name next to the UI label, so
   an agent can call the API/MCP without guessing. One shared file:
   `skills/analytics/analytics-agent-reporting/references/report-recipes.json` (named reports: dimensions, metrics,
   date range, filters, sort, limit).
3. **Decision tables, not prose.** Diagnosis rules are `if <signal> → then <action> → check <metric> in N days`.
4. **Fixed output templates** in `assets/` (weekly report, tracking plan, experiment log) so agent output is the
   same shape every week and diffable in git.
5. **Read-only by default.** Agent mode only *reads* reports (GA4 MCP `run_report`, `run_realtime_report`,
   `run_funnel_report`; Search Console MCP `get_search_analytics`…). Changing property settings, filters, key events
   or sitemaps needs the user's explicit yes, every time.
6. **No invented numbers.** If a report returns nothing, write "no data" and say why (date range, filter, consent).
   Examples with made-up numbers carry the `> **Illustrative example.**` label (repo rule).
7. **Official sources for limits.** Event/parameter limits, data retention, thresholds, consent mode behaviour and
   Search Console data delays are cited to Google's help/developer pages with the date checked.
8. **Stdlib scripts only.** Helpers in `scripts/` use the Python standard library and work on CSV exports, so the
   skills also work with no API access.

## Skills to build

Area: `skills/analytics/` · emoji 📊 · README table like the other areas.

| # | Skill (folder = `name`) | What you get | Level | Time |
|---|---|---|---|---|
| 1 | `analytics-ga4-setup` | A GA4 property set up right once: web stream, enhanced measurement, internal-traffic filter, cross-domain (if site + app/checkout domain), data retention, consent mode, Search Console link, verified in DebugView / Realtime | Beginner | 60–90 min |
| 2 | `analytics-tracking-plan` | A one-page tracking plan: 5–8 events, which are **key events**, parameter names, one UTM convention shared with the channel kits (`utm_source=x|reddit|tiktok|…`), custom dimensions, a test checklist | Beginner | 45–60 min |
| 3 | `analytics-ga4-reports-101` | The learning guide: the 6 reports that matter (Realtime, Traffic acquisition vs User acquisition, Pages & screens, Landing page, Events/Key events, Explorations), what each metric means in plain words, common misreadings | Beginner | 1–2 h (read + practice) |
| 4 | `analytics-traffic-diagnosis` | A weekly diagnosis: channel × landing page table, week-over-week change, Search Console "high impressions, low CTR" and "position 8–20" pages, AI-assistant referrals, a "why did traffic drop" checklist (tracking broke? seasonality? ranking? a channel stopped?) | Intermediate | 30 min/week |
| 5 | `analytics-traffic-growth-loop` | The "traffic to the roof" engine: pick levers **from the data** (refresh a page that ranks 8–20, rewrite titles with low CTR, internal links to pages that convert, new intent pages for queries you half-rank for, double the channel with the best engaged-session rate), one experiment per week, ICE score, stop rules, a 90-day plan | Intermediate | 1 h + 1 h/week |
| 6 | `analytics-funnel-and-conversion` | From visit to key event: funnel exploration (landing → CTA click → sign-up/store click), landing pages ranked by key-event rate, what to fix first | Intermediate | 60 min |
| 7 | `analytics-agent-reporting` | For AI agents: report recipes (JSON), how to call the GA4 and Search Console MCP servers read-only, a stdlib script `ga4_weekly.py` that turns CSV exports (or MCP output saved as JSON) into the weekly report and flags big moves, a scheduled-run recipe | Advanced | 1–2 h once |

Plus one playbook: `playbooks/traffic-growth-with-ga4.md` — the route **setup → tracking plan → reports 101 → 4
weeks of diagnosis → growth loop**, with what "done" looks like at day 7, 30 and 90.

### Planned files per skill (beyond `SKILL.md`)

```text
skills/analytics/
  README.md                                  area table + suggested order
  analytics-ga4-setup/
    references/setup-checklist.md            every setting, where it is in the UI, official link
  analytics-tracking-plan/
    assets/tracking-plan.md                  template (event, trigger, params, key event?, owner, tested?)
    references/utm-convention.md             one table shared with marketing/*/docs/07-metrics-*.md
  analytics-ga4-reports-101/
    references/metrics-glossary.md           UI label · API name · plain meaning · common mistake
    references/learning-path.md              7 short lessons, each with a "do this in your own property" task
  analytics-traffic-diagnosis/
    assets/weekly-diagnosis.md               template
    references/traffic-drop-checklist.md     decision table
  analytics-traffic-growth-loop/
    assets/experiment-log.md                 hypothesis · lever · page · start · metric · result · keep/kill
    references/levers.md                     lever → when the data says use it → how to check it worked
  analytics-funnel-and-conversion/
    assets/funnel-spec.md
  analytics-agent-reporting/
    references/report-recipes.json           named reports with exact API names
    references/mcp-usage.md                  GA4 + Search Console MCP: tools, read-only rules, examples
    scripts/ga4_weekly.py                    stdlib: CSV/JSON in → markdown report out
    assets/weekly-report.md                  the fixed output shape
```

## Official sources to read and cite while writing

Verify each one on the day the skill is written and put the date next to the link. Don't copy limits into this plan.

- GA4 Help Center — setup, data streams, enhanced measurement, internal traffic, cross-domain, data retention,
  key events, event collection limits, data thresholds: <https://support.google.com/analytics>
- Consent mode: <https://developers.google.com/tag-platform/security/guides/consent>
- GA4 Data API schema (dimension/metric API names): <https://developers.google.com/analytics/devguides/reporting/data/v1/api-schema>
- Google Analytics MCP server (official): <https://github.com/googleanalytics/google-analytics-mcp>
- Search Console Performance report help: <https://support.google.com/webmasters>
- Search Console API (search analytics query): <https://developers.google.com/webmaster-tools>
- Google Skillshop — Google Analytics certification (free course, link from `reports-101`):
  <https://skillshop.withgoogle.com>

## How it connects to what exists (link, don't duplicate)

| Existing | Link from | Note |
|---|---|---|
| [growth/action/01-measure-first.md](../skills/growth/action/01-measure-first.md) | setup, tracking plan | Step 1 points to `analytics-ga4-setup` for web products |
| [launch-growth-stack-setup](../skills/launch/launch-growth-stack-setup/SKILL.md) | setup | Apps: Firebase there; web: GA4 here. Same event names where possible |
| [launch-geo-aeo-feature-preview](../skills/launch/launch-geo-aeo-feature-preview/SKILL.md) | diagnosis, growth loop | Reuse its "AI assistants" channel regex; don't redefine it |
| `marketing/*/docs/07-metrics-and-stop-rules.md` | tracking plan | One UTM table; kits link to it |
| [strategy-revenue-target](../skills/strategy/strategy-revenue-target/SKILL.md) | growth loop | Traffic target worked back from the money target |

## Rollout

Each phase ends with `python3 scripts/validate_skills.py` printing `OK` and its own commit.

### Phase 0 · Decisions (maintainer)
- [x] Approve area name `analytics` and the 7 skill names above (approved 2026-10-19).
- [x] Decide on real data: **illustrative examples only** (chosen 2026-10-19), labelled `> **Illustrative example.**`.
      A maintainer product can't be named in this area unless `CLAUDE.md`'s list of allowed places is changed first.
- [x] Confirm agent mode may use the GA4 and Search Console MCP servers (read-only) (confirmed 2026-10-19).

### Phase 1 · Foundations (learn + set up right)
- [x] `analytics-ga4-setup` + `references/setup-checklist.md`
- [x] `analytics-tracking-plan` + template + shared UTM convention
- [x] `analytics-ga4-reports-101` + glossary + learning path
- [x] `skills/analytics/README.md`
- [x] Wire up (repo rule): `.claude-plugin/marketplace.json`, router table in `skills/growth/SKILL.md` (new
      **Analytics** rows, and drop "analytics" from the "doesn't cover yet" line), root `README.md`, `ROADMAP.md`,
      `CHANGELOG.md`

### Phase 2 · Grow traffic
- [ ] `analytics-traffic-diagnosis` + weekly template + drop checklist
- [ ] `analytics-traffic-growth-loop` + levers + experiment log
- [ ] `analytics-funnel-and-conversion`
- [ ] Link from `growth/action/01-measure-first.md` and `07-weekly-rhythm.md`
- [ ] Wire up again (marketplace, router, README, ROADMAP, CHANGELOG)

### Phase 3 · Agent mode
- [ ] `analytics-agent-reporting`: `report-recipes.json`, `mcp-usage.md`, `ga4_weekly.py` (stdlib), output template
- [ ] Test the script on a sample CSV committed under `assets/` (illustrative, labelled)
- [ ] Test agent mode end to end on a real property: weekly report produced with no invented numbers
- [ ] Wire up again

### Phase 4 · Playbook + site
- [ ] `playbooks/traffic-growth-with-ga4.md` (day 7 / 30 / 90)
- [ ] Add the area to the site nav check in `scripts/build_site.py` (area hero image optional; prompts via
      `docs/images/prompts/` if one is made)
- [ ] Replace illustrative examples with real ones as they come in

## Progress

| Phase | Status | Notes |
|---|---|---|
| 0 · Decisions | ✅ done 2026-10-19 | Area `analytics`, all 7 skills, illustrative examples only, MCP read-only allowed |
| 1 · Foundations | ✅ done 2026-10-19 | 3 skills + references, wired into marketplace, router, README, ROADMAP, CHANGELOG. Examples illustrative |
| 2 · Grow traffic | ⬜ not started | |
| 3 · Agent mode | ⬜ not started | |
| 4 · Playbook + site | ⬜ not started | |

## Done when (whole area)

- A beginner can follow skills 1–3 and end with GA4 set up, a tracking plan, and the 6 reports read once.
- Skills 4–5 produce one weekly diagnosis and one experiment per week from real data, not guesses.
- An agent can run skill 7 read-only and produce the same weekly report shape every time, with no invented numbers.
- Every limit or policy cites an official page with the date checked.
- `python3 scripts/validate_skills.py` prints `OK`.
