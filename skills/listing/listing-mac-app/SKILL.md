---
name: listing-mac-app
description: Choose and execute the right way to list a small Mac app (Mac App Store, direct download with notarization and a payment provider, Setapp, Homebrew, Mac directories), in three levels (1 ship it, 2 get found, 3 grow), with screenshot sizes, signing requirements and where Mac users look for apps. Use when publishing a macOS utility or menu-bar app, deciding between Mac App Store and selling direct, or when someone asks "how do I sell my Mac app", "Mac App Store vs direct", "notarize and distribute", or "where to list a Mac app".
license: MIT
metadata:
  category: listing
  niche: Mac apps
  difficulty: beginner → advanced (3 levels)
  time: "Level 1: 2-4 h · Level 2: 1-2 h · Level 3: ongoing"
  version: 1.0.0
  author: nvminhtu
---

# Mac App Listing (App Store · Direct · Directories)

> Pick your channel (or both), ship it correctly, then get it in front of the places Mac users actually browse.

## Goal
Get a small Mac app into users' hands through the channel that fits it, and list it everywhere Mac users go
looking for utilities.

## When to use
- A Mac utility, menu-bar app or productivity tool is ready to ship.
- You can't decide between the Mac App Store and selling directly.
- **Not for:** iPhone/iPad → [listing-app-store](../listing-app-store/SKILL.md).

## Inputs
- A signed, working build, and a list of the system APIs and permissions it needs (this decides whether the sandbox works).
- An Apple Developer Program membership (needed for both the Mac App Store and notarization).
- The price model (free / one-time / subscription / trial), and a landing page or a plan for one.

## Choose the channel

| | Mac App Store | Direct download (your site) |
|---|---|---|
| Needs | Apple Developer Program, **App Sandbox**, App Review | Apple Developer Program, **Developer ID signing + notarization** |
| Payment | Apple (15–30% commission) | A merchant of record such as Paddle, Lemon Squeezy or Gumroad (they handle tax), or Stripe |
| Updates | Automatic via the store | Your own updater (e.g. the Sparkle framework) |
| Best for | Discovery, trust, simple apps that work inside the sandbox | Apps that need system access the sandbox blocks, one-time licenses, trials |

Many indie Mac apps do **both**: the App Store for reach, and direct sales for power features or a lower fee.

## Where Mac users find apps

| Place | Cost | Link |
|---|---|---|
| Mac App Store | Developer Program | [App Store Connect](https://appstoreconnect.apple.com/) |
| Setapp (subscription bundle, curated, revenue share) | Free to apply | [setapp.com/developers](https://setapp.com/developers) |
| MacUpdate | Free listing | [macupdate.com](https://www.macupdate.com/) |
| r/macapps | Free (read the self-promo rules) | [reddit.com/r/macapps](https://www.reddit.com/r/macapps/) |
| Homebrew Cask (`brew install --cask`) | Free, via pull request, must meet the acceptance criteria | [Homebrew/homebrew-cask](https://github.com/Homebrew/homebrew-cask) |
| AlternativeTo, Product Hunt, Softpedia | Free | → [listing-free-directories](../listing-free-directories/SKILL.md) |

## Steps

### Level 1: Ship it
**Mac App Store**
1. Turn on App Sandbox and add only the entitlements you need. Test every feature *inside* the sandbox.
2. Prepare screenshots at **16:10**: 1280×800, 1440×900, 2560×1600 or **2880×1800** (1–10).
3. Fill the listing like [listing-app-store](../listing-app-store/SKILL.md) Level 1 (name, subtitle, keywords,
   privacy, age rating, review notes), choose macOS as the platform, and submit.

**Direct download**
1. Sign with your **Developer ID** certificate, **notarize** with Apple (`xcrun notarytool submit … --wait`), then
   staple the ticket (`xcrun stapler staple`). Unnotarized apps get a Gatekeeper warning most users won't get past.
2. Package it as a DMG or ZIP, and host it on your site with a clear "Download for Mac" button, the minimum macOS
   version and the Apple silicon/Intel support.
3. For paid apps: set up a merchant of record for checkout and license keys. Offer a trial.
4. Add an updater so users get fixes.

### Level 2: Get found
1. **Landing page:** one sentence, a 20-second GIF, the price, the download button, and system requirements.
2. **List on MacUpdate, AlternativeTo** (as an alternative to 3 known apps) **and Product Hunt**.
3. **Post on r/macapps** following its rules ([launch-reddit-posting](../../launch/launch-reddit-posting/SKILL.md) has the Mac subreddit plan and a rules fetcher). Mac users there love menu-bar utilities with a clear demo.
4. **Mac App Store:** keywords and screenshots → [aso-keyword-research](../../aso/aso-keyword-research/SKILL.md),
   [aso-screenshot-strategy](../../aso/aso-screenshot-strategy/SKILL.md).

### Level 3: Grow
- **Apply to Setapp** once the app is polished and has a clear use case.
- **Homebrew Cask** for developer audiences (check the notability and acceptance rules first).
- **Launch discounts** on deal communities → [launch-quick-download-wins](../../launch/launch-quick-download-wins/SKILL.md).
- **Both channels:** keep feature parity clear on your site ("App Store version" vs "Direct version").

## Prompt (copy-paste)
Replace everything in `{{ }}`.

````text
You are a Mac indie distribution expert. Help me list my Mac app.

App: {{what it does}}   System access it needs: {{e.g. accessibility API, full disk access, none}}
Price model: {{free / one-time / subscription / trial}}   Audience: {{developers / general users / ...}}

1. Recommend Mac App Store, direct download, or both, with the reasons (sandbox fit, fees, audience).
2. Level 1 checklist for the chosen channel(s): signing/notarization or sandbox entitlements, screenshots (16:10 sizes),
   listing fields, payment provider options (merchant of record vs Stripe) and an updater.
3. A 2-week plan for Level 2: landing page outline, MacUpdate / AlternativeTo / Product Hunt / r/macapps posts
   (draft the r/macapps post, no hype).
4. Should I apply to Setapp or Homebrew Cask later? What would make the app eligible?
Mark anything uncertain as TODO.
````

## Example output

> **Illustrative example.** Fictional app, shown for format.

*QuickCheck* (a menu-bar checklist, no system access) → **both channels**: the Mac App Store for discovery (a sandbox-friendly
app), and direct sales with a one-time $9 license via a merchant of record for users who dislike the store.
Screenshots at 2880×1800. Week 1: MacUpdate + AlternativeTo (alternative to Things, Reminders). Week 2: an r/macapps post
with a 15-second GIF.

## Common mistakes
- **Shipping an unnotarized DMG.** Gatekeeper blocks it and users think it's malware.
- **Discovering sandbox limits after building.** Check whether the APIs you need work in the sandbox before choosing the Mac App Store.
- **Direct sales without an updater.** Users stay on buggy versions forever.
- **Dumping a link on r/macapps.** Follow the rules and show a demo.

## Related skills
- [listing-app-store](../listing-app-store/SKILL.md): the App Store Connect fields in detail.
- [listing-free-directories](../listing-free-directories/SKILL.md): more free places to list.
- [monetization-pricing-strategy](../../monetization/monetization-pricing-strategy/SKILL.md): one-time vs subscription.

## Credits
Written by [@nvminhtu](https://github.com/nvminhtu). Sources: Apple [screenshot specifications](https://developer.apple.com/help/app-store-connect/reference/app-information/screenshot-specifications/),
Apple Developer documentation on notarizing macOS software and App Sandbox.
