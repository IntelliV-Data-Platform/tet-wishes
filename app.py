import streamlit as st
import time  # <--- THÊM DÒNG NÀY ĐỂ HẾT LỖI NameError
import random
import pytz
from datetime import datetime

# Cấu hình trang với giao diện Tết
st.set_page_config(
    page_title="Chúc Mừng Năm Mới 2026", 
    page_icon="🧧", 
    layout="centered"
)

# Ép khoảng trống phía trên về 0
st.markdown("""
    <style>
    /* Xóa khoảng cách header mặc định của Streamlit */
    .block-container {
        padding-top: 1rem;
        padding-bottom: 0rem;
        padding-left: 3rem;
        padding-right: 3rem;
    }
    
    /* Ẩn bớt các thành phần thừa phía trên */
    header {visibility: hidden;}
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    
    /* Thu nhỏ khoảng cách giữa các widget */
    [data-testid="stVerticalBlock"] {
        gap: 0rem;
    }
    </style>
    """, unsafe_allow_html=True)

# Danh sách lời chúc song ngữ Trung - Việt
loi_chuc_song_ngu = [
    # --- CÔNG DANH & SỰ NGHIỆP ---
    {"vn": "Công việc thuận lợi, sự nghiệp thăng tiến.", "cn": "事业有成, 大展宏图", "pinyin": "Shìyè yǒu chéng, dà zhǎn hóng tú"},
    {"vn": "Thăng quan tiến chức, phát tài phát lộc.", "cn": "升官发财", "pinyin": "Shēng guān fā cái"},
    {"vn": "Mã đáo thành công.", "cn": "马到成功", "pinyin": "Mǎ dào chéng gōng"},
    {"vn": "Một vốn bốn lời, làm ăn phát đạt.", "cn": "一本万利", "pinyin": "Yī běn wàn lì"},
    {"vn": "Tiền vào như nước, tài lộc dồi dào.", "cn": "财源广进", "pinyin": "Cái yuán guǎng jìn"},
    {"vn": "Thuận buồm xuôi gió.", "cn": "一帆风顺", "pinyin": "Yī fān fēng shùn"},
    {"vn": "Khởi đầu thuận lợi, vạn sự thành công.", "cn": "旗开得胜", "pinyin": "Qí kāi dé shèng"},

    # --- SỨC KHỎE & BÌNH AN ---
    {"vn": "Phúc như Đông Hải, Thọ tỷ Nam Sơn.", "cn": "福如东海, 寿比南山", "pinyin": "Fú rú dōng hǎi, shòu bǐ nán shān"},
    {"vn": "Tinh thần minh mẫn, thân thể kiện khang.", "cn": "精神焕发, 身体健康", "pinyin": "Jīng shén huàn fā, shēn tǐ jiàn kāng"},
    {"vn": "Sống lâu trăm tuổi, bách niên giai lão.", "cn": "长命百岁", "pinyin": "Cháng mìng bǎi suì"},
    {"vn": "Mọi sự bình an, cát tường như ý.", "cn": "一切平安, 吉祥如意", "pinyin": "Yī qiè píng'ān, jí xiáng rú yì"},
    {"vn": "An khang thịnh vượng, đời đời ấm no.", "cn": "安康兴旺", "pinyin": "Ānkāng xīngwàng"},

    # --- GIA ĐÌNH & HẠNH PHÚC ---
    {"vn": "Gia đình hạnh phúc, sum vầy vui vẻ.", "cn": "合家欢乐", "pinyin": "Hé jiā huān lè"},
    {"vn": "Ngũ phúc lâm môn.", "cn": "五福临门", "pinyin": "Wǔ fú lín mén"},
    {"vn": "Gia hòa vạn sự hưng.", "cn": "家和万事兴", "pinyin": "Jiā hé wàn shì xīng"},
    {"vn": "Con cháu đầy đàn, hiển vinh rạng rỡ.", "cn": "儿孙满堂", "pinyin": "Ér sūn mǎn táng"},

    # --- TÌNH DUYÊN & CUỘC SỐNG ---
    {"vn": "Muốn gì được nấy, cầu gì được nấy.", "cn": "从心所欲", "pinyin": "Cóng xīn suǒ yù"},
    #{"vn": "Tình sâu nghĩa nặng, bạc đầu giai lão.", "cn": "白头偕老", "pinyin": "Bái tóu xié lǎo"},
    {"vn": "Luôn luôn vui vẻ, nụ cười trên môi.", "cn": "笑口常开", "pinyin": "Xiào kǒu cháng kāi"},
    {"vn": "Trẻ mãi không già, rạng rỡ như hoa.", "cn": "青春永驻", "pinyin": "Qīng chūn yǒng zhù"}
]

# 1. HÌNH ẢNH: Banner Tết (Sử dụng ảnh minh họa rực rỡ)
st.image("https://brocanvas.vn/wp-content/uploads/2025/11/Anh-chu-ngua-Chuc-mung-nam-moi-2026-ngo-nghinh.jpg?auto=format&fit=crop&q=80&w=1000", 
         use_container_width=True, caption="Chúc Mừng Năm Mới 2026")

# 2. HIỆU ỨNG: Pháo hoa (Balloons)
st.balloons()

# 3. TRÌNH BÀY LỜI CHÚC
st.markdown("""
    <h1 style='
        text-align: center; 
        color: #D4AF37; 
        white-space: nowrap; 
        font-size: clamp(20px, 8vw, 60px);
        overflow: hidden;
        text-overflow: ellipsis;
        margin-top: 0px;
        padding-top: 0px;
    '>
        🏮 XUÂN BÍNH NGỌ 2026 🏮
    </h1>
    """, unsafe_allow_html=True)

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
        <h1 style='color: #FF4B4B; white-space: nowrap; 
        font-size: clamp(20px, 8vw, 60px);
        overflow: hidden;'>{item['vn']}</h1>
        <h2 style='color: #B8860B; white-space: nowrap; 
        font-size: clamp(20px, 8vw, 60px);
        overflow: hidden;'>{item['cn']}</h2>
        <p style='font-size: 18px; color: #555;'><i>{item['pinyin']}</i></p>
        <hr>
    </div>
    """, unsafe_allow_html=True)

st.write("") # Tạo khoảng trống

# 4. NÚT BẤM CÁ CÁNH
st.markdown("""
    <style>
    /* Định dạng nút bấm Streamlit */
    div.stButton > button:first-child {
        background-color: #FF4B4B; /* Màu đỏ Tết */
        color: #FFFFFF; /* Chữ trắng (hoặc dùng #D4AF37 cho màu vàng kim) */
        font-size: 20px;
        font-weight: bold;
        border-radius: 50px; /* Bo tròn nút */
        border: 2px solid #D4AF37; /* Viền vàng kim */
        padding: 16px 18px;
        width: 100%; /* Chiếm hết chiều ngang của cột col2 */
        transition: all 0.3s ease;
    }
    
    /* Hiệu ứng khi di chuột vào nút */
    div.stButton > button:first-child:hover {
        background-color: #D4AF37; /* Đổi sang nền vàng */
        color: #FF4B4B; /* Chữ đỏ */
        border: 2px solid #FF4B4B;
    }
    </style>
    """, unsafe_allow_html=True)
col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    if st.button('🧧 NHẬN QUẺ MAY MẮN KHÁC 🧧'):
        st.rerun()
# 5. ÂM THANH: Chèn nhạc Xuân không lời (Tự động phát nếu trình duyệt cho phép)
# Mã ID của video YouTube (Ví dụ bài nhạc Xuân)
video_id = "8EX-TujAa0A" 

# Danh sách các ID video YouTube nhạc Xuân khác nhau
# Bạn có thể thêm bao nhiêu tùy thích vào đây
list_nhac_xuan = [
    "8EX-TujAa0A", # Cả Xóm Khen Nghe List Nhạc Tết Remake Gì Mà Hay Dữ Dậy, Cho Link Mở Nghe Chung Thì Được Lì Xì 5 Xị
    "oma6S1qOGS8", # Nhạc Xuân sôi động
    "JhkMUqckRv8", # Tết Lofi nhẹ nhàng
    "3QHPuydn4y4", # Nhạc Tết Disco 2
    "z_zxcak6b-I"  # Nhạc Tết Disco 1
]

# Lấy thời gian hiện tại (giây) để làm "biến số" chọn nhạc
# Cách này giúp mỗi thời điểm truy cập sẽ ra một bài khác nhau
second_now = int(time.time())
index_nhac = second_now % len(list_nhac_xuan)
video_id = list_nhac_xuan[index_nhac]

# Chèn iframe ẩn với video đã được chọn ngẫu nhiên
st.components.v1.html(
    f"""
    <iframe src="https://www.youtube.com/embed/{video_id}?autoplay=1&loop=1&playlist={video_id}&mute=0" 
    width="0" height="0" frameborder="0" allow="autoplay"></iframe>
    """,
    height=0,
)

# 6. VIDEO: Chèn clip pháo hoa hoặc không khí Tết
#st.video("https://www.youtube.com/watch?v=8EX-TujAa0A&list=RD8EX-TujAa0A&start_radio=1&autoplay=1") # Clip ngắn về không khí Tết



st.markdown("---")
st.markdown("<p style='text-align: center;'>Chúc mừng Mùng 1 Tết! Hy vọng bạn có một năm rực rỡ như những đóa mai vàng.</p>", unsafe_allow_html=True)
