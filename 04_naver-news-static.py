import requests
from bs4 import BeautifulSoup
from datetime import datetime
from urllib.request import urlretrieve

# newsentry class 생성
class NewsEntry:
    def __init__(self, title, href, img_path):
        self.title = title
        self.href = href
        self.img_path = img_path
    
    def __repr__(self):
        return f"NewsEntry<title={self.title}, href={self.href}, img_path={self.img_path}>"

# 1. request -> url 요청
keyword = input('뉴스 검색어 입력: ')
url = f"https://search.naver.com/search.naver?ssc=tab.news.all&where=news&sm=tab_jum&query={keyword}"

response = requests.get(url)

# 2. html 응답
html = response.text

# 3. BeautifulSoup 객체 생성
bs = BeautifulSoup(html, 'html.parser')

# 4. news_contents
news_contents = bs.select('.fds-news-item-list-tab > div')

news_list = []

for idx, news_content in enumerate(news_contents):
    # 제목, 링크, 이미지 뽑아내기
    title_tag = news_content.select_one('span.sds-comps-text-type-headline1')
    href_tag = title_tag.find_parent('a')
    img_tag = news_content.find_all('img')[1]

    title = title_tag.text
    href = href_tag['href'] # 여러 속성 중 href의 값을 가져옴
    img_path = ''

    # 이미지 경로와 파일명 지정
    if img_tag.has_attr('src'):
        img_path = img_tag['src']

        img_dir = 'images'
        file_name = datetime.now().strftime('%y%m%d_%H%M%S_') + str(idx+1) + '.jpg'
        urlretrieve(img_path, f'{img_dir}/{file_name}')

    # 뉴스 하나 하나의 객체를 리스트에 넣어주기
    news_entry = NewsEntry(title, href, img_path)
    news_list.append(news_entry)

for news in news_list:
    print(news)