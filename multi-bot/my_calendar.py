from datetime import datetime, timedelta

# Рабочие дни и выходные для Артура
work_artur = ['work', 'work', 'weekend', 'weekend', 'weekend', 'work', 'work', 'weekend', 'weekend',
              'work', 'work', 'work', 'weekend', 'weekend']
list_weekend_artur = []

def weekend_artur():
    start_data = datetime(2024, 9, 4)  # Начальная дата для Артура
    global work_artur

    for day in range(900):
        current_day_type = work_artur[day % len(work_artur)]  # Циклически перебираем список work_artur
        if current_day_type == 'weekend':
            list_weekend_artur.append(str(start_data)[:10])
        start_data += timedelta(1)

    return list_weekend_artur

# Рабочие дни и выходные для Марии
list_weekend_mariia = []
work_mariia = ['work', 'work', 'work', 'work', 'weekend', 'weekend']

def weekend_mariia():
    start_data = datetime(2025, 2, 7)  # Начальная дата для Марии
    global work_mariia

    for day in range(900):
        current_day_type = work_mariia[day % len(work_mariia)]  # Циклически перебираем список work_mariia
        if current_day_type == 'weekend':
            list_weekend_mariia.append(str(start_data)[:10])
        start_data += timedelta(1)

    return list_weekend_mariia

together_list = []

# Функция для поиска общих выходных, которые больше сегодняшней даты
def together_weekend():
    # Получаем списки выходных
    weekend_mariia()
    weekend_artur()

    # Находим общие выходные
    common_el = set(list_weekend_mariia) & set(list_weekend_artur)
    common_el = list(common_el)

    # Получаем текущую дату
    today = datetime.now().strftime('%Y-%m-%d')

    # Фильтруем общие выходные, оставляя только те, которые больше сегодняшней даты
    future_common_el = [date for date in common_el if date > today]

    # Сортируем и выводим результат
    for date in sorted(future_common_el):
        together_list.append(date)


