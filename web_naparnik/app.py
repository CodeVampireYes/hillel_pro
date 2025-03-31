import streamlit as st

from config import *


col1, col2, col3, col4 = st.columns(4)

with col1:
    input_buy_tm = st.number_input('Buy TM', value=1.0, step=0.1)  # Теперь float

with col2:
    input_sell_st = st.number_input('Sell ST', value=1.0, step=0.1)  # Теперь float

# Вычисления
profit_tm_st = (input_sell_st * 0.85) - (input_buy_tm * exchange_zl)
percent_tm_st = ((input_sell_st * 0.85) / (input_buy_tm * exchange_zl)) * 100 - 100

with col3:
    st.number_input('Profit $', value=profit_tm_st, format="%.2f", disabled=True)

with col4:
    st.number_input('Percent %', value=percent_tm_st, format="%.2f", disabled=True)
