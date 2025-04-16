import streamlit as st
import sqlite3
from contextlib import closing
from typing import List, Tuple, Optional

from config import exchange_zl

# Configuration
st.set_page_config(page_title="TM_ST", layout="wide")
DB_NAME = 'example.db'

st.markdown("""
    <style>
        .stButton>button {
            margin-top: 26px;
        }
    </style>
""", unsafe_allow_html=True)


# Database Utilities
def create_tables():
    with closing(sqlite3.connect(DB_NAME)) as db:
        db.execute("""
            CREATE TABLE IF NOT EXISTS tm_st (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                buy_tm REAL NOT NULL,
                min_sell_st REAL NOT NULL,
                sell REAL  
            )
        """)
        db.execute("""
            CREATE TABLE IF NOT EXISTS st_tm (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                buy_st REAL NOT NULL,
                min_sell_tm REAL NOT NULL,
                sell REAL  
            )
        """)
        db.execute("""
            CREATE TABLE IF NOT EXISTS total_tm_st (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                total_buy_tm REAL,
                total_sell_st REAL,
                total_profit_tm_st REAL,
                total_percent_tm_st REAL
            ) 
        """)
        db.commit()


def add_item_tm_st(name: str, buy_tm: float, min_sell_st: float) -> None:
    with closing(sqlite3.connect(DB_NAME)) as db:
        try:
            db.execute(
                "INSERT INTO tm_st (name, buy_tm, min_sell_st) VALUES (?, ?, ?)",
                (name, buy_tm, min_sell_st)
            )
            db.commit()
            st.success("Item added successfully!")
        except sqlite3.Error as e:
            st.error(f"Database error: {e}")


def update_sell_value(item_id: int, new_sell_value: Optional[float]) -> None:
    with closing(sqlite3.connect(DB_NAME)) as db:
        try:
            db.execute(
                "UPDATE tm_st SET sell = ? WHERE id = ?",
                (new_sell_value, item_id)
            )
            db.commit()
            st.success("Sell value updated!")
        except sqlite3.Error as e:
            st.error(f"Database error: {e}")


def get_all_tm_st_items() -> List[Tuple]:
    with closing(sqlite3.connect(DB_NAME)) as db:
        cursor = db.execute("SELECT * FROM tm_st")
        return cursor.fetchall()


# Calculation Functions
def calculate_profit(buy_tm: float, sell_st: float) -> float:
    return (sell_st * 0.85) - (buy_tm * exchange_zl)


def calculate_percent(buy_tm: float, sell_st: float) -> float:
    return ((sell_st * 0.85) / (buy_tm * exchange_zl)) * 100 - 100


def calculate_min_sell(buy_tm: float) -> float:
    return ((buy_tm * exchange_zl) * 1.06) / 0.85


def calculate_totals(items: List[Tuple]) -> dict:
    totals = {
        'buy_tm': 0.0,
        'sell_st': 0.0,
        'profit': 0.0,
    }

    for item in items:
        totals['buy_tm'] += float(item[2])
        if item[4]:  # if sell value exists
            totals['sell_st'] += float(item[4])
            totals['profit'] += calculate_profit(float(item[2]), float(item[4]))

    if totals['buy_tm'] > 0:
        totals['percent'] = (totals['sell_st'] * 0.85 / (totals['buy_tm'] * exchange_zl)) * 100 - 100
    else:
        totals['percent'] = 0.0

    return totals


# UI Components
def input_section():
    cols = st.columns([1.26, 1, 0.6])
    with cols[0]:
        st.text(' ')
    with cols[1]:
        st.header("TM-ST")
    with cols[2]:
        st.text(' ')


    col1, col2, col3, col4 = st.columns(4)

    with col1:
        input_buy_tm = st.number_input('Buy TM ($)', value=1.0, step=0.1, format="%.2f")

    with col2:
        input_sell_st = st.number_input('Sell ST (ZL)', value=1.0, step=0.1, format="%.2f")

    # Calculations
    profit = calculate_profit(input_buy_tm, input_sell_st)
    percent = calculate_percent(input_buy_tm, input_sell_st)
    min_sell = calculate_min_sell(input_buy_tm)

    with col3:
        st.number_input('Profit ($)', value=profit, format="%.2f", disabled=True)

    with col4:
        st.number_input('Percent (%)', value=percent, format="%.2f", disabled=True)

    return input_buy_tm, min_sell


def add_item_section(buy_tm: float, min_sell: float):
    col1, col2, col3, col4 = st.columns([5.2, 1, 1, 1])

    with col1:
        name = st.text_input('Item Name', key='item_name')

    with col2:
        st.text_input('Min Sell ST', value=f"{min_sell:.2f}", disabled=True)

    with col3:
        if st.button('Add', disabled=not name):
            add_item_tm_st(name, buy_tm, min_sell)
    with col4:
        st.text(' ')


def display_items_section():
    st.header("Мои покупки")
    items = get_all_tm_st_items()
    totals = calculate_totals(items)

    # Display totals
    cols = st.columns(6)
    with cols[0]:
        st.metric("Total Buy ZL", f"{totals['buy_tm'] * exchange_zl:.2f}")
    with cols[1]:
        st.metric("Total Buy USDT", f"{totals['buy_tm']:.2f}")
    with cols[4]:
        st.metric("Total Profit", f"{totals['profit']:.2f}")
    with cols[5]:
        st.metric("Total Percent", f"{totals['percent']:.1f}%")

    # Display items in a table-like format
    for item in items:
        cols = st.columns([0.5, 3.3, 0.8, 0.8, 0.8, 0.8, 0.8, 1])

        with cols[0]:
            st.text_input('ID', value=item[0], key=f'id_{item[0]}', disabled=True)

        with cols[1]:
            st.text_input('Name', value=item[1], key=f'name_{item[0]}', disabled=True)

        with cols[2]:
            st.text_input('Buy', value=f"{item[2]:.2f}", key=f"buy_{item[0]}", disabled=True)

        with cols[3]:
            st.text_input('Min Sell', value=f"{item[3]:.2f}", key=f"min_{item[0]}", disabled=True)

        with cols[4]:
            new_sell = st.text_input('Sell', value=f"{item[4] if item[4] else ''}", key=f"sell_{item[0]}")

        with cols[5]:
            if item[4]:
                profit = calculate_profit(float(item[2]), float(item[4]))
                st.text_input('Profit', value=f"{profit:.2f}", disabled=True, key=f"profit_{item[0]}")
            else:
                st.text_input('Profit', value="", disabled=True, key=f"profit_{item[0]}")

        with cols[6]:
            if item[4]:
                percent = calculate_percent(float(item[2]), float(item[4]))
                st.text_input('Percent', value=f"{percent:.2f}%", disabled=True, key=f"percent_{item[0]}")
            else:
                st.text_input('Percent', value="", disabled=True, key=f"percent_{item[0]}")

        with cols[7]:
            if st.button("Update", key=f"update_{item[0]}"):
                try:
                    sell_value = float(new_sell) if new_sell else None
                    update_sell_value(item[0], sell_value)
                    st.rerun()
                except ValueError:
                    st.error("Please enter a valid number")


# Main App
def main():
    with st.sidebar:
        pass

    create_tables()

    buy_tm, min_sell = input_section()
    add_item_section(buy_tm, min_sell)
    st.markdown("---")
    display_items_section()


if __name__ == "__main__":
    main()