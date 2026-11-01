# Search Console và Bing: bài nào được đưa ra

GA4 chỉ thấy người **đã bấm**. Muốn biết Google có **đưa bài ra** không (kể cả trong AI Overviews và AI Mode), và cho
câu hỏi nào, phải xem Search Console. Muốn biết Copilot của Bing có dùng bài không, xem Bing Webmaster Tools. Cả hai
đều miễn phí và chỉ tính người thật tìm kiếm, nên bạn không cần gạt chính mình ra như ở GA4.

## Google Search Console

Xác minh site một lần (thêm bản ghi DNS hoặc thẻ HTML), gửi `sitemap.xml`, rồi đọc:

1. **Performance → Search results**, bật cả 4 ô: *Clicks, Impressions, CTR, Position*.
2. Tab **Pages** → filter **Page** chứa `/blog/`: bài nào được hiện bao nhiêu lần.
3. Bấm vào một bài → tab **Queries**: người ta gõ câu gì mà thấy bài đó.
4. Tab **Countries** → bấm *Vietnam* rồi chọn **Exclude** nếu muốn bỏ Việt Nam (cùng ý với GA4).

Lượt hiển thị trong AI Overviews và AI Mode được **gộp chung** vào số Web, Google không tách riêng. Vì vậy đừng tìm
một ô tên "AI" trong Search Console.

### Đọc số ra sao

| Thấy gì | Nghĩa là | Làm gì |
|---|---|---|
| Impressions **0** sau 2 tuần | Bài chưa được index | **URL Inspection** → *Request indexing*, kiểm tra link nội bộ tới bài |
| Impressions cao, CTR rất thấp | Bài được hiện nhưng ít người bấm (hay gặp khi có AI Overview) | Sửa tiêu đề + đoạn trả lời ngắn đầu bài cho đúng câu hỏi |
| Position 8–20 cho một câu hỏi rõ | Gần lên trang 1 | Viết thêm một mục H2 trả lời đúng câu đó |
| Truy vấn chứa **tên sản phẩm** tăng | Người ta nghe tên bạn ở đâu đó | Ghi vào sổ theo dõi, so với lịch rải bài |

## Bing Webmaster Tools

Copilot lấy nguồn từ chỉ mục của Bing. Thêm site vào Bing Webmaster Tools (nhập từ Search Console là xong trong 1
phút), rồi xem mục **AI Performance**: bài nào được Copilot dùng làm nguồn và cho câu hỏi nào. Tên mục và số liệu có
thể đổi theo thời gian, hãy đọc trang trợ giúp của Bing trước khi trích số này cho người khác.

## Cho bot AI đọc được site

Kiểm tra `robots.txt` không chặn các bot tìm kiếm của AI. Chặn bot **huấn luyện** và chặn bot **tìm kiếm** là hai việc
khác nhau, ví dụ của OpenAI:

| Bot | Dùng để | Chặn thì |
|---|---|---|
| `OAI-SearchBot` | Tìm kiếm trong ChatGPT | Bài khó được ChatGPT trích dẫn |
| `GPTBot` | Huấn luyện mô hình | Không ảnh hưởng tới việc được trích dẫn |

Chi tiết từng bot và nguồn chính thức: [GEO & AEO learning guide](../skills/launch/launch-geo-aeo-feature-preview/references/geo-aeo-learning-guide.md).

> Tiếp theo: [trang 04](04-theo-doi-hang-tuan.md), gộp ba nguồn số vào một lịch 15 phút mỗi tuần.
