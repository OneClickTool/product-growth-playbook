# GEO: đo xem AI có gửi khách tới blog của bạn không

> Chuyên mục này viết bằng **tiếng Việt** (phần lớn playbook là tiếng Anh). Cập nhật lần cuối: **01/11/2026**.

Bạn viết blog chuẩn SEO, AEO, GEO để Google và ChatGPT, Perplexity, Gemini, Claude trích dẫn. Rồi mở Google Analytics
thấy "Vietnam 53, Direct 96". Tốt hay xấu? Câu trả lời thường là: **phần lớn số đó là chính bạn**. Chuyên mục này chỉ
cách gạt mình ra, gạt bot ra, rồi đo đúng phần khách do AI và Google gửi tới, mỗi tuần 15 phút.

Nhớ một hình là đủ: **Search Console** cho biết Google có *đưa bài ra* không, **GA4** cho biết người ta có *bấm vào*
không, còn **prompt check** cho biết AI có *nhắc tên* bạn không. Cần cả ba, vì mỗi cái chỉ thấy một khúc.

## Đọc theo thứ tự này

1. [Tách khách thật](01-tach-khach-that.md): gạt chính bạn, khách Việt Nam và bot ra khỏi số liệu.
2. [Đo khách từ AI trong GA4](02-do-khach-tu-ai.md): kênh *AI Assistant*, nguồn từng AI, bảng blog × kênh.
3. [Search Console và Bing](03-search-console-bing.md): bài nào được Google / Copilot đưa ra, cho câu hỏi nào.
4. [Theo dõi hằng tuần](04-theo-doi-hang-tuan.md): 15 phút mỗi tuần, cách đọc số mà không tự lừa mình, khi nào sửa bài.

## Ba con số cần nhớ

| Con số | Lấy ở đâu | Trả lời câu hỏi |
|---|---|---|
| **Khách từ AI** (không tính bạn) | GA4, kênh *AI Assistant* + nguồn `chatgpt.com`, `perplexity.ai`… | AI có gửi người tới bài nào không |
| **Lượt hiển thị Google** của bài blog | Search Console → Hiệu suất → Trang | Google có đưa bài ra cho người tìm không |
| **Số lần được nhắc** trong 5 câu hỏi mẫu | Tự hỏi ChatGPT, Perplexity, Google mỗi tuần | AI có biết tới sản phẩm của bạn không |

## Liên quan trong playbook

- Vì sao làm GEO, bằng chứng tới đâu: [AI Search Visibility](../playbooks/ai-search-visibility.md).
- Cơ chế sâu hơn (bản tiếng Anh): [GEO & AEO learning guide](../skills/launch/launch-geo-aeo-feature-preview/references/geo-aeo-learning-guide.md).
- Gắn GA4 lần đầu: [analytics-ga4-setup](../skills/analytics/analytics-ga4-setup/SKILL.md) · đọc báo cáo GA4: [analytics-ga4-reports-101](../skills/analytics/analytics-ga4-reports-101/SKILL.md).
