import streamlit as st
import pandas as pd
import ev_data as ed
import altair as alt

st.title('전국 전기차 등록 현황')
st.header('')

data = pd.DataFrame({
    '지역명' : ['서울특별시', '부산광역시', '대구광역시', '인천광역시', '광주광역시', '대전광역시', '울산광역시', '세종특별자치시', '경기도', '충청북도', '충청남도', '전라남도', '경상북도', '경상남도', '제주특별자치도', '강원특별자치도', '전북특별자치도'],
    '전기차 등록 대수': [ed.seoul[2], ed.busan[2], ed.daegu[2], ed.incheon[2], ed.gwangju[2], ed.daejeon[2], ed.ulsan[2], ed.sejong[2], ed.gyeonggi[2], ed.chungbuk[2], ed.chungnam[2], ed.jeonnam[2], ed.gyeongbuk[2], ed.gyeongnam[2], ed.jeju[2], ed.gangwon[2], ed.jeonbuk[2]] 
})

data['전기차 등록 대수'] = data['전기차 등록 대수'].astype(float) # decimal 값에서 float으로 변경

data['비율(%)'] = data['전기차 등록 대수'] / data['전기차 등록 대수'].max() * 100 # 값 차이가 너무 크기 때문에 비율로 비교

chart = alt.Chart(data).mark_bar().encode(
    x='지역명',
    y=alt.Y('비율(%)', scale=alt.Scale(domain=[0, 100])),
    tooltip=['지역명', '전기차 등록 대수', '비율(%)']
)

st.altair_chart(chart, use_container_width=True) # 그래프 크기 자동 조정

options = ['서울특별시', '부산광역시', '대구광역시', '인천광역시', '광주광역시', '대전광역시', '울산광역시', '세종특별자치시', '경기도', '충청북도', '충청남도', '전라남도', '경상북도', '경상남도', '제주특별자치도', '강원특별자치도', '전북특별자치도']
select_city = st.multiselect('원하는 지역 선택', options)

filtered_data = data[data['지역명'].isin(select_city)]

if not filtered_data.empty:
    chart = alt.Chart(filtered_data).mark_bar(size=50).encode(
        x=alt.X('지역명', sort=None),  # 선택한 순서대로
        y='전기차 등록 대수'
    )
    st.altair_chart(chart, use_container_width=True)
else:
    st.write("그래프를 보려면 지역을 선택해주세요.")