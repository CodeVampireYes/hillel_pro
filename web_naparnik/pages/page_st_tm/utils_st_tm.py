import streamlit as st
from pages.page_st_tm.db import *


def input_section():
    cols = st.columns([1.26, 1, 0.6])
    with cols[0]:
        st.text(' ')
    with cols[1]:
        st.header("ST-TM")
    with cols[2]:
        st.text(' ')

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        input_buy_st = st.number_input('Buy ST (ZL)', value=1.0, step=0.1, format="%.2f")
    with col2:
        input_sell_tm = st.number_input('Sell TM ($)', value=1.0, step=0.1, format="%.2f")

    profit = (input_sell_tm * 0.95) - (input_buy_st / 4)
    percent = ((input_sell_tm * 0.95) / (input_buy_st / 4)) * 100 - 100
    min_sell = (input_buy_st / 4 ) * 0.95

    with col3:
        st.number_input('Profit ($)', value=profit, format="%.2f", disabled=True)

    with col4:
        st.number_input('Percent (%)', value=percent, format="%.2f", disabled=True)
    return input_buy_st, min_sell


def add_item_in_db(input_buy_st: float, min_sell: float):
    col1, col2, col3, col4 = st.columns(4)

    with col1:
        name = st.text_input('Item Name', key='item_name')
    with col2:
        st.text_input('Min Sell ST', value=f"{min_sell:.2f}", disabled=True)
    with col3:
        if st.button('Add to Database', disabled=not name):
            add_item_st_tm(name, input_buy_st, min_sell)
    with col4:
        pass


def item_section_db():
    st.header("Мои покупки")

    def get_all_tm_st_items():
        with sqlite3.connect('example.db') as db:
            cursor = db.execute("SELECT * FROM st_tm")
            return cursor.fetchall()

    def calculate_profit(buy_st: float, sell_tm: float) -> float:
        return (sell_tm * 0.95) - (buy_st / 4)

    def calculate_percent(buy_st: float, sell_tm: float) -> float:
        return ((sell_tm * 0.95) / (buy_st / 4)) * 100 - 100

    def update_sell_value(item_id: int, new_sell_value) -> None:
        with sqlite3.connect('example.db') as db:
            try:
                db.execute(
                    "UPDATE st_tm SET sell = ? WHERE id = ?",
                    (new_sell_value, item_id)
                )
                db.commit()
                st.success("Sell value updated!")
            except sqlite3.Error as e:
                st.error(f"Database error: {e}")

    def calculate_totals(items) -> dict:
        totals = {
            'buy_st': 0.0,
            'sell_tm': 0.0,
            'profit': 0.0,
        }

        for item in items:
            totals['buy_st'] += float(item[2])
            if item[4]:  # if sell value exists
                totals['sell_tm'] += float(item[4])
                totals['profit'] += calculate_profit(float(item[2]), float(item[4]))

        if totals['buy_st'] > 0:
            totals['percent'] = (totals['sell_tm'] * 0.85 / (totals['buy_st'] * 4)) * 100 - 100
        else:
            totals['percent'] = 0.0

        return totals

    items = get_all_tm_st_items()
    totals = calculate_totals(items)

    # Display totals
    cols = st.columns(6)
    with cols[0]:
        st.metric("Total Buy ZL", f"{totals['buy_st'] * 4:.2f}")
    with cols[1]:
        st.metric("Total Buy USDT", f"{totals['buy_st']:.2f}")
    with cols[4]:
        st.metric("Total Profit", f"{totals['profit']:.2f}")
    with cols[5]:
        st.metric("Total Percent", f"{totals['percent']:.1f}%")

    # Display items in a table-like format
    for item in items:
        cols = st.columns([0.5, 3, 1, 1, 1, 1, 1, 1])

        with cols[0]:
            st.text_input('ID', value=item[0], key=f'id_{item[0]}', disabled=True)

        with cols[1]:
            st.text_input('Name', value=item[1], key=f'name_{item[0]}', disabled=True)

        with cols[2]:
            st.text_input('Buy', value=f"{item[2]:.2f}", key=f"buy_{item[0]}", disabled=True)

        with cols[3]:
            st.text_input('Min Sell', value=f"{item[3]:.2f}", key=f"min_{item[0]}", disabled=True)

        with cols[4]:
            new_sell = st.text_input('Actual Sell', value=f"{item[4] if item[4] else ''}", key=f"sell_{item[0]}")

        with cols[5]:
            if item[4]:
                profit = calculate_profit(float(item[2]), float(item[4]))
                st.text_input('Profit', value=f"{profit:.2f}", disabled=True, key=f"profit_{item[0]}")
            else:
                st.text_input('Profit', value="", disabled=True, key=f"profit_{item[0]}")

        with cols[6]:
            if item[4]:
                percent = ((float(item[4]) * 0.95) / (float(item[2]) / 4)) * 100 - 100
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