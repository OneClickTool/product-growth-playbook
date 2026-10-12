# TikTok photo-post API: the facts

Source: [Content Posting API — photo post reference](https://developers.tiktok.com/doc/content-posting-api-reference-photo-post),
[get started](https://developers.tiktok.com/doc/content-posting-api-get-started),
[content sharing guidelines](https://developers.tiktok.com/doc/content-sharing-guidelines). Checked 2026-10-12.

## Request
`POST https://open.tiktokapis.com/v2/post/publish/content/init/`
Scope: `video.publish` (direct post) or `video.upload` (send to inbox). Header `Authorization: Bearer <user token>`.

```json
{
  "media_type": "PHOTO",
  "post_mode": "MEDIA_UPLOAD",
  "post_info": {
    "title": "max 90 UTF-16 runes",
    "description": "max 4000 UTF-16 runes"
  },
  "source_info": {
    "source": "PULL_FROM_URL",
    "photo_images": ["https://your-verified-domain/slide-1.jpg", "..."],
    "photo_cover_index": 0
  }
}
```

| Field | Values / limit |
|---|---|
| `media_type` | `PHOTO` only |
| `post_mode` | `DIRECT_POST` (publishes) or `MEDIA_UPLOAD` (user finishes in the TikTok app; needs app ≥ 31.8; inbox notification) |
| `privacy_level` (direct post) | One of the values returned by the creator-info query: `PUBLIC_TO_EVERYONE`, `MUTUAL_FOLLOW_FRIENDS`, `FOLLOWER_OF_CREATOR`, `SELF_ONLY` |
| `disable_comment`, `auto_add_music`, `brand_content_toggle`, `brand_organic_toggle` | Optional, direct post only |
| `is_aigc` | Optional; adds the AI-generated label |
| `photo_images` | Up to 35 public URLs on a domain/prefix you verified |
| `photo_cover_index` | 0-based cover slide |

## Limits and errors
| Limit | Error |
|---|---|
| 6 requests / minute / user token | HTTP 429 `rate_limit_exceeded` |
| Daily posts per account | `spam_risk_too_many_posts` |
| 5 pending inbox shares per 24 h | `spam_risk_too_many_pending_share` |
| Daily active-publisher quota per client app | `reached_active_user_cap` |
| Unaudited client app | Posts only to private accounts / `SELF_ONLY`: `unaudited_client_can_only_post_to_private_accounts` |

## What this means for the slideshow loop
- You **can't** choose a sound by API. Either `auto_add_music` (direct post) or a human picks a sound.
- Before your app passes TikTok's audit, API posts are private. That's why the Larry setup posts `SELF_ONLY` and a
  human switches it public after adding a sound.
- Direct posting requires a UI that shows the creator-info options (privacy, comment toggle, disclosure) to the user;
  the disclosure toggle must be off by default and branded content can't be `SELF_ONLY`.
- A separate TikTok **Business** API exists with its own endpoint; payloads aren't interchangeable
  ([bundle.social write-up](https://bundle.social/blog/tiktok-photo-posting-api), third party).
