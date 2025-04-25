import requests
import streamlit as st
import pprint


def get_money():
    url_get_money = 'https://market.csgo.com/api/v2/get-money?key=Jp2O97B3uVlNxp8t4bqD96LfX267RN7'
    response = requests.get(url_get_money)
    if response.status_code == 200:
        data = response.json()
    return st.text_input(label='money', value=data['money'])


def items():
    result_list = []
    url = 'https://market.csgo.com/api/v2/items?key=Jp2O97B3uVlNxp8t4bqD96LfX267RN7'
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        #pprint.pprint(data['items'][0])
        i = 0
        for item in data['items']:
            #pprint.pprint(f'{i}: {data['items'][i]}')
            item_buy = data['items'][i]
            name_item = item_buy['market_hash_name']
            price = item_buy['price']
            result_list.append([name_item, price])
            i += 1

    else:
        pprint.pprint('blad')

    return result_list

print(items())