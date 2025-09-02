import urllib.request
import requests
import os
from dotenv import load_dotenv
load_dotenv() # 경로상의 .env 파일을 찾고 자동으로 환경변수 등록

serviceKey = os.getenv("CAR_KEY")
# serviceKey = '1af4071e13d170429862cad56850a006a5f5b96a43fb05aa857ef7edb63e0287'

registYy = '2017'
registMt = '11'
vhctyAsortCode = '1'
registGrcCode = '1'
useFuelCode	= '2'
cnmCode = '000004'
prposSeNm = '1'
sexdstn = urllib.parse.quote('남자')
agrde = '3'
dsplvlCode = '2'
hmmdImpSeNm = urllib.parse.quote('국산')
prye = '2010'

# 요청 URL
# url = "https://openapi.naver.com/v1/search/news.json?query=" + encText
# url = "http://apis.data.go.kr/B553881/newRegistlnfoService_01"
url = "http://apis.data.go.kr/B553881/newRegistlnfoService_01/getNewRegistInfoService?serviceKey=" + serviceKey + "&registYy=" + registYy + "&registMt=" + registMt + "&vhctyAsortCode=" + vhctyAsortCode + "&registGrcCode=" + registGrcCode + "&useFuelCode=" + useFuelCode + "&cnmCode=" + cnmCode + "&prposSeNm=" + prposSeNm + "&sexdstn=" + sexdstn + "&agrde=" + agrde + "&dsplvlCode=" + dsplvlCode + "&hmmdImpSeNm=" + hmmdImpSeNm + "&prye=" + prye


# 요청 URL 등록 = 요청 객체
request = urllib.request.Request(url)
# 요청 헤더: 요청에 대한 기본적인 정보
# request.add_header("serviceKey", serviceKey)

# 실제 요청 보내기
# response = urllib.request.urlopen(request)
response = requests.get(url)
print(response) # getcode(): 응답 코드 반환

# response_body = response.read() # read(): 응답 내용 반환
# print(response_body.decode('utf-8'))