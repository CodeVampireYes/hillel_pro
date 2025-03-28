import aiosqlite

from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command

import keyboards as kb

router = Router()


@router.message(Command("start"))
async def cmd_start_command(message: Message):
    user_id = message.from_user.id
    first_name = message.from_user.first_name
    last_name = message.from_user.last_name
    username = message.from_user.username
    language_code = message.from_user.language_code
    is_bot = message.from_user.is_bot

    if is_bot:
        is_bot = 1
    else:
        is_bot = 0

    async with aiosqlite.connect('example.db') as db:
        await db.execute("""
            INSERT OR REPLACE INTO users (
            user_id, first_name, last_name, username, language_code, is_bot) 
            VALUES (?, ?, ?, ?, ?, ?)
        """, (user_id, first_name, last_name, username, language_code, is_bot))
        await db.commit()

    await message.answer("Menu:", reply_markup=await kb.show_start_btn())
    await message.delete()

