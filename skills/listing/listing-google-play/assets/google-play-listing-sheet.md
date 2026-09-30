# Google Play listing sheet

Fill this before opening Play Console. Keep it in your repo (e.g. `store/google-play.md`) and update it every release.

## Level 1: required

| Field | Limit | Value | Count |
|---|---|---|---|
| App name | 30 chars | | |
| Short description | 80 chars | | |
| Full description | 4,000 chars | see below | |
| App or game | — | | |
| Free or paid | cannot switch free → paid | | |
| Category + tags | — | | |
| Contact email | required | | |
| Website / phone | optional | | |
| Privacy policy URL | must open | | |
| App icon | 512×512 PNG | `store/android/icon-512.png` | |
| Feature graphic | 1024×500 | `store/android/feature.png` | |
| Phone screenshots | 2–8 | `store/android/phone-*.png` | |
| Tablet screenshots | if supported | | |
| Promo video | YouTube URL, optional | | |
| Countries | — | | |

### Full description
<!-- Indexed for search: use each target phrase 2–4 times naturally. No "#1 / best / free". -->

### App content declarations
- [ ] Privacy policy
- [ ] App access (reviewer login / instructions):
- [ ] Ads: yes / no
- [ ] Content rating (IARC) answers:
- [ ] Target audience and content:
- [ ] Data safety (table below)
- [ ] Other declarations that apply (news, health, financial features, government):

| Data type | Collected / shared | By (app / SDK) | Purpose | Optional? |
|---|---|---|---|---|

### Testing (new personal accounts)
- Closed test start date: ____ → 14 days → earliest production access: ____
- Testers (≥ 12, opted in the whole time):

### Release
- [ ] `.aab` uploaded, release notes written
- [ ] Staged rollout: 20% → 50% → 100% (check crashes/ANRs at each step)

## Level 2: optimize
- [ ] Title + short description carry main keywords
- [ ] Screenshots have captions; feature graphic readable
- [ ] Translations for top markets
- [ ] Store listing experiment running (one variable)
- [ ] In-App Review API prompt after a success moment

## Level 3: grow
- [ ] Custom store listings (country / URL / audience)
- [ ] Promotional content for the next event or update
- [ ] Pre-registration (new app or game)
