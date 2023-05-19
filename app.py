import streamlit as st
import HandWritingPage.HandWriting as p4
import PhatHienKhuonMat.face_detect as p1
import NhanDangKhuonMat.predict as p2
import ThiGiacMay.thigiac as p3
import custom_css as ct
import os
import numpy as np

st.set_page_config(
    page_title="Xử lý ảnh số",
    page_icon=":smiley:",
    layout="wide",
    initial_sidebar_state="expanded",
)

def about_section():
    ct.display_header_section("Thông tin đồ án")
    return """
        <p class="text-color paragraph-text">Đồ án của nhóm bao gồm 4 bài nhỏ:</p>
        <ul class="about-list paragraph-text">
            <li>Phát hiện khuôn mặt</li>
            <li>Nhận diện khuôn mặt</li>
            <li>Xử lý ảnh</li>
            <li>Nhận diện chữ viết tay</li>
        </ul>
        """

def ourteam_section():
    ct.display_header_section("Thành viên nhóm")
    return f"""
        <div class="container">
            {card_profile("https://cdn.pixabay.com/photo/2022/02/20/13/57/avatar-7024608_1280.png", "Hứa Lộc Sơn", "20110712")}
            {card_profile("https://cdn.pixabay.com/photo/2022/02/20/14/01/avatar-7024621__480.png", "Lương Minh Chiến", "20110615")}
        </div>
    """

def card_profile(link_img, name, mssv, desc=None):
    return f"""
        <div class="card-profile">
            <div>
                <div class="cover-photo">
                    <img src="{link_img}" class="profile">
                </div>
                <div class="profile-name">{name}</div>
                <p class="about">MSSV: {mssv}</p>
            </div>
            <div class="social-button">
                <i class="fa-brands fa-facebook"></i>
                <i class="fa-brands fa-instagram"></i>
                <i class="fa-brands fa-youtube"></i>
            </div>
        </div>
    """

ct.add_css()

def Welcome():
    ct.display_header_page("Xử lý ảnh số")
    st.markdown(about_section(), unsafe_allow_html=True)
    st.markdown(ourteam_section(), unsafe_allow_html=True)

page_names_to_funcs = {
    "Welcome": Welcome,
    "Hand Writing": p4.run,
    "Phát hiện khuôn mặt": p1.phathien,
    "Nhận diện khuôn mặt": p2.nhandang,
    "Xử lý ảnh": p3.run
}

demo_name = st.sidebar.selectbox("", page_names_to_funcs.keys())
page_names_to_funcs[demo_name]()
