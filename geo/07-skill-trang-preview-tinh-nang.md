# Skill trang preview tính năng: GEO & AEO trước khi code

> Bản tiếng Việt của skill [launch-geo-aeo-feature-preview](../skills/launch/launch-geo-aeo-feature-preview/SKILL.md).
> Bản gốc tiếng Anh kiểm tra ngày 18/10/2026. Muốn cài skill cho agent, dùng bản tiếng Anh; trang này để đọc hiểu.

Trong một buổi chiều, bạn có 1–3 trang preview trung thực cho các tính năng đang thiết kế, cài sẵn để công cụ tìm kiếm
và AI trích được, cộng với một sổ ghi hằng ngày cho biết sau 28 ngày nên làm tính năng nào.

## Mục tiêu

Biết người ta muốn tính năng nào **trước khi** làm, bằng cách đăng mỗi tính năng một trang preview (vấn đề, mockup,
quyết định thiết kế, danh sách chờ), trả lời câu hỏi thật đủ tốt để được tìm thấy trên Google và được trợ lý AI trích.
Kết quả cuối: các trang, phần cài đặt đo lường, và quyết định làm / sửa / bỏ cho từng tính năng, dựa trên số lượt xem
và lượt đăng ký của chính bạn.

Mới với GEO và AEO? Đọc [Hướng dẫn học GEO & AEO](06-huong-dan-hoc-geo-aeo.md) trước (40 phút).

## Khi nào dùng

- Bạn có mockup hoặc buổi soát thiết kế, chưa có code, và muốn bằng chứng nhu cầu trước khi làm.
- Bạn muốn sản phẩm xuất hiện trong câu trả lời AI ("best app for…", "how do I…") ngay từ ngày đầu.
- Bạn có một site (dù chỉ một trang) để đăng trang và sửa robots.txt.
- **Không dành cho:** sản phẩm đã live cần lượt cài trên store → [aso-keyword-research](../skills/aso/aso-keyword-research/SKILL.md).
  Tìm câu hỏi ngay từ đầu → [research-where-users-ask](../skills/research/research-where-users-ask/SKILL.md).
  Checklist ra mắt đầy đủ → [launch-pre-launch-checklist](../skills/launch/launch-pre-launch-checklist/SKILL.md).

## Cần chuẩn bị

- 1–3 tính năng đang thiết kế, mỗi cái có ít nhất một mockup (xuất từ Figma, ảnh chụp prototype).
- Ghi chú buổi soát thiết kế: quyết định, cái đã cắt, câu hỏi còn mở.
- 10+ câu hỏi hay lời phàn nàn thật về vấn đề (thread, review, autocomplete). Chưa có → làm
  [research-where-users-ask](../skills/research/research-where-users-ask/SKILL.md) trước.
- Quyền vào site, Google Search Console, Bing Webmaster Tools và GA4 (đều miễn phí).
- Một form danh sách chờ (chưa có thì xem [email-list-and-deliverability](../skills/email/email-list-and-deliverability/SKILL.md)).

## Các bước

1. **Cài đo lường trước khi đăng (30 phút).** Đây là ngày 0 của sổ ghi; không có mốc gốc thì không phân biệt được tăng
   trưởng với nhiễu.
    - Xác minh site trên [Google Search Console](https://search.google.com/search-console) và
      [Bing Webmaster Tools](https://www.bing.com/webmasters) (Bing có báo cáo *AI Performance* về lượt trích trong Copilot).
    - Trong GA4, thêm kênh riêng **"AI assistants"** đặt trên *Referral* (regex ở
      [hướng dẫn, mục 8](06-huong-dan-hoc-geo-aeo.md#8-theo-doi-hang-ngay)), và một key event cho form danh sách chờ kèm tên
      tính năng.
    - Chép [daily-traffic-log.csv](../skills/launch/launch-geo-aeo-feature-preview/assets/daily-traffic-log.csv) (các dòng
      trong đó là ví dụ minh hoạ; xoá đi) và ghi 7 ngày gần nhất làm mốc gốc.
2. **Mở cửa cho bot (10 phút).** robots.txt cho phép `Googlebot`, `Bingbot`, `OAI-SearchBot`, `PerplexityBot`,
   `Claude-SearchBot`; bot huấn luyện (`GPTBot`, `ClaudeBot`, `Google-Extended`) tuỳ bạn. Kiểm tra lớp chống bot của
   nơi host không chặn chúng. Trang phải có trong sitemap và không `noindex`.
3. **Chọn câu hỏi cho từng tính năng (20 phút).** Từ các câu hỏi đã gom, chọn **một câu hỏi chính** cho mỗi tính năng
   và 4–6 câu hỏi con (giá, nền tảng, "vs X", "có làm được…"). Đó là H1 và các H2. Viết bằng chữ của người dùng, không
   phải tên tính năng của bạn. Trước khi viết, hỏi ChatGPT (bật search), Perplexity và Google câu hỏi chính và ghi lại
   ai được trích: đó là đối thủ và cũng là danh sách nơi cần liên hệ.
4. **Viết mỗi tính năng một trang preview (40 phút mỗi trang).** Dùng [mẫu trang](08-mau-trang-preview-tinh-nang.md):
   dòng trạng thái ("Đang thiết kế · chưa có"), câu trả lời ngắn 40–60 chữ, H2 dạng câu hỏi với câu trả lời đặt trước,
   mockup có nhãn, bảng "so với hiện nay" có dẫn nguồn, các quyết định thiết kế từ buổi soát, những gì nó sẽ không làm,
   FAQ, và **một** hành động (danh sách chờ hoặc bình chọn). Thêm dữ kiện của riêng bạn: một con số từ bài thử
   prototype, một câu trích của nhà thiết kế hay người thử (thật, có xin phép).
5. **Soát độ trung thực (5 phút).** Không có nút Tải về / Mua / Dùng thử, không review hay số người dùng bạn không có,
   mọi ảnh ghi *Mockup thiết kế*, không có trang gần trùng nhau cho từng từ khoá. Những thứ này phạm chính sách spam
   của Google (chức năng gây hiểu lầm, trang cửa ngõ, nội dung hàng loạt) và luật review của FTC; xem
   [hướng dẫn, mục 6](06-huong-dan-hoc-geo-aeo.md#6-geo-khi-san-pham-chua-co).
6. **Đăng và xin index (15 phút).** Đặt link tới mỗi trang từ trang chủ hoặc trang `/roadmap`, gửi sitemap, xin index
   trong Search Console (URL Inspection) và Bing (URL Submission). Ghi ngày đăng vào sổ.
7. **Có mặt ở 3 nơi trong tuần đầu (60 phút).** Công cụ AI cũng trích site khác. Trả lời 3–5 thread thật nơi câu hỏi
   đang được hỏi (chỉ đặt link khi có ích, nói rõ là của bạn), đăng video 30 giây đi qua mockup có phụ đề, và đưa sản
   phẩm lên 1–2 danh bạ đang hiện cho câu hỏi đó. Gắn UTM cho mọi link.
8. **Ghi hằng ngày, đọc hằng tuần (10 phút/ngày, 15 phút/tuần).** Mỗi ngày thêm lượt xem theo trang và nguồn, cộng
   lượt đăng ký. Mỗi tuần chạy bài tự hỏi AI (5 câu × 3 lần × ChatGPT, Perplexity, Google; ghi "được nhắc 1/3") và:

    ```bash
    python3 scripts/traffic_trend.py daily-traffic-log.csv --start 2026-10-01
    ```

    Script so 7 ngày gần nhất với 7 ngày mốc gốc, tách tìm kiếm / AI / mạng xã hội / direct, cho trung bình trượt 7 ngày
    và lượt đăng ký trên 100 lượt xem theo từng trang. Mỗi tuần sửa một thứ trên mỗi trang và ghi ngày.
9. **Quyết định ở ngày 28.** Với mỗi tính năng: **làm** (lượt xem tăng và có người đăng ký), **sửa trang** (lượt xem
   đứng yên: câu hỏi hoặc câu trả lời ngắn chưa đúng), **nghĩ lại tính năng** (có lượt xem nhưng không ai đăng ký),
   hoặc **bỏ**. Ngưỡng của script (tối thiểu 3 lượt/ngày, +10% so với mốc gốc, 2 đăng ký trên 100 lượt xem) là quy tắc
   kinh nghiệm khởi đầu của repo này, không phải chuẩn ngành: chỉnh theo ngách của bạn. Gửi email báo quyết định cho
   danh sách chờ.

## Prompt (chép và dán)

Dùng được trên Claude, ChatGPT, Gemini, Cursor. Thay mọi chỗ trong `{{ }}`. Đính kèm mockup nếu công cụ nhận ảnh.
Prompt giữ nguyên tiếng Anh vì trang preview thường viết cho người đọc tiếng Anh; muốn trang tiếng Việt thì thêm dòng
"Write the page in Vietnamese."

````text
You are a GEO/AEO editor for a small software team. We are promoting a feature we have NOT built yet.
Write an honest feature preview page that search engines and AI assistants (Google AI Overviews, ChatGPT search,
Perplexity, Copilot) can find, quote and cite.

Product: {{product, platform, who it's for}}
Feature: {{name + one line}}
Status: in design, target {{month year}}
Real user questions (verbatim, with links where public): {{10+ questions}}
Design review notes: {{decisions, what we cut, open questions}}
Mockups: {{list what each mockup shows}}
Facts we own: {{prototype test numbers, quotes with names and permission; or "none yet"}}
What people use today: {{competitors / workarounds, with source links}}
Waitlist URL: {{url}}

Do this:
1. Pick the ONE main question for the H1 and 4-6 sub-questions for H2s, in the users' words. Explain the choice in 2 lines.
2. Write the page in Markdown:
   - Status line at the top: "In design · not available yet", target month, last updated date, author.
   - "The short answer": 40-60 words that make sense on their own.
   - Each H2 is a question; the first sentence under it answers it directly.
   - A comparison table vs. what people use today, with every outside fact linked to its source.
   - "Design decisions so far" from the review notes, and "What it won't do (yet)".
   - FAQ (availability, price, platform), then one call to action: join the waitlist or vote.
   - Mark every image "Design mockup".
3. Rules: no Download/Buy/Trial buttons, no invented reviews, numbers, users or logos; if a fact is missing, write
   {{TODO: fact}} instead of guessing. No keyword stuffing. Write for a person first.
4. After the page, list: the title tag (under 60 chars), meta description (~150 chars), 5 prompts I should check
   weekly in AI assistants, and 3 places (threads, directories) where I should answer this question this week.
````

## Ví dụ kết quả

> **Ví dụ minh hoạ.** Sản phẩm hư cấu và số bịa ra để thấy định dạng.

*Snapsort*, một app sắp xếp ảnh cho Mac đang thiết kế. Tính năng: đổi tên hàng loạt. Trang `/features/batch-rename`:

> **Status: In design · not available yet.** Planned for Feb 2027. Last updated 1 Oct 2026 by Linh, product designer.
>
> **The short answer.** Batch Rename will rename hundreds of photos on a Mac by date, place or camera in one step.
> Unlike Finder's rename, it shows every new file name before applying it and can undo the whole batch.
>
> **Can I rename photos by the date they were taken on Mac?** Yes, that's the default pattern…

Sổ ghi hằng ngày, ngày 28, từ `traffic_trend.py`:

| Trang | Lượt xem (7 ngày) | So với mốc gốc | Từ AI | Đăng ký / 100 lượt | Quyết định |
|---|---|---|---|---|---|
| /features/batch-rename | 73 | +480% | 7 | 5,5 | Làm: tiếp tục thiết kế, phỏng vấn 5 người trong danh sách chờ |
| /features/smart-albums | 41 | +270% | 5 | 4,9 | Giữ trang; thử câu trả lời ngắn sắc hơn |
| /features/cloud-sync | 9 | +12% | 0 | 0,0 | Nghĩ lại: người ta không tìm thứ này |

Tự hỏi AI tuần 4: "best app to batch rename photos on Mac", Perplexity: được nhắc 1/3 (trang được trích:
/features/batch-rename); ChatGPT 0/3 (trích hai thread Reddit → vào trả lời hai thread đó).

## Lỗi hay gặp

- **"Tải về ngay" cho tính năng chưa tồn tại.** Với Google và với người đọc đó là chức năng gây hiểu lầm. Hành động
  duy nhất là danh sách chờ, bình chọn hoặc góp ý.
- **Chấm sau 3 ngày.** Trang mới mất vài ngày tới vài tuần để được index, và lâu hơn để được trích. Đọc trung bình 7
  ngày và quyết định ở ngày 28.
- **Sửa năm thứ cùng lúc.** Mỗi tuần một thay đổi trên mỗi trang, có ghi ngày, không thì không bao giờ biết cái gì có
  tác dụng.
- **H2 là tên tính năng ("Giới thiệu SmartSort™").** Không ai hỏi thế. Dùng câu hỏi người ta gõ.
- **Chỉ có site của mình.** Câu trả lời AI dựa nhiều vào Reddit, review và danh bạ. Không hiện diện thì được đọc
  nhưng không được giới thiệu.
- **Bỏ qua lượt đăng ký.** Lượt xem cho biết người ta nhìn; đăng ký trên 100 lượt xem cho biết họ muốn. Làm dựa trên
  con số thứ hai.
- **Tin số lượt từ AI là tổng.** Một số trợ lý không gửi referrer; lượt đó trốn trong *Direct*.

## Skill liên quan (bản tiếng Anh)

- [research-where-users-ask](../skills/research/research-where-users-ask/SKILL.md): gom câu hỏi thật trước.
- [research-source-finding](../skills/research/research-source-finding/SKILL.md): dẫn nguồn đáng tin trên trang.
- [social-build-in-public](../skills/social/social-build-in-public/SKILL.md): chia sẻ mockup và quyết định thiết kế trong lúc làm.
- [email-beta-program](../skills/email/email-beta-program/SKILL.md): biến danh sách chờ thành người thử beta khi bắt tay làm.
- [launch-pre-launch-checklist](../skills/launch/launch-pre-launch-checklist/SKILL.md): khi một tính năng thắng và đã có ngày ra.

## Ghi công

Viết bởi [@nvminhtu](https://github.com/nvminhtu). Nguồn: Google Search Central
([AI features and your website](https://developers.google.com/search/docs/appearance/ai-features),
[spam policies](https://developers.google.com/search/docs/essentials/spam-policies)),
[OpenAI crawlers](https://developers.openai.com/api/docs/bots), [Perplexity crawlers](https://docs.perplexity.ai/guides/bots),
[Anthropic crawlers](https://support.claude.com/en/articles/8896518-about-claude-s-web-crawler),
[Bing AI Performance](https://blogs.bing.com/webmaster/February-2026/Introducing-AI-Performance-in-Bing-Webmaster-Tools-Public-Preview),
Aggarwal et al., [GEO: Generative Engine Optimization](https://arxiv.org/abs/2311.09735) (KDD 2024),
[luật review của FTC](https://www.ftc.gov/news-events/news/press-releases/2024/08/federal-trade-commission-announces-final-rule-banning-fake-reviews-testimonials),
và skill `ai-seo` giấy phép MIT trong [coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills).
