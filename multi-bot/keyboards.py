from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder

from my_config import game_id




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
    return keyboard.adjust(1).as_markup()
