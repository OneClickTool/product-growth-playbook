# Hiện diện trên AI search: SEO, AEO, AIO, GEO

> Bản tiếng Việt của [Playbook: AI Search Visibility](../playbooks/ai-search-visibility.md). Bản gốc tiếng Anh kiểm tra
> ngày 21/10/2026. Nếu hai bản lệch nhau, theo bản tiếng Anh.

Bốn chữ viết tắt nghĩa là gì, chồng lên nhau ra sao, cái gì còn hiệu quả năm 2026, bằng chứng mạnh tới đâu, và làm theo
thứ tự nào cho một sản phẩm nhỏ. Đây là tài liệu kiến thức: đọc một lần, rồi dùng các skill ở cuối trang.

> AI search đổi theo từng tháng. Kiểm tra lại phần [Nguồn](#nguon) trước khi trích một con số cho ai. Muốn hiểu sâu cơ
> chế (AI chọn nguồn thế nào, cho bot vào, đo hằng ngày), đọc [Hướng dẫn học GEO & AEO](06-huong-dan-hoc-geo-aeo.md).

## Tóm tắt một phút

- **SEO** giúp trang được index và xếp hạng. **AEO** giúp một đoạn văn được chọn làm *câu trả lời*. **AIO** là xuất
  hiện làm nguồn trong **AI Overviews** của Google (và AI Mode). **GEO** là được ChatGPT, Perplexity, Gemini, Claude và
  Copilot trích dẫn và nhắc tên.
- Chúng là **các tầng, không phải lựa chọn thay thế**. Mọi sản phẩm AI search đều lấy trang từ một chỉ mục trước khi
  viết. Không được index thì không được trích.
- Tầng 1–2 chủ yếu làm trên site của bạn. Tầng 3–4 phụ thuộc ngày càng nhiều vào **các site khác nói gì về bạn**.
- Vì sao là lúc này: khi có AI Overview, người ta bấm vào kết quả ít hẳn (một nghiên cứu ngẫu nhiên năm 2026 đo được
  −38%), nhưng trang **được trích trong** Overview vẫn được bấm nhiều hơn trang không được trích.

## Vì sao quan trọng năm 2026

| Phát hiện | Nguồn | Độ tin |
|---|---|---|
| Có AI Overview thì lượt bấm tự nhiên giảm **38%**, tìm kiếm không bấm tăng từ 54% lên 72% | Thí nghiệm ngẫu nhiên, 1.065 người dùng Mỹ, 1–2/2026 (Agarwal & Sen, SSRN, 4/2026) | **Cao**: có nhóm đối chứng |
| CTR của trang top 1 thấp hơn khoảng **58%** khi có AI Overview (34,5% ở lần đo 2025) | Ahrefs, 300.000 từ khoá, 2/2026 | Trung bình: tương quan |
| Khoảng 68% lượt tìm Google ở Mỹ kết thúc không có cú bấm nào, đầu năm 2026 | Dữ liệu SparkToro | Trung bình |
| Trên truy vấn có AI Overview: trang được trích CTR ~2,1%, không được trích ~0,9% | Seer Interactive | Trung bình |
| 10/2026: Google đưa link nguồn lên cao hơn trong AI Mode / AI Overviews và thử một khối riêng cho **site chính thức** | Thông báo của Google, 15/10/2026 (qua báo chí) | Cao, nhưng nên đọc bài gốc của Google |

**Nghĩa là:** chỉ lọt top 10 thì giờ thu về ít hơn trước. Mục tiêu mới là **được trích trong câu trả lời**, và **trang
chính thức** có cấu trúc rõ (sản phẩm, giá, tài liệu) đang được coi trọng hơn.

## Bốn thuật ngữ

Mỗi tầng được mô tả dưới đây theo cùng một khung: viết tắt của gì, mục tiêu, xuất hiện ở đâu, khi nào thắng, làm chủ
yếu ở đâu, đo bằng gì.

**SEO** (Search engine optimization): xếp hạng trong danh sách link trên Google, Bing. Thắng khi vào top 10 và có lượt
bấm. Làm trên site của bạn. Đo bằng Search Console.

**AEO** (Answer engine optimization): đoạn văn của bạn được chọn làm câu trả lời, ở featured snippet, People Also Ask,
trợ lý giọng nói, câu trả lời AI. Thắng khi đoạn của bạn được trích nguyên văn. Làm trên site của bạn. Đo bằng
snippet và nguồn trong AIO.

**AIO** (Google AI Overviews): bạn là một nguồn trong AI Overview / AI Mode của Google Search. Thắng khi link của bạn
nằm trong Overview. Làm trên site của bạn cộng độ tin cậy. Đo bằng tự kiểm tra tay, hoặc công cụ theo dõi thứ hạng có
dữ liệu AIO.

**GEO** (Generative engine optimization): trợ lý AI trích dẫn và giới thiệu bạn, trên ChatGPT, Perplexity, Gemini,
Claude, Copilot. Thắng khi câu trả lời nói "dùng X" và X là bạn. Làm **chủ yếu ngoài site của bạn**. Đo bằng một bộ
câu hỏi cố định, chạy lại mỗi tháng.

> "AIO" có hai nghĩa: ở đây là **Google AI Overviews**. Có người dùng nó cho "AI optimization" nói chung. Hỏi lại người
> nói xem họ định nói cái nào.

```
 Tầng 4  GEO  — được NHẮC TÊN        ← nhắc tới bạn ngoài site (báo, Reddit, review, bài so sánh)
 Tầng 3  AIO  — có trong AI Overview ← phủ đủ ý + có nguồn + tác giả thật
 Tầng 2  AEO  — được TRÍCH làm đáp án ← trả lời trước, tiêu đề dạng câu hỏi, bảng, FAQ
 Tầng 1  SEO  — được INDEX, có hạng   ← kỹ thuật, on-page, link
```

## Mỗi công cụ lấy trang từ đâu

| Công cụ | Nguồn trang chính | Giúp nhiều nhất |
|---|---|---|
| Google AI Overviews / AI Mode / Gemini | Chỉ mục của Google. **Không có "chỉ mục AI" riêng** | SEO cổ điển, đủ điều kiện hiện snippet, tín hiệu tin cậy |
| ChatGPT search | Bing + bot riêng của OpenAI (theo báo cáo) | **Có mặt trên Bing**, trang mới, trang chính thức rõ ràng |
| Perplexity | Chỉ mục riêng + tìm kiếm web | Đoạn văn tự đứng được, cập nhật gần đây |
| Copilot | Bing | Bing Webmaster Tools, IndexNow, tốc độ |
| Claude (tìm web) | Công cụ tìm kiếm bên thứ ba (theo báo cáo: Brave) | Trang dày dữ kiện, nguồn rõ |

Hệ quả thực tế: phải được index trên **cả Google lẫn Bing**. Nhiều site nhỏ bỏ qua Bing nên gần như vô hình trên
ChatGPT và Copilot.

## Làm gì ở mỗi tầng (và bỏ gì)

Có một checklist "SEO + AEO + AIO + GEO" hay được chia sẻ. Dưới đây là từng mục, kèm chỉnh sửa cho năm 2026.

### Tầng 1: SEO

| Mục trong checklist | Còn đúng? | Ghi chú |
|---|---|---|
| Title, meta description, H1–H4, link nội bộ | ✅ | Title ≲ 60 ký tự, description ~140–155, mỗi trang một chủ đề chính |
| Mật độ từ khoá | ❌ **Bỏ** | Google không dùng. Nhồi từ khoá làm trang tệ hơn với người đọc và bản tóm tắt AI. Hãy phủ đúng ý định tìm kiếm |
| Core Web Vitals, thân thiện di động | ✅ | LCP < 2,5 s, INP < 200 ms |
| XML sitemap, robots.txt | ✅ | Ngày `lastmod` trung thực. Đừng chặn OAI-SearchBot hay PerplexityBot nếu muốn được trích |
| *(thiếu)* HTML render sẵn ở server | ➕ | Nhiều bot AI chạy JavaScript kém. Nội dung chỉ hiện sau khi chạy JS có thể bị thấy là trang trống |
| *(thiếu)* Bing Webmaster Tools + IndexNow | ➕ | Cho ChatGPT search và Copilot |
| Backlink, "Domain Authority" | ⚠️ | Link vẫn quan trọng. "Domain Authority" là chỉ số của Moz/Ahrefs mà **Google không dùng**. Hãy đếm số tên miền liên quan trỏ về |
| SEO địa phương, Google Business Profile | ✅ nếu bán tại chỗ | Thường bỏ qua với app hay SaaS toàn cầu |

### Tầng 2: AEO

| Mục trong checklist | Còn đúng? | Ghi chú |
|---|---|---|
| Trả lời trước, 40–50 chữ | ✅ | Mở mỗi mục bằng 40–60 chữ (tiếng Anh) mà **cắt riêng ra vẫn hiểu được** |
| Câu hỏi thật làm H2/H3 | ✅ | Lấy từ Google autocomplete, People Also Ask, Reddit và truy vấn trong Search Console của bạn |
| Schema `FAQPage`, `HowTo`, `Article` | ⚠️ **Cập nhật** | Từ 8/2023 Google **bỏ rich result HowTo** và chỉ hiện **rich result FAQ cho site chính phủ và y tế có tiếng**. Giữ markup cho rõ nghĩa, nhưng đừng mong thấy ô FAQ thả xuống trên Google |
| Bảng, gạch đầu dòng, số tóm tắt | ✅ | Bảng so sánh và checklist là khối dễ được lấy nhất |

### Tầng 3: AIO (Google AI Overviews / AI Mode)

| Mục trong checklist | Còn đúng? | Ghi chú |
|---|---|---|
| Phủ đủ, nhiều góc nhìn | ✅ | AI search tách một câu hỏi thành nhiều lượt tìm con (query fan-out). Phủ cả các câu hỏi nối tiếp |
| Trích số liệu, chuyên gia, nguồn chính thức | ✅ | Thêm ít nhất một con số **chính bạn đo** |
| Ngôn ngữ rõ, tự nhiên | ✅ | Mỗi đoạn một ý, định nghĩa thuật ngữ ở lần đầu xuất hiện |
| *(thiếu)* Tín hiệu E-E-A-T | ➕ | Tác giả thật có tiểu sử, ngày "cập nhật lần cuối", ghi chú "đã thử trên" |
| *(thiếu)* Không cần markup đặc biệt | ➕ | Google nói AI Overviews không cần markup hay file đặc biệt: trang chỉ cần được index và đủ điều kiện hiện snippet. AIO là SEO + AEO làm tốt, cộng độ tin cậy |

### Tầng 4: GEO (ChatGPT, Perplexity, Gemini, Claude)

| Mục trong checklist | Còn đúng? | Ghi chú |
|---|---|---|
| Xây thực thể (entity) | ✅ | **Cùng một câu mô tả** trên site, trang store, LinkedIn, X, GitHub, Product Hunt và danh bạ, nối bằng `sameAs` trong schema |
| Wikipedia | ⚠️ | Thương hiệu mới thường **không** có được trang Wikipedia (cần báo chí độc lập). Bắt đầu bằng báo, blog ngách và Wikidata |
| Bài dài, case study, quan điểm | ✅ | **Dữ liệu gốc** hiệu quả nhất: thứ mà người khác sẽ trích |
| PR số, được nhắc tên | ✅ **Quan trọng nhất** | Một phân tích của Muck Rack (do một bên bán dịch vụ dẫn lại) thấy ~84% trích dẫn của AI đến từ báo chí và nơi khác viết về thương hiệu, không phải trang của chính thương hiệu |
| *(thiếu)* Trang chính thức có cấu trúc | ➕ | Trang giá, tính năng, tài liệu rõ ràng. Lượt trích bài listicle được báo cáo là giảm sau ChatGPT 5.6; Google đang thử khối site chính thức |
| *(thiếu)* `llms.txt` | ➕ | Thêm rẻ. **Chưa có bằng chứng công khai mạnh** rằng nó tăng lượt trích |

## Bằng chứng mạnh tới đâu?

Dùng bảng này trước khi hứa hẹn gì với khách, sếp hay chính mình.

| Nhận định | Bằng chứng |
|---|---|
| AI Overviews làm giảm lượt bấm | **Mạnh**: một thí nghiệm ngẫu nhiên cộng nhiều nghiên cứu lớn |
| Phải được index mới được trích | **Mạnh**: Google nói vậy |
| Số liệu và nguồn trích dẫn làm tăng hiện diện trên AI | **Khá**: bài GEO ở KDD 2024 đo được tới ~30–40%. Một khảo sát nghiên cứu GEO tháng 7/2026 thấy chiến thuật chung **khó áp dụng chéo** giữa các công cụ, mỗi công cụ trích nguồn khác nhau, và kết quả đổi theo từng lần chạy |
| Được nơi khác nhắc quan trọng hơn trang của chính bạn | **Khá**: dữ liệu ngành PR, chưa có nghiên cứu độc lập |
| Trích dẫn của ChatGPT trùng ~87% với top kết quả Bing | **Yếu**: con số của bên bán dịch vụ, chưa kiểm được nghiên cứu gốc |
| `llms.txt` làm tăng lượt trích | **Chưa có bằng chứng** |
| "Bảo đảm lên ChatGPT" | **Không ai bảo đảm được**: câu trả lời đổi theo câu hỏi, người dùng và từng tuần |

## Đo mỗi tầng thế nào

| Tầng | Câu hỏi | Công cụ |
|---|---|---|
| SEO | Google và Bing có index tôi không? Tôi đứng hạng mấy? | Google Search Console, Bing Webmaster Tools |
| AEO | Đoạn văn của tôi có thành snippet không? | Truy vấn trong Search Console + tự kiểm tra tay |
| AIO | Tôi có là nguồn trong AI Overviews không? | Tự kiểm tra tay; công cụ theo dõi hạng có tính năng AIO |
| GEO | ChatGPT và Perplexity có nhắc tên tôi không? | **Một bộ 20 câu hỏi cố định**, chạy lại ngày 1 mỗi tháng, lưu ảnh chụp. Cần thì dùng công cụ trả phí sau |
| Khách từ AI | Có ai bấm từ AI sang không? | GA4 với kênh "AI assistants": `chatgpt.com`, `perplexity.ai`, `gemini.google.com`, `copilot.microsoft.com` |

Cách làm từng bước bằng tiếng Việt: [Đo khách từ AI trong GA4](02-do-khach-tu-ai.md) và
[Search Console và Bing](03-search-console-bing.md). Gắn GA4 lần đầu:
[analytics-ga4-setup](../skills/analytics/analytics-ga4-setup/SKILL.md), luật kênh trong
[utm-convention.md](../skills/analytics/analytics-tracking-plan/references/utm-convention.md).

## Những lầm tưởng nên bỏ qua

1. **"SEO chết rồi, chỉ GEO mới quan trọng."** Công cụ AI lấy trang từ chỉ mục tìm kiếm. SEO là nền móng.
2. **"Schema FAQ giúp vào AI Overviews."** Google nói không cần markup đặc biệt, và rich result FAQ đã bị giới hạn.
3. **"Đăng 100 bài do AI viết."** Trang mỏng, làm hàng loạt không được trích và có thể bị hạ hạng.
4. **"Viết listicle Top 10 với chính mình ở #1."** Lượt trích listicle đang giảm; công cụ ưu tiên trang chính thức và
   nguồn độc lập.
5. **"Thêm llms.txt là ChatGPT đọc mình."** Chưa có bằng chứng.
6. **"Mua link hay review cho nhanh."** Có thể bị phạt thủ công cho cả tên miền. Kiểu hay gặp: một template SEO dùng
   chung gắn cứng cùng một số sao cho mọi trang. Chỉ markup điểm đánh giá có thật.

## Thứ tự cho một sản phẩm nhỏ

| Khi nào | Tầng | Làm |
|---|---|---|
| Tuần 1 | Đo | Search Console, Bing Webmaster Tools, GA4, và một bảng 20 câu hỏi của người mua kèm câu trả lời AI hôm nay |
| Tuần 2 | SEO | Sửa index, sitemap, robots, canonical, tốc độ |
| Tuần 3–4 | AEO | Viết lại 5 trang quan trọng nhất theo kiểu trả lời trước; thêm bảng và schema |
| Tháng 2 | AIO | Mỗi chủ đề chính một bài hướng dẫn sâu, có nguồn và số của chính bạn |
| Tháng 2 trở đi | GEO | Một câu mô tả ở mọi nơi, đăng danh bạ, mỗi tuần một đóng góp thật lòng cho cộng đồng, mỗi tháng một dữ liệu gốc |
| Mỗi tháng | Tất cả | Chạy lại đúng 20 câu hỏi đó và so sánh |

## Skill làm từng bước (bản tiếng Anh)

- Học cơ chế, cho bot vào, chạy thử 28 ngày trên một trang preview:
  [launch-geo-aeo-feature-preview](../skills/launch/launch-geo-aeo-feature-preview/SKILL.md)
  (bản tiếng Việt: [Skill trang preview tính năng](07-skill-trang-preview-tinh-nang.md))
- Tìm câu hỏi người mua thật sự hỏi: [research-where-users-ask](../skills/research/research-where-users-ask/SKILL.md)
- Được nhắc trong cộng đồng mà không bị xoá bài: [launch-reddit-posting](../skills/launch/launch-reddit-posting/SKILL.md)
- Đăng danh bạ và trang launch: [launch-quick-download-wins](../skills/launch/launch-quick-download-wins/SKILL.md),
  [launch-product-hunt-launch](../skills/launch/launch-product-hunt-launch/SKILL.md)
- Đo: [analytics-ga4-setup](../skills/analytics/analytics-ga4-setup/SKILL.md),
  [analytics-ga4-reports-101](../skills/analytics/analytics-ga4-reports-101/SKILL.md)
- Với app store, cùng ý "là câu trả lời": [Playbook: ASO Optimization](../playbooks/aso-optimization.md)

## Bảng thuật ngữ

| Thuật ngữ | Nghĩa |
|---|---|
| **AI Overviews** | Đoạn tóm tắt do AI viết phía trên kết quả Google, có link nguồn |
| **AI Mode** | Chế độ trả lời kiểu chat ngay trong Google Search |
| **Featured snippet** | Khối trả lời được trích ở đầu kết quả Google cổ điển |
| **Zero-click** | Lượt tìm kết thúc mà không bấm vào kết quả nào |
| **Query fan-out** | Công cụ AI tách một câu hỏi thành nhiều lượt tìm chạy ngầm |
| **Entity (thực thể)** | Thương hiệu, sản phẩm hay người mà máy nhận ra là một thứ rõ ràng |
| **E-E-A-T** | Experience, Expertise, Authoritativeness, Trust: cách người đánh giá của Google xét độ tin cậy |
| **Schema / JSON-LD** | Dữ liệu có cấu trúc mô tả trang cho máy đọc |
| **IndexNow** | Giao thức báo cho Bing (và nơi khác) là một trang vừa đổi |
| **llms.txt** | File đề xuất đặt ở gốc site, tóm tắt site cho mô hình ngôn ngữ |
| **Earned media** | Nội dung người khác viết về bạn: báo, review, bài cộng đồng |

## Nguồn

- Google Search Central: [AI features and your website](https://developers.google.com/search/docs/appearance/ai-features) ·
  [Changes to HowTo and FAQ rich results (8/2023)](https://developers.google.com/search/blog/2023/08/howto-faq-changes)
- Thử nghiệm link nguồn và khối site chính thức của Google tháng 10/2026, theo
  [Business Today](https://www.businesstoday.in/technology/news/story/google-ai-search-now-makes-it-easier-to-find-the-websites-behind-its-answers-heres-how-562057-2026-10-16) và
  [BetaNews](https://betanews.com/article/google-ai-mode-inline-links-higher-click-data/)
- Tóm tắt yêu cầu của Google cho AI Overviews / AI Mode:
  [Trusted Shops](https://ai-trust-audit.trustedshops.com/en/blog/ai-overviews-and-ai-mode-google-s-requirements-for-websites-2026)
- Nghiên cứu lượt bấm: [Ahrefs](https://ahrefs.com/blog/ai-overviews-reduce-clicks/) ·
  [Search Engine Land về Seer Interactive](https://searchengineland.com/google-ai-overviews-ctr-recovery-study-475566) ·
  [TechWyse về SparkToro](https://www.techwyse.com/news/reports-data/google-zero-click-searches-68-percent-2026) ·
  [SEOWorth về Ahrefs 2026](https://seoworth.it.com/news/ahrefs-ai-overviews-ctr-study/)
- Nghiên cứu GEO: [Aggarwal et al., "GEO: Generative Engine Optimization" (KDD 2024)](https://arxiv.org/abs/2311.09735) ·
  [Survey of GEO, 2023–2026 (arXiv, 7/2026)](https://arxiv.org/pdf/2607.14035)
- Hướng dẫn của bên bán dịch vụ, trích thận trọng: [Averi (số của Muck Rack)](https://www.averi.ai/learn/the-definitive-guide-to-geo-get-cited-by-ai-in-2026) ·
  [LLM Pulse](https://llmpulse.ai/blog/geo-guide/)
- Bing: [Bing Webmaster Tools](https://www.bing.com/webmasters) · [IndexNow](https://www.indexnow.org/)
