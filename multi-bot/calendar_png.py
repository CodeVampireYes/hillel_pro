import calendar
import asyncio
import matplotlib.pyplot as plt
from my_calendar import work_calendar_artur, work_calendar_mariia
from datetime import datetime
from database import db  # Импортируем асинхронную БД


async def generate_calendar(month_number):
    """
    Генерирует календарь для указанного месяца и сохраняет его в виде изображения,
    используя данные из work_calendar_artur для окраски дней.

    :param month_number: Номер месяца (1-12).
    :return: Имя файла с изображением календаря.
    """
    async with db.pool.acquire() as conn:
        async with conn.cursor() as cursor:
            await cursor.execute('SELECT list_weekend FROM users')
            result = await cursor.fetchone()

            print(f"Полученные данные из базы: {result}")  # Отладочное сообщение

            if not result or result[0] is None:
                return "Ошибка: Данные не найдены"

            if result[0] == 1:
                list_weekend = work_calendar_artur
                who = 'Artur'
            else:
                list_weekend = work_calendar_mariia
                who = 'Mariia'

    year = 2025  # Можно заменить на текущий год
    cal = calendar.monthcalendar(year, month_number)

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
    ax.set_title(f"{who}\n{calendar.month_name[month_number]} {year}", fontsize=14, fontweight="bold")

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
            date_str = f"{year}-{month_number:02d}-{day:02d}"

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



