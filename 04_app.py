import streamlit as st
import pandas as pd
import plotly.express as px


# 기본 설정
st.set_page_config(page_title="전기차 충전기 분석", layout="wide")
st.title("🔌 전기차 충전기 분석 대시보드")
st.markdown("---")

# 데이터 읽어오기
df = pd.read_csv("charger_analysis.csv")

# 데이터 미리보기
with st.expander("🔍 데이터 미리보기"):
    st.dataframe(df)

# 카테고리 순서 정의
# 충전기 타입 순서: 급속 → 완속
type_order = ["급속 충전", "완속 충전"]

# 운영기관 순서: 공공 → 사설
org_order = ["공공", "사설"]

# 조합 순서: 공공-급속, 공공-완속, 사설-급속, 사설-완속
combo_order = [
    "공공 - 급속 충전",
    "공공 - 완속 충전",
    "사설 - 급속 충전",
    "사설 - 완속 충전"
]

# 색상 설정
type_colors = {
    '급속 충전': '#CC0000',
    '완속 충전': '#FF6666',
}
org_colors = {
    '공공': '#3399FF',
    '사설': '#003366',
}
combo_colors = {
    '공공 - 급속 충전': '#669900',
    '공공 - 완속 충전': '#99CC66',
    '사설 - 급속 충전': '#FF9900',
    '사설 - 완속 충전': '#FFCC66',
}

# 파이차트 1: 급속 vs 완속
df_type = (
    df.groupby("충전기타입")["개수"]
    .sum()
    .reindex(type_order)
    .reset_index()
)

fig1 = px.pie(
    df_type,
    names="충전기타입",
    values="개수",
    title="⚡ 급속 vs 완속",
    color="충전기타입",
    color_discrete_map=type_colors,
    category_orders={"충전기타입": type_order}
)

# 파이차트 2: 공공 vs 사설
df_org = (
    df.groupby("운영기관")["개수"]
    .sum()
    .reindex(org_order)
    .reset_index()
)

fig2 = px.pie(
    df_org,
    names="운영기관",
    values="개수",
    title="🏢 공공 vs 사설",
    color="운영기관",
    color_discrete_map=org_colors,
    category_orders={"운영기관": org_order}
)

# 파이차트 3: 조합 (공공/사설 + 급속/완속)
df["그룹"] = df["운영기관"] + " - " + df["충전기타입"]

df_combo = (
    df.groupby("그룹")["개수"]
    .sum()
    .reindex(combo_order)
    .reset_index()
)

fig3 = px.pie(
    df_combo,
    names="그룹",
    values="개수",
    title="🔗 공공/사설 + 급속/완속 조합",
    color="그룹",
    color_discrete_map=combo_colors,
    category_orders={"그룹": combo_order}
)

# 레이아웃 구성
col1, col2 = st.columns(2)

with col1:
    st.plotly_chart(fig1, use_container_width=True)

with col2:
    st.plotly_chart(fig2, use_container_width=True)

st.markdown("---")
st.plotly_chart(fig3, use_container_width=True)




