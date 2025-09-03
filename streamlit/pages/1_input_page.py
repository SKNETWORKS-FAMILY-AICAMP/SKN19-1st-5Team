import streamlit as st
import pandas as pd
import glob

cwd = "../dataset/"

file_name = "charger_list.csv"
csv_path = cwd + file_name

# st.set_page_config(page_title="🪫찌릿 Chill IT🪫", page_icon="🔌")
st.page_link("main_page.py", label="🏠 홈으로 이동")

_, col1, _ = st.columns([0.1, 0.8, 0.1])

st.markdown("<h2 style='text-align: center; color: black;'>✍️원하는 지역을 선택하세요</h2>", unsafe_allow_html=True)
# st.header()
df = pd.read_csv(csv_path)

location = df['지역코드'].unique()
selected_location = st.multiselect("조회할 지역 선택", options=location, default=list(location))
if len(selected_location) < 5:
    st.warning("5개 이상을 선택해주세요!", icon='⚠️')

# st.session_state['filters'] = {
# }

st.success(f"필터 조건이 저장되었습니다. 데이터 페이지에서 확인하세요.")
st.page_link("pages/2_data_page.py", label="👉 데이터 페이지로 이동")