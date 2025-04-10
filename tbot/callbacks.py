from aiogram import Router, F
from aiogram.types import CallbackQuery, FSInputFile
from db import get_token_setting_tbot

import keyboards as kb
from utils import pi5
from utils.my_calendar import generate_calendar

import aiosqlite
import subprocess


router = Router()  # Используем Router для удобной регистрации обработчиков


@router.callback_query(F.data == "show_db")
async def callback_show_db_btn(callback: CallbackQuery):
    keyboard = await kb.show_db_btn()
    await callback.message.edit_text('          DB Menu          ', reply_markup=keyboard)
    await callback.answer()


@router.callback_query(F.data == "show_db_users")
async def callback_show_db__users_btn(callback: CallbackQuery):
    keyboard = await kb.show_db_users_btn()
    await callback.message.edit_text('DB-users: ', reply_markup=keyboard)
    await callback.answer()


@router.callback_query(F.data == "back_show_menu")
async def callback_show_menu_btn(callback: CallbackQuery):
    keyboard = await kb.show_start_btn()
    await callback.message.edit_text('           Menu:            ', reply_markup=keyboard)
    await callback.answer()


@router.callback_query(F.data == "show_db_setting_tbot")
async def show_db_setting_tbot(callback: CallbackQuery):
    async with aiosqlite.connect('example.db') as db:
        async with db.execute("SELECT * FROM setting_tbot") as cursor:
            data = await cursor.fetchall()
        await db.commit()

    await callback.message.edit_text(f"""
        id: {data[0][0]}
        token: {data[0][1]}
        create_calendar: {data[0][2]}
        
        """)
    await callback.answer()


@router.callback_query(F.data == "show_db_users_username")
async def callback_show_db_users_btn(callback: CallbackQuery):
    async with aiosqlite.connect('example.db') as db:
        async with db.execute("SELECT username, user_id FROM users") as cursor:
            all_users = await cursor.fetchall()
        await db.commit()

    keyboard = await kb.show_db_users_username_btn(all_users)
    await callback.message.edit_text('        Name users:        ', reply_markup=keyboard)
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
    keyboard = await kb.show_pi5_btn()
    await callback.message.edit_text('             Pi5:             ', reply_markup=keyboard)
    await callback.answer()


@router.callback_query(F.data == "show_pi5_metrics")
async def show_pi5_metrics_btn(callback: CallbackQuery):
    result = pi5.get_metrics_pi5()

    await callback.message.edit_text(result)
    await callback.answer()


@router.callback_query(F.data == "show_pi5_update")
async def show_pi5_metrics_btn(callback: CallbackQuery):
    await callback.message.answer("🔄 Начинаю обновление бота...")

    result = subprocess.run(
        ["/mnt/ssd2/hillel_pro/tbot/terminal/update.sh"],
        capture_output=True,
        text=True
    )
    await callback.message.answer(f"✅ Обновление завершено!")
    # Закрываем инлайн-уведомление (чтобы не висело)
    await callback.answer()


@router.callback_query(F.data == "show_pi5_reboot")
async def show_pi5_metrics_btn(callback: CallbackQuery):
    await callback.message.answer("🔄 Начинаю перезагрузку...")

    try:
        # Выполняем скрипт
        result = subprocess.run(
            ["/mnt/ssd2/hillel_pro/tbot/terminal/reboot_pi5.sh"],
            capture_output=True,
            text=True,
            check=True  # Поднимет исключение в случае ошибки
        )
        # Проверяем результат выполнения
        if result.returncode == 0:
            await callback.message.answer("✅ Перезагрузка прошла успешно!")
        else:
            await callback.message.answer(f"⚠️ Ошибка при перезагрузке: {result.stderr}")

    except subprocess.CalledProcessError as e:
        # Обработка ошибок
        await callback.message.answer(f"❌ Ошибка при выполнении скрипта: {e}")

    except Exception as e:
        # Обработка других непредвиденных ошибок
        await callback.message.answer(f"❌ Произошла непредвиденная ошибка: {e}")

    # Закрываем инлайн-уведомление
    await callback.answer()


@router.callback_query(F.data == "show_schedule")
async def show_schedule_btn(callback: CallbackQuery):
    keyboard = await kb.show_schedule_btn()
    await callback.message.edit_text('График для:', reply_markup=keyboard)
    await callback.answer()


@router.callback_query(F.data == "show_schedule_mariia")
async def show_schedule_mariia_btn(callback: CallbackQuery):
    async with aiosqlite.connect('example.db') as db:
        await db.execute("UPDATE setting_tbot SET create_calendar = ? WHERE id = 1", ('mariia',))
        await db.commit()

    keyboard = await kb.show_schedule_month_btn()
    await callback.message.edit_text('Календарь для Марии', reply_markup=keyboard)
    await callback.answer()


@router.callback_query(F.data == "show_schedule_artur")
async def show_schedule_artur_btn(callback: CallbackQuery):
    async with aiosqlite.connect('example.db') as db:
        await db.execute("UPDATE setting_tbot SET create_calendar = ? WHERE id = 1", ('artur',))
        await db.commit()

    keyboard = await kb.show_schedule_month_btn()
    await callback.message.edit_text('Календарь для Артура', reply_markup=keyboard)
    await callback.answer()


@router.callback_query(F.data.startswith('month_'))
async def press_month(callback_query: CallbackQuery):
    number_month = int(callback_query.data.replace('month_', ''))

    await callback_query.message.edit_reply_markup(reply_markup=None)
    # Используем await для генерации календаря
    filename = await generate_calendar(number_month)

    photo = FSInputFile(filename)
    await callback_query.message.answer_photo(photo)

    await callback_query.answer()


@router.callback_query(F.data == 'show_app')
async def press_month(callback_query: CallbackQuery):
    keyboard = await kb.show_app_btn()

    await callback_query.message.edit_text('My app', reply_markup=keyboard)
    await callback_query.answer()


@router.callback_query(F.data == 'show_app_tbot')
async def press_month(callback_query: CallbackQuery):
    keyboard = await kb.show_app_tbot_update()

    await callback_query.message.edit_text('tbot', reply_markup=keyboard)
    await callback_query.answer()


@router.callback_query(F.data == "show_tbot_app_update")
async def show_app_tbot_update_btn(callback: CallbackQuery):
    await callback.message.answer("🔄 Начинаю перезагрузку...")

    try:
        # Выполняем скрипт
        result = subprocess.run(
            ["/mnt/ssd2/hillel_pro/tbot/terminal/reboot_pi5.sh"],
            capture_output=True,
            text=True,
            check=True  # Поднимет исключение в случае ошибки
        )
        # Проверяем результат выполнения
        if result.returncode == 0:
            await callback.message.answer("✅ Перезагрузка прошла успешно!")
        else:
            await callback.message.answer(f"⚠️ Ошибка при перезагрузке: {result.stderr}")

    except subprocess.CalledProcessError as e:
        # Обработка ошибок
        await callback.message.answer(f"❌ Ошибка при выполнении скрипта: {e}")

    except Exception as e:
        # Обработка других непредвиденных ошибок
        await callback.message.answer(f"❌ Произошла непредвиденная ошибка: {e}")

    # Закрываем инлайн-уведомление
    await callback.answer()