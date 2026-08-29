import streamlit as st

# ==============================
# CẤU HÌNH TRANG
# ==============================
st.set_page_config(
    page_title="CV Nguyễn Thị Thu Tuyền",
    page_icon="📄",
    layout="wide"
)

# ==============================
# CSS GIAO DIỆN
# ==============================
st.markdown("""
<style>

    .stApp {
        background-color: #f5f7fb;
    }

    .main {
        padding-top: 20px;
    }

    .header {
        background: linear-gradient(135deg, #123c69, #1f5f99);
        color: white;
        padding: 35px;
        border-radius: 15px;
        margin-bottom: 25px;
    }

    .name {
        font-size: 42px;
        font-weight: bold;
        margin-bottom: 5px;
    }

    .position {
        font-size: 20px;
        font-weight: 500;
    }

    .section-title {
        color: #123c69;
        font-size: 25px;
        font-weight: bold;
        border-bottom: 2px solid #123c69;
        padding-bottom: 7px;
        margin-top: 25px;
        margin-bottom: 15px;
    }

    .card {
        background-color: white;
        padding: 22px;
        border-radius: 12px;
        margin-bottom: 18px;
        box-shadow: 0px 3px 10px rgba(0,0,0,0.08);
    }

    .info-title {
        font-weight: bold;
        color: #123c69;
    }

</style>
""", unsafe_allow_html=True)


# ==============================
# HEADER
# ==============================
st.markdown("""
<div class="header">
    <div class="name">NGUYỄN THỊ THU TUYỀN</div>
    <div class="position">THỰC TẬP SINH NGÂN HÀNG TMCP QUÂN ĐỘI</div>
</div>
""", unsafe_allow_html=True)


# ==============================
# CHIA 2 CỘT
# ==============================
col1, col2 = st.columns([1, 2])


# ==============================
# CỘT TRÁI
# ==============================
with col1:

    # ==============================
    # ẢNH ĐẠI DIỆN
    # ==============================
    st.image(
        "photo.jpg",
        width=250
    )

    st.markdown("<br>", unsafe_allow_html=True)


    # ==============================
    # THÔNG TIN CÁ NHÂN
    # ==============================
    st.markdown(
        '<div class="section-title">Thông tin cá nhân</div>',
        unsafe_allow_html=True
    )

    st.markdown("""
    <div class="card">
        <p><span class="info-title">Ngày sinh:</span> 13/03/2004</p>
        <p><span class="info-title">Giới tính:</span> Nữ</p>
        <p><span class="info-title">Điện thoại:</span> 0346954274</p>
        <p><span class="info-title">Email:</span> thutuyen74t@gmail.com</p>
        <p><span class="info-title">Địa chỉ:</span> Phường Thạnh Xuân, Quận 12, TP.HCM</p>
    </div>
    """, unsafe_allow_html=True)


    # ==============================
    # SỞ THÍCH
    # ==============================
    st.markdown(
        '<div class="section-title">Sở thích</div>',
        unsafe_allow_html=True
    )

    st.markdown("""
    <div class="card">
        ✈️ Du lịch<br><br>
        🎵 Nghe nhạc<br><br>
        📚 Đọc sách
    </div>
    """, unsafe_allow_html=True)


    # ==============================
    # GIẢI THƯỞNG
    # ==============================
    st.markdown(
        '<div class="section-title">Giải thưởng</div>',
        unsafe_allow_html=True
    )

    st.markdown("""
    <div class="card">
        🏆 <b>2023</b><br>
        Sinh viên 5 tốt cấp trường
    </div>
    """, unsafe_allow_html=True)


# ==============================
# CỘT PHẢI
# ==============================
with col2:

    # ==============================
    # MỤC TIÊU NGHỀ NGHIỆP
    # ==============================
    st.markdown(
        '<div class="section-title">Mục tiêu nghề nghiệp</div>',
        unsafe_allow_html=True
    )

    st.markdown("""
    <div class="card">
        Tôi mong muốn trở thành một thực tập sinh ngân hàng TMCP QUÂN ĐỘI,
        nơi tôi có thể áp dụng kiến thức tài chính và ngân hàng đã học được
        trong suốt quá trình học tập, đồng thời phát triển kỹ năng chuyên môn
        trong môi trường làm việc thực tế.
        <br><br>
        Với sự ham học hỏi và khả năng làm việc nhóm, tôi hy vọng có thể
        đóng góp vào sự phát triển của ngân hàng, đồng thời học hỏi và
        trau dồi thêm kinh nghiệm để hướng tới việc phát triển sự nghiệp
        trong ngành ngân hàng.
        <br><br>
        Mục tiêu của tôi là hiểu rõ hơn về các quy trình nghiệp vụ ngân hàng,
        phát triển khả năng phân tích tài chính và nâng cao kỹ năng giao tiếp
        với khách hàng, từ đó trở thành một chuyên viên khách hàng trong lĩnh
        vực tài chính và ngân hàng trong tương lai.
    </div>
    """, unsafe_allow_html=True)


    # ==============================
    # HỌC VẤN
    # ==============================
    st.markdown(
        '<div class="section-title">Học vấn</div>',
        unsafe_allow_html=True
    )

    st.markdown("""
    <div class="card">
        <h4>TRƯỜNG ĐẠI HỌC NGUYỄN TẤT THÀNH</h4>
        <p><b>Thời gian:</b> 2022 - 2026</p>
        <p><b>Chuyên ngành:</b> Tài chính - Ngân hàng</p>
        <p><b>Trình độ:</b> Sinh viên năm 3</p>
    </div>
    """, unsafe_allow_html=True)


# ---------------------------------------------------------
# KỸ NĂNG
# ---------------------------------------------------------

with col1:

    st.markdown(
        '<div class="section-title">KỸ NĂNG</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        """
        <div class="skill-title">
            Kỹ năng giao tiếp
        </div>

        <div class="skill-content">
            Là một thực tập sinh, tôi có khả năng giao tiếp tốt, thích ứng với mỗi môi trường làm việc.
        </div>


        <div class="skill-title">
            Kỹ năng làm việc nhóm
        </div>

        <div class="skill-content">
            Là thực tập sinh ngân hàng, 
            tôi có khả năng làm việc nhóm tốt, biết cách phối hợp và hỗ trợ đồng nghiệp để hoàn thành các nhiệm vụ chung. 
            Tôi luôn lắng nghe, trao đổi ý kiến và đảm bảo hiệu quả công việc trong môi trường hợp tác.
        </div>


        <div class="skill-title">
            Kỹ năng quản lý thời gian
        </div>

        <div class="skill-content">
            Có kỹ năng quản lý và sắp xếp thời gian hợp lý, biết xác định và ưu tiên các công việc quan trọng. 
            Có khả năng lập kế hoạch, hoàn thành công việc đúng thời hạn và đảm bảo hiệu quả công việc.
        </div>


        <div class="skill-title">
            Kỹ năng tin học
        </div>

        <div class="skill-content">
            Tôi có kiến thức cơ bản về Tin học văn phòng, 
            có thể soạn thảo văn bản và sử dụng các phần mềm cơ bản trong tài chính. 
            Mặc dù còn mới mẻ trong việc sử dụng các công cụ này, 
            tôi luôn sẵn sàng học hỏi và cải thiện kỹ năng của mình để làm việc hiệu quả hơn.
        </div>
        """,
        unsafe_allow_html=True
    )




# ==============================
# FOOTER
# ==============================
st.markdown("---")

st.markdown(
    """
    <center>
        <p>© CV Nguyễn Thị Thu Tuyền | Streamlit Portfolio</p>
    </center>
    """,
    unsafe_allow_html=True
)
