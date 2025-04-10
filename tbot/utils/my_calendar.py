from datetime import date, timedelta
import calendar
import matplotlib.pyplot as plt
import aiosqlite


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
    start_date = date(2025, 2, 11)

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


async def generate_calendar(number_month):
    async with aiosqlite.connect('example.db') as db:
        async with db.execute("SELECT create_calendar FROM setting_tbot") as cursor:
            username_calendar = await cursor.fetchone()
            print(username_calendar)
        await db.commit()

        if username_calendar[0] == 'artur':
            print('artur')
            list_weekend = work_calendar_artur
            who = 'Artur'
        elif username_calendar[0] == 'mariia':
            print('mariia')
            list_weekend = work_calendar_mariia
            who = 'Mariia'

    year = 2025  # Можно заменить на текущий год
    cal = calendar.monthcalendar(year, number_month)

    # Цвета для разных типов дней
    color_map = {
        "day": "yellow",
        "night": "black",
        "weekend": "green"
    }

    # Преобразуем work_calendar_artur в словарь для быстрого доступа
    work_dates = {}
    for date_str, day_type in list_weekend:

        work_dates[date_str] = day_type

    fig, ax = plt.subplots(figsize=(8, 6))
    # Устанавливаем цвет фона всей фигуры
    fig.patch.set_facecolor('lightgray')

    # Устанавливаем цвет фона области графика
    ax.set_facecolor('lightgray')
    ax.set_title(f"{who}\n{calendar.month_name[number_month]} {year}", fontsize=14, fontweight="bold")

    # Отрисовываем названия дней недели
    days_of_week = ["Пн", "Вт", "Ср", "Чт", "Пт", "Сб", "Вс"]
    for i, day in enumerate(days_of_week):
        ax.text(i, 0, day, fontsize=18, ha="center", va="center", fontweight="bold")

    # Проходим по дням и отмечаем их
    for week_idx, week in enumerate(cal):
        for day_idx, day in enumerate(week):
            if day == 0:
                continue  # Пропускаем пустые ячейки

            # Формируем строку для даты
            date_str = f"{year}-{number_month:02d}-{day:02d}"

            # Проверяем тип дня из work_dates и выбираем цвет
            day_type = work_dates.get(date_str, None)

            if day_type:
                color = color_map.get(day_type, "black")  # Используем цвет из work_calendar_artur
            else:
                color = "black"  # Если день не найден, используем черный цвет

            # Отрисовка дня в календаре
            ax.text(day_idx, -week_idx - 1, str(day), fontsize=24, ha="center", va="center", color=color,
                    fontweight="bold")

    # Настройки осей и сохранение
    ax.set_xticks(range(7))
    ax.set_xticklabels(days_of_week, fontsize=10)
    ax.set_yticks([])
    ax.set_xlim(-0.5, 6.5)
    ax.set_ylim(-len(cal) - 0.5, 0.5)
    ax.axis("off")

    filename = "calendar.png"
    plt.savefig(filename, bbox_inches="tight")
    plt.close()

    return filename
