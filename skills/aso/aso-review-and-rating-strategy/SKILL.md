---
name: aso-review-and-rating-strategy
description: Raise an app's rating and review volume within App Store and Google Play rules, covering when to trigger the native review prompt, how to handle unhappy users, and templates for replying to reviews. Use when an app's rating is low or has few ratings, before adding a review prompt, after a bad update, or when someone asks "how do I get more reviews", "improve my app rating", "when to ask for a review", or "how to reply to bad reviews".
license: MIT
metadata:
  category: aso
  difficulty: beginner
  time: 45-60 min
  version: 1.0.0
  author: nvminhtu
---

# Review & Rating Strategy

> In under an hour you will have a review-prompt plan (trigger, timing, limits), a support path for unhappy
> users, and reply templates for the reviews you already have.

## Goal
More ratings, a higher average and fewer angry 1★ reviews, without breaking the rules that get apps rejected
or removed. Ratings affect both ranking and whether people install.

## When to use
- Fewer than ~100 ratings, or an average below 4.3★.
- You're about to add a review prompt.
- A bad release caused a wave of negative reviews.
- **Not for:** fixing the root cause of bad reviews. If people hate a bug, fix the bug first.

## Inputs
- Current rating, number of ratings, and the last 50 reviews.
- Your app's "success moments": when a user just got real value (finished a workout, exported a file, hit a streak).
- Whether you have in-app support or feedback today.

## Rules you must follow
- **App Store:** use the system prompt (`SKStoreReviewController` / StoreKit `requestReview`). Custom review prompts
  are not allowed. The system shows the prompt **at most 3 times in 365 days** per user and may decide not to show it.
  You can **reset your summary rating** when you release a new version (use it rarely).
- **Google Play:** use the **In-App Review API**. There is a quota, so don't call it from a button. Don't ask any
  question before the prompt that could bias the answer (e.g. "Do you like the app?" and then only sending happy users
  to the prompt).
- **Both stores:** never offer rewards, discounts or content in exchange for ratings. Don't write or buy fake reviews.

## Steps
1. **Read your reviews (10 min).** Tag the last 50 by theme (bug, missing feature, price, praise). The top negative
   theme is your #1 fix. Put it on the roadmap and mention the fix in release notes.
2. **Pick the trigger (10 min).** Call the native prompt right *after* a success moment, never at launch, never during
   a task, never after an error. Add guards: the user has used the app on at least 3 different days, completed the
   success action at least 2 times, and hasn't seen a crash this session.
3. **Give unhappy users a better door (10 min).** Add a visible "Send feedback" / "Report a problem" item in settings
   and on error screens. It goes to *you*, not the store. This is separate from the review prompt, so it's allowed on
   both stores.
4. **Reply to reviews (15 min now, then weekly).** Reply to every 1–3★ review within 48 hours: thank them, be
   specific, say what you fixed or will fix, and give a support contact. The reviewer is notified of your reply,
   and many people update their rating when the issue is fixed.
5. **Measure.** Track ratings per week and the average of *new* ratings (not the lifetime average), before and after
   the change.

## Prompt (copy-paste)
Replace everything in `{{ }}`.

````text
You are an app growth specialist. Improve my app's ratings within App Store and Google Play rules.

App: {{what it does}}   Platforms: {{iOS / Android}}
Rating: {{average}} from {{count}} ratings
Last 30-50 reviews: {{paste}}
Success moments in the app: {{actions where users just got value}}
Current review prompt (if any): {{when it triggers}}

1. Group the reviews by theme with counts; name the #1 thing to fix.
2. Design the native review-prompt trigger: which success moment, the guard conditions, and when NOT to show it.
   Follow the rules: iOS system prompt only (max 3 times in 365 days), Google In-App Review API without
   a biasing question beforehand, no incentives.
3. Design the in-app feedback path for unhappy users (where it lives, what it asks).
4. Write replies to the 5 most negative reviews (under 350 characters each, specific, no copy-paste feel)
   and 3 reusable reply templates: bug fixed, feature request, pricing complaint.
````

## Example output

> **Illustrative example.** Fictional app and numbers, shown for format.

**Trigger:** after the user logs their 3rd daily goal completion, on a day with no crash, and at least 5 days after
install. Never during onboarding or on the paywall.

**Reply to a 1★ "Reminders stopped working after update":**
> Sorry about that, Linh. Version 2.3 broke reminders on some Android 14 phones. It's fixed in 2.3.1, out now.
> If it still happens, email help@sipwell.app and I'll look into it personally. — Tu, developer

Result in 4 weeks: new ratings went from 2 to 11 per week, and the average of new ratings from 3.9 to 4.6.

## Common mistakes
- **Prompting on app launch.** The user hasn't got any value yet, so you get low ratings or nothing.
- **"Enjoying the app?" → only happy users go to the store.** Google explicitly prohibits biasing questions, and it
  looks bad on any platform.
- **Offering rewards for reviews.** Both stores prohibit it, and it can get the app removed.
- **Defensive replies.** Arguing in public costs you more installs than the review itself.

## Related skills
- [aso-screenshot-strategy](../aso-screenshot-strategy/SKILL.md): ratings and screenshots sit on the same page.
- [aso-keyword-research](../aso-keyword-research/SKILL.md): better ratings help you rank for harder keywords.

## Credits
Written by [@nvminhtu](https://github.com/nvminhtu). Rules from Apple's App Store Review Guidelines (5.6.1, App Store
Reviews), Apple's `requestReview` documentation, Android Developers "In-App Review API" guidelines, and Google Play's
ratings and reviews policies.
