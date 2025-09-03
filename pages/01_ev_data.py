import streamlit as st
import pandas as pd
import ev_data as ed
import altair as alt
import charger_data as cd

# 전기차 그래프
st.title('전국 전기차 등록 현황')
st.header('')

data = pd.DataFrame({
    '지역명' : ['서울특별시', '부산광역시', '대구광역시', '인천광역시', '광주광역시', '대전광역시', '울산광역시', '세종특별자치시', '경기도', '충청북도', '충청남도', '전라남도', '경상북도', '경상남도', '제주특별자치도', '강원특별자치도', '전북특별자치도'],
    '전기차 등록 대수': [ed.seoul[2], ed.busan[2], ed.daegu[2], ed.incheon[2], ed.gwangju[2], ed.daejeon[2], ed.ulsan[2], ed.sejong[2], ed.gyeonggi[2], ed.chungbuk[2], ed.chungnam[2], ed.jeonnam[2], ed.gyeongbuk[2], ed.gyeongnam[2], ed.jeju[2], ed.gangwon[2], ed.jeonbuk[2]] 
})

data['전기차 등록 대수'] = data['전기차 등록 대수'].astype(float) # decimal 값에서 float으로 변경

data['비율(%)'] = data['전기차 등록 대수'] / data['전기차 등록 대수'].max() * 100 # 값 차이가 너무 크기 때문에 비율로 비교

chart = alt.Chart(data).mark_bar(color='pink').encode(
    x='지역명',
    y=alt.Y('비율(%)', scale=alt.Scale(domain=[0, 100])),
    tooltip=['지역명', '전기차 등록 대수', '비율(%)']
)

st.altair_chart(chart, use_container_width=True) # 그래프 크기 자동 조정

# 충전소 그래프
st.title('전국 전기차 충전소 현황')
st.header('')

c_data = pd.DataFrame({ 
    '지역명' : ['서울특별시', '부산광역시', '대구광역시', '인천광역시', '광주광역시', '대전광역시', '울산광역시', '세종특별자치시', '경기도', '충청북도', '충청남도', '전라남도', '경상북도', '경상남도', '제주특별자치도', '강원특별자치도', '전북특별자치도'],
    '충전소 수' : [cd.c_seoul[1], cd.c_busan[1], cd.c_daegu[1], cd.c_incheon[1], cd.c_gwangju[1], cd.c_daejeon[1], cd.c_ulsan[1], cd.c_sejong[1], cd.c_gyeonggi[1], cd.c_chungbuk[1], cd.c_chungnam[1], cd.c_jeonnam[1], cd.c_gyeongbuk[1], cd.c_gyeongnam[1], cd.c_jeju[1], cd.c_gangwon[1], cd.c_jeonbuk[1]]
})

st.bar_chart(c_data.set_index('지역명')['충전소 수'])

# 전기차 + 충전소 그래프
# 두 데이터 병합
merged_data = pd.merge(data[['지역명', '전기차 등록 대수']], c_data[['지역명', '충전소 수']], on='지역명')

select_city = st.multiselect('원하는 지역 선택', merged_data['지역명'].tolist())

filtered_data = merged_data[merged_data['지역명'].isin(select_city)]

# 그래프
if not filtered_data.empty:
    long_df = filtered_data.melt(id_vars='지역명', 
                                 value_vars=['전기차 등록 대수', '충전소 수'],
                                 var_name='항목', 
                                 value_name='값')

    chart = alt.Chart(long_df).mark_bar(size=50).encode(
        x=alt.X('지역명:N', title='지역명'),
        y=alt.Y('값:Q', title='수'),
        color=alt.Color('항목:N',
                        scale=alt.Scale(
                            domain=['전기차 등록 대수', '충전소 수'],
                            range=['pink', 'skyblue']
                        )),
        tooltip=['지역명', '항목', '값']
    ).properties(width=600)

    st.altair_chart(chart, use_container_width=True)
else:
    st.write("그래프를 보려면 지역을 선택해주세요.")

# 꺾은선 그래프
st.title('전기차 등록 수 대비 충전소 비율')
st.header('')

merged_data['전기차당 충전소 수'] = merged_data['충전소 수'] / merged_data['전기차 등록 대수']

area_data = pd.DataFrame({
    '전기차당 충전소 수': merged_data['전기차당 충전소 수'].values
}, index=merged_data['지역명'])

st.area_chart(area_data)