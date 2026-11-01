# Mẫu trang preview tính năng

> Bản tiếng Việt của [Feature preview page: template](../skills/launch/launch-geo-aeo-feature-preview/references/feature-preview-page-template.md).
> Dùng cùng [skill trang preview tính năng](07-skill-trang-preview-tinh-nang.md).

Mỗi tính năng đang thiết kế nhưng chưa làm thì một trang. Trạng thái trung thực, mockup thật, mỗi mục trả lời trước,
một hành động rõ ràng. Chép vào site của bạn (Markdown, MDX, CMS) và thay mọi chỗ trong `{{ }}`.

Khung trang bên dưới giữ tiếng Anh vì trang preview thường viết cho người đọc tiếng Anh. Phần giải thích bằng tiếng
Việt nằm ngay trong từng ô `{{ }}`.

## URL và tiêu đề

- URL: `/features/{{feature-slug}}` (ngắn, đúng chữ người ta tìm; không để ngày trong slug).
- `<title>`: `{{Tên tính năng}}: {{làm gì, 5–8 chữ}} ({{Sản phẩm}})`, dưới 60 ký tự.
- Meta description: câu trả lời ngắn bên dưới, cắt còn khoảng 150 ký tự.

## Khung trang

```markdown
# {{Tên tính năng}}: {{làm gì, bằng chữ của người dùng}}

**Status: In design · not available yet.** Planned for {{tháng năm}}. Last updated {{ngày}} by {{tên, vai trò}}.

## The short answer
{{40–60 chữ. Tính năng sẽ làm gì, cho ai, và một điểm khác biệt. Không dùng chữ thổi phồng.
Ví dụ: "Batch Rename will rename hundreds of photos by date, place or camera in one step on Mac. Unlike Finder's
rename, it previews every new name before applying it and can undo the whole batch."}}

![Design mockup: {{mockup này cho thấy gì}}]({{mockup-1.png}})
*Design mockup, not the final app.*

## What problem does {{feature}} solve?
{{2–4 câu, bằng đúng chữ người ta dùng trong thread, review và lượt tìm bạn đã gom. Đặt link 1–2 thread công khai
làm bằng chứng vấn đề có thật.}}

## How will {{feature}} work?
1. {{Bước 1, một dòng}}
2. {{Bước 2}}
3. {{Bước 3}}

![Design mockup: {{màn 2}}]({{mockup-2.png}})
*Design mockup.* {{Tuỳ chọn: video prototype 30 giây có phụ đề.}}

## {{Feature}} vs. {{thứ người ta đang dùng}}
| | {{Cách hiện nay / đối thủ}} | {{Feature}} (planned) |
|---|---|---|
| {{tiêu chí người dùng quan tâm}} | {{dữ kiện, có link nguồn}} | {{hành vi dự kiến}} |
| {{tiêu chí}} | {{dữ kiện}} | {{dự kiến}} |
| Price | {{dữ kiện, nguồn}} | {{giá dự kiến hoặc "not decided"}} |

## Design decisions so far
From our design review on {{ngày}}:
- **{{Quyết định}}**: {{vì sao, một dòng}}. {{Tuỳ chọn trích lời: "…" — {{tên, vai trò}}}}
- **{{Quyết định}}**: {{vì sao}}.
- **Not doing:** {{cái đã cắt và vì sao}}.

## What it won't do (yet)
- {{Giới hạn 1}}
- {{Giới hạn 2}}

## FAQ
### When will {{feature}} be available?
{{Trả lời trung thực: tháng dự kiến, và "we'll email the waitlist first".}}
### How much will it cost?
{{Giá dự kiến, hoặc "Not decided yet. Waitlist members get {{ưu đãi}}."}}
### Does it work on {{nền tảng / offline / với X}}?
{{Câu trả lời ngắn đặt trước.}}

## Want it? Help shape it
[Join the waitlist]({{form-url}}?utm_source={{source}}&utm_campaign=preview-{{feature-slug}}) · or
[vote on the mockup / leave a comment]({{feedback-url}}). {{N}} design questions are still open: {{liệt kê 1–2}}.
```

## Checklist trước khi đăng

- [ ] Dòng trạng thái trên cùng nói rõ chưa có, kèm tháng dự kiến.
- [ ] Mọi ảnh ghi **Design mockup**. Không khung điện thoại giả với điểm đánh giá giả.
- [ ] Không có nút "Download", "Buy" hay "Start trial". Hành động duy nhất là danh sách chờ / bình chọn / góp ý.
- [ ] Không có review, số người dùng hay logo bạn không có.
- [ ] Câu trả lời ngắn dài 40–60 chữ và cắt riêng ra vẫn hiểu được.
- [ ] Mỗi H2 là một câu ai đó thật sự đã hỏi; câu trả lời là câu đầu tiên bên dưới.
- [ ] Mọi dữ kiện bên ngoài có link tới nguồn.
- [ ] Chữ nằm trong HTML (không in vào ảnh); ảnh có `alt`.
- [ ] Có ngày "Last updated" và tên tác giả.
- [ ] Trang có trong sitemap, có link từ trang chủ hoặc trang `/roadmap`, và không `noindex`.
- [ ] Form danh sách chờ bắn một key event GA4 (ví dụ `generate_lead` với `feature={{slug}}`).

## Dữ liệu có cấu trúc (tuỳ chọn)

Chỉ dùng khi khớp với trang đang hiện. Google nói không bắt buộc cho tính năng AI.

```json
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [{
    "@type": "Question",
    "name": "When will {{feature}} be available?",
    "acceptedAnswer": { "@type": "Answer", "text": "{{đúng chữ như trên trang}}" }
  }]
}
```

Đừng đánh dấu một tính năng chưa tồn tại là `SoftwareApplication` kèm điểm đánh giá hay giá bán.
