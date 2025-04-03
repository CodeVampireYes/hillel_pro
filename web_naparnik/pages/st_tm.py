import streamlit as st

from pages.page_st_tm.utils_st_tm import *


st.set_page_config(page_title="ST_TM", layout="wide")

st.markdown("""
    <style>
        .stButton>button {
            margin-top: 26px;
        }
    </style>
""", unsafe_allow_html=True)


def main():
    st.page_link('app.py', label='TM-ST')
    input_buy_st, min_sell = input_section()
    add_item_in_db(input_buy_st, min_sell)
    st.markdown("---")
    item_section_db()


if __name__ == "__main__":
    main()