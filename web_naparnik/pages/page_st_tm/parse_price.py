import requests
import json
import time
import pprint

API_TM = 'Jp2O97B3uVlNxp8t4bqD96LfX267RN7'


def get_price_tm(item: str):
    time.sleep(1)
    url = f'https://market.csgo.com/api/v2/search-item-by-hash-name?key={API_TM}&hash_name={item}'
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        if data.get('success'):
            items = data.get('data', [])
            if items:
                entry = items[0]  # Берем первый элемент
                price = entry.get('price', 0) / 1000  # цена в долларах
                return price
            else:
                print(f'Предмет "{item}" не найден.')
        else:
            print('Ошибка в данных API:', data.get('error'))
    else:
        print('Ошибка при выполнении запроса:', response.status_code)

    return 0


all_item = []

def get_items_list():
    url = f'https://market.csgo.com/api/v2/prices/USD.json?key={API_TM}'  # этот эндпоинт отдаёт список предметов
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        if data.get('success'):
            items = data.get('items', [])
            for item in items:
                name = item.get('market_hash_name')
                price = float(item.get('price'))
                volume = item.get('volume')
                all_item.append([name, price])

        else:
            print('Ошибка в данных API:', data.get('error'))
    else:
        print('Ошибка при выполнении запроса:', response.status_code)


def search_item_price(item: str):
    get_items_list()

    for el in all_item:
        if el[0] == item:
            return el[1]


