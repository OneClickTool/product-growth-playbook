# Installs & uninstalls: hai con số quan trọng nhất

**Installs** cho biết bao nhiêu người mới đến (acquisition). **Uninstalls** cho biết bao nhiêu người bỏ đi (churn).
Nhìn riêng một số thì không kết luận được gì; phải đặt hai số cạnh nhau.

## Ba con số cần tính

| Con số | Cách tính | Ý nghĩa |
|---|---|---|
| **Tăng trưởng installs** | Installs kỳ này so với kỳ trước (dashboard tính sẵn: "↑ 25.93% compared to the previous period") | Kênh kéo người mới đang mạnh lên hay yếu đi |
| **Tỷ lệ uninstall / install** | Uninstalls 30 ngày ÷ Installs 30 ngày × 100 | Trong 100 người đến, có bao nhiêu "người đi" tương ứng |
| **Xu hướng Weekly users** | Weekly users hôm nay so với 4 tuần trước | Kết quả cuối cùng của cả hai: tổng thể đang lớn lên hay co lại |

Lưu ý: installs và uninstalls đếm theo đơn vị hơi khác nhau (xem [trang 01](01-doc-dashboard.md)), nên tỷ lệ này là
**chỉ báo xu hướng**, không phải tỷ lệ churn chính xác. So nó với chính nó qua các tháng là dùng đúng.

## Mốc tham khảo

Google không công bố mức uninstall "bình thường", và chưa có nghiên cứu công khai đủ tin cậy. Mốc dưới đây là **quy
tắc kinh nghiệm của playbook này** để bạn có chỗ bắt đầu, không phải chuẩn ngành:

| Uninstall / install (30 ngày) | Đọc là |
|---|---|
| **dưới 30%** | 🟢 Phần lớn người cài ở lại |
| **30–60%** | 🟡 Có rò rỉ, tìm chỗ user bỏ đi |
| **trên 60%** | 🔴 Đổ nước vào xô thủng: kéo thêm người lúc này là phí |

Để tham khảo thêm: một developer trên [Indie Hackers](https://www.indiehackers.com/post/what-does-your-install-uninstall-ratio-look-like-f44076717a)
kể 30–40% người cài gỡ ngay, và họ cho là do bắt đăng ký tài khoản. Đó là một trường hợp, không phải mức trung bình.

## 7 tình huống khi so installs với uninstalls

| # | Installs | Uninstalls | Nghĩa là | Làm gì |
|---|---|---|---|---|
| 1 | ↑ | ↔ hoặc ↓ | **Tăng trưởng thật.** Kênh mới hiệu quả và sản phẩm giữ được người | Tìm kênh nào mang người về và đổ thêm sức vào đó |
| 2 | ↑ | ↑ nhanh hơn | **Xô thủng.** Kênh mang về sai người, hoặc listing hứa nhiều hơn sản phẩm làm được, hoặc onboarding khó | Sửa trải nghiệm 1 phút đầu và mô tả listing trước khi kéo thêm người |
| 3 | ↓ | thấp, ổn định | **Sản phẩm tốt, thiếu khách.** Ai dùng rồi thì ở lại | Làm marketing, SEO listing, tìm kênh mới. Đây là tình huống dễ cứu nhất |
| 4 | ↓ | ↑ | **Báo động.** Có thể do bản cập nhật lỗi, đối thủ mới, trang web extension hỗ trợ thay đổi, hoặc vi phạm chính sách | Xem review 1 sao gần nhất, kiểm tra bản mới, xem đối thủ |
| 5 | ↔ | vọt lên ngay sau một bản cập nhật | **Bản cập nhật có vấn đề.** Thêm quyền mới khiến Chrome tạm tắt extension cho tới khi user đồng ý, hoặc tính năng bị hỏng | So ngày phát hành với ngày uninstall vọt; cân nhắc rút bớt quyền hoặc sửa nhanh |
| 6 | vọt 1 ngày | vọt 1–3 ngày sau | **Lượng truy cập sai đối tượng.** Một bài viral (Reddit, Product Hunt) mang người tò mò, không mang người cần | Bình thường, đừng hoảng. Xem Weekly users sau 2 tuần mới tính được đợt đó giữ lại bao nhiêu |
| 7 | ≈ uninstalls, đều đều | ≈ installs | **Đứng yên.** Extension trưởng thành, người mới chỉ bù người cũ | Cần tính năng mới, thị trường mới (dịch listing) hoặc kênh mới để thoát |

## Biết thêm vì sao người ta gỡ

Dashboard chỉ cho biết **bao nhiêu** người gỡ, không cho biết **vì sao**. Chrome có API
[`chrome.runtime.setUninstallURL`](https://developer.chrome.com/docs/extensions/reference/api/runtime#method-setUninstallURL)
để mở một trang web khi user gỡ extension. Đặt ở đó một form 1 câu hỏi ("Vì sao bạn gỡ?", 4–5 lựa chọn): sau vài
chục câu trả lời bạn sẽ biết mình đang ở tình huống nào trong bảng trên.

## Quay lại ví dụ thật

Extension trong [trang 01](01-doc-dashboard.md): **68 installs, +25.93%**, ngày cuối vọt lên 8. Hai khả năng:

- Uninstalls cùng kỳ ~10–15 (tỷ lệ ~15–22%) → **tình huống 1**, đang tăng trưởng tốt.
- Uninstalls vọt theo trong 1–3 ngày sau ngày 8 installs → **tình huống 6**, chờ Weekly users 2 tuần nữa mới kết luận.

Muốn biết là cái nào: mở khối Uninstalls cùng kỳ, hoặc export cả hai ra CSV rồi chạy [script chấm điểm](05-export-csv.md).
