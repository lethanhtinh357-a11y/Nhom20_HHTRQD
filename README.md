# Hướng dẫn chi tiết cài đặt và chạy dự án Nhom20_HHTRQD

Tài liệu này cung cấp các bước chi tiết để bạn có thể quay video hướng dẫn cài đặt dự án từ GitHub, cấu hình cơ sở dữ liệu và chạy ứng dụng.

## 1. Chuẩn bị công cụ (Prerequisites)
Trước khi bắt đầu, hãy đảm bảo máy tính đã cài đặt:
- **Python 3.9+**: [Tải tại đây](https://www.python.org/downloads/)
- **PostgreSQL**: [Tải tại đây](https://www.postgresql.org/download/)
- **Git**: [Tải tại đây](https://git-scm.com/downloads)

## 2. Các bước thực hiện (Step-by-step)

### Bước 1: Clone dự án từ GitHub
Mở terminal (CMD hoặc PowerShell) và chạy lệnh:
```bash
git clone https://github.com/lethanhtinh357-a11y/Nhom20_HHTRQD.git
cd Nhom20_HHTRQD
```

### Bước 2: Tạo môi trường ảo (Virtual Environment)
Việc này giúp quản lý thư viện riêng biệt cho dự án:
```bash
# Tạo môi trường ảo tên là .venv
python -m venv .venv

# Kích hoạt môi trường ảo (Windows)
.venv\Scripts\activate

# Kích hoạt môi trường ảo (macOS/Linux)
# source .venv/bin/activate
```

### Bước 3: Cài đặt các thư viện cần thiết
Cài đặt tất cả dependencies từ file `requirements.txt`:
```bash
pip install -r requirements.txt
```

### Bước 4: Cấu hình Cơ sở dữ liệu (PostgreSQL)
Ứng dụng sử dụng PostgreSQL để lưu trữ phản hồi của khách hàng. Bạn có 2 cách cấu hình:

#### Cách A: Sử dụng Biến môi trường (Khuyên dùng)
Thiết lập thông tin kết nối trực tiếp trong terminal trước khi chạy app:
```powershell
# Windows PowerShell
$env:PGHOST="localhost"
$env:PGPORT="5432"
$env:PGDATABASE="airline"
$env:PGUSER="postgres"
$env:PGPASSWORD="Mật_khẩu_Postgres_của_bạn"
$env:FLASK_SECRET_KEY="any-secret-key"
```
*(Lưu ý: Thay `Mật_khẩu_Postgres_của_bạn` bằng mật khẩu thật của user `postgres` trên máy bạn)*

#### Cách B: Chỉnh sửa trực tiếp trong code
Mở file `flask_ui/app_flask.py`, tìm đến dòng ~175 (biến `DB_CONFIG`) và điền thông tin của bạn vào.

### Bước 5: Chạy ứng dụng Flask
Chạy lệnh sau để khởi động server:
```bash
python flask_ui/app_flask.py
```
**Lưu ý:** Trong lần chạy đầu tiên, hệ thống sẽ tự động:
1. Kết nối tới PostgreSQL.
2. Tạo database tên là `airline` (nếu chưa có).
3. Tạo các bảng `feedback_submissions` và `admin_users`.
4. Tạo tài khoản admin mặc định: `admin` / `admin`.

### Bước 6: Truy cập và sử dụng
- **Giao diện khách hàng (Khảo sát):** Mở trình duyệt truy cập `http://localhost:8502/survey`
- **Giao diện Quản trị viên (Dashboard):** Truy cập `http://localhost:8502/admin/login`
  - Tài khoản: `admin`
  - Mật khẩu: `admin`

---

## 3. Kịch bản video gợi ý (Video Script Outline)

1. **Giới thiệu (0:00 - 0:30):** Giới thiệu dự án Hệ thống Hỗ trợ Ra quyết định (DSS) đánh giá mức độ hài lòng khách hàng hàng không.
2. **Clone & Cài đặt (0:30 - 2:00):** Show màn hình terminal thực hiện các lệnh `git clone`, `venv`, và `pip install`.
3. **Cấu hình Database (2:00 - 3:30):** Hướng dẫn mở PostgreSQL, giải thích cách app tự động tạo bảng. Show cách đặt biến môi trường cho mật khẩu.
4. **Chạy App (3:30 - 4:30):** Chạy lệnh `python flask_ui/app_flask.py`. Quay cảnh server khởi động thành công.
5. **Demo chức năng (4:30 - Kết thúc):** 
   - Thực hiện nhập 1 khảo sát mẫu (Survey).
   - Đăng nhập vào trang Admin để xem Dashboard và các đề xuất quyết định (Decision Support) dựa trên thuật toán AHP.

## 4. Các lệnh quan trọng cần nhớ
| Lệnh | Mô tả |
| :--- | :--- |
| `python -m venv .venv` | Tạo môi trường ảo |
| `.venv\Scripts\activate` | Kích hoạt môi trường (Windows) |
| `pip install -r requirements.txt` | Cài đặt thư viện |
| `python flask_ui/app_flask.py` | Chạy ứng dụng Web |
| `streamlit run app.py` | Chạy bản demo Streamlit (nếu cần) |
