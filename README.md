# Tool OCR Tiếng Việt - VietOCR

Ứng dụng Streamlit cho phép upload ảnh/PDF → OCR chữ đánh máy tiếng Việt bằng mô hình **VietOCR** (chuyên biệt tiếng Việt) → Xuất file TXT và Word.

## Tính năng
- Hỗ trợ ảnh (JPG, PNG) và PDF nhiều trang
- Sử dụng mô hình VietOCR Transformer (độ chính xác cao với tiếng Việt)
- Xuất kết quả .txt và .docx
- Xem theo từng trang

## Cách Deploy lên Streamlit Community Cloud (Miễn phí)

### Bước 1: Tạo GitHub Repository
1. Vào [github.com](https://github.com) → New repository
2. Đặt tên repo ví dụ: `vietocr-streamlit-tool`
3. Chọn **Public**
4. Tạo repository

### Bước 2: Upload các file
Upload 3 file sau vào repository:
- `app.py` (code trên)
- `requirements.txt`
- `README.md` (file này)

### Bước 3: Deploy trên Streamlit
1. Truy cập [https://share.streamlit.io/](https://share.streamlit.io/)
2. Đăng nhập bằng tài khoản GitHub
3. Nhấn **"New app"**
4. Điền thông tin:
   - Repository: chọn repo vừa tạo
   - Branch: `main` (hoặc master)
   - Main file path: `app.py`
5. Nhấn **Deploy**

> **Lưu ý**: Lần đầu deploy có thể mất **5-10 phút** vì phải tải model VietOCR (~400-500MB).

### Sau khi deploy
- Link ứng dụng sẽ có dạng: `https://ten-app-cua-ban.streamlit.app`
- Ai cũng có thể truy cập qua link này.

## Lưu ý quan trọng
- Ứng dụng chạy trên **CPU** (không GPU) → tốc độ OCR khoảng 1-3 giây/trang.
- Với PDF rất dài (>50 trang) nên chạy local sẽ nhanh hơn.
- Model VietOCR được tự động tải khi chạy lần đầu.

---

**Mọi thắc mắc hoặc muốn thêm tính năng (parse form, searchable PDF...)** thì liên hệ qua GitHub Issues.