import mysql.connector
import streamlit as st
import pandas as pd
from numpy.random import default_rng as rng

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
daegu = ev_data[2]
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

print(seoul)

cursor.close()
connection.close()

print(seoul[2])