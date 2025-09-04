# 🪫찌릿 Chill IT
전기 자동차 충전소 정보 조회 시스템


| **배상준** | **이상혁** | **장효정** | **왕혁준** |
|------------|------------|------------|------------|
| <a href="https://github.com/windy"><img src="https://img.shields.io/badge/GitHub-000?logo=github&logoColor=white"></a> <br> <a href="mailto:email1@example.com"><img src="https://img.shields.io/badge/Email-D14836?logo=gmail&logoColor=white"></a> | 
<a href="https://github.com/sangpiri"><img src="https://img.shields.io/badge/GitHub-000?logo=github&logoColor=white"></a> <br> <a href="mailto:email2@example.com"><img src="https://img.shields.io/badge/Email-D14836?logo=gmail&logoColor=white"></a> |
<a href="https://github.com/hyojungJ"><img src="https://img.shields.io/badge/GitHub-000?logo=github&logoColor=white"></a> <br> <a href="mailto:email3@example.com"><img src="https://img.shields.io/badge/Email-D14836?logo=gmail&logoColor=white"></a> |
<a href="https://github.com/vibevibe26"><img src="https://img.shields.io/badge/GitHub-000?logo=github&logoColor=white"></a> <br> <a href="mailto:email4@example.com"><img src="https://img.shields.io/badge/Email-D14836?logo=gmail&logoColor=white"></a> |


## 📜프로젝트 개요
- 지역별 전기자동차 등록 현황과 전기차 충전소 설치 현황 데이터를 제공
- 시중 전기자동차 관련 FAQ에서 자주 묻는 질문들을 종합.

### 주요 목표
- 지역별 전기자동차 수 대비 충전소 수를 비교할 수 있는 자료를 제공
- 실제 지도 기반 시각화를 통해 충전소 설치 현황을 한눈에 확인
- 사용자가 충전소 위치를 쉽게 찾을 수 있도록 위치 정보와 충전소 관련 상세 정보를 제공

## 🔭기반 데이터
- **전국 전기 차량 등록대수**
  - 한국교통안전공단 공공데이터
- **지역별 전기 자동차 충전소 현황**
  - 한국환경공단 공공데이터
- **전기 자동차 관련 FAQ**
  - 기아, PSE EV, 혼다 e-모빌리티, 폴스타
 
## 👜ERD
![initial](https://github.com/user-attachments/assets/de0877ac-404b-47bd-a526-510310d02f46)

## 🔨기술 스택
- **기반 언어** : Python 3.12
  - **웹 크롤링** : BeautifulSoup
  - **데이터 처리** : Pandas
  - **시각화** : Pydeck, Altair
- **웹 페이지 제작** : Streamlit
- **데이터베이스** : MySQL

## ✅ WBS
<img width="748" height="712" alt="Image" src="https://github.com/user-attachments/assets/46235984-e31e-445d-9a76-76533d001a95" />

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
  - 비전공자로서, 실력이 부족한데다가, 프로젝트 기간이 짧아서, 버거운 점이 많았다. 많이 도와주신 팀원들께 감사하다.
수업 진도가 빠르게 느껴지지만 예복습을 잘해서, 다음 프로젝트 때는 맡은 역할을 더 잘 수행할 수 있도록 해야겠다.
- **팀원2**
  - csv파일의 데이터들을 mysql database에 넣고 그 데이터들에서 필요한 값을 추출, 수정, 취합하는 과정들과 web crawling, ERD 다이어그램을 만드는 것, 그 모든 과정을 거쳐 streamlit에 유용한 자료들을 사용자에게 보여주는 모든 과정들을 직접 수행해보고 이 과정에서 내가 부족한 부분들을 알아갈 수 있는 값진 경험이었습니다. 옆에서 많은 것들을 도와주신 팀원들에게 감사합니다.
- **팀원3**
  - 이번 프로젝트를 통해 그동안 학습했던 Python 내용과 DB 부분까지 모두 다시 상기할 수 있어 인상 깊었습니다. streamlit을 다루는 부분이나 github를 다루는 부분들은 캠프 초반에 학습했던 내용들이라 기억이 잘나지 않아 프로젝트 초반에 많이 애를 먹었지만 다시 복습을 할 수 있어 많은 도움이 되었던 시간이라고 생각합니다. 또한 강사님께서 주신 데이터를 활용하는 것이 아닌 직접 데이터를 구하고 DB를 구축해보니 MySQL과 Python에 대한 이해가 더 깊어질 수 있었습니다.
- **팀원4**
  - 생소했던 Streamlit의 고급 기능과 파이썬을 사용한 DB 조작을 좀 더 실전 감각에 가깝게 활용해볼 수 있었고, GitHub를 통해 협업에 있어 체계적인 파트분담의 중요성을 절실히 느낄 수 있었습니다. 또 필요한 데이터를 직접 찾고 정제하는 과정이 생각보다 시간을 많이 쓰는 작업이었고, 프로젝트에서 데이터 확보가 얼마나 중요한지를 크게 배웠습니다. 배운 내용을 망라해 다양한 지식을 사용하려다보니 조금 과부하가 되기도 했지만 현재 저의 레벨을 객관적으로 재확인할 수 있었습니다. 
