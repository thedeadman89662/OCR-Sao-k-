import streamlit as st
from PIL import Image
import easyocr
import numpy as np
from pdf2image import convert_from_bytes
import io
from docx import Document
from datetime import datetime

st.set_page_config(page_title="OCR Tiếng Việt", page_icon="🔍", layout="wide")

st.title("🔍 Tool OCR Chữ Đánh Máy Tiếng Việt")
st.markdown("**Hỗ trợ PDF & Ảnh • Xuất TXT & Word**")

@st.cache_resource
def load_reader():
    return easyocr.Reader(['vi', 'en'], gpu=False)

reader = load_reader()

uploaded_file = st.file_uploader("Upload ảnh hoặc PDF", 
                                 type=["jpg", "jpeg", "png", "pdf"])

if uploaded_file is not None:
    all_text = ""
    pages = []

    try:
        if uploaded_file.type == "application/pdf":
            st.info(f"📄 Đang xử lý PDF: {uploaded_file.name}")
            with st.spinner("Chuyển PDF sang ảnh..."):
                images = convert_from_bytes(uploaded_file.read(), dpi=220)  # Giảm dpi để nhanh hơn
        else:
            images = [Image.open(uploaded_file)]
    except Exception as e:
        st.error("❌ Không thể xử lý file PDF. Đảm bảo đã có file `packages.txt` chứa `poppler-utils`.")
        st.stop()

    # OCR
    progress_bar = st.progress(0)
    status_text = st.empty()

    for i, img in enumerate(images):
        status_text.text(f"OCR trang {i+1}/{len(images)} ...")
        img_array = np.array(img)
        
        results = reader.readtext(img_array, detail=0, paragraph=True)
        page_text = "\n\n".join(results)
        
        all_text += f"--- Trang {i+1} ---\n{page_text}\n\n"
        pages.append((i+1, img, page_text))
        
        progress_bar.progress((i + 1) / len(images))

    st.success(f"✅ Hoàn tất OCR! ({len(images)} trang)")

    # Tabs
    tab1, tab2, tab3 = st.tabs(["📋 Toàn bộ Text", "📄 Xem theo trang", "📥 Tải file"])

    with tab1:
        st.text_area("Kết quả OCR:", all_text, height=400)

    with tab2:
        for page_num, img, text in pages:
            with st.expander(f"Trang {page_num}"):
                col1, col2 = st.columns([1,1])
                with col1:
                    st.image(img, use_column_width=True)
                with col2:
                    st.text_area("Nội dung", text, height=250)

    with tab3:
        col1, col2 = st.columns(2)
        with col1:
            st.download_button("📥 Tải .txt", all_text, f"ocr_result_{datetime.now().strftime('%Y%m%d')}.txt")
        with col2:
            doc = Document()
            doc.add_heading('KẾT QUẢ OCR', 0)
            doc.add_paragraph(all_text)
            bio = io.BytesIO()
            doc.save(bio)
            st.download_button(
                "📥 Tải Word (.docx)", 
                bio.getvalue(),
                f"ocr_result_{datetime.now().strftime('%Y%m%d')}.docx",
                mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document"
            )

else:
    st.info("👆 Upload file ảnh hoặc PDF để bắt đầu OCR")
