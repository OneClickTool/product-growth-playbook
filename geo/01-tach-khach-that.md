# Tách khách thật: gạt bạn, khách Việt Nam và bot ra

Site mới thì người vào nhiều nhất là chính bạn: mở bài để soát chữ, bấm thử nút, gửi link cho bạn bè. Nếu không gạt
ra, mọi con số GEO phía sau đều sai. Có hai việc khác nhau, đừng lẫn:

| Việc | Làm ở đâu | Có sửa được số cũ không |
|---|---|---|
| **A. Không ghi lượt của bạn nữa** | Admin của GA4 (bộ lọc dữ liệu) hoặc trình duyệt của bạn | ❌ Chỉ tính từ ngày bật |
| **B. Lọc bỏ một nước khi xem báo cáo** | Báo cáo / Explore | ✅ Xem lại được cả số cũ |

## A. Không ghi lượt truy cập của bạn

### Cách 1: theo trình duyệt (nên dùng)

Nhà mạng ở Việt Nam hay đổi IP theo ngày, IPv6 còn đổi thường hơn, nên lọc theo IP dễ trượt. Lọc theo trình duyệt
chắc hơn.

**Nhanh nhất:** cài extension **Google Analytics Opt-out Add-on** của Google trên mọi trình duyệt bạn dùng (máy
tính, điện thoại). Nhược điểm: nó chặn GA trên **mọi** website bạn vào, không riêng site của bạn.

**Gọn hơn, chỉ cho site của bạn:** gắn nhãn `traffic_type: 'internal'` cho lượt xem của bạn. Mở site một lần với
`?me=1` ở cuối địa chỉ, trình duyệt nhớ mãi:

```js
// Đặt trước dòng gtag('config', ...) đang có
if (location.search.includes('me=1')) localStorage.setItem('me', '1');
gtag('config', 'G-XXXXXXX', localStorage.getItem('me') ? { traffic_type: 'internal' } : {});
```

Làm lại `?me=1` trên từng trình duyệt, từng máy. Xoá dữ liệu trang web thì phải mở lại link đó. Nhãn này chỉ có tác
dụng sau khi bạn bật bộ lọc ở bước 3 bên dưới.

### Cách 2: theo IP (thêm vào nếu bạn có IP cố định ở văn phòng)

1. **Admin → Data streams →** chọn web **→ Configure tag settings → Show all → Define internal traffic**.
2. **Create**: giữ `traffic_type = internal`, chọn *IP address equals*, dán IP hiện tại của bạn.
3. **Admin → Data collection and modification → Data filters → Internal Traffic.** Bộ lọc mặc định đang ở
   **Testing**. Để Testing 1–2 ngày, xem số có đúng không, rồi đổi sang **Active**.

⚠️ Khi đã **Active**, lượt bị lọc bị **xoá hẳn**, không lấy lại được. Lúc còn Testing, bạn xem được lượt nào sẽ bị lọc
bằng dimension *Test data filter name* trong Explore.

## B. Lọc bỏ Việt Nam khi xem báo cáo

Nếu blog viết cho người đọc tiếng Anh, khách Việt Nam chủ yếu là bạn và người quen. Lọc ở báo cáo thì xem lại được cả
số cũ.

### Nhanh: so sánh (comparison)

1. **Reports → Engagement → Pages and screens.**
2. Bấm **Add comparison** trên cùng → Dimension **Country** → đổi điều kiện thành **Exclude** → chọn **Vietnam** →
   **Apply**.
3. Mỗi bài hiện 2 dòng: *All users* và *không tính Vietnam*. Dòng thứ hai mới là số để chấm bài.

### Bền: Explore lưu sẵn

1. **Explore → Free form**, đặt tên "Blog — khách nước ngoài".
2. **Dimensions:** `Page path and screen class`, `Page title`, `Country`, `Session default channel group`,
   `Session source`.
3. **Metrics:** `Active users`, `Views`, `Average engagement time per active user`, `Engaged sessions`.
4. **Filters:**
   - `Country` **does not exactly match** `Vietnam`
   - `Page path and screen class` **contains** `/blog/`
5. Kéo `Page title` vào **Rows**, `Session default channel group` vào **Columns**. Đổi khoảng ngày ở góc trên.

Explore được lưu, lần sau mở lại là có ngay.

## Gạt bot ra

Dấu hiệu một nước là bot chứ không phải người thật:

- Thời gian xem gần **0 giây**, tỷ lệ engaged sessions gần **0%**.
- Toàn vào **Direct**, cùng một trang, cùng một giờ.
- Một nước lạ bỗng có số lượng lớn rồi mất hẳn (hay gặp: China, Singapore, Ireland, nơi đặt máy chủ đám mây).

Cách xử lý giống Việt Nam: thêm một điều kiện `Country` **does not exactly match** vào Explore. Đừng lọc vĩnh viễn ở
Admin, vì tuần sau có thể có người thật từ nước đó.

## Tự kiểm tra trong 2 phút

1. Mở **Reports → Realtime** trên một tab.
2. Mở blog của bạn trên tab khác.
3. Nếu Realtime **không** tăng (Cách 1) hoặc lượt của bạn mang nhãn internal (Cách 2) là xong.

> Đã làm xong: sang [trang 02](02-do-khach-tu-ai.md) để đo phần khách do AI gửi tới.
