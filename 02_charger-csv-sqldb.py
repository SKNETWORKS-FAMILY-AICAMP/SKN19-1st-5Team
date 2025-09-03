import pandas as pd
from sqlalchemy import create_engine

import pymysql

# CSV 파일 읽기
df = pd.read_csv(r"C:\SKN_19\00_project1\chargers.csv", encoding='utf-8')

# ✅ 컬럼명 변환 (한글 → 영문)
# 컬럼명 변경
df = df.rename(columns={
    "지역코드": "city_code",
    "기관명": "company",
    "충전소명": "charger_name",
    "충전기타입": "charger_type",
    "시설타입": "facility_type",
    "위도": "lat",
    "경도": "lng"
})

# lat, lng를 float으로 변환
df["lat"] = pd.to_numeric(df["lat"], errors="coerce")
df["lng"] = pd.to_numeric(df["lng"], errors="coerce")

# ✅ MySQL 연결 정보 (유저, 패스워드 수정해서 DB에 올리기)
user = "ohgiraffers"
password = "ohgiraffers"
host = "localhost"
port = 3306
database = "chargerdb"
table_name = "tbl_charger"

# SQLAlchemy 연결 엔진 생성
engine = create_engine(f"mysql+pymysql://{user}:{password}@{host}:{port}/{database}?charset=utf8mb4")

# ✅ 데이터 업로드 (기존 테이블에 추가: append)
df.to_sql(name=table_name, con=engine, if_exists="append", index=False)

print("✅ chargers.csv 데이터를 MySQL의 tbl_charger 테이블에 업로드 완료!")
