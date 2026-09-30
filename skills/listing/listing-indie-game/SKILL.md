---
name: listing-indie-game
description: List a small indie game in the right places (itch.io, Steam, web game portals like CrazyGames and Poki, Game Jolt, Newgrounds, mobile stores, game jams) in three levels (1 get it playable, 2 get wishlists and players, 3 grow), with fees, revenue shares, review steps and page essentials. Use when releasing a web, PC or mobile indie game, choosing where to publish a small game, or when someone asks "where should I publish my indie game", "itch.io or Steam", "how to get my HTML5 game on CrazyGames or Poki", or "Steam page checklist".
license: MIT
metadata:
  category: listing
  niche: indie games
  difficulty: beginner → advanced (3 levels)
  time: "Level 1: 1-3 h · Level 2: weeks (wishlists) · Level 3: ongoing"
  version: 1.0.0
  author: nvminhtu
---

# Indie Game Listing (itch.io · Steam · Web portals)

> Match the game to the platform, get it playable where players are, then build wishlists and players before and after release.

## Goal
Put a small game where its players already are, with a page that makes them click *Play*, *Download* or *Wishlist*.

## When to use
- A web (HTML5/WebGL), PC or mobile game is playable.
- You're choosing between itch.io, Steam and web portals.
- **Not for:** mobile store field-by-field details → [listing-app-store](../listing-app-store/SKILL.md), [listing-google-play](../listing-google-play/SKILL.md).

## Inputs
- A playable build (HTML5/WebGL, PC or mobile), a cover image, 3–5 screenshots and a 30-second gameplay clip.
- Your goal: players, revenue or a portfolio piece. It changes which platforms are worth it.

## Where to list

| Platform | Best for | Cost / share | Link |
|---|---|---|---|
| **itch.io** | Any small game, jams, prototypes, pay-what-you-want | Free. You pick the revenue share (default 10%, 0–100%) | [itch.io](https://itch.io/) |
| **Steam** | PC games with a real audience plan | **US$100 per game** (recouped after US$1,000 adjusted gross revenue), then the standard revenue share | [Steam Direct](https://partner.steamgames.com/steamdirect) |
| **CrazyGames** | HTML5 / Unity WebGL games | Free upload. QA in about 1–2 days. *Basic Launch* → *Full Launch* with the SDK and revenue share | [docs.crazygames.com](https://docs.crazygames.com/) |
| **Poki** | Polished web games | Apply with a form. Curated, and terms are negotiated per game (the default web deal includes exclusivity) | [developers.poki.com](https://developers.poki.com/) |
| **Game Jolt, Newgrounds** | Community-driven discovery, web and download games | Free | [gamejolt.com](https://gamejolt.com/) · [newgrounds.com](https://www.newgrounds.com/) |
| **Mobile stores** | Touch-first casual games | Store fees | → Listing skills |
| **Game jams** (itch.io jams) | Visibility and feedback for new devs | Free | [itch.io/jams](https://itch.io/jams) |

## Steps

### Level 1: Get it playable
1. **Pick 1–2 platforms (10 min):** web game → itch.io + CrazyGames. PC game → itch.io now, Steam when the page can
   gather wishlists. Mobile → the stores.
2. **Page essentials (1 h):** a cover/capsule image that reads at small size, a **GIF or trailer in the first
   10 seconds of gameplay** (not a logo intro), 3–5 screenshots, a 1–2 sentence hook (genre + twist), controls, and platforms.
3. **itch.io:** create the project, upload the build (HTML5 builds play in the browser), set a price or
   pay-what-you-want, and tag the genre accurately.
4. **CrazyGames:** upload through the developer portal, pass QA, start with *Basic Launch*, and integrate the SDK when invited to *Full Launch*.

### Level 2: Get wishlists and players
1. **Steam:** pay the Direct fee, then build the store page early. It must show as **Coming Soon** for a period before
   release (check the current Steamworks rule). Collect wishlists for months, not days.
2. **Take part in events:** itch.io jams and Steam Next Fest (with a demo) are the biggest free visibility boosts for small games.
3. **Devlogs:** post short progress GIFs on itch.io devlogs and relevant subreddits and communities (follow each one's rules).
4. **Web portals:** if a CrazyGames Basic Launch performs well, consider Poki's application for a polished version.

### Level 3: Grow
- **Update and re-announce:** each update is a new chance to appear in "recently updated" feeds and devlogs.
- **Bundles and sales:** itch.io bundles and Steam seasonal sales.
- **Press kit + creators:** a one-page press kit and keys for small streamers → [launch-quick-download-wins](../../launch/launch-quick-download-wins/SKILL.md) #14.
- **Port where it works:** a web hit → mobile. A PC game with wishlists → consoles later.

## Prompt (copy-paste)
Replace everything in `{{ }}`.

````text
You are an indie game publishing advisor. Help me list my game.

Game: {{genre, core twist, session length}}   Engine + builds: {{Unity WebGL / Godot HTML5 / PC / mobile}}
Stage: {{prototype / demo / finished}}   Price model: {{free / paid / ads / IAP}}   Goal: {{players / revenue / portfolio}}

1. Recommend 1-3 platforms from: itch.io, Steam, CrazyGames, Poki, Game Jolt, Newgrounds, App Store / Google Play,
   and explain each choice (fees, revenue share, audience fit). Mention Steam's per-game fee and Poki's curated terms.
2. Write the page: a hook (≤ 2 sentences), a description (≤ 150 words), 5 tags, a shot list for 5 screenshots and
   a 30-second trailer (gameplay in the first 10 seconds).
3. A launch plan: jams/events to join (e.g. Steam Next Fest if on Steam), devlog cadence, communities to post in.
Mark anything you're unsure about as TODO.
````

## Example output

> **Illustrative example.** Fictional game, shown for format.

*Dino Dash* (Godot HTML5 endless runner, 2-minute sessions, free with ads) → **itch.io + CrazyGames** now, mobile later.
Hook: *"An endless runner where the dino shrinks every time you jump."* Plan: a Basic Launch on CrazyGames, an itch.io page
with a devlog, and an entry in a 48-hour jam in week 2 to get feedback.

## Common mistakes
- **A trailer that starts with logos.** Show gameplay in the first seconds.
- **Paying the Steam fee without a wishlist plan.** Many small games never earn back the fee.
- **A web game with no mobile or touch support** on portals where much of the audience is on phones.
- **Wrong tags,** which put your game in front of the wrong players.

## Related skills
- [listing-free-directories](../listing-free-directories/SKILL.md): itch.io and other free places in context.
- [case-study-success-story-analysis](../../case-study/case-study-success-story-analysis/SKILL.md): learn from similar small games.
- [launch-post-writing](../../launch/launch-post-writing/SKILL.md): devlog and launch posts.

## Credits
Written by [@nvminhtu](https://github.com/nvminhtu). Sources: [Steam Direct fee](https://partner.steamgames.com/doc/gettingstarted/appfee),
[itch.io open revenue sharing](https://itch.io/docs/general/about), [CrazyGames docs](https://docs.crazygames.com/requirements/intro/),
[Working with Poki](https://developers.poki.com/guide/working-with-poki). Terms change, so check them before committing.
