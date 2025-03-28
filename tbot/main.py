import asyncio
import datetime

from aiogram import Bot, Dispatcher
from aiogram.types import BotCommand

import handlers
import callbacks
from db import *


async def main():
    commands = [
        BotCommand(command="/start", description="Start the bot"),
    ]

    async def set_commands(bot: Bot):
        await bot.set_my_commands(commands)

    await init_db_setting_tbot()
    await init_db_users()

    TOKEN = await get_token_setting_tbot(1)  # Теперь вызываем внутри async функции
    if not TOKEN:
        print("Ошибка: токен не найден в базе данных.")
        return

    bot = Bot(token=TOKEN)

    # Создаем диспетчер и передаем bot в качестве аргумента
    dp = Dispatcher()

    # Регистрируем обработчики
    dp.include_router(handlers.router)
    dp.include_router(callbacks.router)

    await set_commands(bot)

    print("Бот запущен!")
    try:
        # Запуск бота для обработки обновлений
        await dp.start_polling(bot)
    except Exception as e:
        print(f"Ошибка при запуске polling: {e}")
    finally:
        # Закрытие сессии бота
        await bot.close()

if __name__ == "__main__":
    asyncio.run(main())
