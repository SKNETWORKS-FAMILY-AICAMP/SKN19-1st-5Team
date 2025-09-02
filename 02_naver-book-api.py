# import 구문
import mysql.connector
import urllib.request
import os
import json

# API 키 설정
from dotenv import load_dotenv
load_dotenv()

NAVER_CLIENT_ID = os.getenv("NAVER_CLIENT_ID")
NAVER_CLIENT_SECRET = os.getenv("NAVER_CLIENT_SECRET")

# 검색어 설정
searchText = urllib.parse.quote("소설")

# url 및 헤더 설정
url = "https://openapi.naver.com/v1/search/book.json?query=" + searchText

request = urllib.request.Request(url)
request.add_header("X-Naver-Client-Id", NAVER_CLIENT_ID)
request.add_header("X-Naver-Client-Secret", NAVER_CLIENT_SECRET)

# api 요청 및 결과값 json 반환
response = urllib.request.urlopen(request)
response_body = response.read()

# json <-> 파이썬 딕셔너리 변환
#   import json
#   json.loads(json)
json_to_dict = json.loads(response_body)

# DB 연결 객체 생성
connection = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "0912",
    database = "bookdb"
)

# SQL 수행을 위한 커서 생성
cursor = connection.cursor()

# API를 통해 받아온 정보를 가지고 insert 수행
sql = "insert into naver_book(book_title, book_image, author, publisher, isbn, book_description, pub_date) values (%s, %s, %s, %s, %s, %s, %s)"

for book in json_to_dict['items']:
    values = (book['title'], book['image'], book['author'], book['publisher'], str(book['isbn']), book['description'], book['pubdate'])

    cursor.execute(sql, values)

# 데이터베이스 트랜잭션 처리 (commit -> 반영)
connection.commit()

# 커서 및 연결 객체 종료
cursor.close()
connection.close()