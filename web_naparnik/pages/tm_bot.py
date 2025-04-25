import streamlit as st
from pages.page_tm_bot.utils_tm_bot import *


def main():
    with st.sidebar:
        pass
    cols = st.columns(3)
    with cols[0]:
        pass
    with cols[1]:
        pass
    with cols[2]:
        get_money()

    st.markdown("---")

    st.text('BUY')
    cols = st.columns(2)
    i = 0
    for el in items():
        with cols[0]:
            st.text_input(label="Name", value=el[0], key=f'buy_item_{i}')
        with cols[1]:
            st.text_input(label="Price", value=el[1], key=f'price_item_{i}')
        i += 1


if __name__ == "__main__":
    main()