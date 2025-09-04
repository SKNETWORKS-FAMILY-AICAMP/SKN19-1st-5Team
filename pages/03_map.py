import pandas as pd
import streamlit as st
from numpy.random import default_rng as rng
import mysql.connector

connection = mysql.connector.connect(
    host='localhost', 
    user='ohgiraffers',
    password='ohgiraffers',
    database='chargerdb' 
)

cursor = connection.cursor()

cursor.execute('select city_code, lat, lng from tbl_mapf')

map_data = cursor.fetchall()

print(map_data)

df = pd.DataFrame(map_data, columns=["지역코드", "lat", "lon"])


city_name = {
    11: "서울특별시",
    26: "부산광역시",
    27: "대구광역시",
    28: "인천광역시",
    29: "광주광역시",
    30: "대전광역시",
    31: "울산광역시",
    36: "세종특별자치시",
    41: "경기도",
    43: "충청북도",
    44: "충청남도",
    46: "전라남도",
    47: "경상북도",
    48: "경상남도",
    50: "제주특별자치도",
    51: "강원특별자치도",
    52: "전북특별자치도"
}

df['지역명'] = df['지역코드'].map(city_name)

st.header('🗺️ 전국 전기차 충전소 지도')

st.map(df[['lat', 'lon']])

st.subheader('')

st.header('🏠 지역별 충전소 위치 확인')

selected_city = st.selectbox("지역을 선택하세요:", df['지역명'].unique())

filtered_df = df[df['지역명'] == selected_city]

st.map(filtered_df[['lat', 'lon']])