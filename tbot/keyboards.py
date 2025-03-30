from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder, ReplyKeyboardBuilder


async def show_start_btn():
    keyboard = InlineKeyboardBuilder()
    keyboard.add(InlineKeyboardButton(text='🖥️ Pi5', callback_data="show_pi5"))
    keyboard.add(InlineKeyboardButton(text='🗄️ DB', callback_data="show_db"))
    return keyboard.adjust(1).as_markup()


async def show_db_btn():
    keyboard = InlineKeyboardBuilder()
    keyboard.add(InlineKeyboardButton(text='⚙️ Setting bot', callback_data="show_db_setting_tbot"))
    keyboard.add(InlineKeyboardButton(text='👤 Users', callback_data="show_db_users"))
    keyboard.add(InlineKeyboardButton(text='🔙 Back', callback_data="back_show_menu"))
    return keyboard.adjust(1).as_markup()


async def show_db_users_btn():
    keyboard = InlineKeyboardBuilder()
    keyboard.add(InlineKeyboardButton(text='👥 Показать пользователей', callback_data="show_db_users_username"))
    keyboard.add(InlineKeyboardButton(text='🔙 Back', callback_data="show_db"))
    return keyboard.adjust(1).as_markup()


async def show_db_users_username_btn(all_users: list):
    keyboard = InlineKeyboardBuilder()
    for user in all_users:
        keyboard.add(InlineKeyboardButton(text=user[0], callback_data=f'show_db_users_username_{user[1]}'))
    keyboard.add(InlineKeyboardButton(text='🔙 Back', callback_data="show_db_users"))
    return keyboard.adjust(1).as_markup()


async def show_db_setting_tbot_btn():
    pass


async def show_pi5_btn():
    keyboard = InlineKeyboardBuilder()
    keyboard.add(InlineKeyboardButton(text='Состояние Pi5', callback_data="show_pi5_metrics"))
    keyboard.add(InlineKeyboardButton(text='Reboot', callback_data="show_pi5_reboot"))
    keyboard.add(InlineKeyboardButton(text='Update', callback_data="show_pi5_update"))
    keyboard.add(InlineKeyboardButton(text='🔙 Back', callback_data="back_show_menu"))
    return keyboard.adjust(1).as_markup()


