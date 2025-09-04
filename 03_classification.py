import pandas as pd
import pymysql

# DB 연결 설정
conn = pymysql.connect(
    host='localhost',
    user='root',
    password='1234',
    db='chargerdb',
    charset='utf8mb4'
)

# 쿼리
query = """
SELECT 
    기관_분류,
    충전속도_분류,
    COUNT(*) AS 개수,
    ROUND(COUNT(*) / (SELECT COUNT(*) FROM tbl_charger) * 100, 2) AS 비율_퍼센트
FROM (
    SELECT 
        *,
        CASE
            WHEN company LIKE '%부안군%' OR
                 company LIKE '%대구공공시설관리공단%' OR
                 company LIKE '%대구시%' OR
                 company LIKE '%대한송유관공사%' OR
                 company LIKE '%광주시%' OR
                 company LIKE '%강진군%' OR
                 company LIKE '%군포시%' OR
                 company LIKE '%인천국제공항공사%' OR
                 company LIKE '%익산시%' OR
                 company LIKE '%제주에너지공사%' OR
                 company LIKE '%제주도청%' OR
                 company LIKE '%전주시%' OR
                 company LIKE '%정읍시%' OR
                 company LIKE '%김해시%' OR
                 company LIKE '%순천시%' OR
                 company LIKE '%한국환경공단%' OR
                 company LIKE '%한국전력%' OR
                 company LIKE '%환경부%' OR
                 company LIKE '%나주시%' OR
                 company LIKE '%한국전자금융%' OR
                 company LIKE '%서울시%' OR
                 company LIKE '%세종시%' OR
                 company LIKE '%서울에너지공사%' OR
                 company LIKE '%순천시 체육시설관리소%' OR
                 company LIKE '%태백시%' OR
                 company LIKE '%울산시%' OR
                 company LIKE '%양양군%'
            THEN '공공'
            ELSE '사설'
        END AS 기관_분류,
        CASE
            WHEN charger_type LIKE '%2%' OR charger_type LIKE '%6%' THEN '완속 충전'
            ELSE '급속 충전'
        END AS 충전속도_분류
    FROM tbl_charger
) AS 분석대상
GROUP BY 기관_분류, 충전속도_분류
ORDER BY 기관_분류, 충전속도_분류;
"""

# 데이터 프레임으로 로드
df = pd.read_sql(query, conn)

# 저장
df.to_csv("charger_analysis.csv", index=False, encoding='utf-8-sig')

print("CSV 파일 저장 완료: charger_analysis.csv")

conn.close()
