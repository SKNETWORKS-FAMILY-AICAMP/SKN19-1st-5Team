import mysql.connector
import streamlit as st
import pandas as pd
from numpy.random import default_rng as rng

connection = mysql.connector.connect(
    host='localhost', 
    user='ohgiraffers',
    password='ohgiraffers',
    database='chargerdb' 
)

cursor = connection.cursor()

cursor.execute('select * from tbl_charger_sum')

charger_data = cursor.fetchall()

c_seoul = charger_data[0]
c_busan = charger_data[12]
c_daegu = charger_data[13]
c_incheon = charger_data[5]
c_gwangju = charger_data[14]
c_daejeon = charger_data[7]
c_ulsan= charger_data[15]
c_sejong = charger_data[16]
c_gyeonggi = charger_data[6]
c_chungbuk = charger_data[4]
c_chungnam = charger_data[8]
c_jeonnam = charger_data[2]
c_gyeongbuk = charger_data[3]
c_gyeongnam = charger_data[9]
c_jeju = charger_data[1]
c_gangwon = charger_data[11]
c_jeonbuk = charger_data[10]

cursor.close()
connection.close()

