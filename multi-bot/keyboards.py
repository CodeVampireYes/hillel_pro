from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup, KeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder, ReplyKeyboardBuilder

from my_config import game_id
from database import db

async def inline_game():
    keyboard = InlineKeyboardBuilder()
    keyboard.add(InlineKeyboardButton(text='WOT', callback_data='run_wot'))
    for game in game_id:
        game_name = game[0]
        id_game = game[1]
        keyboard.add(InlineKeyboardButton(text=game_name, callback_data=f'id_{id_game}'))
    return keyboard.adjust(1).as_markup()


async def inline_discord():
    keyboard = InlineKeyboardBuilder()
    keyboard.add(InlineKeyboardButton(text='On', callback_data='discord_on'),
                 (InlineKeyboardButton(text='Off', callback_data='discord_off')))
    return keyboard.adjust(1).as_markup()


async def my_week():
    keyboard = InlineKeyboardBuilder()
    keyboard.add(InlineKeyboardButton(text='Artur', callback_data='week_artur'))
    keyboard.add(InlineKeyboardButton(text='Mariia', callback_data='week_mariia'))
    return keyboard.adjust(1).as_markup()


year = ['январь', "февраль", 'Март' , 'Апрель' , 'Май', 'Июнь', 'Июль' , 'Август', 'Сентябрь', 'Октябрь' , 'Ноябрь', 'Декабрь']


async def year_month():
    x = 1
    keyboard = InlineKeyboardBuilder()
    for month in year:
        keyboard.add(InlineKeyboardButton(text=month, callback_data=f'month{x}'))
        x +=1
    return keyboard.adjust(2).as_markup()


async def info_db():
    keyboard = InlineKeyboardBuilder()
    async with db.pool.acquire() as conn:
        async with conn.cursor() as cursor:
            await cursor.execute("""SHOW TABLES;""")
            tables = await cursor.fetchall()
            await conn.commit()

    for table in tables:
        # Извлекаем строку из кортежа. Предполагается, что каждый элемент в tables - это кортеж с одним элементом (название таблицы).
        table_name = table[0]  # Это первый элемент кортежа (название таблицы)
        keyboard.add(InlineKeyboardButton(text=table_name, callback_data=f'table_{table_name}'))

    return keyboard.adjust(1).as_markup()


async def info_table_users():
    keyboard = InlineKeyboardBuilder()
    async with db.pool.acquire() as conn:
        async with conn.cursor() as cursor:
            await cursor.execute("""SELECT * FROM users;""")
            data_table = await cursor.fetchall()
            print(data_table)
            await conn.commit()
    for data in data_table:
        data_name = data[0]
        keyboard.add(InlineKeyboardButton(text=data_name, callback_data='data_table_users'))

    return keyboard.adjust(1).as_markup()