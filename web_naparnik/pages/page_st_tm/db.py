import streamlit as st
import sqlite3


def add_item_st_tm(name: str, buy_st: float, min_sell_tm: float):
    with sqlite3.connect('example.db') as db:
        try:
            db.execute(
                "INSERT INTO st_tm (name, buy_st, min_sell_tm) VALUES (?, ?, ?)",
                (name, buy_st, min_sell_tm)
            )
            db.commit()
            st.success("Item added successfully!")
        except sqlite3.Error as e:
            st.error(f"Database error: {e}")