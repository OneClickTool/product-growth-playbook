# Đo khách từ AI trong GA4

Khi ChatGPT, Perplexity, Gemini hay Copilot trích bài của bạn và người đọc bấm vào link, GA4 ghi một phiên mới. Trang
này chỉ cách tìm các phiên đó, biết AI nào gửi, vào bài nào, và vì sao con số bạn thấy luôn **thấp hơn** số thật.

## Kênh "AI Assistant" có sẵn

Từ khoảng **tháng 5/2026**, nhóm kênh mặc định của GA4 có thêm kênh **AI Assistant**. Phiên đến từ một trợ lý AI mà
GA4 nhận ra sẽ có medium `ai-assistant` và rơi vào kênh này, thay vì nằm lẫn trong *Referral* như trước. Các bài viết
về thay đổi này kể ra ChatGPT, Gemini, Copilot, Deepseek, Grok. Danh sách đầy đủ do Google giữ. Lúc viết trang này,
playbook chưa kiểm được bảng chính thức trên trang trợ giúp của Google.

Xem ở đâu:

- **Reports → Acquisition → Traffic acquisition**, cột *Session primary channel group*: tìm dòng **AI Assistant**.
- Trong Explore ở [trang 01](01-tach-khach-that.md), dimension `Session default channel group` cũng có giá trị này.

## Biết chính xác AI nào gửi khách

Kênh gom tất cả AI vào một dòng. Muốn tách từng AI, xem **Session source**:

1. Mở Explore "Blog — khách nước ngoài".
2. Thêm filter: `Session source` **matches regex**:

```text
chatgpt|openai|perplexity|gemini|claude|copilot|deepseek|grok|you\.com|phind
```

3. Kéo `Session source` vào **Rows**, `Page title` vào hàng thứ hai. Bạn có bảng *AI nào → bài nào → bao nhiêu người*.

ChatGPT thường tự gắn `utm_source=chatgpt.com` vào link nó đưa ra, nên ChatGPT là nguồn dễ thấy nhất.

## Tự tạo kênh riêng (nếu muốn chắc tay hơn)

Kênh mặc định do Google định nghĩa và có thể đổi. Nếu bạn muốn tự giữ luật, tạo kênh riêng một lần:

1. **Admin → Data display → Channel groups → Create new channel group**, sao chép từ nhóm mặc định.
2. **Add new channel**, đặt tên **AI tự đo**, điều kiện *Session source* **matches regex** đoạn regex ở trên.
3. Kéo kênh này lên **trên Referral** (luật nào khớp trước thì thắng). Lưu lại.

Kênh tự tạo áp dụng được cho cả số cũ, nên xem lại được các tháng trước.

## Vì sao số AI luôn thấp hơn thật

- Nhiều app AI (app điện thoại, app máy tính) **không gửi referrer**. Người bấm link vẫn tới, nhưng GA4 ghi là
  **Direct**.
- Người đọc câu trả lời của AI rồi **gõ tên** sản phẩm vào Google: GA4 ghi là *Organic Search*.
- Người thấy tên bạn trong câu trả lời nhưng **không bấm** gì: không có trong GA4.

Vì vậy coi số AI trong GA4 là **mức sàn**, không phải tổng. Hai dấu hiệu gián tiếp nên xem kèm:

| Dấu hiệu | Xem ở đâu | Nghĩa là |
|---|---|---|
| **Direct** vào thẳng một bài blog sâu (không phải trang chủ) tăng lên | Explore, kênh Direct × Page path | Có thể là khách từ app AI không gửi referrer |
| Lượt tìm **tên thương hiệu** trên Google tăng | Search Console, lọc truy vấn chứa tên sản phẩm | Người ta nghe tên bạn ở đâu đó (thường có AI) |

## Gắn UTM cho link bạn tự rải

Link bạn tự đặt ở chỗ AI hay đọc (Reddit, Medium, GitHub, danh bạ) nên có UTM để không lẫn với khách AI thật:

```text
https://example.com/blog/bai-viet?utm_source=reddit&utm_medium=social&utm_campaign=geo-2026-11
```

Như vậy khi Direct hoặc AI Assistant tăng, bạn biết chắc không phải do bài Reddit hôm qua.

## Chỉ số nào để chấm một bài

| Chỉ số | Vì sao |
|---|---|
| **Active users** (không tính VN, không tính bot) | Bao nhiêu người thật đọc |
| **Average engagement time** | Khách AI đọc kỹ (trên 1 phút) hay vào rồi đi |
| **Key event** (đăng ký email, bấm tải app) trên 100 người | Bài có đưa được người tới sản phẩm không. Đây là số quyết định |

## Nguồn

Kiểm tra ngày 01/11/2026. Đây là bài của bên thứ ba, chưa phải trang chính thức của Google:
[TechWyse: GA4 thêm kênh AI Assistant](https://www.techwyse.com/?p=76271) ·
[Scalevise: AI Assistant channel group](https://scalevise.com/resources/ga4-ai-assistant-traffic-channel-group/).
Kênh *AI Assistant* cũng hiện trong GA4 thật của người viết ngày 01/11/2026.

> Tiếp theo: [trang 03](03-search-console-bing.md), xem Google và Bing có đưa bài ra không, kể cả khi chưa ai bấm.
