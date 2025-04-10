import aiosqlite


async def init_db_setting_tbot():
    """Инициализация базы данных и таблицы setting_tbot"""
    async with aiosqlite.connect('example.db') as db:
        await db.execute("""
            CREATE TABLE IF NOT EXISTS setting_tbot (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                token TEXT NOT NULL,
                create_calendar TEXT
            )
        """)
        await db.commit()


async def get_token_setting_tbot(record_id: int):
    """Получение токена из базы данных по ID"""
    async with aiosqlite.connect('example.db') as db:
        async with db.execute('SELECT token FROM setting_tbot WHERE id = ?', (record_id,)) as cursor:
            row = await cursor.fetchone()
            return row[0] if row else None

######

#Вставка или обновление (INSERT OR REPLACE)
#query = "INSERT OR REPLACE INTO setting_tbot (id, token) VALUES (?, ?)"
#params = (2, "2",)
######

# Удаляем запись с ID = 5
#query = "DELETE FROM setting_tbot WHERE id = ?"
#params = (2,)
######


async def init_db_users():
    """Инициализация базы данных и таблицы setting_tbot"""
    async with aiosqlite.connect('example.db') as db:
        await db.execute("""
            CREATE TABLE IF NOT EXISTS users (
                user_id INTEGER PRIMARY KEY AUTOINCREMENT,
                first_name TEXT,
                last_name TEXT,
                username TEXT,
                language_code TEXT,
                is_bot INTEGER
            )
        """)
        await db.commit()


