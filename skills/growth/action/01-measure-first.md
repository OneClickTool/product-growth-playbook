# Step 1: Measure first

**Week 1 · ~3 hours** · [← Action plan](README.md) · Next: [Step 2](02-owned-audience.md)

## Goal
Know where every install or sign-up comes from before you spend time on any channel.

## Steps
- [ ] **Pick one hero product** to push for the next 6 weeks. Other products support it, they don't compete with it.
- [ ] **One landing page** for the hero product: what it does in one line, a short demo (GIF or video), the store or
      download button, and one email field ("tell me about updates").
- [ ] **One tracked link per channel.** Write them in `growth/tracking.md`:

      | Channel | Link | Tool |
      |---|---|---|
      | Other products (cross-promo) | `...?utm_source=extension&utm_medium=crosspromo` | UTM on landing page |
      | Short video | `...?utm_source=tiktok&utm_medium=video` | UTM |
      | Reddit | `...?utm_source=reddit&utm_medium=post` | UTM |
      | App Store links | store campaign link (provider + campaign token) | App Store Connect App Analytics |

      For App Store products, use App Store Connect campaign links so store installs are attributed. For direct
      downloads, count downloads on your own site with UTM. Set up analytics events with
      [launch-growth-stack-setup](../../launch/launch-growth-stack-setup/SKILL.md).
- [ ] **Write a baseline** for the last 4 weeks: store page views, installs or downloads, conversion (installs ÷ page
      views), email sign-ups, paying users. Missing numbers are fine; write "unknown" and start counting today.
- [ ] **Set a target** so you know what "working" means:
      [strategy-revenue-target](../../strategy/strategy-revenue-target/SKILL.md).

## Done when
Every channel you plan to use has its own link, and `growth/tracking.md` has a baseline row.

## Common mistakes
- Pointing every channel to the same plain store URL. You'll never know which one worked.
- Tracking only views or likes. Track the action you want: installs, sign-ups, purchases.
