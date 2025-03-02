import mysql.connector
from mysql.connector import Error


class MySQLHelper:
    def __init__(self, host, user, password, database):
        self.host = host
        self.user = user
        self.password = password
        self.database = database
        self.connection = None

    def connect(self):
        """Устанавливает соединение с базой данных."""
        try:
            self.connection = mysql.connector.connect(
                host=self.host,
                user=self.user,
                password=self.password,
                database=self.database
            )
            if self.connection.is_connected():
                print("Успешное подключение к базе данных")
        except Error as e:
            print(f"Ошибка подключения: {e}")

    def disconnect(self):
        """Закрывает соединение с базой данных."""
        if self.connection and self.connection.is_connected():
            self.connection.close()
            print("Соединение закрыто")

    def execute_query(self, query, params=None):
        """Выполняет SQL-запрос (INSERT, UPDATE, DELETE)."""
        try:
            cursor = self.connection.cursor()
            cursor.execute(query, params)
            self.connection.commit()
            print("Запрос выполнен успешно")
        except Error as e:
            print(f"Ошибка при выполнении запроса: {e}")
        finally:
            cursor.close()

    def fetch_all(self, query, params=None):
        """Выполняет SELECT-запрос и возвращает все результаты."""
        try:
            cursor = self.connection.cursor(dictionary=True)
            cursor.execute(query, params)
            return cursor.fetchall()
        except Error as e:
            print(f"Ошибка при выполнении запроса: {e}")
            return None
        finally:
            cursor.close()

    def fetch_one(self, query, params=None):
        """Выполняет SELECT-запрос и возвращает одну запись."""
        try:
            cursor = self.connection.cursor(dictionary=True)
            cursor.execute(query, params)
            return cursor.fetchone()
        except Error as e:
            print(f"Ошибка при выполнении запроса: {e}")
            return None
        finally:
            cursor.close()

    def insert(self, table, data):
        """Вставляет данные в таблицу."""
        keys = ", ".join(data.keys())
        values = ", ".join(["%s"] * len(data))
        query = f"INSERT INTO {table} ({keys}) VALUES ({values})"
        self.execute_query(query, tuple(data.values()))

    def update(self, table, data, condition):
        """Обновляет данные в таблице."""
        set_clause = ", ".join([f"{key} = %s" for key in data.keys()])
        query = f"UPDATE {table} SET {set_clause} WHERE {condition}"
        self.execute_query(query, tuple(data.values()))

    def delete(self, table, condition):
        """Удаляет данные из таблицы."""
        query = f"DELETE FROM {table} WHERE {condition}"
        self.execute_query(query)

