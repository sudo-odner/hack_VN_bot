import types

from aiogram import Router, Bot, Dispatcher
from aiogram.filters import Command, Text
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, ReplyKeyboardRemove
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

router = Router()

@router.message(Command("languages"))
async def cmd_languages(message: Message):
    kb = [
        [
         KeyboardButton(text="С пюрешкой"),
         KeyboardButton(text="Без пюрешки")
        ]
    ]
    keyboard = ReplyKeyboardMarkup(keyboard=kb, resize_keyboard=True)

    await message.answer("Как подавать котлеты?", reply_markup=keyboard)

