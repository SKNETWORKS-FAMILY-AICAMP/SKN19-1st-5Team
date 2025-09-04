import streamlit as st
import requests, os
from datetime import datetime
from dotenv import load_dotenv
load_dotenv()

st.set_page_config(page_title="찌릿 Chill IT", page_icon="🔌")

@st.cache_data(ttl=3600)
def get_naver_news(query: str, display: int = 3):
    client_id = os.getenv("NAVER_CLIENT_ID")
    client_secret = os.getenv("NAVER_CLIENT_SECRET")
    
    if client_id == "NAVER_CLIENT_ID":
        return get_demo_news()
    
    url = "https://openapi.naver.com/v1/search/news.json"
    headers = {
        "X-Naver-Client-Id": client_id,
        "X-Naver-Client-Secret": client_secret
    }
    
    params = {
        "query": query,
        "display": display,
        "sort": "sim"
    }
    
    try:
        response = requests.get(url, headers=headers, params=params)
        response.raise_for_status()
        
        data = response.json()
        news_items = []
        
        for item in data.get("items", []):
            news_items.append({
                "title": item["title"].replace("<b>", "").replace("</b>", ""),
                "description": item["description"].replace("<b>", "").replace("</b>", ""),
                "link": item["link"],
                "pub_date": item["pubDate"]
            })
        
        return news_items
        
    except Exception as e:
        st.error(f"뉴스를 불러오는 중 오류가 발생했습니다: {e}")
        return get_demo_news()

def get_demo_news():
    """데모 뉴스 데이터 (API 키가 없을 때 사용)"""
    return [
        {
            "title": "전기차 보급 확산으로 충전 인프라 확충 필요성 대두",
            "description": "국내 전기차 보급이 급속히 확산되면서 충전 인프라 확충이 시급한 과제로 떠오르고 있습니다.",
            "link": "https://example.com/news1",
            "pub_date": "Mon, 01 Jan 2024 00:00:00 +0900"
        },
        {
            "title": "정부, 전기차 충전소 설치 지원 정책 발표",
            "description": "정부가 전기차 충전소 설치를 위한 다양한 지원 정책을 발표하며 친환경 자동차 보급에 박차를 가하고 있습니다.",
            "link": "https://example.com/news2",
            "pub_date": "Mon, 01 Jan 2024 00:00:00 +0900"
        },
        {
            "title": "전기차 배터리 기술 발전으로 주행거리 대폭 향상",
            "description": "최신 전기차 배터리 기술의 발전으로 한 번 충전으로 더 먼 거리를 주행할 수 있게 되었습니다.",
            "link": "https://example.com/news3",
            "pub_date": "Mon, 01 Jan 2024 00:00:00 +0900"
        }
    ]

def format_pub_date(pub_date_str):
    try:
        dt = datetime.strptime(pub_date_str, "%a, %d %b %Y %H:%M:%S %z")
        return dt.strftime("%Y-%m-%d %H:%M")
    except:
        return pub_date_str

_, col1, _ = st.columns([0.1, 0.8, 0.1])
with col1:
    st.markdown("<h1 style='text-align: center; color: skyblue;'>🪫찌릿 Chill IT🪫</h1>", unsafe_allow_html=True)
    st.markdown("<h2 style='text-align: center; color: black;'>가장 가까운 충전소는 어디에</h2>", unsafe_allow_html=True)
    
    st.info("사이드바 또는 아래 버튼을 사용하여 페이지를 이동할 수 있어요.")
    
    _, mini_col, _ = st.columns(3)
    with mini_col:
        st.page_link("pages/01_ev_data.py", label="👉 분석 페이지로 이동")

st.markdown("---")
st.markdown("<h2 style='text-align: center; color: #2E8B57;'>📰 전기차 관련 최신 뉴스</h2>", unsafe_allow_html=True)

news_query = "전기차 OR 전기자동차"
news_items = get_naver_news(news_query, display=3)

if news_items:
    for i, news in enumerate(news_items, 1):
        with st.container():
            st.markdown(f"""
            <a href="{news['link']}" target="_blank" style="text-decoration: none; color: inherit;">
                <div style="
                    border: 1px solid #ddd;
                    border-radius: 8px;
                    padding: 10px;
                    margin: 5px 0;
                    background-color: #f9f9f9;
                    box-shadow: 0 1px 3px rgba(0,0,0,0.1);
                    width: 100%;
                    height: 120px;
                    transition: all 0.3s ease;
                    cursor: pointer;
                    overflow: hidden;
                " onmouseover="this.style.backgroundColor='#f0f0f0'; this.style.transform='translateY(-2px)'; this.style.boxShadow='0 3px 6px rgba(0,0,0,0.15)'" 
                   onmouseout="this.style.backgroundColor='#f9f9f9'; this.style.transform='translateY(0)'; this.style.boxShadow='0 1px 3px rgba(0,0,0,0.1)'">
                    <h4 style="color: #2E8B57; margin-top: 0; font-size: 14px; margin-bottom: 8px;">{news['title']}</h4>
                    <p style="color: #666; margin: 8px 0; font-size: 12px; line-height: 1.4; display: -webkit-box; -webkit-line-clamp: 4; -webkit-box-orient: vertical; overflow: hidden;">{news['description']}</p>
                    <small style="color: #888; font-size: 10px;">발행일: {format_pub_date(news['pub_date'])}</small>
                </div>
            </a>
            """, unsafe_allow_html=True)

else:
    st.info("뉴스를 불러올 수 없습니다. 잠시 후 다시 시도해주세요.")