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

cursor.execute('select city_code, lat, lng from tbl_map')

map_data = cursor.fetchall()

print(map_data)
