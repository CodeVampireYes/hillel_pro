from aiogram import Router, F
from aiogram.types import CallbackQuery
from db import get_token_setting_tbot

import keyboards as kb
from utils import pi5

import aiosqlite


router = Router()  # Используем Router для удобной регистрации обработчиков


@router.callback_query(F.data == "show_db")
async def callback_show_db_btn(callback: CallbackQuery):
    keyboard = await kb.show_db_btn()
    await callback.message.edit_text('DB Menu: ', reply_markup=keyboard)
    await callback.answer()


@router.callback_query(F.data == "show_db_users")
async def callback_show_db__users_btn(callback: CallbackQuery):
    keyboard = await kb.show_db_users_btn()
    await callback.message.edit_text('DB-users: ', reply_markup=keyboard)
    await callback.answer()


@router.callback_query(F.data == "back_show_menu")
async def callback_show_menu_btn(callback: CallbackQuery):
    keyboard = await kb.show_start_btn()
    await callback.message.edit_text('Menu: ', reply_markup=keyboard)
    await callback.answer()


@router.callback_query(F.data == "show_db_users_username")
async def callback_show_db_users_btn(callback: CallbackQuery):
    async with aiosqlite.connect('example.db') as db:
        async with db.execute("SELECT username, user_id FROM users") as cursor:
            all_users = await cursor.fetchall()
        await db.commit()

    keyboard = await kb.show_db_users_username_btn(all_users)
    await callback.message.edit_text('Name users: ', reply_markup=keyboard)
    await callback.answer()


@router.callback_query(F.data.startswith("show_db_users_username_"))
async def callback_show_db_users_username_btn(callback: CallbackQuery):
    user_id = int(callback.data.replace('show_db_users_username_', ''))
    async with aiosqlite.connect('example.db') as db:
        async with db.execute("SELECT * FROM users WHERE user_id = ?", (user_id,)) as cursor:
           result = await cursor.fetchone()
        await db.commit()

    await callback.message.edit_text(f"""
    user_id: {result[0]}
    first_name: {result[1]}
    last_name: {result[2]}
    username: {result[3]}
    language_code: {result[4]}
    is_bot: {result[5]}
    """)
    await callback.answer()


@router.callback_query(F.data == "show_pi5")
async def show_pi5_metrics_btn(callback: CallbackQuery):
    pi5.cpu_temp()
    keyboard = await kb.show_pi5_btn()
    await callback.message.edit_text('Pi5: ', reply_markup=keyboard)
    await callback.answer()