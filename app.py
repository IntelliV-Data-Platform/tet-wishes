import streamlit as st
import random

# Danh sách lời chúc ngẫu nhiên
loi_chuc = [
    "🧧 Chúc bạn năm mới vạn sự như ý, tỷ sự như mơ!",
    "💰 Năm mới Bính Ngọ: Tiền vào như nước, lộc phát đầy nhà!",
    "🌸 Chúc gia đình bạn mạnh khỏe, bình an, hạnh phúc đong đầy.",
    "🚀 Công việc hanh thông, sự nghiệp thăng tiến, dữ liệu luôn 'clean'!",
    "🍀 Chúc bạn một năm mới rực rỡ, gặp nhiều may mắn và quý nhân phù trợ.",
    "🍊 Xuân sang hy vọng, ấm áp tình thân, vạn dặm bình an.",
    "✨ Chúc bạn năm mới 2026: Đa lộc, đa tài, đa phú quý!",
    "🏮 Tâm an lạc, thân kiện khang, mọi điều tốt lành sẽ đến với bạn."
]

# Cấu hình trang
st.set_page_config(page_title="Chúc Mừng Năm Mới 2026", page_icon="🧧")

# Hiệu ứng pháo hoa/bóng bay khi vừa vào trang
st.balloons()

# Giao diện chính
st.title("🧧 Chúc Mừng Năm Mới 2026")

st.markdown("---")

# Chọn ngẫu nhiên một lời chúc
wish = random.choice(loi_chuc)

# Hiển thị lời chúc nổi bật
st.subheader("Lời chúc dành riêng cho bạn:")
st.info(f"### {wish}")

st.markdown("---")
st.caption("Trang web được tạo bởi [Tên của bạn] - Chúc mừng Xuân Bính Ngọ!")

# Nút bấm để đổi lời chúc khác
if st.button('Nhận thêm một lời chúc khác 🧧'):
    st.rerun()
