import streamlit as st
import pandas as pd
import numpy as np
import pydeck as pdk
from datetime import datetime, timedelta
from io import StringIO

st.set_page_config(
    page_title="전국 전기차 대비 충전소 보급 현황",
    page_icon="🔌",
    layout="wide",
)

# ------------------------------------------------------------
# Demo data generator (used when no file uploaded)
# ------------------------------------------------------------
@st.cache_data(show_spinner=False)
def generate_demo_data(seed: int = 42) -> pd.DataFrame:
    rng = np.random.default_rng(seed)

    regions = [
        "서울", "부산", "대구", "인천", "광주", "대전", "울산",
        "세종", "경기", "강원", "충북", "충남", "전북", "전남", "경북", "경남", "제주",
    ]

    start_date = datetime.today().replace(day=1) - timedelta(days=365)
    months = pd.date_range(start=start_date, periods=13, freq="MS")

    rows = []
    for month in months:
        base_ev = rng.integers(150000, 220000)
        for region in regions:
            stations = int(rng.normal(400, 120))
            stations = max(stations, 30)
            chargers = stations * rng.integers(2, 6)
            ev_registered = int(base_ev * (0.7 + rng.random() * 0.6))
            lat = 33.0 + rng.random() * 5 + (0.02 if region == "제주" else 0)
            lon = 126.0 + rng.random() * 9

            rows.append(
                {
                    "date": month.date(),
                    "region": region,
                    "stations": stations,
                    "chargers": chargers,
                    "ev_registered": ev_registered,
                    "lat": lat,
                    "lon": lon,
                }
            )

    df = pd.DataFrame(rows)
    return df

# ------------------------------------------------------------
# Data loading
# ------------------------------------------------------------
@st.cache_data(show_spinner=False)
def load_data(uploaded: bytes | None) -> pd.DataFrame:
    if uploaded is None:
        return generate_demo_data()

    try:
        text = uploaded.decode("utf-8")
    except Exception:
        text = uploaded.decode("cp949", errors="ignore")

    df = pd.read_csv(StringIO(text))

    # Required columns (case-insensitive mapping)
    required = {
        "date": ["date", "날짜", "월", "month"],
        "region": ["region", "행정구역", "시도", "광역시도"],
        "stations": ["stations", "충전소수", "충전소"],
        "chargers": ["chargers", "충전기수", "충전기"],
        "ev_registered": ["ev_registered", "전기차등록대수", "ev", "등록대수"],
        "lat": ["lat", "위도", "latitude"],
        "lon": ["lon", "경도", "longitude"],
    }

    def find_col(candidates: list[str]) -> str | None:
        lower_cols = {c.lower(): c for c in df.columns}
        for name in candidates:
            if name.lower() in lower_cols:
                return lower_cols[name.lower()]
        return None

    mapping: dict[str, str] = {}
    for k, cands in required.items():
        col = find_col(cands)
        if col is not None:
            mapping[k] = col

    # minimal required
    minimal_fields = {"date", "region", "stations", "chargers", "ev_registered"}
    if not minimal_fields.issubset(mapping.keys()):
        st.warning("필수 컬럼이 누락되어 데모 데이터를 사용합니다. 필요 컬럼: date, region, stations, chargers, ev_registered")
        return generate_demo_data()

    df = df.rename(columns={v: k for k, v in mapping.items()})

    # Coerce dtypes
    df["date"] = pd.to_datetime(df["date"]).dt.date
    for col in ["stations", "chargers", "ev_registered"]:
        df[col] = pd.to_numeric(df[col], errors="coerce").fillna(0).astype(int)

    # lat/lon optional; if missing, infer rough centroids per region using demo means
    if "lat" not in df.columns or "lon" not in df.columns:
        demo = generate_demo_data()
        centroids = demo.groupby("region")[['lat', 'lon']].mean().reset_index()
        df = df.merge(centroids, on="region", how="left")

    return df

# ------------------------------------------------------------
# Sidebar: data source and filters
# ------------------------------------------------------------
with st.sidebar:
    st.header("데이터 설정")
    uploaded_file = st.file_uploader("CSV 업로드 (선택)", type=["csv"])  # Optional

    df = load_data(uploaded_file.read() if uploaded_file else None)

    st.markdown("---")
    st.header("필터")

    # Date range
    min_date, max_date = df["date"].min(), df["date"].max()
    default_start = max_date.replace(day=1) - timedelta(days=180)
    start_date, end_date = st.date_input(
        "기간",
        value=(default_start, max_date),
        min_value=min_date,
        max_value=max_date,
        format="YYYY-MM-DD",
    )

    # Region multi-select
    regions = sorted(df["region"].unique().tolist())
    selected_regions = st.multiselect("지역", regions, default=regions)

# Apply filters
mask = (
    (df["date"] >= start_date) & (df["date"] <= end_date) & (df["region"].isin(selected_regions))
)
filtered = df.loc[mask].copy()

# ------------------------------------------------------------
# Title and description
# ------------------------------------------------------------
st.title("전국 전기 자동차 등록대수 대비 지역별 충전소 보급 현황")
st.caption("CSV 업로드로 실제 데이터를 분석하거나, 기본 데모 데이터로 탐색할 수 있습니다.")

# ------------------------------------------------------------
# KPIs
# ------------------------------------------------------------
latest_date = filtered["date"].max()
latest = filtered[filtered["date"] == latest_date]

kpi_cols = st.columns(4)
with kpi_cols[0]:
    st.metric("선택 기간 전기차 등록대수", f"{filtered['ev_registered'].sum():,}")
with kpi_cols[1]:
    st.metric("선택 기간 충전소 수", f"{filtered['stations'].sum():,}")
with kpi_cols[2]:
    st.metric("선택 기간 충전기 수", f"{filtered['chargers'].sum():,}")
with kpi_cols[3]:
    ratio = (filtered["ev_registered"].sum() / max(filtered["chargers"].sum(), 1))
    st.metric("전기차/충전기 비율", f"{ratio:,.1f}")

st.markdown("---")

# ------------------------------------------------------------
# Charts
# ------------------------------------------------------------
left, right = st.columns((1.2, 1))

with left:
    st.subheader("지역별 보급 현황 (최근월)")
    if not latest.empty:
        by_region = (
            latest.groupby("region")[["stations", "chargers", "ev_registered"]]
            .sum()
            .sort_values("ev_registered", ascending=False)
            .reset_index()
        )
        st.bar_chart(
            by_region.set_index("region")[["ev_registered", "stations", "chargers"]],
            height=360,
        )
    else:
        st.info("선택된 기간의 데이터가 없습니다.")

with right:
    st.subheader("전국 추이")
    by_month = (
        filtered.groupby("date")[["ev_registered", "stations", "chargers"]]
        .sum()
        .sort_index()
        .reset_index()
    )
    st.line_chart(by_month.set_index("date"), height=360)

st.markdown("---")

# ------------------------------------------------------------
# Map
# ------------------------------------------------------------
st.subheader("충전 인프라 지도")
# For map, use latest month per region to avoid duplicates
latest_per_region = (
    filtered.sort_values("date").groupby("region").tail(1)
)

if latest_per_region.empty:
    st.info("지도를 표시할 데이터가 없습니다.")
else:
    midpoint = [latest_per_region["lat"].mean(), latest_per_region["lon"].mean()]

    layer = pdk.Layer(
        "ScatterplotLayer",
        data=latest_per_region,
        get_position="[lon, lat]",
        get_radius="chargers",
        radius_scale=10,
        radius_min_pixels=3,
        radius_max_pixels=60,
        get_fill_color="[min(255, chargers*2), 120, 180]",
        pickable=True,
        auto_highlight=True,
    )

    tooltip = {
        "html": "<b>{region}</b><br/>충전소: {stations:,}<br/>충전기: {chargers:,}<br/>전기차: {ev_registered:,}",
        "style": {"backgroundColor": "#1e1e1e", "color": "white"},
    }

    view_state = pdk.ViewState(latitude=midpoint[0], longitude=midpoint[1], zoom=5.7)

    st.pydeck_chart(
        pdk.Deck(
            layers=[layer],
            initial_view_state=view_state,
            tooltip=tooltip,
            map_style="mapbox://styles/mapbox/light-v11",
        ),
        use_container_width=True,
    )

# ------------------------------------------------------------
# Raw data expander
# ------------------------------------------------------------
with st.expander("원본 데이터 보기"):
    st.dataframe(filtered.sort_values(["date", "region"]).reset_index(drop=True), use_container_width=True)
