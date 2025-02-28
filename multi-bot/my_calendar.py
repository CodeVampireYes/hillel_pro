from datetime import date, timedelta

# Рабочие дни и выходные для Артура
work_artur = ['day', 'day', 'weekend', 'weekend', 'weekend', 'night', 'night', 'weekend', 'weekend',
              'day', 'day', 'day', 'weekend', 'weekend', 'night', 'night', 'weekend', 'weekend', 'weekend', 'day',
              'day', 'weekend', 'weekend',
              'night', 'night', 'night', 'weekend', 'weekend']

work_mariia_4_2 = ['day', 'day', 'night', 'night', 'weekend', 'weekend']
work_mariia_4_4 = ['day', 'day', 'night', 'night', 'weekend', 'weekend', 'weekend', 'weekend']

work_calendar_artur = []
work_calendar_mariia = []


def grafik_artur():
    start_date = date(2024, 5, 15)

    current_date = start_date

    for i in range(900):
        # Циклически выбираем тип дня из графика
        day_type = work_artur[i % len(work_artur)]
        # Добавляем дату и тип дня в календарь
        work_calendar_artur.append([str(current_date), day_type])
        # Переходим к следующему дню
        current_date += timedelta(days=1)

    return work_calendar_artur

grafik_artur()

def grafik_mariia():
    start_date = date(2025, 2, 9)

    current_date = start_date

    for i in range(900):
        # Циклически выбираем тип дня из графика
        day_type = work_mariia_4_4[i % len(work_mariia_4_4)]
        # Добавляем дату и тип дня в календарь
        work_calendar_mariia.append([str(current_date), day_type])
        # Переходим к следующему дню
        current_date += timedelta(days=1)

    return work_calendar_mariia


grafik_mariia()