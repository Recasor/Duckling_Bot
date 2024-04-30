from aiogram.types import KeyboardButton, ReplyKeyboardMarkup
from aiogram.utils.keyboard import ReplyKeyboardBuilder
from lexicon.lexicon import LEXICON_RU

duckling_mode_button = KeyboardButton(text=LEXICON_RU['duckling_mode_button'])
unusual_information_button = KeyboardButton(text=LEXICON_RU['unusual_information_button'])

start_keybord_builder = ReplyKeyboardBuilder()
start_keybord_builder.row(duckling_mode_button, unusual_information_button, width=2)

start_keybord: ReplyKeyboardMarkup = start_keybord_builder.as_markup(
    one_time_keyboard=True,
    resize_keyboard=True
)
