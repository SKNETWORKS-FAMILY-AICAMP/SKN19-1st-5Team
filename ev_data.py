import mysql.connector
import streamlit as st

connection = mysql.connector.connect(
    host='localhost', 
    user='ohgiraffers',
    password='ohgiraffers',
    database='cardb' 
)

cursor = connection.cursor()

cursor.execute('select * from ev_data')

ev_data = cursor.fetchall()

seoul = ev_data[0]
busan = ev_data[1]
deagu = ev_data[2]
incheon = ev_data[3]
gwangju = ev_data[4]
daejeon = ev_data[5]
ulsan= ev_data[6]
sejong = ev_data[7]
gyeonggi = ev_data[8]
chungbuk = ev_data[9]
chungnam = ev_data[10]
jeonnam = ev_data[11]
gyeongbuk = ev_data[12]
gyeongnam = ev_data[13]
jeju = ev_data[14]
gangwon = ev_data[15]
jeonbuk = ev_data[16]

cursor.close()
connection.close()

st.title('전국 지역별 전기차 등록 현황')
