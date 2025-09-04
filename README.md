# 1. 팀 소개
## 팀명: 🪫찌릿 Chill IT

## 팀원 소개 😄 
| **배상준** <br> <a href="https://github.com/windyale"><img src="https://img.shields.io/badge/GitHub-000?logo=github&logoColor=white"></a> | **이상혁** <br> <a href="https://github.com/sangpiri"><img src="https://img.shields.io/badge/GitHub-000?logo=github&logoColor=white"></a> | **장효정** <br> <a href="https://github.com/hyojungJ"><img src="https://img.shields.io/badge/GitHub-000?logo=github&logoColor=white"></a> | **왕혁준** <br> <a href="https://github.com/vibevibe26"><img src="https://img.shields.io/badge/GitHub-000?logo=github&logoColor=white"></a> |
|------------|------------|------------|------------|



---
# 2. 프로젝트 소개

## 📋프로젝트 명
- 지역별 전기차 등록 현황 및 충전소 현황

## ⭐프로젝트 필요성
- 전기차 소유자 및 구매 예정자에게 충전소 위치, 충전기 타입 등을 포함한 충전소 정보와 전기차 FAQ 정보, 최신 뉴스 등을  
  웹 페이지 내에서 한 눈에 볼 수 있도록 하여 정보 습득에 있어 편의성 제고

## 📜프로젝트 개요
- 지역별 전기자동차 등록 현황과 전기차 충전소 설치 현황 데이터를 제공
- 시중 전기자동차 관련 FAQ에서 자주 묻는 질문들을 종합.

## 🎯주요 목표
- 지역별 전기자동차 수 대비 충전소 수를 비교할 수 있는 자료를 제공
- 실제 지도 기반 시각화를 통해 충전소 설치 현황을 한눈에 확인
- 사용자가 충전소 위치를 쉽게 찾을 수 있도록 위치 정보와 충전소 관련 상세 정보를 제공

## 🗂️프로젝트 구조

```
SKN19-1st-5Team/
├── front/
|	└── main.py           
|	└── pages/   
│		├── 01_chart.py          # 지역별 전기차 등록 현황        
│		├── 02_analysis.py       # 지역별 전기차 등록 대수 대비 충전소 현황   
│		├── 03_map               # 실제 지도에 지역별 전기차 충전소 표시
│		└── 04_전기차 충전 FAQ
├── data/
|	└── charger_data.py        # 충전소 db 코드 추출              
|	└── ev_data.py             # 전기차 등록 db 코드 추출    	  
|	└── map_data.py            # 충전소 위도, 경도 정보 코드 추출
├── back/
|	└── chargerdb.sql          # 전체 db
|	└── evdata_chargerdb.sql   # 전기차 등록 현황 db  
|	└── data.csv               # 전기차 등록 현황 수집 데이터 csv
|	└── chargers_map.csv       # 지도 위도 경도 수집 데이터 csv
|	└── chargers.csv           # 충전소 현황 수집 데이터 csv
|	└── chargers_fixed.csv     # 충전소 위도 경도 데이터 수정
|	└── charger_analysis.csv   # 급속, 완속 충전 비교
├── .env                      
├── .gitignore       
├── requirements.txt        
└── README.md
```


---
# 3. 요구사항 명세서
<img width="755" height="544" alt="Image" src="https://github.com/user-attachments/assets/5a5f75d2-aa52-4708-aaa8-f67c5604295a" />


---
# 4. 데이터 및 기술

## 🔭기반 데이터
- **전국 전기 차량 등록대수**
  - 한국교통안전공단 공공데이터
- **지역별 전기 자동차 충전소 현황**
  - 한국환경공단 공공데이터
- **전기 자동차 관련 FAQ**
  - 기아, PSE EV, 혼다 e-모빌리티, 폴스타
 

## 🔨기술 스택
- **기반 언어** : Python 3.12
  - **웹 크롤링** : BeautifulSoup
  - **데이터 처리** : Pandas
  - **시각화** : Pydeck, Altair
- **웹 페이지 제작** : Streamlit
- **데이터베이스** : MySQL

---
# 5. ERD
<img width="799" height="422" alt="Image" src="https://github.com/user-attachments/assets/00753442-3676-4da0-bff9-7e462ab2a08b" />


---
# 6. 실행 결과

## 6-1)
![Image](https://github.com/user-attachments/assets/5b17d058-e1a9-459d-b118-6df2ced732c8)

![Image](https://github.com/user-attachments/assets/8166f59d-4706-42fe-865d-f6c26a0349d4)

main(Home)화면, 다른 페이지로 이동 가능. 전기차 관련 정보 제공을 위한 뉴스 삽입.

## 6-2)

![Image](https://github.com/user-attachments/assets/21aa2b28-a2d0-47f8-8f8d-52561db4f6e2)

전국 전기차 등록 지역별 현황 그래프. 지역들 간의 차이가 커 비율로 비교한 막대 그래프.

## 6-3)

![Image](https://github.com/user-attachments/assets/cad211e9-f996-4549-8396-43031e98d1e5)

전국 전기차 충전소 지역별 현황 그래프.

## 6-4)
![Image](https://github.com/user-attachments/assets/1a9d5e2d-84be-4884-89af-ef4c4e6f5dfb)

원하는 지역을 선택하여 그 지역의 전기차와 충전소 수를 비교할 수 있는 그래프.

## 6-5)

![Image](https://github.com/user-attachments/assets/00199d05-d03b-4f8a-9cbf-fa06781dc079)

전기차 등록 대비 충전소 비율을 나타낸 꺾은선 그래프.

## 6-6)

![Image](https://github.com/user-attachments/assets/6c6a46e9-72fb-4bdc-b15e-39f6aebbdc42)

전기차 충전기 타입, 제공 기관에 대한 비교 분석 표.

## 6-7)

![Image](https://github.com/user-attachments/assets/3741362e-15b4-480b-ae4e-64472bd408dd)

![Image](https://github.com/user-attachments/assets/362ef62b-17e0-4d43-89c9-04bef828e8f6)

충전기 타입, 제공 기관을 비교할 수 있도록 나타낸 그래프

## 6-8)

![Image](https://github.com/user-attachments/assets/11a187ed-cfd6-4235-8f32-a11c1cb1412a)

전국 충전소 위치 지도

## 6-9)

![Image](https://github.com/user-attachments/assets/d9068fe6-82fd-4e63-85eb-15657983dfca)

원하는 지역별 충전소 위치 지도

## 6-10)

![Image](https://github.com/user-attachments/assets/65acc852-34a8-4451-9b0c-47c9e7351c5e)

![Image](https://github.com/user-attachments/assets/8d73ec03-0818-465b-a1dc-b9a18402b1a5)

![Image](https://github.com/user-attachments/assets/be0e4abb-0942-466a-b08e-bd4969b66405)

전기차 & 전기차 충전소 관련 FAQ 정리


---
# 7. ✅ WBS
<img width="775" height="685" alt="Image" src="https://github.com/user-attachments/assets/1c067a30-e691-449f-ab45-5cf6854b2976" />


---
# 8. 회고

## 🔫트러블슈팅
- **API 호출 시 트래픽 차단 현상**
  - 최대한 적은 호출수로 많은 양을 추출하도록 코드 조정
- **ERD 설계 미스로 인한 데이터 관계 혼동**
  - 팀 모두가 상의하며 우리의 주제가 무엇이고 가진 데이터가 무엇인지 재확인하여 엔터티 확정
- **DB 데이터 정제 과정에서 오류사항 다수**
  - insert 대신 update 명령어를 사용해 정확성 향상
  - 중복 데이터 결합 시 like에 의존하기보다 코드 구조 자체를 바꾸는 것으로 방향 전환
- **크롤링 데이터 과다로 인한 시간 지연**
  - 크롤링 중 동시에 DB로 insert 되도록 하여 작업 실시간화
- **지도상 충전소 출력 시 엉뚱한 위치에 표시되는 현상**
  - 데이터 정제 과정상 오류로 판단, 위도&경도 데이터와 지역코드가 맞지않는 데이터를 조회하며 찾아 수정


## 💬프로젝트 회고
- **팀원1**
  - 부족한 실력과 짧은 프로젝트 기간에 버거운 점이 많았지만, 많이 도와주신 팀원분들께 감사하다.  오픈API를 통해 크롤링하는 것은 처음 해보는 작업이었는데, 방대한 양이었기 때문에 일단 cvs파일로 저장한 후, MySQL DB로 옮기는 작업을 수행하였다. 수업시간에 배운 쿼리문을 이용해 운영기관별로, 충전기타입별로 그룹화해서 조회해보는 작업도 해보았는데 오류없이 잘 구현되어 안도감이 들었다.  예복습을 더욱 잘해서, 다음 프로젝트  때는 맡은 역할을 더 잘 수행할 수 있도록 해야겠다.
- **팀원2**
  - csv파일의 데이터들을 mysql database에 넣고 그 데이터들에서 필요한 값을 추출, 수정, 취합하는 과정들과 web crawling, ERD 다이어그램을 만드는 것, 그 모든 과정을 거쳐 streamlit에 유용한 자료들을 사용자에게 보여주는 모든 과정들을 직접 수행해보고 이 과정에서 내가 부족한 부분들을 알아갈 수 있는 값진 경험이었습니다. 옆에서 많은 것들을 도와주신 팀원들에게 감사합니다.
- **팀원3**
  - 이번 프로젝트를 통해 그동안 학습했던 Python 내용과 DB 부분까지 모두 다시 상기할 수 있어 인상 깊었습니다. streamlit을 다루는 부분이나 github를 다루는 부분들은 캠프 초반에 학습했던 내용들이라 기억이 잘나지 않아 프로젝트 초반에 많이 애를 먹었지만 다시 복습을 할 수 있어 많은 도움이 되었던 시간이라고 생각합니다. 또한 강사님께서 주신 데이터를 활용하는 것이 아닌 직접 데이터를 구하고 DB를 구축해보니 MySQL과 Python에 대한 이해가 더 깊어질 수 있었습니다.
- **팀원4**
  - 생소했던 Streamlit의 고급 기능과 파이썬을 사용한 DB 조작을 좀 더 실전 감각에 가깝게 활용해볼 수 있었고, GitHub를 통해 협업에 있어 체계적인 파트분담의 중요성을 절실히 느낄 수 있었습니다. 또 필요한 데이터를 직접 찾고 정제하는 과정이 생각보다 시간을 많이 쓰는 작업이었고, 프로젝트에서 데이터 확보가 얼마나 중요한지를 크게 배웠습니다. 배운 내용을 망라해 다양한 지식을 사용하려다보니 조금 과부하가 되기도 했지만 현재 저의 레벨을 객관적으로 재확인할 수 있었습니다. 
