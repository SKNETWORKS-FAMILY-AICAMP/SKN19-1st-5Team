# 크롤링 시 필수요소
# - 요청 url
# - 파라미터
# - api 키

import urllib.request
import os
from dotenv import load_dotenv
load_dotenv() # 경로상의 .env 파일을 찾고 자동으로 환경변수 등록

NAVER_CLIENT_ID = os.getenv("NAVER_CLIENT_ID")
NAVER_CLIENT_SECRET = os.getenv("NAVER_CLIENT_SECRET")

# 인코딩하기 위해(한글, 특문 등) 위해 사용하는 함수
encText = urllib.parse.quote("인공지능")

# 요청 URL
# url = "https://openapi.naver.com/v1/search/news.json?query=" + encText
url = "https://openapi.naver.com/v1/search/news.xml?query=" + encText

# 요청 URL 등록 = 요청 객체
request = urllib.request.Request(url)
# 요청 헤더: 요청에 대한 기본적인 정보
request.add_header("X-Naver-Client-Id", NAVER_CLIENT_ID)
request.add_header("X-Naver-Client-Secret", NAVER_CLIENT_SECRET)

# 실제 요청 보내기
response = urllib.request.urlopen(request)
print(response.getcode()) # getcode(): 응답 코드 반환

response_body = response.read() # read(): 응답 내용 반환
print(response_body.decode('utf-8'))