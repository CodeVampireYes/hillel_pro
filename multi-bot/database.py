import aiomysql
import asyncio
from my_config import DB_CONFIG  # Импортируем конфиг с настройками


class Database:
    def __init__(self):
        self.pool = None  # Пул подключений

    async def connect(self):
        """Подключение к базе данных и создание пула"""
        self.pool = await aiomysql.create_pool(**DB_CONFIG)
        print("✅ Подключение к MySQL установлено.")

    async def close(self):
        """Закрытие пула соединений"""
        if self.pool:
            self.pool.close()
            await self.pool.wait_closed()
            print("❌ Подключение к MySQL закрыто.")

    async def execute(self, query, params=None, fetchone=False, fetchall=False):
        """
        Выполняет SQL-запрос.
        :param query: SQL-запрос
        :param params: Параметры запроса (tuple)
        :param fetchone: True - вернуть одну строку
        :param fetchall: True - вернуть все строки
        :return: Данные запроса или None
        """
        async with self.pool.acquire() as conn:
            async with conn.cursor(aiomysql.DictCursor) as cursor:
                await cursor.execute(query, params or ())

                if fetchone:
                    return await cursor.fetchone()
                if fetchall:
                    return await cursor.fetchall()

                await conn.commit()

    async def create_tables(self):
        """Создаёт таблицы (если их нет)"""
        query = """
        CREATE TABLE IF NOT EXISTS users (
            id INT AUTO_INCREMENT PRIMARY KEY,
            user_id BIGINT UNIQUE NOT NULL,
            username VARCHAR(255),
            balance FLOAT DEFAULT 0
        );
        """
        await self.execute(query)
        print("✅ Таблицы проверены/созданы.")


# Создаём объект базы данных
db = Database()
