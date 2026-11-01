# Theo dõi hằng tuần: 15 phút, một sổ ghi

Chiến dịch GEO cho kết quả chậm: Google cần vài ngày tới vài tuần để index, AI trích dẫn thường còn chậm hơn. Nhìn số
mỗi ngày sẽ chỉ thấy nhiễu. Làm một lần mỗi tuần, cùng một ngày, ghi vào một bảng.

## Lịch 15 phút (ví dụ: sáng thứ Hai)

1. **GA4, 5 phút.** Mở Explore "Blog — khách nước ngoài" ([trang 01](01-tach-khach-that.md)), chọn 7 ngày qua. Ghi lại
   từng bài: active users, số người đến từ AI Assistant, thời gian đọc trung bình, key event.
2. **Search Console, 5 phút.** Performance → Pages → `/blog/`, 7 ngày qua. Ghi impressions, clicks, vị trí trung bình
   của từng bài.
3. **Prompt check, 5 phút.** Hỏi 5 câu (dưới đây) trên ChatGPT (bật search), Perplexity và Google. Ghi lại: có nhắc
   tên bạn không, có trích link bài nào không, ai khác được trích.

## Chọn 5 câu hỏi mẫu

Chọn câu một người **sắp cần** sản phẩm của bạn sẽ gõ, giữ nguyên 5 câu này suốt chiến dịch để so được tuần này với tuần
trước:

| Loại câu | Mẫu |
|---|---|
| Biết vấn đề | "how do I … " |
| Đang tìm giải pháp | "best tool for …" |
| So sánh | "X vs Y for …" |
| Tên sản phẩm | "what is <tên sản phẩm>" |
| Câu dài, cụ thể | đúng một câu hỏi mà một bài blog của bạn trả lời |

Câu trả lời của AI đổi giữa các lần hỏi. Hỏi mỗi câu **3 lần** và ghi "được nhắc 1/3", đừng kết luận từ một lần.

## Mẫu sổ theo dõi

> **Ví dụ minh hoạ.** Số dưới đây là số giả để thấy cách ghi, không phải số của một site thật.

| Tuần | Bài | Người (không VN) | Từ AI | Impressions | Được nhắc (15 lần hỏi) | Đã sửa gì |
|---|---|---|---|---|---|---|
| 03/11 | bai-a | 12 | 1 | 340 | 0/15 | — |
| 10/11 | bai-a | 15 | 2 | 410 | 1/15 | Thêm đoạn trả lời 50 chữ đầu bài |
| 17/11 | bai-a | 21 | 4 | 520 | 3/15 | — |

Cột **Đã sửa gì** quan trọng nhất: mỗi tuần chỉ đổi **một** thứ trên mỗi bài, ghi ngày, để biết cái gì có tác dụng.

## Đọc số mà không tự lừa mình

- **Số nhỏ thì nhiễu.** 3 người tuần này, 9 người tuần sau chưa nói lên gì. So **trung bình 4 tuần** với 4 tuần trước
  khi bắt đầu chiến dịch.
- **Chấm bài sau 28 ngày**, không phải sau 3 ngày.
- **Tách kênh.** Đăng Reddit hôm thứ Ba làm số nhảy lên không có nghĩa GEO đang có tác dụng. GEO hiện ra từ từ, qua
  Organic Search, AI Assistant và lượt tìm tên thương hiệu, trong nhiều tuần.
- **Người tới sản phẩm trên 100 người đọc** mới là số quyết định. Nhiều người đọc mà không ai bấm tải hay đăng ký thì
  bài trả lời đúng câu hỏi nhưng chưa dẫn về sản phẩm.

## Khi nào làm gì

| Sau 4 tuần thấy | Làm gì |
|---|---|
| Không impressions, không được nhắc | Kiểm tra index, link nội bộ, `robots.txt` ([trang 03](03-search-console-bing.md)) |
| Có impressions, AI không nhắc | Thêm số liệu tự đo, bảng so sánh, đoạn trả lời ngắn đầu bài; rải bài ở nơi AI hay trích |
| AI nhắc đối thủ, không nhắc bạn | Trang được trích thay bạn chính là danh sách nơi cần có mặt (review, danh bạ, bài so sánh) |
| Có khách AI, không ai chuyển đổi | Sửa lời kêu gọi trong bài, link thẳng tới trang tải / đăng ký |
| Có khách AI và có chuyển đổi | Viết thêm bài cùng cụm chủ đề, cập nhật bài cũ mỗi quý |

> Quay lại [mục lục GEO](README.md).
