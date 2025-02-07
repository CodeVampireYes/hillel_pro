from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder

from config import game_id
from my_calendar import together_list, together_weekend

together_weekend()
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


async def together_week():
    keyboard = InlineKeyboardBuilder()
    i = 0
    for week in together_list:
        keyboard.add(InlineKeyboardButton(text=week, callback_data='together'))
        i += 1
        if i == 10:
            break
    return keyboard.adjust(1).as_markup()