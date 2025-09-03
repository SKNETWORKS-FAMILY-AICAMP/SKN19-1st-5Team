import requests
import warnings
import os
import pandas as pd
# import charger_inputdb as chgdb
import mysql.connector
from bs4 import BeautifulSoup
from bs4 import MarkupResemblesLocatorWarning
from dotenv import load_dotenv
load_dotenv()

warnings.filterwarnings("ignore", category=MarkupResemblesLocatorWarning)

# API Key
ServiceKey = os.getenv("EV_KEY")

class CreateURL:
    def __init__(self, base, pageNo, numOfRows, zcode):
        self.base = base
        self.pageNo = pageNo
        self.numOfRows = numOfRows
        self.zcode = zcode

def init_connection():
    connection = mysql.connector.connect(
        host = "localhost",
        user = "root",
        password = "0912",
        database = "chargerdb"
    )

    return connection

def insert_db(charger):
    sql = "insert into tbl_charger(city_code, company, charger_name, charger_type, facility_type, lat, lng) values (%s, %s, %s, %s, %s, %s, %s)"

    values = (charger['city_code'], charger['company'], charger['charger_name'], charger['charger_type'], charger['facility_type'], charger['lat'], charger['lng'])
    
    cursor.execute(sql, values)  
    print('Successfully inserted')

def web_request(url):
    response = requests.get(url).text
    return response

def charger_crawler():
    item_list = bs.find_all('item')

    for item in item_list:
        zcode = item.find('zcode').text
        busiNm = item.find('busiNm').text
        statNm = item.find('statNm').text
        chgType = item.find('chgerType').text
        kind = item.find('kind').text
        # kindDetail = bs.find('kindDetail').text
        lat = item.find('lat').text
        lng = item.find('lng').text
    
        if statNm not in distinct_chk:
            distinct_chk.append(statNm)
            charger_dict = {
                'city_code': int(zcode),
                'company': busiNm,
                'charger_name': statNm,
                'charger_type': chgType,
                'facility_type': kind,
                'lat': float(lat),
                'lng': float(lng)
            }
            print(charger_dict)
            insert_db(charger_dict)

            # charger_list.append(charger_dict)

    return charger_list

url = CreateURL(
    base="http://apis.data.go.kr/B552584/EvCharger/getChargerInfo",
    pageNo=1,
    numOfRows=1,
    zcode=11
)

connection = init_connection()
cursor = connection.cursor()

charger_list = []
distinct_chk = []

while 1:
    target_url = f"{url.base}?ServiceKey={ServiceKey}&pageNo={url.pageNo}&numOfRows={url.numOfRows}&zcode={url.zcode}"
    response = web_request(target_url)
    print(f"=={url.pageNo} 페이지==")

    bs = BeautifulSoup(response, 'xml')
    if bs.find('numOfRows').text == '0':
        print("데이터가 없습니다.")
        break

    charger_crawler()
    url.pageNo += 1

connection.commit()

cursor.close()
connection.close()
# print(charger_list)