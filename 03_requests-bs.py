# pip install requests beautifulsoup4 selenium
# 정적 페이지 스크래핑 : requests, beautifulsoup
# 정적 페이지 : 요청한 url에서 응답받은 html을 그대로 사용 (SSR : Server Side Rendering)

import requests
from bs4 import BeautifulSoup

def web_request(url):
    response = requests.get(url)
    print(response)             # Reponse [200]
    print(response.status_code) # 응답코드
    print(response.text[0])     # html
    return response

url = "https://naver.com"
response = web_request(url)

with open('C:\\SKN_19\\03_web_crawling\\html_sample.html', 'r', encoding='utf-8') as f:
    html = f.read()

# BeautifulSoup = html, xml을 파싱해서 데이터 추출
bs = BeautifulSoup(html, 'html.parser')

# find, find_all = HTML의 태그/속성을 딕셔너리로 읽어옴
def test_find():
    # find : 맨 처음 나오는 1개만
    tag = bs.find('li')
    print('>>> find:', tag)
    print(type(tag))

    # find_all : 전부
    # tags = bs.find_all('section')
    tags = bs.find_all('section', {'id': 'section1'})
    print('>>> find_all:', tags)
    print(type(tags))

# CSS 선택자로 특정 태그 찾기
def test_selector():
    tag = bs.select_one('section#section2') # section 태그 중 id(#)가 section2인 것
    print('>>> select_one:', tag)
    print(type(tag))

    tags = bs.select('.section-content')
    print('>>> select:', tags)
    print(type(tags))

# find : 태그의 이름으로 조회
# select : CSS 선택자로 특정 태그 조회
# 더 복합적으로 찾으려면 select가 유용

# id가 section2인 section 태그의 자손 li 태그들 추출
def get_content():
    tags = bs.select('section#section2 li')
    for tag in tags:
        print(tag.text)

# id가 section1인 section 태그의 자손 h2, p의 내용 추출
def get_content2():
    h2_tag = bs.select_one('section#section1 > h2')
    print('h2_tag', h2_tag.text)
    
    p_tags = bs.select('section#section1 > p')
    for p_tag in p_tags:
        print('p_tag', p_tag.text)

# id가 section1인 section 태그의 자손 h2, p의 내용과 모든 자식
def get_content3():
    sc1_tag = bs.select_one('section#section1')
    
    h2_tag = sc1_tag.select_one('h2')
    print(h2_tag.text)

    p_tags = sc1_tag.select('p')
    print([p_tag for p_tag in p_tags])

    children = sc1_tag.findChildren()
    print(children)

get_content3()