# 동적 페이지 웹 크롤링 : Selenium
# 동적 페이지 : URL 요청 시, 응답받은 HTML 안의 JS를 실행하여 HTML을 새로 만드는 경우 (Client Side Rendering)

# Selenium
# - 인증을 요구하는 특정 웹 페이지의 데이터 스크랩
# - 무한 댓글 스크랩
# - 브라우저용 매크로
from selenium import webdriver                      # 브라우저 조작
from selenium.webdriver.common.keys import Keys     # 키보드 조작
from selenium.webdriver.common.by import By         # 웹 페이지 요소 조작
import time

# 1. Chrome 실행
path = 'chromedriver.exe'
service = webdriver.chrome.service.Service(path)
driver = webdriver.Chrome(service=service) # 실제 브라우저 실행 객체

# 2. 특정 url 접근
driver.get("https://naver.com")
time.sleep(1)

# 3. 검색 처리
# - 검색어 입력 및 검색
search_box = driver.find_element(By.ID, 'query')
search_box.send_keys('인공지능')
search_box.send_keys(Keys.RETURN) # RETURN : 엔터를 누른 것과 같음
time.sleep(1)

# - 뉴스 탭 이동(XPath로 복사해서 넣기)
news_btn = driver.find_element(By.XPATH, '//*[@id="lnb"]/div[1]/div/div[1]/div/div[1]/div[2]/a')
news_btn.click()
time.sleep(1)

# 4. 스크롤 처리
for _ in range(3):
    body = driver.find_element(By.TAG_NAME, "body") # 화면에 표시되는 내용이 body 태그 안에 있기 때문
    body.send_keys(Keys.END) # 스크롤을 끝까지
    time.sleep(1)

# 5. 특정 요소 접근
news_contents_elems = driver.find_elements(By.CSS_SELECTOR, 'span.sds-comps-text-type-headline1') # CSS 선택자 이용

for news_content_elem in news_contents_elems:
    parent = news_content_elem.find_element(By.XPATH, "..")

    title = news_content_elem.text
    href = parent.get_attribute('href')

    print(title, '|', href)

driver.quit()