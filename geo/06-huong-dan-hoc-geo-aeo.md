# Hướng dẫn học GEO & AEO

> Bản tiếng Việt của [GEO & AEO: a learning guide](../skills/launch/launch-geo-aeo-feature-preview/references/geo-aeo-learning-guide.md).
> Bản gốc tiếng Anh kiểm tra ngày 18/10/2026. Nếu hai bản lệch nhau, theo bản tiếng Anh.

Đọc một lần từ đầu tới cuối (khoảng 40 phút). Sau đó dùng [skill trang preview tính năng](07-skill-trang-preview-tinh-nang.md)
để áp dụng cho một tính năng. AI search đổi nhanh: mỗi quý kiểm tra lại các trang chính thức ở phần [Nguồn](#nguon).

## Mục lục

1. [Các thuật ngữ](#1-cac-thuat-ngu)
2. [Câu trả lời AI chọn nguồn thế nào](#2-cau-tra-loi-ai-chon-nguon-the-nao)
3. [Tài liệu chính thức nói gì](#3-tai-lieu-chinh-thuc-noi-gi)
4. [Nghiên cứu nói gì](#4-nghien-cuu-noi-gi)
5. [Ba trụ cột](#5-ba-tru-cot-cau-truc-uy-tin-hien-dien)
6. [GEO khi sản phẩm chưa có](#6-geo-khi-san-pham-chua-co)
7. [Cho bot vào (robots.txt)](#7-cho-bot-vao-robotstxt)
8. [Theo dõi hằng ngày](#8-theo-doi-hang-ngay)
9. [Lầm tưởng](#9-lam-tuong)
10. [Kế hoạch học 4 tuần](#10-ke-hoach-hoc-4-tuan)

---

## 1. Các thuật ngữ

| Thuật ngữ | Nghĩa đơn giản | Xuất hiện ở đâu |
|---|---|---|
| **SEO** (search engine optimization) | Đưa trang lên **hạng cao** trong danh sách link. | Kết quả cổ điển của Google, Bing |
| **AEO** (answer engine optimization) | Đưa một đoạn văn **được dùng làm câu trả lời trực tiếp** cho một câu hỏi. | Featured snippet, People Also Ask, trợ lý giọng nói, AI Overviews |
| **GEO** (generative engine optimization) | Trang của bạn **được trích, hoặc sản phẩm được nhắc tên** trong câu trả lời do AI viết. | ChatGPT search, Perplexity, Google AI Overviews / AI Mode, Copilot, Gemini, Claude |
| **LLMO / AI SEO** | Tên khác của GEO. | Blog của các bên bán dịch vụ |
| **Citation (trích dẫn)** | Câu trả lời đặt link tới trang bạn làm nguồn. | Mọi công cụ AI |
| **Mention / recommendation (nhắc tên / giới thiệu)** | Câu trả lời nêu tên sản phẩm của bạn, tốt nhất là trong danh sách ngắn. | Chủ yếu ChatGPT, Perplexity, Gemini |
| **Grounding query** | Lượt tìm AI chạy ngầm để kiếm nguồn. | Báo cáo AI Performance của Bing |
| **Query fan-out** | Một câu hỏi bị tách thành nhiều lượt tìm chạy ngầm. | Google AI Mode, ChatGPT |

AEO và GEO chồng lên nhau. Thực tế: **AEO = viết câu trả lời sao cho lấy ra được; GEO = là nguồn mà mô hình đủ tin để
trích hoặc giới thiệu.** Cả hai nằm trên SEO bình thường, không thay thế nó.

## 2. Câu trả lời AI chọn nguồn thế nào

Phần lớn sản phẩm AI search chạy cùng một vòng (retrieval-augmented generation):

```
Câu hỏi của người dùng
   │
   ▼
Fan-out: 3–20 lượt tìm ngầm ("best X for Y", "X vs Z", "X pricing", "site:official")
   │
   ▼
Lấy trang: từ chỉ mục của công cụ (Google, Bing, bot riêng)  ← bạn phải cho bot đọc + được index
   │
   ▼
Chọn đoạn: các khối ngắn trả lời rõ một câu hỏi con          ← AEO: cấu trúc
   │
   ▼
Viết câu trả lời + trích các đoạn đã dựa vào                  ← GEO: uy tín, dữ kiện, đồng thuận
```

Ba điều rút ra:

- **Không index thì không được trích.** Nếu công cụ không đọc được trang, mọi thứ khác vô nghĩa.
- **Đoạn văn thắng, không phải cả trang.** Một khối 40–60 chữ rõ ràng dưới tiêu đề dạng câu hỏi thì dễ lấy. Một mảng
  chữ quảng cáo dày đặc thì không.
- **Site khác cũng tính.** Công cụ còn lấy cả thread Reddit, review, danh bạ, chữ trên YouTube và tin tức. Những gì
  *họ* nói về bạn quyết định bạn có được giới thiệu hay không.

## 3. Tài liệu chính thức nói gì

Đây là những "luật" duy nhất. Mọi thứ khác trong bài là nghiên cứu hoặc kinh nghiệm.

**Google (AI Overviews, AI Mode).** Theo [AI features and your website](https://developers.google.com/search/docs/appearance/ai-features) (cập nhật 10/12/2025):

- Muốn được hiện, trang phải **được index và đủ điều kiện hiện snippet**. **Không có yêu cầu thêm** nào, không cần tối
  ưu đặc biệt.
- Bạn **không cần** file máy đọc mới, file chữ cho AI hay markup schema.org đặc biệt.
- Lượt bấm và lượt hiển thị từ tính năng AI được **tính trong Search Console → Performance, loại tìm kiếm "Web"**.
  Không có báo cáo AI riêng.
- Công cụ điều khiển: `nosnippet`, `data-nosnippet`, `max-snippet`, `noindex`. `Google-Extended` điều khiển việc dùng
  trang để huấn luyện và grounding cho Gemini, không phải cho Search.

**Chính sách spam của Google** ([Spam policies for Google web search](https://developers.google.com/search/docs/essentials/spam-policies)). Ba điều quan trọng với trang preview tính năng:

- **Misleading functionality (chức năng gây hiểu lầm)**: trang làm người dùng tưởng họ dùng được một dịch vụ mà thực
  ra không có. Nút "Dùng thử ngay" cho tính năng chưa tồn tại chính là kiểu này.
- **Doorway abuse (trang cửa ngõ)**: nhiều trang gần giống hệt nhau làm ra để lên hạng cho các truy vấn na ná.
- **Scaled content abuse (nội dung hàng loạt)**: nhiều trang sinh ra chủ yếu để thao túng thứ hạng.

**OpenAI** ([Overview of OpenAI crawlers](https://developers.openai.com/api/docs/bots)):

- `OAI-SearchBot` quyết định bạn có được xuất hiện trong câu trả lời **ChatGPT search** không. Cho phép nó trong
  robots.txt và tường lửa. Thay đổi mất khoảng 24 giờ.
- `GPTBot` dùng để **huấn luyện** mô hình. Chặn nó không làm bạn biến mất khỏi ChatGPT search.
- `ChatGPT-User` lấy trang khi người dùng yêu cầu; không phải bot tự động.

**Perplexity** ([Perplexity crawlers](https://docs.perplexity.ai/guides/bots)): cho phép `PerplexityBot` (kết quả tìm
kiếm, không huấn luyện) và các IP họ công bố; `Perplexity-User` lấy trang khi người dùng yêu cầu.

**Anthropic** ([About Claude's web crawlers](https://support.claude.com/en/articles/8896518-about-claude-s-web-crawler)):
`ClaudeBot` (huấn luyện), `Claude-SearchBot` (chất lượng tìm kiếm), `Claude-User` (lấy trang khi người dùng yêu cầu).

**Microsoft Bing** ([AI Performance in Bing Webmaster Tools, bản thử công khai, 2/2026](https://blogs.bing.com/webmaster/February-2026/Introducing-AI-Performance-in-Bing-Webmaster-Tools-Public-Preview)):
báo cáo **trích dẫn** đầu tiên do chính nhà cung cấp đưa ra, cho Copilot và câu trả lời AI của Bing (tổng lượt trích,
trang được trích, grounding query). Không có số lượt bấm.

**FTC Mỹ** ([Rule on consumer reviews and testimonials, 16 CFR Part 465](https://www.ftc.gov/news-events/news/press-releases/2024/08/federal-trade-commission-announces-final-rule-banning-fake-reviews-testimonials), hiệu lực 21/10/2024):
cấm review giả hoặc do AI viết, cấm review người nhà không công khai, cấm site review "độc lập" do chính bạn điều
khiển. Trang trước khi ra mắt **chưa có review nào**. Đừng bịa ra.

## 4. Nghiên cứu nói gì

**Bài GEO** (Aggarwal et al., Princeton / IIT Delhi, KDD 2024, [arXiv 2311.09735](https://arxiv.org/abs/2311.09735))
thử 9 cách viết lại một trang nguồn và đo xem câu trả lời AI dùng trang đó bao nhiêu. Mức thay đổi hiện diện so với
không sửa, trên GEO-bench của họ (Bảng 1, chỉ số đếm chữ):

| Cách viết lại | Thay đổi |
|---|---|
| Thêm trích dẫn lời của người có tên | khoảng **+41%** |
| Thêm số liệu | khoảng **+33%** |
| Trôi chảy (viết rõ, mượt hơn) | khoảng **+29%** |
| Dẫn nguồn | khoảng **+28%** |
| Thuật ngữ chuyên môn | khoảng +18% |
| Ngôn ngữ dễ hiểu | khoảng +14% |
| Giọng văn uy quyền | khoảng +12% |
| Nhồi từ khoá | khoảng **−9%** |

Hai phát hiện quan trọng nhất cho site nhỏ, mới:

- **Trang hạng thấp được lợi nhiều nhất.** Với trang ở vị trí thứ 5, *dẫn nguồn* tăng hiện diện khoảng +115%, trong
  khi trang ở vị trí 1 lại *mất* phần. GEO là một trong số ít đòn bẩy mà nhỏ không phải là bất lợi.
- **Kết quả khác nhau theo chủ đề.** Thử trên truy vấn của chính bạn; đừng chép phần trăm vào dự báo.

Coi các con số là **hướng đi, không phải lời hứa**: đây là thí nghiệm trong phòng lab trên một công cụ nghiên cứu và
Perplexity giai đoạn 2023–24.

**Thực tế ngành** (nghiên cứu của bên bán dịch vụ, kiểm lại trước khi trích): AI Overviews hiện trên phần lớn truy vấn
tìm thông tin và làm giảm lượt bấm vào link đầu; kiểu trang ChatGPT ưa thích đã dịch chuyển trong năm 2026 sang trang
chính thức, trang nguồn gốc và rời xa listicle. Bài học đúng qua các nghiên cứu: **trang "chính thức" của bạn với dữ
kiện rõ ràng, cộng với lượt nhắc thật từ nơi khác, thắng các listicle mỏng.**

## 5. Ba trụ cột: cấu trúc, uy tín, hiện diện

### Cấu trúc (làm cho lấy ra được) — đây là AEO

- Một trang = một câu hỏi chính. H1 nói rõ thứ đó là gì.
- Dưới mỗi H2 viết dạng câu hỏi ("X có chạy offline không?"), đặt **câu trả lời trước** trong 40–60 chữ, rồi mới tới
  chi tiết.
- Bảng cho so sánh, danh sách đánh số cho các bước, mỗi đoạn một ý.
- Chữ quan trọng nằm trong HTML, không nằm trong ảnh hay sau phần chỉ render bằng JavaScript. Ảnh có `alt`.
- Có ngày **"Cập nhật lần cuối"** hiện rõ và tên tác giả.
- Dữ liệu có cấu trúc khớp với chữ hiện trên trang (`SoftwareApplication`, `FAQPage`, `Article`), không bắt buộc.
  Google nói nó không cần cho tính năng AI; nó có thể giúp công cụ khác và là SEO tốt bình thường.

### Uy tín (làm cho đáng trích) — đây là GEO

- **Dữ kiện của riêng bạn**: số từ bài thử của bạn, một quyết định thiết kế có ngày, một benchmark đã đo. "Xuất một
  khung hình 4K trong 1,8 giây trên M2 Air trong bài thử của chúng tôi" hơn hẳn "nhanh như chớp".
- **Dẫn nguồn** cho mọi nhận định bên ngoài, có link.
- **Người có tên**: trích lời nhà thiết kế hay một người thử bản beta (có xin phép, và là người thật).
- **Cho thấy quá trình làm**: mockup, nhật ký soát thiết kế, changelog. Đây là trải nghiệm trực tiếp mà mô hình không
  lấy được ở đâu khác.

### Hiện diện (có mặt ở nơi AI tìm)

- Trả lời câu hỏi thật ở nơi người ta hỏi (Reddit, diễn đàn, Discord, Stack Exchange), chỉ đặt link khi có ích.
- Có mặt trong danh bạ và trang "alternatives" đang được trích cho truy vấn của bạn.
- Video ngắn có mô tả bằng chữ và phụ đề (lớp chữ mới là thứ được đọc).
- Nói cùng một câu định vị ở mọi nơi: trang About, trang store, danh bạ, hồ sơ. Mô hình tìm sự thống nhất giữa các
  nguồn.

## 6. GEO khi sản phẩm chưa có

Bạn làm GEO được trước cả khi viết code, vì thứ AI trích là **một câu trả lời rõ ràng**, không phải một bản app chạy
được. Thứ bạn đăng là **trang preview tính năng**: một trang trung thực về thứ bạn đang thiết kế.

**Trang preview được phép đưa ra**

- Vấn đề, bằng đúng chữ người ta dùng khi tìm (từ nghiên cứu của bạn).
- Thiết kế: mockup, video ngắn bấm thử prototype, nhật ký quyết định từ buổi soát thiết kế.
- Nó sẽ làm và không làm gì, và trạng thái: *Đang thiết kế · Chưa có · Dự kiến tháng {{month}}*.
- Một việc để làm: đăng ký danh sách chờ, bình chọn, góp ý mockup, đăng ký thử beta.
- So với thứ người ta đang dùng hôm nay thì sao (dữ kiện về đối thủ, có dẫn nguồn).

**Trang preview tuyệt đối không được**

- Nút "Tải về" hay "Dùng thử miễn phí" cho thứ chưa tồn tại (Google: chức năng gây hiểu lầm).
- Review giả, số người dùng giả, logo "đã lên báo" giả (luật FTC).
- Mỗi biến thể từ khoá một trang ("X cho sinh viên", "X cho giáo viên"… cùng một nội dung) (trang cửa ngõ / nội dung
  hàng loạt).
- Ảnh mockup trình bày như app thật. Ghi nhãn **"Mockup thiết kế"**.

**Vòng kiểm chứng.** Lượt truy cập cho biết người ta có đang tìm không; lượt đăng ký cho biết họ có muốn không.

```
Nghiên cứu câu hỏi  →  mỗi tính năng 1 trang preview  →  index + chia sẻ ở 3 nơi
        ▲                                                      │
        │                                                      ▼
 làm / sửa / bỏ  ◄──  đọc xu hướng 7 ngày  ◄──  sổ hằng ngày: lượt xem, lượt từ AI, đăng ký
```

## 7. Cho bot vào (robots.txt)

Quyết định theo mục đích. Một cấu hình hay dùng cho sản phẩm mới muốn được tìm thấy nhưng không bị dùng để huấn luyện:

```text
# Công cụ tìm kiếm và trả lời: cho phép
User-agent: Googlebot
Allow: /
User-agent: Bingbot
Allow: /
User-agent: OAI-SearchBot
Allow: /
User-agent: PerplexityBot
Allow: /
User-agent: Claude-SearchBot
Allow: /

# Huấn luyện mô hình: tuỳ bạn (chặn những bot này không làm bạn mất khỏi câu trả lời tìm kiếm)
User-agent: GPTBot
Disallow: /
User-agent: ClaudeBot
Disallow: /
User-agent: Google-Extended
Disallow: /

Sitemap: https://example.com/sitemap.xml
```

Sau đó kiểm tra tường lửa hay lớp chống bot của nơi host (Cloudflare, Vercel) không chặn mất các bot đã cho phép.

**`llms.txt`** là một đề xuất của cộng đồng ([llmstxt.org](https://llmstxt.org)). Google nói không cần file chữ cho
AI. Tốn 10 phút và không hại gì; đừng mong có lượt truy cập từ nó.

## 8. Theo dõi hằng ngày

### Đo được gì, ở đâu

| Tín hiệu | Công cụ | Độ trễ | Cho biết |
|---|---|---|---|
| Lượt hiển thị, lượt bấm, truy vấn theo trang (gồm AI Overviews / AI Mode) | Google Search Console → Performance → Web | 1–3 ngày | Google có đưa trang ra không, cho câu hỏi nào |
| Lượt trích trong Copilot / Bing | Bing Webmaster Tools → AI Performance | vài ngày | AI của Bing dùng trang bạn, kèm grounding query |
| Lượt truy cập từ trợ lý AI | GA4 (session source `chatgpt.com`, `perplexity.ai`, `claude.ai`, `gemini.google.com`, `copilot.microsoft.com`) | trong ngày | Có người bấm từ câu trả lời sang |
| Đăng ký danh sách chờ, bình chọn mockup | Key event GA4 + công cụ form của bạn | trong ngày | Họ muốn nó |
| Có được nhắc không | Tự hỏi AI (bên dưới) | hằng tuần | AI biết bạn tồn tại |

**Cài GA4 (10 phút).** Admin → Data display → Channel groups → tạo kênh riêng **"AI assistants"** với điều kiện
*Session source matches regex*:

```text
chatgpt\.com|chat\.openai\.com|perplexity\.ai|claude\.ai|gemini\.google\.com|copilot\.microsoft\.com|bing\.com/chat
```

Đặt nó **trên** "Referral" (luật nào khớp trước thì thắng). ChatGPT thường thêm `utm_source=chatgpt.com` vào link; các
trợ lý khác hay không gửi referrer, nên một phần lượt từ AI sẽ hiện là *Direct*. Số AI của bạn là **mức sàn**, không
phải tổng. Từ khoảng 5/2026 GA4 còn có sẵn kênh *AI Assistant*: xem [trang 02](02-do-khach-tu-ai.md).

### Đọc số hằng ngày mà không tự lừa mình

- **Lượt truy cập hằng ngày của trang mới là nhiễu.** Hôm nay 3, mai 11 chẳng nói lên gì. Đọc **trung bình trượt 7
  ngày** và so với **mốc gốc** (7 ngày trước khi bạn đăng hay sửa trang).
- **Mỗi lần sửa một thứ trên mỗi trang**, và ghi ngày vào sổ. Không thì bạn sẽ không biết cái gì có tác dụng.
- **Chờ độ trễ.** Index có thể mất vài ngày tới vài tuần; trích dẫn của AI thường tới sau lượt hiển thị trên Google.
  Chấm một trang sau **28 ngày**, không phải 3.
- **Đếm tỷ lệ, không phải một lần chạy.** Câu trả lời AI thay đổi. Chạy mỗi câu hỏi 3 lần và ghi "được nhắc 1/3".
- **Lượt đăng ký trên 100 lượt xem** là con số quyết định có làm hay không. Có lượt xem mà không ai đăng ký nghĩa là
  trang trả lời được câu hỏi nhưng tính năng không được muốn (hoặc trang chưa kêu gọi rõ).

### Tự hỏi AI hằng tuần (15 phút)

Chọn 5 câu một người mua sẽ gõ (biết vấn đề: "how do I…"; biết giải pháp: "best app for…"; so sánh: "X vs Y"). Chạy
mỗi câu 3 lần trên ChatGPT (bật search), Perplexity và Google. Ghi: *có nhắc không? trích trang nào? ai khác được
trích?* Các site được trích thay bạn chính là danh sách nơi cần liên hệ. Mẫu sổ ghi: [trang 04](04-theo-doi-hang-tuan.md).

## 9. Lầm tưởng

| Lầm tưởng | Thực tế |
|---|---|
| "GEO thay thế SEO." | Câu trả lời AI lấy trang từ chỉ mục tìm kiếm. Không index, không trích. |
| "Cần llms.txt / schema đặc biệt cho Google AI." | Google nói không cần file hay markup đặc biệt. |
| "Chặn GPTBot là ẩn khỏi ChatGPT." | Việc có mặt trong tìm kiếm do `OAI-SearchBot`. Huấn luyện và tìm kiếm là hai bot riêng. |
| "Viết trang riêng cho AI." | Google gọi các biến thể hàng loạt nhắm vào AI là nội dung hàng loạt. Viết cho người, cấu trúc rõ. |
| "Nhiều từ khoá hơn = nhiều trích dẫn hơn." | Nhồi từ khoá làm giảm hiện diện trong nghiên cứu GEO. |
| "Trang preview không lên hạng được vì app chưa ra." | Công cụ trích câu trả lời rõ và nội dung gốc. Preview trung thực có mockup và quyết định thiết kế chính là nội dung gốc. |
| "Số nhảy vọt sau bài Reddit nghĩa là GEO có tác dụng." | Tách kênh trong sổ ghi. GEO hiện ra qua nguồn tự nhiên + AI trong nhiều tuần. |

## 10. Kế hoạch học 4 tuần

| Tuần | Học | Làm (trên sản phẩm của bạn) |
|---|---|---|
| 1 | Mục 1–3 | Xác minh site trên Search Console và Bing Webmaster Tools; thêm kênh "AI assistants" trong GA4; sửa robots.txt; bắt đầu sổ ghi hằng ngày. |
| 2 | Mục 4–6 | Chọn 1–3 tính năng. Gom câu hỏi thật. Mỗi tính năng đăng một trang preview có mockup và danh sách chờ. |
| 3 | Mục 5 (hiện diện) | Trả lời 5 thread thật; lên 2 danh bạ đang được trích cho truy vấn của bạn; đăng video 30 giây đi qua mockup có phụ đề. |
| 4 | Mục 8–9 | Chạy bài tự hỏi AI hằng tuần. Chạy `traffic_trend.py` trên sổ ghi. Quyết định cho từng tính năng: làm, sửa trang, hay bỏ. |

## Nguồn

- Google Search Central: [AI features and your website](https://developers.google.com/search/docs/appearance/ai-features) · [Spam policies](https://developers.google.com/search/docs/essentials/spam-policies)
- OpenAI: [Overview of OpenAI crawlers](https://developers.openai.com/api/docs/bots)
- Perplexity: [Perplexity crawlers](https://docs.perplexity.ai/guides/bots)
- Anthropic: [Claude's web crawlers](https://support.claude.com/en/articles/8896518-about-claude-s-web-crawler)
- Microsoft: [AI Performance in Bing Webmaster Tools (public preview)](https://blogs.bing.com/webmaster/February-2026/Introducing-AI-Performance-in-Bing-Webmaster-Tools-Public-Preview)
- Aggarwal et al., [GEO: Generative Engine Optimization](https://arxiv.org/abs/2311.09735), KDD 2024
- FTC Mỹ: [Final rule banning fake reviews and testimonials](https://www.ftc.gov/news-events/news/press-releases/2024/08/federal-trade-commission-announces-final-rule-banning-fake-reviews-testimonials)
- [Đề xuất llms.txt](https://llmstxt.org)
- Kinh nghiệm thực tế: skill mã nguồn mở `ai-seo` trong [coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills) (MIT), cho checklist soát và mẫu nội dung.
