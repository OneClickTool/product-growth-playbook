---
name: monetization-open-source-funding
description: Add a Sponsor button and a support section to a free or open-source GitHub repo (or a free app distributed from GitHub) in about 30 minutes, so people who like it can pay you without you adding a paywall. Covers the .github/FUNDING.yml file (Ko-fi, GitHub Sponsors, Buy Me a Coffee, Patreon, Open Collective, Polar, Liberapay, custom links), turning the button on, a README badge and "Support this project" section, UTM links to your paid product, one org-wide default for all repos, and the App Store and Google Play rules that keep tip links out of store apps. Use when someone asks "add a sponsor button", "FUNDING.yml", "ko-fi on github", "github sponsors", "buy me a coffee button", "donate button for my repo", "how do I get money from a free app", "support this project section", "hít sponsor", or ships a free tool, template or APK from GitHub.
license: MIT
metadata:
  category: monetization
  difficulty: beginner
  time: 30 min per repo (5 min for each repo after the first)
  version: 1.0.0
  author: nvminhtu
---

# Open-Source Funding: Sponsor Button + Support Section

> In 30 minutes your free repo has a ❤️ Sponsor button at the top, a support section people actually read, and a link
> that sends grateful users to whatever you sell.

## Goal
A free repo that people like should give them one obvious, honest way to pay you back. Usually that means a
coffee-sized payment, a star, or a visit to your paid product. Tips are rarely real income. Their value is the
signal (someone cared enough to pay) and the hand-off to the thing you do sell.

## When to use
- You publish a free tool, library, template, playbook or app (APK, DMG, EXE) on GitHub.
- People star, fork or thank you in issues, and there is no way for them to give back.
- You have several free repos and want the same button on all of them.
- **Not for:** charging for the product itself. See [monetization-payment-setup](../monetization-payment-setup/SKILL.md)
  and [launch-open-source-funnel](../../launch/launch-open-source-funnel/SKILL.md) (open core, free tool → paid app).

## Inputs
- Admin access to the repo (or the org).
- At least one funding account that is **already live**: a Ko-fi page, a Buy Me a Coffee page, an approved GitHub
  Sponsors profile, Patreon, Open Collective, Polar or Liberapay. A link to an account that isn't approved yet makes
  the button lead to a dead page.
- Optional: the URL of your paid product or site, for the "custom" link.

## Which platform? (checked 2026-10-08)

| Platform | `FUNDING.yml` key | Good for | Note |
|---|---|---|---|
| Ko-fi | `ko_fi: name` | One-off "buy me a coffee", no account needed to pay | Fastest to set up |
| Buy Me a Coffee | `buy_me_a_coffee: name` | Same as Ko-fi | Pick one of the two, not both |
| GitHub Sponsors | `github: [user]` | Monthly sponsors who already use GitHub | Needs an approved Sponsors profile first; payouts aren't available in every country |
| Polar | `polar: name` | Dev tools; can also sell licenses | |
| Patreon / Open Collective / Liberapay | `patreon:` · `open_collective:` · `liberapay:` | Ongoing community funding | Open Collective shows the money publicly |
| Your own link | `custom: ["https://…"]` | Your paid app, site or newsletter | Up to 4 links; quote every URL |

Source: [GitHub Docs: Displaying a sponsor button in your repository](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/displaying-a-sponsor-button-in-your-repository)
(one username per platform, up to 4 custom URLs, `github:` takes up to 4 developers plus 1 organization).

Start with **Ko-fi + one custom link** to your own product. Add `github:` the day your Sponsors profile is approved.

## Steps
1. **Write `.github/FUNDING.yml` on the default branch.** One platform per line. Keep not-yet-approved accounts as a
   comment so you remember to switch them on:
   ```yaml
   # Shows the "Sponsor" button at the top of this repo page.
   ko_fi: your-kofi-name
   # github: [your-github-user]   # uncomment once GitHub Sponsors is approved
   custom: ["https://your-site.com/?utm_source=github&utm_medium=funding&utm_campaign=<repo>"]
   ```
   Check: GitHub shows a preview of the links when you open the file in the web editor. With the CLI:
   `gh api graphql -f query='{repository(owner:"OWNER",name:"REPO"){fundingLinks{platform url}}}'` lists them.
2. **Turn the button on.** Repo → Settings → General → Features → tick **Sponsorships**. Check: a ❤️ **Sponsor**
   button appears next to Watch / Fork / Star, and a "Sponsor this project" box appears in the right sidebar.
3. **Add a badge near the top of the README.** Put it under the download button or install command, not above it.
   The download comes first.
   ```html
   <a href="https://ko-fi.com/your-kofi-name"><img src="https://img.shields.io/badge/Ko--fi-Support%20<Name>-FF5E5B?logo=ko-fi&logoColor=white" alt="Support <Name> on Ko-fi"></a>
   ```
4. **Add a "Support <Name>" section before Versions / License.** Use four lines:
   - the promise (free, and what "free" means: no ads, no account, stays free)
   - the paid ask, one tap, with the platform named
   - free ways to help (star, share, open an issue). Many people can't pay but will do these.
   - one link to your other products, with UTM
5. **Tag every link to your own site with UTM.** Use `utm_source=github`, `utm_medium=funding` for the Sponsor
   button and `utm_medium=readme` for the README, plus `utm_campaign=<repo>`. Check: the visits show up under that
   campaign in your analytics.
6. **Many repos? Set it once.** Create a public repo named `.github` in your account or org and put `FUNDING.yml` in
   its `.github/` folder. Every repo without its own file uses it. A repo that needs its own UTM campaign keeps its own file.
7. **Keep tip links out of store apps.** On GitHub and your website, tip links are fine. Inside an app sold on a store,
   they are not:
   - **App Store:** tipping the developer must use in-app purchase (Guideline 3.1.1), and a gift is exempt only if
     it isn't tied to any content or service (3.2.1(vii)). Raising money for charity inside the app is not allowed
     unless you are an approved nonprofit (3.2.2(iv)). So: no Ko-fi or "donate" button in iOS or Mac App Store builds,
     and don't call a subscription a donation.
   - **Google Play:** apps can't steer users to a payment method outside Play billing. Tax-exempt donations are the
     listed exception
     ([Payments policy](https://support.google.com/googleplay/android-developer/answer/9858738)).
   - **Sideloaded APK, DMG or EXE from GitHub:** no store rules apply, but if the same app also ships to a store,
     keep the link on the GitHub page and website only. That way both builds stay the same.
8. **Thank people in public (with their consent).** Add a "Supporters" line in release notes. It is the cheapest way
   to get the next supporter.

## Prompt (copy-paste)
Works in Claude, ChatGPT, Gemini, Cursor. Replace everything in `{{ }}`.

````text
You are helping me add funding to a free GitHub repo.

Repo: {{owner/repo}}
What it is (1 line): {{what the project does and for whom}}
How it's distributed: {{source only | library | APK/DMG/EXE download | also on App Store / Google Play}}
Live funding accounts (only ones already approved): {{e.g. ko_fi: name; github sponsors: pending}}
My paid product or site (optional): {{URL}}
Current README: {{paste it}}

Do this:
1. Write .github/FUNDING.yml: live accounts as keys, pending ones as comments, my site as a `custom` link with
   utm_source=github&utm_medium=funding&utm_campaign={{repo}}. Quote every URL.
2. Give me a README badge line and say exactly where it goes: after the download/install block, never above it.
3. Write a "Support {{Name}}" section (max 6 lines) for just before Versions/License: what "free" means here,
   one paid ask, free ways to help (star, share, issue), one UTM link to my other products.
   Plain words, no guilt, no made-up numbers or promises I haven't made.
4. If the app is on the App Store or Google Play, list what must NOT go inside the app (no tip/donate buttons or
   links; tips through in-app purchase only) and confirm the GitHub page is the only place for the link.
5. List the manual steps I must click: Settings → Features → Sponsorships, and how to verify the button shows.
````

## Example output
A free Android screen recorder shipped as an APK from GitHub, Ko-fi live, GitHub Sponsors pending.

`.github/FUNDING.yml`
```yaml
# Shows the "Sponsor" button at the top of this repo page.
ko_fi: icecraftdigital
# github: [nvminhtu]   # uncomment once GitHub Sponsors is approved
custom: ["https://oneclicktool.app/?utm_source=github&utm_medium=funding&utm_campaign=taprec"]
```

README, after the download link and QR code:
```markdown
## Support TapRec

TapRec is free, with no ads and no paid version. If it saved you time, you can help keep it going:

- [☕ Buy me a coffee on Ko-fi](https://ko-fi.com/icecraftdigital): one-time, no account needed.
- ⭐ Star this repo, or share TapRec with a friend who needs a screen recorder.
- Found a bug or want a feature? [Open an issue](https://github.com/nvminhtu/taprec/issues).
```

Live: [nvminhtu/taprec](https://github.com/nvminhtu/taprec) and this repo use exactly this setup. Both are the
maintainer's. More free apps: [OneClickTool](https://oneclicktool.app/?utm_source=github&utm_medium=skill&utm_campaign=growth-playbook).

## Common mistakes
- **Linking an account that isn't live yet.** A GitHub Sponsors link before approval leads to an empty page. Keep it
  commented out until approval.
- **Adding the file but not ticking Sponsorships in Settings.** The links are valid, but no button shows.
- **Putting the badge above the download.** People came for the app. Ask after they've seen what they get.
- **Guilt copy** ("I work on this for free so…"). State what's free and offer a way to help. That's enough.
- **A Ko-fi button inside an App Store or Google Play app.** This gets the app rejected. Tips there go through in-app
  purchase, or stay on GitHub.
- **No UTM on the custom link.** Then you can't tell whether the repo sends anyone to your paid product.
- **Five platforms at once.** One paid option plus your own product converts better than a menu.

## Related skills
- [launch-open-source-funnel](../../launch/launch-open-source-funnel/SKILL.md): turn a free repo into users of a paid product.
- [launch-github-repo-seeding](../../launch/launch-github-repo-seeding/SKILL.md): get the repo its first stars and visitors.
- [monetization-payment-setup](../monetization-payment-setup/SKILL.md): when you're ready to sell, not just accept tips.
