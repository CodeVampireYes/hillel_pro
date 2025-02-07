from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder
from config import game_id


async def inline_game():
    keyboard = InlineKeyboardBuilder()
    for game in game_id:
        game_name = game[0]
        id_game = game[1]
        keyboard.add(InlineKeyboardButton(text=game_name, callback_data=f'id_{id_game}'))
    return keyboard.adjust(1).as_markup()
