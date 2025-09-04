# Streamlit 여러 페이지 열기(서버 추가)
# streamlit run [파일명] --server.port [포트]
import streamlit as st
st.set_page_config(page_title="TourGather", page_icon="🔌")

_, col1, _ = st.columns([0.1, 0.8, 0.1])
with col1:
    st.markdown("<h1 style='text-align: center; color: skyblue;'>🪫찌릿 Chill IT🪫</h1>", unsafe_allow_html=True)
    st.markdown("<h2 style='text-align: center; color: black;'>가장 가까운 충전소는 어디에</h2>", unsafe_allow_html=True)
    
    st.info("사이드바 또는 아래 버튼을 사용하여 페이지를 이동할 수 있어요.")
    
    _, mini_col, _ = st.columns(3)
    with mini_col:
        st.page_link("pages/01_ev_data.py", label="👉 분석 페이지로 이동")