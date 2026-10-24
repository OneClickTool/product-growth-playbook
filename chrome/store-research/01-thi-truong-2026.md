# Thị trường Chrome Web Store 2026

> Khảo sát ngày **24/10/2026**. Số liệu từ bên thứ ba (tự crawl store), không phải từ Google.

## Tóm tắt trong 5 dòng

1. Store **đang phình to rất nhanh**: 221.717 extension đã xuất bản vào 30/6/2026, riêng quý 2 tăng ròng **+43.418**.
2. Chrome tăng nhanh hơn hẳn các store khác: số tăng ròng quý 2 gấp **hơn 5 lần** Firefox và Edge cộng lại.
3. **Đuôi dài cực dài**: extension ở giữa chỉ có **14 users**; 70% extension có ≤ 100 users.
4. Một số danh mục **đông người bán hơn người mua**: ở danh mục Privacy (chặn quảng cáo, chặn theo dõi, VPN…), số extension tăng gần **1,5 lần** trong 3 tháng mà lượt cài gần như đứng yên ([giải thích bên dưới](#vi-du-privacy-cho-nhieu-sap-it-khach)).
5. Vẫn còn **khoảng trống**: ở nhiều danh mục lớn, hơn một nửa listing chưa có đánh giá nào.

## Quy mô và tốc độ

| Mốc | Chrome | Firefox | Edge | Nguồn |
|---|---|---|---|---|
| Extension đã xuất bản, 30/6/2026 | **221.717** | 89.952 | 30.636 | [Exstats Q2/2026](https://exstats.com/blog/state-of-browser-extensions-q2-2026) |
| Tăng ròng trong quý 2/2026 | **+43.418** | +6.487 | +1.895 | như trên |
| Extension "active", 3/2026 | 178.299 | — | — | [Exstats Q1/2026](https://exstats.com/blog/state-of-browser-extensions-q1-2026) |

Bối cảnh: khi Chrome gỡ các extension Manifest V2, [Exstats](https://exstats.com/blog/mv2-purge-in-numbers) đếm được
**44.158** extension bị gỡ. Các bài viết cũ còn trích con số ~112.000 extension (dữ liệu khoảng 8/2024). Tức là store
đã co lại sau đợt dọn MV2 rồi tăng mạnh trở lại trong 2026. **Giả thuyết của playbook** (chưa có nguồn chứng minh):
công cụ AI giúp làm extension nhanh hơn là một phần lý do.

## Ý nghĩa với người làm extension nhỏ

![Bậc thang users](../../site/images/chrome-user-ladder.svg)

| Thực tế | Nghĩa là |
|---|---|
| Mỗi quý thêm hàng chục nghìn extension mới | Ra mắt rồi chờ người tự tìm thấy thì gần như không ai thấy. Phải có kênh kéo người (bài viết, cộng đồng, SEO listing) |
| Median 14 users, 70% ≤ 100 users ([Exstats](https://exstats.com/blog/state-of-browser-extensions-q2-2026)) | Có 100 users là đã hơn phần lớn store. Đừng so mình với Grammarly, so với mốc này (xem [thang vị trí](../dev-analytics/04-suc-khoe-extension.md)) |
| Chỉ 2,63% extension vượt 10.000 users | Top nhỏ, rất khó vào; nhưng dưới đó còn nhiều chỗ cho extension giải quyết đúng một việc |
| Danh mục Privacy: đối thủ tăng nhanh hơn hẳn khách ([ví dụ bên dưới](#vi-du-privacy-cho-nhieu-sap-it-khach)) | Vào đó bây giờ là chia một miếng bánh nhỏ cho nhiều người hơn. Chọn ngách mà khách tăng nhanh hơn đối thủ |
| Nhiều danh mục lớn có hơn một nửa listing 0 đánh giá | Có vài đánh giá thật là đã nổi hơn nửa danh mục. Xin review sớm ([aso-review-and-rating-strategy](../../skills/aso/aso-review-and-rating-strategy/SKILL.md)) |

## Ví dụ Privacy: chợ nhiều sạp, ít khách

**Privacy & Security** là danh mục của các extension chặn quảng cáo, chặn theo dõi, VPN, quản lý mật khẩu, xóa cookie.
Theo [Exstats](https://exstats.com/blog/browser-extension-category-opportunity-map-2026), trong 90 ngày gần nhất:

- **Số extension** trong danh mục tăng **47,7%**: cứ 100 extension thì thêm 48 cái mới.
- **Tổng lượt cài** của cả danh mục chỉ tăng **8,5%**: cứ 100 lượt cài thì chỉ thêm 8–9 lượt.

Hình dung một **cái chợ**: 3 tháng trước có 100 sạp bán rau, mỗi ngày 1.000 khách. Bây giờ có 148 sạp, nhưng khách chỉ
tăng lên 1.085. Rau không đổi, khách gần như không đổi, chỉ có thêm người bán. **Mỗi sạp tự nhiên bán ít đi.**

> **Illustrative example.** Phép tính từ hai con số trên, giả sử danh mục bắt đầu với 100 extension và 100.000 lượt cài:
>
> | | 3 tháng trước | Bây giờ |
> |---|---|---|
> | Số extension | 100 | 148 (+47,7%) |
> | Tổng lượt cài | 100.000 | 108.500 (+8,5%) |
> | **Trung bình mỗi extension** | **1.000** | **~733 (giảm ~27%)** |
>
> Mỗi extension trong danh mục trung bình mất khoảng **1/4 lượt cài**, dù chẳng ai làm gì sai.

**Bài học:** trước khi chọn ngách, so **tốc độ tăng của đối thủ** với **tốc độ tăng của khách**:

| Đối thủ tăng | Khách tăng | Nghĩa là |
|---|---|---|
| chậm | nhanh | 🟢 Chợ đang đông khách lên: vào ngay |
| nhanh | nhanh | 🟡 Đông vui nhưng phải có điểm khác biệt rõ |
| nhanh | chậm | 🔴 Như Privacy bây giờ: chỉ vào khi bạn có thứ người khác không có |

Tự kiểm ngách của bạn: tìm từ khóa chính trên Chrome Web Store, đếm xem trong 10–20 kết quả đầu có bao nhiêu extension
mới ra trong 3 tháng gần đây, và số users của chúng có tăng không (xem lịch sử users trên
[Exstats](https://exstats.com/) hoặc [Chrome-Stats](https://chrome-stats.com/)).

## Store xếp hạng thế nào (còn tranh cãi)

Google không công bố thuật toán. Theo phân tích ~120.000 điểm dữ liệu của
[Extension Ranker](https://extensionranker.com/blog/chrome-web-store-ranking-patterns): **mức độ liên quan với từ
khóa** quyết định extension vào nhóm kết quả nào, rồi **weekly users, rating và số review** quyết định thứ tự trong
nhóm. Một bài trên [DEV Community](https://dev.to/extensionbooster/the-chrome-web-store-ranking-algorithm-changed-heres-what-actually-moves-installs-in-2026-29g1)
cho rằng năm 2026 weekly users được tính nặng hơn tổng installs; chưa kiểm chứng được. Điểm chung của cả hai:
**giữ chân user** (weekly users) ảnh hưởng tới thứ hạng, nên uninstall cao không chỉ mất user mà còn mất vị trí.

## Nguồn

- [Exstats: Browser Extension Market Q2 2026](https://exstats.com/blog/state-of-browser-extensions-q2-2026)
- [Exstats: Q1 2026](https://exstats.com/blog/state-of-browser-extensions-q1-2026)
- [Exstats: Extension Opportunity Map 2026](https://exstats.com/blog/browser-extension-category-opportunity-map-2026)
- [Exstats: MV2 Purge in Numbers](https://exstats.com/blog/mv2-purge-in-numbers)
- [Extension Ranker: Chrome Web Store Rankings, Patterns Across 120K Data Points](https://extensionranker.com/blog/chrome-web-store-ranking-patterns)
