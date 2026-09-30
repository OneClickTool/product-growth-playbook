# Kế hoạch triển khai: Product Growth Playbook (bản đã review)

> Free knowledge. Paid tools.
> Một repo duy nhất, đi sâu vào ít mảng trước, mở rộng theo nhu cầu thật.

Ngày bắt đầu (Day 0): **2026-09-29** · Chủ repo: `OneClickTool/product-growth-playbook`

---

## 0. Những gì đã đổi so với bản nháp (và tại sao)

| # | Bản nháp | Bản này | Lý do |
|---|---|---|---|
| 1 | Skill = 1 file `.md` rời (`skills/aso/keyword-research.md`) | Skill = **thư mục có `SKILL.md`** theo chuẩn Agent Skills (`skills/aso/aso-keyword-research/SKILL.md`) | Vừa đọc được trên GitHub như bài viết, vừa **cài được** vào Claude Code / Codex / Gemini CLI / Cursor. "Cài được" là lý do lớn nhất để người ta star repo skill hiện nay. |
| 2 | Frontmatter tự chế (`difficulty`, `time`, `works_with`) | `name` + `description` (chuẩn) + các trường riêng để trong `metadata:` | Trình đọc skill chỉ hiểu `name`/`description`; `description` quyết định AI có tự gọi skill hay không. |
| 3 | Template có code block lồng code block (```` ``` ```` trong ```` ``` ````) | Dùng fence 4 dấu hoặc `~~~` | Bản nháp render vỡ trên GitHub ngay ở phần "Prompt mẫu". |
| 4 | Nội dung trộn Việt / Anh | **Nội dung skill + README: tiếng Anh**. Tài liệu nội bộ (`docs/PLAN.md`): tiếng Việt. Bản dịch VN để Backlog. | Mục tiêu là Show HN, Reddit, awesome-list, 300–500 star, nên kênh nào cũng cần tiếng Anh. |
| 5 | Hứa 15 skill trong 30 ngày, nhưng lại chốt nhịp "1 skill/tuần" | **12 skill / 90 ngày**: 2 skill/tuần trong 4 tuần đầu, sau đó 1 skill/tuần | Hai con số cũ mâu thuẫn nhau. Kế hoạch trễ hạn thì người làm dễ bỏ giữa chừng. |
| 6 | Không có cơ chế kiểm tra chất lượng | `scripts/validate_skills.py` (contributor tự chạy trước khi mở PR, không dùng GitHub Actions) | Học từ Claude-Code-Game-Studios (có skill-testing framework). Khi có contributor, script bắt lỗi format thay cho người review. |
| 7 | Không có "cửa vào" | Skill router **`growth`**: hỏi sản phẩm đang ở giai đoạn nào rồi chỉ sang skill phù hợp | Giống `/app` trong app-AI-skills. Người mới không phải tự đọc mục lục. |
| 8 | `templates/` tách riêng ở root | Template của skill nào để trong `assets/` của skill đó. `templates/` ở root chỉ để template dùng chung | Khi cài một skill, template đi kèm luôn. |
| 9 | "Ví dụ thật có số liệu" nhưng không có luật | Ví dụ minh họa phải **ghi nhãn rõ** là minh họa; `examples/` chỉ nhận số liệu thật | Số bịa mà trông như số thật thì mất uy tín, và uy tín là tài sản chính của repo này. |
| 10 | Không nói tới AI agent đóng góp | Có `CLAUDE.md` + `AGENTS.md` | Contributor ngày nay viết skill bằng AI. Hai file này giữ cho AI viết đúng format. |

Giữ nguyên: định vị, 3 mảng ASO / Launch / Monetization, link sản phẩm khiêm tốn ở cuối có UTM, kế hoạch phân phối, bảng rủi ro.

---

## 1. Mục tiêu & định vị

**Tagline:** Free, open-source growth skills for people building digital products: ASO, launch, monetization and more.

**Đối tượng:** người build app, SaaS, game, AI product, website, extension.

**Nguyên tắc:**
1. Một repo duy nhất để dồn star và contributor.
2. Gọi là "Growth Skills". Chạy được với mọi AI và cả khi làm tay.
3. Nội dung quan trọng hơn cấu trúc. Sâu quan trọng hơn rộng.
4. Mỗi skill vừa là **bài hướng dẫn cho người đọc**, vừa là **skill cài được cho AI agent**.
5. Link sản phẩm của mình để ở cuối, nói rõ là của mình, có UTM.

**KPI 90 ngày (tới 2026-12-28):**

| Chỉ số | Mục tiêu |
|---|---|
| Skill hoàn chỉnh (qua validator + qua checklist chất lượng) | 12 (tối thiểu 4 / mảng) |
| Playbook | 2 |
| GitHub star | 300–500 |
| Contributor ngoài có PR được merge | 5+ |
| Click sang Markdown Viewer / Shotmatic | theo dõi bằng UTM, không đặt KPI |

---

## 2. Cấu trúc repo (tham khảo Claude-Code-Game-Studios + app-AI-skills)

```text
product-growth-playbook/
├── README.md                    # landing page (EN)
├── CLAUDE.md                    # luật cho Claude Code khi làm việc trong repo
├── AGENTS.md                    # như trên, cho Codex / Cursor / Gemini CLI
├── CONTRIBUTING.md
├── CODE_OF_CONDUCT.md
├── CHANGELOG.md
├── LICENSE                      # MIT
├── SKILL_TEMPLATE.md            # format chuẩn cho mọi skill
│
├── .claude-plugin/
│   └── marketplace.json         # /plugin marketplace add OneClickTool/product-growth-playbook
├── .github/
│   ├── ISSUE_TEMPLATE/          # skill-request · skill-feedback
│   └── PULL_REQUEST_TEMPLATE.md # checklist chất lượng
│
├── skills/
│   ├── growth/SKILL.md          # ROUTER: "đang ở giai đoạn nào?" → trỏ skill
│   ├── aso/
│   │   ├── README.md            # mục lục mảng
│   │   └── aso-keyword-research/
│   │       ├── SKILL.md
│   │       ├── assets/          # template CSV, bảng tính…
│   │       └── scripts/         # (tùy chọn) script nhỏ, chạy không cần cài gì thêm
│   ├── launch/
│   └── monetization/
│
├── playbooks/                   # ghép nhiều skill thành lộ trình (md thường)
├── examples/                    # case thật có số liệu (chưa có thì chưa tạo)
├── scripts/validate_skills.py
└── docs/
    ├── PLAN.md                  # file này
    └── skill-anatomy.md         # giải thích vì sao skill có format như vậy
```

**Quy ước tên:** thư mục skill = `name` trong frontmatter = `<mảng>-<việc>`, ví dụ `aso-keyword-research`. Có tiền tố mảng thì không trùng tên với skill của repo khác khi người dùng cài chung.

**Chưa tạo:** `examples/`, `templates/`, `case-studies/`, `checklists/`, `launch/`, `monetization/`. Mảng nào có skill đầu tiên thì mới tạo thư mục mảng đó.

---

## 3. Danh sách skill giai đoạn 1 (theo thứ tự viết)

| # | Skill | Mảng | Tuần |
|---|---|---|---|
| 0 | `growth` (router) | — | 1 ✅ |
| 1 | `aso-keyword-research` | ASO | 1 ✅ bản nháp, **cần thay ví dụ minh họa bằng case thật** |
| 2 | `launch-pre-launch-checklist` | Launch | 2 → ✅ bản nháp 30/09 |
| 3 | `monetization-pricing-strategy` | Monetization | 2 → ✅ bản nháp 30/09 |
| 4 | `aso-title-subtitle-optimization` | ASO | 3 → ✅ bản nháp 30/09 |
| 5 | `launch-get-first-100-users` | Launch | 3 → ✅ bản nháp 30/09 |
| 6 | `monetization-paywall-design` | Monetization | 4 → ✅ bản nháp 30/09 |
| 7 | `aso-screenshot-strategy` | ASO | 4 → ✅ bản nháp 30/09 |
| 8 | `launch-product-hunt-launch` | Launch | 5 → ✅ bản nháp 30/09 |
| 9 | `monetization-free-trial-vs-freemium` | Monetization | 6 → ✅ bản nháp 30/09 |
| 10 | `aso-review-and-rating-strategy` | ASO | 7 → ✅ bản nháp 30/09 |
| 11 | `launch-post-writing` | Launch | 8 → ✅ bản nháp 30/09 |
| 12 | `monetization-subscription-tiers` | Monetization | 9 → ✅ bản nháp 30/09 |
| — | `aso-competitor-audit`, `launch-community-seeding`, `monetization-pricing-experiments` | | dự phòng / cho contributor (`good first issue`) |

> **Cập nhật 30/09:** cả 12 skill đã có bản nháp (viết sớm hơn lịch). Việc của các tuần tới đổi thành:
> (1) chạy thử từng skill với AI trên sản phẩm thật, (2) thay ví dụ `Illustrative` bằng số liệu thật,
> (3) phân phối theo mục 5. **ShotMatic không phải công cụ làm screenshot** (nó là "một màn hình cho mọi repo
> AI-agent"), nên không gắn vào `aso-screenshot-strategy`. Link ShotMatic và Markdown Viewer chỉ để ở cuối README.

Viết xen kẽ các mảng để mảng nào cũng sớm có ít nhất 1 skill. Một mảng chỉ có README mà không có skill thì nhìn như khung rỗng.

---

## 4. Chuẩn chất lượng một skill (Definition of Done)

- [ ] Có frontmatter `name` (trùng tên thư mục) và `description` (≤ 1024 ký tự, nói **làm gì + khi nào dùng**).
- [ ] Có đủ các mục: Goal · When to use · Inputs · Steps · Prompt · Example output · Common mistakes · Related skills.
- [ ] Có ít nhất 1 prompt copy-paste được (đặt trong fence 4 dấu).
- [ ] Ví dụ output: số liệu thật, hoặc ghi nhãn `Illustrative` rõ ràng.
- [ ] Làm theo trong ≤ 1 giờ. `SKILL.md` ≤ 500 dòng; phần dài thì tách sang `references/`.
- [ ] Không có "10 tips chung chung". Bước nào cũng có hành động cụ thể và đầu ra kiểm tra được.
- [ ] Đã chạy thử skill với ít nhất 1 AI (Claude / ChatGPT) trên một sản phẩm thật.
- [ ] Đã có trong `marketplace.json`, bảng README của mảng và README gốc. `python3 scripts/validate_skills.py` pass.

---

## 5. Phân phối

| Kênh | Hành động | Khi nào |
|---|---|---|
| GitHub SEO | Topics: `agent-skills`, `claude-skills`, `growth-hacking`, `aso`, `app-marketing`, `product-launch`, `monetization`, `indie-hacker`; social preview image | Tuần 1 |
| Skill directories | Gửi vào `VoltAgent/awesome-agent-skills`, skills.sh, các awesome-claude-skills | Khi có ≥ 4 skill |
| Awesome-list growth / ASO / indie | PR vào 3–5 list | Khi có ≥ 6 skill |
| Reddit | r/indiehackers, r/SaaS, r/iOSProgramming, r/androiddev, r/startups. Đăng nguyên nội dung skill, link repo để cuối | Mỗi tuần 1 bài |
| X / LinkedIn | Thread "1 skill / tuần", kèm ví dụ thật | Mỗi tuần |
| Hacker News | Show HN | Khi có ≥ 10 skill |
| Cộng đồng VN | Group indie hacker / dev / marketing | Từ tuần 2 |
| Product Hunt | Chỉ khi đã có landing / newsletter | Sau ngày 60 |

---

## 6. Lộ trình

### Tuần 1 (29/09 – 05/10): Nền móng ✅ phần repo
- [x] LICENSE, `.gitignore`, `SKILL_TEMPLATE.md`, `CONTRIBUTING.md`, `CODE_OF_CONDUCT.md`, `CLAUDE.md`, `AGENTS.md`
- [x] README bản đầu, marketplace.json, issue/PR templates, validator script
- [x] Router `growth` + skill mẫu `aso-keyword-research`
- [ ] **Bạn:** thay ví dụ minh họa trong `aso-keyword-research` bằng số liệu thật từ 1 app của bạn
- [ ] **Bạn:** tạo repo trên GitHub, push, thêm topics, social preview, bật Discussions
- [ ] Nhờ review skill #1 để chốt chuẩn chất lượng trước khi viết hàng loạt

### Ngày 8–30 (06/10 – 29/10): Mỗi mảng có skill
- [x] Skill #2 → #7 (viết sớm, xong 30/09)
- [x] Playbook `playbooks/launch-a-product.md`
- [ ] Gửi vào skill directories. Bắt đầu nhịp 1 bài/tuần trên Reddit và X

### Ngày 31–60 (30/10 – 28/11): Đẩy phân phối
- [x] Skill #8 → #11 (xong 30/09)
- [ ] Playbook `aso-optimization.md`
- [ ] `examples/` với ≥ 2 case thật
- [ ] Mở 3–5 `good first issue` (các skill dự phòng)
- [ ] PR vào awesome-list. Show HN khi đủ 10 skill

### Ngày 61–90 (29/11 – 28/12): Mở rộng có căn cứ
- [x] Skill #12 (xong 30/09).
- [ ] Dựa vào traffic, issue và Discussions để chọn 1–2 mảng mới từ Backlog
- [ ] `case-studies/` khi có ≥ 3 case thật. Cân nhắc newsletter / landing
- [ ] Nếu mỗi mảng ≥ 6 skill: tách `marketplace.json` thành plugin theo từng mảng (`growth-aso`, `growth-launch`…)

---

## 7. Backlog
- Mảng: `seo`, `content`, `social`, `conversion`, `retention`, `analytics`, `competitor-research`, `user-research`
- Playbooks: `get-first-1000-users`, `grow-an-app`, `monetization`
- Bản dịch tiếng Việt (`README.vi.md`, sau đó là skill)
- Bộ test hành vi cho skill (kiểu CCGS Skill Testing Framework): mỗi skill có 1–2 test case "input → output phải có…"

---

## 8. Vận hành cộng đồng
- Mọi skill theo `SKILL_TEMPLATE.md`; validator fail thì chưa review.
- PR template có checklist Definition of Done (mục 4).
- Trả lời issue/PR trong 48h. Dùng GitHub Discussions, không lập Discord sớm.
- Ghi công contributor trong `metadata.author` của skill và trong README (all-contributors khi có ≥ 3 người).

## 9. Rủi ro

| Rủi ro | Cách tránh |
|---|---|
| Repo nhìn như khung rỗng | Chỉ tạo folder khi có nội dung, không liệt kê skill chưa viết như thể đã có |
| Nội dung chung chung | Definition of Done + Example output bắt buộc |
| Số liệu bịa làm mất uy tín | Nhãn `Illustrative`; `examples/` chỉ nhận số thật |
| Quảng cáo lộ liễu | Link sản phẩm ở cuối, minh bạch, có UTM |
| Không có traffic | Phân phối chạy song song ngay từ tuần 2 |
| Format lộn xộn khi có contributor | Validator + `CLAUDE.md` / `AGENTS.md` |
| Bỏ dở | 1–2 skill/tuần, có ngày cụ thể ở mục 6 |
