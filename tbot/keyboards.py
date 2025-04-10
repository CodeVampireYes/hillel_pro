from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder, ReplyKeyboardBuilder


async def show_start_btn():
    keyboard = InlineKeyboardBuilder()
    keyboard.add(InlineKeyboardButton(text='🖥️ Pi5', callback_data="show_pi5"))
    keyboard.add(InlineKeyboardButton(text='🗄️ DB', callback_data="show_db"))
    keyboard.add(InlineKeyboardButton(text=' App', callback_data="show_app"))
    keyboard.add(InlineKeyboardButton(text='📅 График', callback_data="show_schedule"))
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
    keyboard.add(InlineKeyboardButton(text='💻 Состояние Pi5', callback_data="show_pi5_metrics"))
    keyboard.add(InlineKeyboardButton(text='🔄 Reboot', callback_data="show_pi5_reboot"))
    keyboard.add(InlineKeyboardButton(text='🛠️ Update', callback_data="show_pi5_update"))
    keyboard.add(InlineKeyboardButton(text='🔙 Back', callback_data="back_show_menu"))
    return keyboard.adjust(1).as_markup()


async def show_schedule_btn():
    keyboard = InlineKeyboardBuilder()
    keyboard.add(InlineKeyboardButton(text='Мария', callback_data="show_schedule_mariia"))
    keyboard.add(InlineKeyboardButton(text='Артур', callback_data="show_schedule_artur"))
    keyboard.add(InlineKeyboardButton(text='Совместные', callback_data="show_schedule_together"))
    keyboard.add(InlineKeyboardButton(text='🔙 Back', callback_data="back_show_menu"))
    return keyboard.adjust(1).as_markup()


async def show_schedule_month_btn():
    year = ['январь', "февраль", 'Март', 'Апрель', 'Май', 'Июнь', 'Июль', 'Август', 'Сентябрь', 'Октябрь', 'Ноябрь',
            'Декабрь']
    num_month = 1
    keyboard = InlineKeyboardBuilder()
    for month in year:
        keyboard.add(InlineKeyboardButton(text=month, callback_data=f'month_{num_month}'))
        num_month += 1
    return keyboard.adjust(2).as_markup()


async def show_app_btn():
    my_app = ['tbot']
    keyboard = InlineKeyboardBuilder()
    for app in my_app:
        keyboard.add(InlineKeyboardButton(text=app, callback_data=f"show_app_{app}"))

    return keyboard.adjust(1).as_markup()


async def show_app_tbot_update():
    keyboard = InlineKeyboardBuilder()
    keyboard.add(InlineKeyboardButton(text='Update', callback_data=f"show_tbot_app_update"))
    keyboard.add(InlineKeyboardButton(text='🔙 Back', callback_data="show_app"))

    return keyboard.adjust(1).as_markup()