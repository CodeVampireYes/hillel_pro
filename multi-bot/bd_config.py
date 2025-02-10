import sqlite3

# Подключение к базе данных (или создание новой, если она не существует)
with sqlite3.connect('example.db') as conn:
    # Создание курсора для выполнения SQL-запросов
    cursor = conn.cursor()

    # Сохранение изменений
    conn.commit()

    # Выборка данных
    cursor.execute("SELECT * FROM users")
    rows = cursor.fetchall()


with sqlite3.connect('film.db') as conn_2:
    # Создание курсора для выполнения SQL-запросов
    cursor_2 = conn_2.cursor()

    # Сохранение изменений
    conn_2.commit()

    # Выборка данных
    cursor_2.execute("SELECT * FROM Film")
    rows_2 = cursor_2.fetchall()

