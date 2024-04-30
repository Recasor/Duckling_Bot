from aiogram.types import Message
from aiogram.filters import Command
from aiogram import Router
from aiogram import F

from lexicon.lexicon import LEXICON_RU, PHRASES_LIST
from keybords.keyboards import start_keybord
from random import choice

router = Router()
duckling_mode = False

@router.message(Command(commands=['start']))
async def start_message_process(message: Message):
    await message.answer(text=LEXICON_RU['/start'], reply_markup=start_keybord)


@router.message(Command(commands=['help']))
async def help_message_process(message: Message):
    await message.answer(text=LEXICON_RU['/help'])


@router.message(F.text == LEXICON_RU['duckling_mode_button'])
async def start_duck_message_process(message: Message):
    await message.answer(text=LEXICON_RU['duckling_mode_text'])



@router.message()
async def random_duck_message_process(message: Message):
    if duckling_mode:
        await message.answer(text=PHRASES_LIST.choice())
    else:
        await message.answer(text=message.text)
