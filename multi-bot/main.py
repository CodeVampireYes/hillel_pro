import asyncio
import sqlite3
from io import BytesIO
from aiogram import Bot, Dispatcher, types, F
from aiogram.filters import Command
from aiogram.types import Message, CallbackQuery, BotCommand, FSInputFile, InputFile, ReplyKeyboardRemove
import logging

import keyboards as kb  # Импортируем клавиатуры
from calendar_png import generate_calendar
from bd_config import cursor, conn, cursor_2, conn_2
from parser.parser_film import parser_site
from my_calendar import work_calendar_mariia

import os


logging.basicConfig(level=logging.INFO)

# Список команд с описаниями
commands = [
    BotCommand(command="week", description="Weekend"),
    BotCommand(command="go", description="Запустить игру"),
    BotCommand(command="discord", description="Настройка запуска Discord"),
    BotCommand(command="myid", description="Мой id"),
    BotCommand(command="db", description="Data Base"),
    BotCommand(command="parse", description="Parse"),
]


# Функция для установки команд
async def set_commands(bot: Bot):
    await bot.set_my_commands(commands)


# Создаем бота и диспетчер + sql3
cursor.execute('SELECT token FROM users')
TOKEN = cursor.fetchone()

bot = Bot(TOKEN[0])
dp = Dispatcher()


# Функция запуска игр стим и дискорда
def run_game_steam(value: str):
    cursor.execute('SELECT discord_on, discord_link FROM users')
    result = cursor.fetchall()
    if result[0][0] == 'False':
        os.system(f'start steam://run/{value[3:]}')
    else:
        os.system(result[0][1])
        os.system(f'start steam://run/{value[3:]}')


# Функция запуска wot и дискорда
## улучшить для всех декстоп приложений ##
def run_game_wot():
    cursor.execute('SELECT discord_on, discord_link FROM users')
    result = cursor.fetchall()
    if result[0][0] == 'False':
        os.system(r'C:\Games\World_of_Tanks_EU\wgc_api.exe --open')
    else:
        os.system(result[0][1])
        os.system(r'C:\Games\World_of_Tanks_EU\wgc_api.exe --open')


async def next_kb(message: Message):
    await message.answer(text="Какую игру запустить", reply_markup=await kb.inline_game())


@dp.message(Command('start'))
async def start(message: Message):
    await message.answer(text='', reply_markup=await kb.start_kb())


@dp.message(Command('myid'))
async def get_my_id(message: Message):
    await message.answer(f'{message.from_user.id}')
    await message.delete()


# Обработчик команды /go
@dp.message(Command("go"))
async def start_command(message: Message):
    if message.from_user.id == 5409293287:
        await message.reply(text="Какую игру запустить", reply_markup=await kb.inline_game())
        await message.delete()
    else:
        await message.answer(f'Для вас {message.from_user.first_name} доступна только команда /week')
        await message.delete()


# Обработчик команды /discord
@dp.message(Command('discord'))
async def on_discord(message: Message):
    if message.from_user.id == 5409293287:
        await message.reply(text='Запускать с игрой дискорд?', reply_markup=await kb.inline_discord())
        await message.delete()
    else:
        await message.answer(f'Для вас {message.from_user.first_name} доступна только команда /week')
        await message.delete()


@dp.message(Command('week'))
async def my_week(message: Message):
    await message.reply(text='Выходные:', reply_markup=await kb.my_week())
    await message.delete()


@dp.message(Command('db'))
async def bot_db(message: Message):
    cursor.execute('SELECT * FROM users')
    rows = cursor.fetchall()
    for row in rows:
        await message.answer(
            text=f"🔹Token: {row[0]}\n"
                 f"🔹Discord ON: {row[1]}\n"
                 f"🔹Discord Link: {row[2]}\n"
                 f"🔹ID: {row[3]}\n"
                 f"🔹Name: {message.from_user.first_name} "
                 f"🔹ID: {row[5]}\n"
        )

    cursor_2.execute('SELECT * FROM Film')
    rows_2 = cursor_2.fetchall()
    print(rows_2)


@dp.message(Command('parse'))
async def start_parse(message: Message):
    # Вызов функции парсинга
    parser_site()

    # Выборка данных из базы данных
    cursor_2.execute('SELECT parse_film FROM Film')
    rows_2 = cursor_2.fetchall()

    # Обработка результатов
    for row in rows_2:
        name = row[0]
        if name is not None and name.startswith('Декстер'):  # Проверка на None и начало строки
            await message.answer(str(name))  # Преобразуем кортеж в строку для вывода
            break
    cursor_2.execute("""
        UPDATE Film
        SET parse_film = NULL;
    """)
    conn.close()


# Фильтр сообщений, которые начинаются с "Привет"
@dp.message()
async def handle_message(message: Message):
    if message.text.startswith("Привет"):  # Проверяем начало сообщения
        text_after = message.text[len("Привет"):].strip()  # Убираем "Привет" и пробелы
        if text_after:
            cursor_2.execute("INSERT INTO Film (name_film) VALUES (?)", (text_after,))
            conn_2.commit()  # Ensure changes are committed to the database
            response = f"Фильм '{text_after}' добавлен!"  # Confirmation message
        else:
            response = "Ты ничего не написал после 'Привет'!"  # Message if nothing is written after "Привет"

        await message.answer(response)  # Send the response back to the user


# Ожидание колбэка который начинается на id_
@dp.callback_query(F.data.startswith('id_'))  # Фильтруем все callback_data
async def process_callback(callback_query: CallbackQuery):
    callback_data = callback_query.data  # Получаем callback_data

    # Удаляем сообщение с кнопками
    chat_id = callback_query.message.chat.id
    message_id = callback_query.message.message_id
    await bot.delete_message(chat_id, message_id)

    run_game_steam(callback_data)  # Вызываем функцию с этим значением
    # Обязательно отправляем ответ, иначе кнопка зависнет
    await callback_query.answer(f"Вы нажали: {callback_data}")


# Ожидание колбэка discord_on
@dp.callback_query(F.data =='discord_on')
async def process_discord_callback(callback_query: CallbackQuery):
    callback_data = callback_query.data

    # Удаляем сообщение с кнопками
    chat_id = callback_query.message.chat.id
    message_id = callback_query.message.message_id
    await bot.delete_message(chat_id, message_id)

    cursor.execute("UPDATE users SET discord_on = ? WHERE id = ?", ('True', 5409293287))

    await callback_query.answer(f"Вы нажали: {callback_data}")
    await next_kb(callback_query.message)
    #os.system('taskkill /f /im chrome.exe')


# Ожидание колбэка discord_off
@dp.callback_query(F.data =='discord_off')
async def process_discord_callback(callback_query: CallbackQuery):
    callback_data = callback_query.data
    cursor.execute("UPDATE users SET discord_on = ? WHERE id = ?", ('False', 5409293287))

    # Удаляем сообщение с кнопками
    chat_id = callback_query.message.chat.id
    message_id = callback_query.message.message_id
    await bot.delete_message(chat_id, message_id)

    await callback_query.answer(f"Вы нажали: {callback_data}")
    await next_kb(callback_query.message)
    #os.system('taskkill /f /im chrome.exe')
    #os.system('taskkill /f /im telegram.exe')


# Ожидание колбэка run_wot
@dp.callback_query(F.data == 'run_wot')
async def game_wot(callback_query: CallbackQuery):
    callback_data = callback_query.data

    # Удаляем сообщение с кнопками
    chat_id = callback_query.message.chat.id
    message_id = callback_query.message.message_id
    await bot.delete_message(chat_id, message_id)

    run_game_wot()
    await callback_query.answer('Wot запущен')


@dp.callback_query(F.data == 'week_artur')
async def watch_week_artur(callback_query: CallbackQuery):
    callback_data = callback_query.data

    cursor.execute("""
        UPDATE users
        SET list_weekend = '1'
    """)
    conn.commit()
    keyboard = await kb.year_month()
    await callback_query.message.edit_reply_markup(reply_markup=keyboard)

    await callback_query.answer()


@dp.callback_query(F.data == 'week_mariia')
async def watch_week_artur(callback_query: CallbackQuery):
    callback_data = callback_query.data

    cursor.execute("""
            UPDATE users
            SET list_weekend = '0'
        """)
    conn.commit()

    keyboard = await kb.year_month()
    await callback_query.message.edit_reply_markup(reply_markup=keyboard)

    await callback_query.answer()


@dp.callback_query(F.data.startswith('month'))
async def press_month(callback_query: CallbackQuery):
    callback_data = int(callback_query.data.replace('month', ''))
    generate_calendar(callback_data)
    # Создаем объект FSInputFile для отправки файла
    photo = FSInputFile("calendar.png")

    # Отправляем сгенерированное изображение в чат
    await callback_query.message.answer_photo(photo)

    # Подтверждаем обработку callback
    await callback_query.answer()
    # Удаляем сообщение с кнопками
    chat_id = callback_query.message.chat.id
    message_id = callback_query.message.message_id
    await bot.delete_message(chat_id, message_id)


# Запуск бота
async def main():
    await set_commands(bot)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())

# pyinstaller --onefile main.py