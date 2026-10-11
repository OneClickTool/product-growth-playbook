# 08 · Rules and risks

Things that can cost you the account, the checkmark or trust. Checked 2026-10-11.

## X automation rules ([source](https://help.x.com/en/rules-and-policies/x-automation))
- No duplicate or substantially similar posts on one account or across accounts you run.
- No automated replies or mentions to reach people unsolicited; replies triggered by keyword search alone are banned.
- No scripting the X website (non-API automation); it can lead to permanent suspension.
- No automated posting about trending topics to ride or manipulate them.
- You're responsible for what third-party apps do with your account. Read what a tool does before connecting it.

Allowed: scheduling your own original posts through X or a tool that uses the official API.

## X Premium ([source](https://help.x.com/en/using-x/x-premium))
- Changing profile photo, display name or @handle removes the blue checkmark until the account is reviewed again.
- X can remove the checkmark if you break the Terms or the account is suspended.

## Temporary label: "may impact its reach"
An automated label X can add when it suspects spam or platform manipulation. It lowers reach until a review clears it.
X doesn't say which action triggered it (sources: user reports collected by
[Circleboom](https://circleboom.com/blog/why-does-my-x-account-have-a-label), not official X docs).

> **Real case (the maintainer's account, 2026-10-11).** Posting went from ~1 a day to 6 posts + 9 replies a day in 3
> days, impressions jumped ~10×, and the profile photo was changed the same day. X added the label, then removed it
> about 2 hours later ("not found to contain spam"). The trigger is a guess, not confirmed by X.
> Full pattern: [flow/analytics-pattern.md](../flow/analytics-pattern.md).

To lower the odds:
- Ramp up over 2–3 weeks: don't jump from 1 to 15 actions a day.
- No mass follows or follow/unfollow cycles; keep "following" from running far ahead of followers.
- Link in the bio or first reply, not the same URL in every post or reply.
- No auto-reply, auto-follow or auto-DM tools.
- Don't stack risky signals on one day (profile change + activity spike + many links).
- If reach still looks low after the label is removed, check X's **Under the Hood** report when it's available to you
  ([glossary](../reference/glossary.md)).

## Honesty and disclosure ([FTC Endorsement Guides FAQ](https://www.ftc.gov/business-guidance/resources/ftcs-endorsement-guides-what-people-are-asking))
- Say it's your product when you recommend it ("I built this").
- Disclose affiliate links, sponsorships and free products in the post itself.
- No fake reviews, bought followers or bought engagement.
- Income or user numbers must be real, with time range and base. More: [social-credible-posting](../../skills/social/social-credible-posting/SKILL.md).

## Tools to avoid
Anything that auto-replies, auto-DMs, auto-follows, scrapes x.com or "bypasses Cloudflare". See the watch-outs in
[reference/x-repos.md](../reference/x-repos.md).
