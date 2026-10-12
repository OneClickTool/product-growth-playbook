# Changelog

## [Unreleased]
### Added
- `instagram-marketing/`: an Instagram kit for indie devs, built around one goal: impressions from non-followers →
  website visits. `docs/04-image-flow.md` takes one true fact to a finished post in 10 checkable steps (fact,
  format, hook, slide script, design kit, visuals with real screenshots first, export, caption + alt text + ≤5
  hashtags, link path, publish and measure). Other docs: strategy, profile setup (5 UTM bio links, Highlights,
  pins), how Instagram ranks (from its own explainer and dated press reports), 12 post formats and the weekly
  rotation, Stories and the link path, metrics per reach with stop rules, rules and risks. `flow/` (daily routine,
  website funnel + UTM map + GA4 report), `templates/` (design kit, carousel brief, post file, Story sequence,
  weekly numbers), `reference/` (facts with Official / Reported / Practice labels, research log), `posts/`
  (6-product rotation, week 1, 30-day plan Oct 12 → Nov 10). Skills: `social-instagram` (router),
  `social-instagram-image-flow`, `social-instagram-growth`. The validator now also checks `instagram-marketing/skills/`.
- `social-x`: one command for the X kit (`/social-x today · week · reply · profile · promo · talk · numbers ·
  premium · risk`) that routes to the right X skill or doc. `social-x-daily`: today's two posts (one product slot at
  most), first-reply UTM link, three reply sessions and an hourly checklist sized to 25/60/120 min, with a ramp-up.
- `x-marketing/flow/a-day-on-x.md`: a day on X hour by hour for promoting 3–5 products while the rest of the posts
  and replies earn reach, follows and trust; the weekly mix, ramp-up and what moves each goal.
- `x-marketing/posts/`: `product-rotation.md` (5 products, 3 hooks each, demo shot lists, when a reply may link),
  `talk-bank.md` (non-promo tips, questions, takes, build log, honest numbers, reply openers) and `week-02-mix.md`.
  `templates/product-rotation.md` is the blank version. `posts/plan-30-days.md`: Oct 12 → Nov 8 day by day
  (posts, reply split, link-drop days, follows, weekly checks, stop signs). `docs/06`: when to drop a product link
  in "what are you building?" posts (6 checks). `reference/tips-and-tricks.md`: hashtags, and X's July 2026
  statement that links are no longer penalized. `social-x` 1.1.0 adds `month`, `drop` and `check`.
  `x-marketing/reference/fake-proof-and-scams.md`: how to check revenue screenshots and accounts, scams aimed at
  indie devs on X, and keeping motivation from real numbers. `flow/tools.md` now links every outside tool.
- `flow/README-product-growth-hack.md`: the order of operations from zero to the first sale in 10 phases with gates
  (free hook → email list → beta → list-first launch, traffic engine for product pages, planned gaps).
- `x-marketing/docs/09-post-variants.md` + `templates/variants/`: 20 X post variants in 5 families (Show, Teach,
  Prove, Talk, Sell), each with stage, link placement, media and a copy-ready post file; a week built from variants
  and a real two-post comparison with a rewrite.
- `x-marketing/docs/10-best-practices.md`: every posting rule on one page with its evidence label (Code, Help, Real,
  Practice): hooks, banned openers, media, links, volume, first hour, replies, Communities, measuring by variant,
  paid promotion, and a pre-post checklist.
- `x-marketing/flow/cross-channel-funnel.md`: every channel → X profile → free trial. Reddit → X → trial route,
  making the X profile convert, clean follower growth, search surfaces for an X account, synced email signatures per
  address, a UTM map and a one-afternoon setup checklist.
- `x-marketing/flow/analytics-pattern.md`: a real 28-day X analytics baseline (2K impressions, 7 profile visits,
  ~10× impressions in 3 days of daily posts + replies), what it says, the safe routine and next targets.
- `x-marketing/`: a self-contained X (Twitter) kit for indie devs. `README-X-Marketing.md`; `docs/` (strategy to the
  first paid subscriber, profile setup, how the ranker works, 30-day Premium plan, 7-day post formats, reply
  playbook, metrics and stop rules, rules and risks); `reference/` (research log, ranker weights and Premium facts
  from X's code and help pages, tips by evidence level, articles, repos, glossary); `skills/` with
  `social-x-growth`, `social-x-reply` and `social-x-profile-funnel`; `flow/` (daily routine, tools); `resources/`
  (live links to share, UTM pattern); `templates/` (fact bank, post file, weekly numbers, reply targets); `posts/`
  (a starter week). The validator now also checks `x-marketing/skills/`.
- `case-study/`: a reading list of real launches taken apart, one page each. First: Shipfolks × GoViralDev, how a new
  directory sells two flat-price ad slots from day one, and how to use a $100–150 sponsor slot as a launch channel
  (stop rule, banner, matching landing, UTMs, day-30 decision).
- `monetization-open-source-funding`: a Sponsor button for a free repo or app in 30 minutes: `.github/FUNDING.yml`
  (Ko-fi, GitHub Sponsors, Buy Me a Coffee, Polar, custom links), turning it on, a README badge and support section,
  UTM links, one org-wide default, and the App Store / Google Play rules that keep tip links out of store apps.
- README "Free apps": TapRec, a free Android screen recorder with a simple editor (APK + QR on its GitHub page).
- `docs/subreddits/`: a wiki page per subreddit (13 Mac-related to start: r/macapps, r/MacOSApps, r/MacOS, r/apple,
  r/SideProject, r/SwiftUI, r/indiehackers, r/AppHookup, r/shortcuts, r/applehelp, r/mac, r/macbookpro, r/MacBook)
  with self-promotion rules, post format, voice, images, readers and sources, plus a ranked list for Mac apps.

### Changed
- Renamed the plugin and display name to **Product Growth Hack** (`product-growth-hack`).
- `social-x-growth` (1.3.0): the weekly rotation now picks from the 20 variants, the prompt returns a variant id
  per post and bans ad-style openers; post files gain a `variant:` field. `reference/tips-and-tricks.md` adds the
  **Real** evidence label.
- `x-marketing/templates/post-file.md` and `social-x-growth` (1.2.0): `link:` now says where the link goes
  (`first-comment` / `bio` / `direct` / `none`) and the URL lives in `## Reply 1`, matching campaign tools that read
  post files.
- `x-marketing/docs/02-profile-setup.md`: what you can change without losing the checkmark.
  `08-rules-and-risks.md`: the temporary reach label, with a real case and how to avoid it.
- `research-source-finding` 1.1.0: verified competitor revenue from TrustMRR's public Markdown profiles
  (`/startup/<slug>.md`, slugs from the sitemap, fetch slowly), and reading a competitor's SEO plan from the URL
  patterns in its sitemap (`/vs/`, `/alternatives/`, `/uses/`).
- `research-where-users-ask` 1.1.0: a step for event-driven waves (new cheap device, end of support, a product
  shutting down): track rising "how to <task> on <device>" queries in Google Trends and autocomplete.
- `social-short-video` 1.2.0: `references/ready-made-pipelines.md`, open-source short-video pipelines to follow,
  starting with video-mkt-agents (HyperFrames): its genres (app promo, AI tips, AI news, book debates, finance,
  long-form), reusable blocks, publish log and cover helpers, mapped to this skill's formats, with license and
  auto-upload cautions.
- `social-short-video` 1.1.0: a 17-format catalog (`references/formats.md`) marking which formats an AI agent can
  render on its own, which need one in-app step and which need a person; which footage and music are safe (stock
  clips and free music yes, re-uploading other creators' videos no); a script → render spec → video pipeline
  (`references/auto-render.md`); `format`, `test` and `variant` tags for A/B tests.
- `launch-reddit-posting` 1.4.0: read the subreddit wiki before fetching rules; the profile template gains voice,
  images, difficulty, audience and `verified:`.
- `launch-reddit-posting` 1.3.0: macOS ladder from easy to hard (comments in Mac help subreddits → r/MacOSApps →
  r/SwiftUI → r/macapps → r/apple on Sundays / r/MacOS after modmail), and which subreddits hold buyers vs builders.
- `launch-reddit-posting` 1.2.0: save one rules profile per subreddit (`assets/subreddit-profile.md`), shared by every
  product and re-checked after 60 days; write one post per request and log posts in the order you asked for them.
- `listing-mac-app` 1.1.0: more places Mac users look for apps (MacNative, Awesome Native macOS Apps, awesome-mac,
  MenuBarApps, macmenubar.com, PayOnceApps, IndieAppCircle), App Store featuring nominations and Apple Ads, plus
  mistakes on dormant Reddit accounts, posting outside US hours and sending web-wrapper apps to native-only lists.

## [0.12.0] - 2026-10-02
### Added
- New area **🧭 Strategy** with 4 skills, the thinking behind every other skill:
  - `strategy-revenue-target`: turn "$X in N months" into a weekly funnel worked backward from the target, with a
    reality check, go / fix / kill rules and `scripts/revenue_backsolve.py`.
  - `strategy-spend-and-timing`: sort costs into must-pay / pays-back / skip, fund the one bottleneck, read momentum
    and slump signals, and run a 2-week finishing sprint behind what works.
  - `strategy-contrarian-marketing`: map what the herd does, invert it through 6 lenses (channel, audience, side door,
    free-tool bait, offer inversion, unscalable), filter for honesty, and run 3 experiments with pass numbers.
  - `strategy-product-as-funnel`: treat apps and games as entry points to an owned audience: give → get per product,
    one capture point at the moment of value, honest cross-promotion, owned-audience tracking.
- New area **📣 Social** with 3 skills:
  - `social-short-video`: TikTok, Reels and Shorts with fewer, better videos: one format, 10 hooks, 3 scripts, a 3-week
    test and a keep/kill rule, with TikTok and FTC disclosure rules.
  - `social-credible-posting`: posts on X, Threads, Facebook and LinkedIn that people trust: the proof ladder, 5 trust
    formats, a red-flag list and FTC Endorsement Guides disclosure rules.
  - `social-build-in-public`: a weekly update habit, what to share and keep private, followers → email list.
- `launch-open-source-funnel`: a free repo as the front door to a product (open core, free tool → paid app,
  hosted, content → product, sponsorware), with honest, UTM-tagged hand-off points.
- `launch-growth-stack-setup`: Firebase Analytics (5–8 events), Crashlytics, Remote Config, AdMob (test ads,
  app-ads.txt, UMP consent, ATT, placement), one real payment and matching privacy labels, with a verified checklist.
- `email-segments-and-tools`: lifecycle, product, source and interest segments driven by events, one retention email
  per segment, monthly list cleanup, and choosing an email tool by situation.
### Changed
- `launch-reddit-posting` 1.1.0: new step 6, *Fewer posts, more users*: a 5-point quality bar, post types ranked by
  users per post, and a monthly rhythm of 2–4 strong posts.
- The `growth` router, Growth Map, README and ROADMAP now include strategy and social, so every skill sits on one route.

## [0.11.0] - 2026-10-01
### Added
- New area **📧 Email** with 4 skills:
  - `email-list-and-deliverability`: waitlist and opt-in form, own-domain sending, SPF/DKIM/DMARC with a
    verification step, one-click unsubscribe, and a compliance table sourced from the Gmail and Yahoo sender
    guidelines, the FTC CAN-SPAM guide and the UK ICO.
  - `email-beta-program`: recruit and track beta testers, invite them through TestFlight, Google Play testing tracks
    or Chrome Web Store trusted testers (official limits cited), nudge rules, 5 email templates, and ending the beta
    with a tester offer.
  - `email-onboarding-sequence`: welcome + onboarding emails built around one activation event, with
    activated/not-activated branches and exit rules.
  - `email-trial-sequence`: trial emails with timing for 7-, 14- and 30-day trials, a billing reminder for
    card-up-front trials, cancellation and one win-back email, plus what to do instead for App Store / Google Play trials.

## [0.10.0] - 2026-10-01
### Added
- `launch-reddit-posting`: subreddits by product type (with a macOS deep dive), Reddit-wide rules, title formulas,
  a body template and first comment, a one-subreddit-per-day schedule, and `scripts/fetch_subreddit_rules.py`, which
  pulls each subreddit's current rules and pinned posts into Markdown (rules aren't copied into the repo because they change).
- `case-study-award-winning-design`: study Apple Design Awards, App Store Awards, Google Play Best of, Product
  Hunt (Golden Kitty and leaderboard) and Chrome Web Store Featured winners at one growth moment (store page,
  onboarding, paywall, launch page, shareable moment), compare them with controls, check public growth signals, and
  apply up to 3 patterns. Includes a sourced list of award programs, a pattern taxonomy, a result report and an
  apply plan.
- Playbook: [Growth Map](playbooks/growth-map.md), the whole playbook on one page in 7 chapters (research → learn
  from others → get paid → publish → launch → grow in stores → share results). Each chapter lists its skills, research,
  tools, official references, templates and prompt. The App Store chapter is split part by part: signing files
  (CSR, `.cer`, `.p12`, provisioning profile, API key), text, images (icon, screenshots, preview), privacy and submit.
- `monetization-payment-setup`: pick a payment provider that works from your country and get a first payout, in 3
  levels (a real payment this week → verified checkout → lower fees, local payments, taxes). Covers Stripe and Stripe
  Managed Payments (not in Vietnam), Paddle, Lemon Squeezy, Polar, Creem, Dodo, Gumroad, PayPal, App Store and Google
  Play payouts, and Vietnamese gateways (payOS, SePay, VNPay, MoMo, ZaloPay), with a sourced country/fee/review-time
  reference and a setup sheet.
- `monetization-in-app-purchase-setup`: in-app purchases on iOS, macOS and Android, choosing between coding
  StoreKit 2 + Play Billing Library yourself, a free wrapper (Flutter, React Native, Expo, Capacitor, Unity) or a
  subscription SDK (RevenueCat, Adapty, Qonversion, Superwall), in 3 levels (first sandbox purchase →
  production-ready with restore, acknowledge, server notifications and an App Review checklist → offers, paywall
  tests, web purchases). Includes minimal StoreKit 2 and Kotlin code and a sourced facts file (PBL 8+ required since
  31 Aug 2026, verifyReceipt deprecated).

## [0.9.0] - 2026-09-30
### Added
- `launch-github-repo-seeding`: seed an open-source repo in 3 levels (star-worthy repo → 7-day seeding via your
  circle, awesome lists and bigger repos' ecosystems → weekly habits), what GitHub bans (bought or exchanged stars),
  and how to reach classic developers vs vibe coders.
- Playbook: [ASO Optimization](playbooks/aso-optimization.md), a 4-week route (baseline → keywords → title → screenshots
  → ratings) plus a monthly one-change-at-a-time measurement loop.
### Changed
- Launch a Product playbook now routes non-app products to their niche listing skill, open-source repos to
  GitHub repo seeding, and apps to the ASO playbook after launch.

## [0.8.0] - 2026-09-30
### Added
- `listing-digital-template`: Notion Marketplace + Gumroad in 3 levels (free template → paid → Discover, bundles,
  affiliates), with current fees, the Notion paid-seller waitlist, safe delivery of duplicate links, and a listing sheet.

## [0.7.0] - 2026-09-30
### Added
- Listing by niche, each in 3 levels: `listing-browser-extension` (Chrome, Edge, Firefox), `listing-mac-app`
  (Mac App Store, direct + notarization, Setapp, Homebrew), `listing-indie-game` (itch.io, Steam, CrazyGames, Poki),
  `listing-dev-plugin` (VS Code + Open VSX, JetBrains, Raycast, Obsidian, Figma, npm), `listing-ai-product`
  (AI directories, GPT Store, skills.sh, Claude Code plugins, MCP Registry).

## [0.6.0] - 2026-09-30
### Added
- New **Case Study** area: `case-study-competitor-teardown` (learn from the enemy, with a teardown sheet),
  `case-study-success-story-analysis` (5 successes and 2 failures, bias-checked),
  `case-study-write-your-own` (an honest case study template, ready to contribute).

## [0.5.0] - 2026-09-30
### Added
- `launch-quick-download-wins`: 16 low-effort channels for fast downloads, ranked in 3 levels by effort and speed.
### Fixed
- `listing-app-store`: only in-app purchase promo codes were retired (March 2026). App download promo codes still work.

## [0.4.0] - 2026-09-30
### Added
- New **Listing** area, each skill in 3 levels: `listing-app-store` and `listing-google-play` (step by step, with
  fill-in listing sheets), `listing-free-directories` (25+ free launch platforms, directories and alternative stores,
  with a launch kit and tracker).
### Changed
- Router, README, playbook and pre-launch checklist link to the listing skills.

## [0.3.0] - 2026-09-30
### Added
- New **Research** area: `research-source-finding`, `research-doc-organization` (with note, sources and decision
  templates), `research-where-users-ask` (a linked map of communities where people ask for software),
  `research-review-mining`.
- README: who it's for, what you get (all free), why use it, and a 3-step start.
- CONTRIBUTING: a no-coding guide for first-time contributors.
### Changed
- `growth` router covers the idea stage. The launch playbook adds an optional research step.

## [0.2.0] - 2026-09-30
### Added
- Launch: `launch-pre-launch-checklist`, `launch-post-writing`, `launch-product-hunt-launch`, `launch-get-first-100-users`.
- ASO: `aso-title-subtitle-optimization`, `aso-screenshot-strategy`, `aso-review-and-rating-strategy`.
- Monetization: `monetization-free-trial-vs-freemium`, `monetization-pricing-strategy`, `monetization-paywall-design`,
  `monetization-subscription-tiers`.
- Playbook: `playbooks/launch-a-product.md`.
- The `growth` router now covers all 12 skills.

## [0.1.0] - 2026-09-29
### Added
- Repository foundation: skill template, contributing guide, agent rules, validator script, plugin marketplace.
- `growth` router skill.
- `aso-keyword-research` skill with keyword sheet template and `pack_keywords.py`.
