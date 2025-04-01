import streamlit as st
import sqlite3
import asyncio

from config import *


# Создание таблиц при запуске
def create_tables():
    with sqlite3.connect('example.db') as db:
        db.execute("""
            CREATE TABLE IF NOT EXISTS tm_st (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT,
                buy_tm REAL,
                min_sell_st REAL,
                sell REAL  
            )
        """)
        db.execute("""
            CREATE TABLE IF NOT EXISTS st_tm (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT,
                buy_st REAL,
                min_sell_tm REAL,
                sell REAL  
            )
        """)
        db.execute("""
            CREATE TABLE IF NOT EXISTS total_tm_st (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                total_buy_tm REAL,
                total_sell_st REAL,
                total_profit_tm_st REAL,
                total_percent_tm_st REAL,  
            ) 
        """)
        db.commit()


col1, col2, col3, col4 = st.columns(4)

with col1:
    input_buy_tm = st.number_input('Buy TM', value=1.0, step=0.1)  # Теперь float

with col2:
    input_sell_st = st.number_input('Sell ST', value=1.0, step=0.1)  # Теперь float

# Вычисления
profit_tm_st = (input_sell_st * 0.85) - (input_buy_tm * exchange_zl)
percent_tm_st = ((input_sell_st * 0.85) / (input_buy_tm * exchange_zl)) * 100 - 100
min_sell_st = ((input_buy_tm * exchange_zl) * 1.06) / 0.85


with col3:
    st.number_input('Profit $', value=profit_tm_st, format="%.2f", disabled=True)

with col4:
    st.number_input('Percent %', value=percent_tm_st, format="%.2f", disabled=True)

col5, col6, col7, col8 = st.columns(4)

with col5:
    name_item = st.text_input('Name')
with col6:
    min_sell_item = st.text_input(label='Min Sell ST', value=str(min_sell_st)[:4])
with col7:
    def add_item_db_tm_st():
        if name_item != '':
            with sqlite3.connect('example.db') as db:
                db.execute("""
                    INSERT OR REPLACE INTO tm_st (
                    name, buy_tm, min_sell_st) 
                    VALUES (?, ?, ?)
                """, (name_item, input_buy_tm, min_sell_item))
                db.commit()
        else:
            print('Vvedi imia')


    st.text('')
    st.button(label='Add', on_click=add_item_db_tm_st)

#st.text('-------------------------------------------------------------------------------------------------------------')


def refresh_item():
    with sqlite3.connect('example.db') as db:
        cursor = db.execute("""
            SELECT * FROM tm_st
        """)
        data = cursor.fetchall()
    return data

col14, col15, col16, col17, col18, col19 = st.columns(6)

with col14:
    st.number_input(label='Total Buy ZL')
with col15:
    st.number_input(label='Total Buy USDT')
with col16:
    st.number_input(label='Total Sell ZL')
with col17:
    st.number_input(label='Total Sell USDT')
with col18:
    st.number_input(label='Total Profit')
with col19:
    st.number_input(label='Total Percent')


if st.button("Refresh"):
    data = refresh_item()
    col9, col11, col12, col13, col20, col10, col21 = st.columns([0.65, 6, 1, 1, 1, 1, 1])
    for index, el in enumerate(data):
        index += 1
        with col9:
            st.text_input(label='№', value=index, key=f'number_{index}')
        with col11:
            st.text_input(label='name', value=el[1], key=f'name_{index}')
        with col12:
            st.text_input(label='buy', value=el[2], key=f"buy_{index}")
        with col13:
            st.text_input(label='min sell', value=el[3], key=f"min_sell_{index}")
        with col20:
            st.text_input(label='sell', key=f"sell_{index}")
        with col10:
            st.text_input(label='percent', key=f'percent_{index}')
        with col21:
            st.text_input(label='profit', key=f'profit_{index}')
