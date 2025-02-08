import asyncio
from aiogram import Bot, Dispatcher, types, F
from aiogram.filters import Command
from aiogram.types import Message, CallbackQuery, BotCommand

from config import TOKEN, DISCORD_ON, discord_link
import keyboards as kb  # Импортируем клавиатуры
from my_calendar import together_weekend

import os


# Список команд с описаниями
commands = [
    BotCommand(command="go", description="Запустить игру"),
    BotCommand(command="discord", description="Настройка запуска Discord"),
    BotCommand(command="tog", description="Показать выходные")
]


# Функция для установки команд
async def set_commands(bot: Bot):
    await bot.set_my_commands(commands)


# Создаем бота и диспетчер
bot = Bot(TOKEN)
dp = Dispatcher()


# Функция запуска игр стим и дискорда
def run_game_steam(value: str):
    print(value[3:])
    if DISCORD_ON == False:
        os.system(f'start steam://run/{value[3:]}')
    else:
        os.system(discord_link)
        os.system(f'start steam://run/{value[3:]}')


# Функция запуска игр декстоп и дискорда
def run_game_wot():
    if DISCORD_ON == False:
        os.system(r'C:\Games\World_of_Tanks_EU\wgc_api.exe --open')
    else:
        os.system(discord_link)
        os.system(r'C:\Games\World_of_Tanks_EU\wgc_api.exe --open')


# Функция переключения состояния запуска дискорд
def toggle_discord(values):
    global DISCORD_ON
    if values == 'discord_on':
        DISCORD_ON = True
        print(DISCORD_ON)
        return DISCORD_ON
    else:
        DISCORD_ON = False
        print(DISCORD_ON)
        return DISCORD_ON


# Обработчик команды /go
@dp.message(Command("go"))
async def start_command(message: Message):
    await message.reply(text="Какую игру запустить", reply_markup=await kb.inline_game())


# Обработчик команды /discord
@dp.message(Command('discord'))
async def on_discord(message: Message):
    await message.reply(text='Запускать с игрой дискорд?', reply_markup=await kb.inline_discord())


# Обработчик команды /tog
@dp.message(Command('tog'))
async def tog_week(message: Message):
    await message.reply(text="Следующие 10 выходных вместе:", reply_markup=await kb.together_week())


# Ожидание колбэка который начинается на id_
@dp.callback_query(F.data.startswith('id_'))  # Фильтруем все callback_data
async def process_callback(callback_query: CallbackQuery):
    callback_data = callback_query.data  # Получаем callback_data
    run_game_steam(callback_data)  # Вызываем функцию с этим значением
    # Обязательно отправляем ответ, иначе кнопка зависнет
    await callback_query.answer(f"Вы нажали: {callback_data}")


# Ожидание колбэка discord_on
@dp.callback_query(F.data =='discord_on')
async def process_discord_callback(callback_query: CallbackQuery):
    callback_data = callback_query.data
    toggle_discord(callback_data)
    await callback_query.answer(f"Вы нажали: {callback_data}")


# Ожидание колбэка discord_off
@dp.callback_query(F.data =='discord_off')
async def process_discord_callback(callback_query: CallbackQuery):
    callback_data = callback_query.data
    toggle_discord(callback_data)
    await callback_query.answer(f"Вы нажали: {callback_data}")


# Ожидание колбэка run_wot
@dp.callback_query(F.data == 'run_wot')
async def game_wot(callback_query: CallbackQuery):
    callback_data = callback_query.data
    run_game_wot()
    await callback_query.answer('Wot запущен')


# Запуск бота
async def main():
    await set_commands(bot)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
