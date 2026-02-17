import streamlit as st
import random

# Cấu hình trang với giao diện Tết
st.set_page_config(
    page_title="Chúc Mừng Năm Mới 2026", 
    page_icon="🧧", 
    layout="centered"
)

# Danh sách lời chúc song ngữ Trung - Việt
loi_chuc_song_ngu = [
    {"cn": "万事如意", "pinyin": "Wàn shì rú yì", "vn": "Vạn sự như ý - Mọi việc đều tốt đẹp như ý muốn."},
    {"cn": "身体健康", "pinyin": "Shēn tǐ jiàn kāng", "vn": "Sức khỏe dồi dào - Thân thể luôn mạnh khỏe, an khang."},
    {"cn": "心想事成", "pinyin": "Xīn xiǎng shì chéng", "vn": "Sớm đạt ý nguyện - Những gì bạn mong cầu đều thành hiện thực."},
    {"cn": "阖家平安", "pinyin": "Hé jiā píng'ān", "vn": "Gia đạo bình an - Cả nhà luôn yên ấm, hòa thuận."},
    {"cn": "吉星高照", "pinyin": "Jí xīng gāo zhào", "vn": "Cát tinh cao chiếu - Ngôi sao may mắn luôn soi sáng cho bạn."}
]

# 0. ÂM THANH: Chèn nhạc Xuân không lời (Tự động phát nếu trình duyệt cho phép)
st.components.v1.html(
    """
    <iframe src="https://www.youtube.com/watch?v=8EX-TujAa0A&list=RD8EX-TujAa0A?autoplay=1&loop=1&playlist=S8L6_fCAnW8" 
    width="0" height="0" frameborder="0" allow="autoplay"></iframe>
    """,
    height=0,
)

# 1. NÚT BẤM CÁ CÁNH
col1, col2, col3 = st.columns([1,2,1])
with col2:
    if st.button('🧧 NHẬN QUẺ MAY MẮN KHÁC 🧧'):
        st.rerun()

# 2. HÌNH ẢNH: Banner Tết (Sử dụng ảnh minh họa rực rỡ)
st.image("https://brocanvas.vn/wp-content/uploads/2025/11/Anh-chu-ngua-Chuc-mung-nam-moi-2026-ngo-nghinh.jpg?auto=format&fit=crop&q=80&w=1000", 
         use_container_width=True, caption="Chúc Mừng Năm Mới 2026")

# 3. HIỆU ỨNG: Pháo hoa (Balloons)
st.balloons()

# 4. TRÌNH BÀY LỜI CHÚC
st.markdown("<h1 style='text-align: center; color: #D4AF37;'>🏮 XUÂN BÍNH NGỌ 2026 🏮</h1>", unsafe_allow_html=True)

# CSS để tạo khung lời chúc đẹp hơn
st.markdown("""
    <style>
    .wish-box {
        background-color: #fce4ec;
        border-radius: 15px;
        padding: 10px;
        border: 2px solid #ff4b4b;
        text-align: center;
    }
    </style>
    """, unsafe_allow_html=True)

# Chọn ngẫu nhiên
item = random.choice(loi_chuc_song_ngu)

st.markdown(f"""
    <div class='wish-box'>
        <h1 style='color: #FF4B4B;'>{item['vn']}</h1>
        <h2 style='color: #B8860B; font-size: 50px;'>{item['cn']}</h2>
        <p style='font-size: 20px; color: #555;'><i>{item['pinyin']}</i></p>
        <hr>
    </div>
    """, unsafe_allow_html=True)

st.write("") # Tạo khoảng trống

# 5. VIDEO: Chèn clip pháo hoa hoặc không khí Tết
#st.video("https://www.youtube.com/watch?v=8EX-TujAa0A&list=RD8EX-TujAa0A&start_radio=1&autoplay=1") # Clip ngắn về không khí Tết



st.markdown("---")
st.markdown("<p style='text-align: center;'>Chúc mừng Mùng 1 Tết! Hy vọng bạn có một năm rực rỡ như những đóa mai vàng.</p>", unsafe_allow_html=True)
