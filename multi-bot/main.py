import asyncio
from aiogram import Bot, Dispatcher, types, F
from aiogram.filters import Command
from aiogram.types import Message, CallbackQuery

from config import TOKEN
import keyboards as kb  # Импортируем клавиатуры

import os


# Создаем бота и диспетчер
bot = Bot(TOKEN)
dp = Dispatcher()


# Функция обработки нажатий кнопок
def btn_click(value: str):
    print(value[3:])
    os.system(f'start steam://run/{value[3:]}')


# Обработчик команды /go
@dp.message(Command("go"))
async def start_command(message: Message):
    await message.reply(text="Какую игру запустить", reply_markup=await kb.inline_game())


@dp.callback_query(F.data.startswith('id_'))  # Фильтруем все callback_data
async def process_callback(callback_query: CallbackQuery):
    callback_data = callback_query.data  # Получаем callback_data
    btn_click(callback_data)  # Вызываем функцию с этим значением
    # Обязательно отправляем ответ, иначе кнопка зависнет
    await callback_query.answer(f"Вы нажали: {callback_data}")


# Запуск бота
async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
