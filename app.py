import streamlit as st
import random

# Danh sách lời chúc song ngữ Trung - Việt
loi_chuc_song_ngu = [
    {
        "cn": "万事如意",
        "pinyin": "Wàn shì rú yì",
        "vn": "Vạn sự như ý - Mọi việc đều tốt đẹp như ý muốn."
    },
    {
        "cn": "身体健康",
        "pinyin": "Shēn tǐ jiàn kāng",
        "vn": "Sức khỏe dồi dào - Chúc cho thân thể luôn mạnh khỏe."
    },
    {
        "cn": "大吉大利",
        "pinyin": "Dà jí dà lì",
        "vn": "Đại cát đại lợi - Gặp nhiều may mắn, thu được lợi lộc lớn."
    },
    {
        "cn": "心想事成",
        "pinyin": "Xīn xiǎng shì chéng",
        "vn": "Sớm đạt ý nguyện - Những gì bạn mong cầu đều thành hiện thực."
    },
    {
        "cn": "阖家平安",
        "pinyin": "Hé jiā píng'ān",
        "vn": "Cả nhà bình an - Chúc cho gia đình luôn yên ấm, hòa thuận."
    },
    {
        "cn": "学业进步",
        "pinyin": "Xué yè jìn bù",
        "vn": "Học hành tiến tới - Dành riêng cho các em nhỏ, mong sớm thành tài."
    },
    {
        "cn": "生意兴隆",
        "pinyin": "Shēng yì xīng lóng",
        "vn": "Làm ăn phát đạt - Công việc kinh doanh ngày càng thịnh vượng."
    },
    {
        "cn": "五福临门",
        "pinyin": "Wǔ fú lín mén",
        "vn": "Ngũ phúc lâm môn - Năm loại phúc đức cùng đến cửa nhà."
    }
]

st.set_page_config(page_title="Chúc Mừng Năm Mới 2026", page_icon="🧧")
st.balloons()

st.title("🧧 Chúc Mừng Năm Mới 2026")
st.markdown("---")

# Chọn ngẫu nhiên
item = random.choice(loi_chuc_song_ngu)

st.subheader("Lời chúc may mắn dành cho bạn:")
st.markdown(f"<h1 style='text-align: center; color: #FF4B4B;'>{item['cn']}</h1>", unsafe_allow_html=True)
st.markdown(f"<p style='text-align: center; font-size: 20px;'><i>({item['pinyin']})</i></p>", unsafe_allow_html=True)
st.info(f"👉 **Nghĩa là:** {item['vn']}")

st.markdown("---")
if st.button('Nhận một quẻ may mắn khác 🧧'):
    st.rerun()
