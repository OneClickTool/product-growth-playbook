# 07 · Rules and risks: AI labels, ad disclosure, many accounts, automation

Checked 2026-10-12. TikTok's guidelines were re-released in August 2026, effective 2026-09-24; check the live pages.

## Disclose that you're promoting your own product
- TikTok requires the **content disclosure setting** for posts that promote a brand, product or service, including
  your own ("Your brand"). It adds a *Promotional content* / *Paid partnership* label.
  Sources: [Branded Content Policy](https://www.tiktok.com/legal/page/global/bc-policy/en),
  [Commercial Content Disclosure for creators](https://ads.tiktok.com/help/article/about-the-content-disclosure-setting-for-creators),
  [Regulated Goods, Services and Commercial Activities](https://www.tiktok.com/safety/en/policies-and-engagement/regulated-commercial-activities).
- TikTok's help page says the label itself doesn't change recommendation, but **undisclosed** commercial content may
  not be eligible for For You, and repeated failures can restrict or ban the account.
- If you pay or gift anyone to post about the app (affiliates, UGC creators), they must disclose too. In the US see the
  FTC's [Disclosures 101](https://www.ftc.gov/business-guidance/resources/disclosures-101-social-media-influencers).

## AI-generated images
- TikTok asks creators to label **realistic** AI-generated or heavily edited content (people, places, scenes that
  could pass as real) and auto-labels some content using C2PA metadata
  ([TikTok newsroom via AP/NBC](https://www.nbcnewyork.com/news/national-international/tiktok-to-start-labeling-ai-generated-content-as-technology-becomes-more-universal/5399109/)).
- The photo-post API has an `is_aigc` flag for this ([API reference](https://developers.tiktok.com/doc/content-posting-api-reference-photo-post)).
- An "AI room makeover" is honest *only if* the slideshow makes clear it's an AI result. Don't present AI images as a
  real renovation, a real customer, or a real testimonial.

## Many accounts, "slideshow farms" and automation
Some guides push running many faceless accounts per app. TikTok's Integrity and Authenticity rules
([guidelines](https://www.tiktok.com/safety/en/policies-and-engagement/integrity-authenticity)) allow more than one
account but ban:
- operating large networks of accounts controlled by one entity, or through automation, to spread content;
- registering or running accounts in bulk with automation;
- manipulating engagement signals (bought views, follow-for-follow, comment pods);
- using a second account to get around a restriction.

**Safe version:** one account per product (or one founder account), posts made by a person who publishes them,
engagement that's real. If you want more accounts, each should be a real, distinct voice (a co-founder, a creator you
pay and who discloses). Founders who ran several accounts: [notes](../case-studies/2026-other-founders-slideshow-notes.md).

## API limits that protect you from yourself
From the [photo-post reference](https://developers.tiktok.com/doc/content-posting-api-reference-photo-post):
6 requests per minute per user token; a daily post cap per account (`spam_risk_too_many_posts`); max 5 pending
inbox shares per 24 h; unaudited clients can only post privately. Don't try to route around these.

## New accounts
The cases (and most guides) warm up a new account before posting promotion: 3 days in one case, 7–14 days of
30–60 min normal use in the Larry skill. This is **practice, not a published TikTok rule**. It doesn't hurt: watch
and engage with your niche so you learn what it looks like.

## Claims we do not repeat
Unsourced claims seen in vendor posts and **not** used in this kit: "TikTok detects Midjourney images in half a second
and downranks them", "API posts from server IPs are penalized", "slideshows get 5× reach". If you need to decide based
on one of these, test it on your own account and log the result.
