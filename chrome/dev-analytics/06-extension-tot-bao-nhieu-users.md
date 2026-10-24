# Extension tốt có bao nhiêu installs, bao nhiêu users

**Trả lời ngắn:** đo bằng **users** (con số "users" công khai trên trang listing, gần với Weekly users trong
dashboard), không đo bằng tổng installs. Có **≥ 1.000 users** là đã vào **top ~10%** Chrome Web Store, playbook gọi
là **"tốt"**. Có **≥ 10.000 users** là top ~3%, **"rất tốt"**.

## Phân bố users của cả store

Theo [Backlinko](https://backlinko.com/chrome-users) (dữ liệu Chrome-Stats, 5/2026):

| Users | Tỷ lệ extension | Cộng dồn: bạn đứng trên |
|---|---|---|
| 0 | ~13,5% | — |
| 1–9 | 34,23% | ~13% store |
| 10–99 | 26,97% | ~48% store |
| 100–999 | 15,47% | ~75% store |
| 1.000–9.999 | 6,78% | ~90% store |
| 10.000–99.999 | 2,40% | ~97% store |
| 100.000–999.999 | 0,58% | ~99,3% store |
| ≥ 1.000.000 | 0,12% | ~99,9% store |

Dòng "0 users" là phần còn lại để tổng ra 100%; Backlinko cũng ghi 90,11% extension có dưới 1.000 users, khớp với
bảng. [Exstats](https://exstats.com/blog/state-of-browser-extensions-q2-2026) cho mốc tương tự: extension ở giữa
(median) chỉ có **14 users** (Q2/2026).

## Thang 6 bậc để tự xếp hạng

| Bậc | Users | Vị trí | Gợi ý việc tiếp theo |
|---|---|---|---|
| Mới bắt đầu | < 100 | ~75% store ở đây | Tìm 1 kênh mang người về đều đặn |
| **Sống được** | ≥ 100 | top ~25% | Hỏi user vì sao họ ở lại, viết lại listing theo lời họ |
| **Tốt** | ≥ 1.000 | top ~10% | Dịch listing, xin review, thử bản trả phí |
| **Rất tốt** | ≥ 10.000 | top ~3% | Kênh bài viết / báo chí, đưa lên Edge và Firefox |
| **Xuất sắc** | ≥ 100.000 | top ~0,7% | Đội nhóm, hỗ trợ khách hàng, nhiều trình duyệt |
| **Huyền thoại** | ≥ 1.000.000 | top ~0,1% | — |

Tên các bậc là cách gọi của playbook; phần trăm lấy từ bảng phân bố trên.

## Cần bao nhiêu installs mỗi ngày

Số users đứng yên khi người mới đến bằng người rời đi. Một cách ước lượng (phép tính của playbook, không phải số
liệu đo được):

**users ≈ installs mỗi ngày × số ngày một người ở lại trung bình**

> **Illustrative example.** Installs mỗi ngày cần có để giữ mức users, theo thời gian ở lại trung bình:
>
> | Mục tiêu | User ở lại ~60 ngày | ~120 ngày | ~240 ngày |
> |---|---|---|---|
> | 1.000 users (tốt) | ~17 / ngày | ~8 / ngày | ~4 / ngày |
> | 10.000 users (rất tốt) | ~167 / ngày | ~83 / ngày | ~42 / ngày |
>
> Thời gian ở lại của chính bạn đo bằng số liệu thật: export Installs và Weekly users vài tháng rồi chia.

Đọc bảng theo hai chiều: muốn nhiều users thì **kéo thêm installs** hoặc **giữ người lâu hơn**. Giữ người lâu gấp
đôi thì chỉ cần nửa số installs, nên sửa uninstalls thường rẻ hơn chạy quảng cáo.

## "Active users" thì sao

| Con số | Có trong dashboard? | Nghĩa là |
|---|---|---|
| **Weekly users** | Có | Trình duyệt đã tải extension trong 7 ngày; gần nhất với "active" mà dashboard có, nhưng Google ghi rõ nó không đo user có thật sự dùng không |
| **Enabled %** | Có | Trong các bản đang cài, bao nhiêu đang bật. Dưới 75% nghĩa là nhiều người cài rồi tắt đi |
| **Active thật (DAU / WAU)** | Không | Phải tự gắn analytics trong extension (đếm lượt bấm nút, lượt dùng tính năng chính) |

Một extension khỏe: **Weekly users tăng đều qua các tháng**, Enabled cao, và (nếu có đo) số người dùng tính năng chính
mỗi tuần tăng theo.

![Trang Users: Weekly users over time và Enabled vs disabled](../../docs/images/chrome/cws-04-users.png)
*Ảnh: [Google, Analyze your store listing](https://developer.chrome.com/docs/webstore/metrics), CC BY 4.0. Hai chỗ cần nhìn: đường **Weekly users over time** (đi lên đều là khỏe) và vòng **Enabled vs disabled**. Số trong ảnh là dữ liệu mẫu của Google, không phải extension thật.*

## Ví dụ thật

Đều là số do developer tự kể hoặc bên thứ ba đưa tin, không phải số Google xác nhận.

| Extension | Số liệu | Bài học | Nguồn |
|---|---|---|---|
| Extension theo dõi giới hạn dùng Claude | **70 weekly active users sau 4 tuần**, không tốn tiền marketing | Tháng đầu có vài chục người là bình thường và đáng mừng | [Indie Hackers](https://www.indiehackers.com/post/built-a-chrome-extension-to-stop-getting-cut-off-by-claude-70-users-in-4-weeks-zero-marketing-budget-3b49b2ad35) |
| Ra mắt Product Hunt + Hacker News tốt | **~1.000 installs trong ~1 tuần**; cùng con số đó đi đường tự nhiên mất **3–6 tháng** | Một đợt ra mắt có chuẩn bị rút ngắn vài tháng | [ExtensionBooster](https://extensionbooster.net/blog/chrome-extension-first-1000-users-growth-marketing-guide/) (nguồn thứ cấp) |
| Pinterest Pin Stats | Lên **10.000 users**; nhóm làm nói việc dịch listing sang 52 ngôn ngữ là đòn bẩy lớn nhất | Dịch listing là cách rẻ để vượt bậc | ExtensionBooster, như trên |
| Compass (so giá) | Từ **100 lên 10.000 users trong ~1 tuần** sau khi được Lifehacker viết bài | Một bài báo đúng chỗ đáng giá hơn nhiều tháng tự đăng bài | [Indie Hackers](https://www.indiehackers.com/post/how-did-you-get-your-first-1000-customers-BAka4MXr0zYbPmSvWyrk) (một bình luận) |
| TimeYourWeb (đếm thời gian lướt web) | **~20.000 users sau 10 năm**, nhưng chỉ **10 khách trả tiền, ~$60/tháng** | Nhiều users chưa chắc ra tiền | [Indie Hackers](https://www.indiehackers.com/post/i-built-a-chrome-extension-in-2-weeks-10-years-later-20-000-users-10-paying-customers-60-mrr-YaK5THoaKqXgTlgBjHgO) |
| GMass (gửi email hàng loạt trong Gmail) | **~10.000 người trả phí, ~$130.000/tháng** (developer kể, 2019) | Ít users nhưng giải đúng nỗi đau gắn với tiền thì doanh thu lớn | [ExtensionPay](https://extensionpay.com/articles/browser-extensions-make-money) |

## Áp vào extension trong ảnh dashboard

Ở [trang 01](01-doc-dashboard.md): **68 installs / 30 ngày ≈ 2,3 installs mỗi ngày**.

> **Illustrative example.** Nếu user ở lại trung bình ~120 ngày (chưa đo, chỉ giả định), extension sẽ dừng ở khoảng
> 2,3 × 120 ≈ **~270 users**, bậc **"Sống được"**. Muốn lên **1.000 users** với cùng thời gian ở lại thì cần **~8
> installs mỗi ngày**, gấp ~3,5 lần hiện tại.

Ngày cao nhất trong ảnh cũng là **8 installs**. Nói cách khác: **biến ngày tốt nhất thành ngày bình thường** là đủ để
lên bậc "Tốt". Tìm xem hôm đó chuyện gì đã xảy ra, rồi lặp lại.
