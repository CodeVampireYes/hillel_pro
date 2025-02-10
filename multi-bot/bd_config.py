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

