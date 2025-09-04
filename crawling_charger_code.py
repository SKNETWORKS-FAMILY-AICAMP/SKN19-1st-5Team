import urllib.request
import xml.etree.ElementTree as ET
import pandas as pd
import time

# 인증키 및 설정
ServiceKey = "c10ac54b9ffb432249ec5b420615ec25bcc67f857873855f0ab0dd58201b2782"
numOfRows = 500
page = 1
all_items = []

while True:
    print(f'🔄 {page} 페이지 요청 중...')

    url = f"http://apis.data.go.kr/B552584/EvCharger/getChargerInfo?ServiceKey={ServiceKey}&pageNo={page}&numOfRows={numOfRows}"

    response = urllib.request.urlopen(url)
    response_body = response.read()
    root = ET.fromstring(response_body)

    # 첫 페이지에서 전체 페이지 수 계산
    if page == 1:
        totalCount = int(root.findtext(".//totalCount"))
        totalPages = (totalCount // numOfRows) + (1 if totalCount % numOfRows != 0 else 0)
        print(f"✅ 총 충전기 수: {totalCount}, 총 페이지 수: {totalPages}")

    items = root.findall(".//item")

    for item in items:
        data = {
            "지역코드": item.findtext("zcode"),
            "기관명": item.findtext("busiNm"),
            "충전소명": item.findtext("statNm"),
            "충전기타입": item.findtext("chgerType"),
            "시설타입": item.findtext("kind"),
            "위도": item.findtext("lat"),
            "경도": item.findtext("lng")
        }
        all_items.append(data)

    # 반복 종료 조건
    if page >= totalPages:
        print("🏁 마지막 페이지까지 수집 완료.")
        break

    page += 1
    time.sleep(1)

# DataFrame 변환
df = pd.DataFrame(all_items)
print(f"\n📊 최종 수집된 충전기 수 (원본): {len(df)}")

# 중복 제거
df = df.drop_duplicates(subset=["충전소명", "기관명", "위도", "경도", "충전기타입"])
print(f"✅ 중복 제거 후 충전기 수: {len(df)}")

# 저장
df.to_csv("chargers.csv", index=False, encoding="utf-8-sig")
print("💾 chargers.csv 저장 완료!")

