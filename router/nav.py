from aiogram import Router
from aiogram.types import Message, ReplyKeyboardRemove, KeyboardButton, ReplyKeyboardMarkup
from aiogram.filters import Text

router = Router()

@router.message(Text("Навигация"))
async def nav(message:Message):
    kb = [
        [KeyboardButton(text="Общая карта")],
        [KeyboardButton(text="Мероприятие")],
        [KeyboardButton(text="Коллектив")],
        [KeyboardButton(text="Туалеты")],
        [KeyboardButton(text="Выходы")],
        [KeyboardButton(text="Дополнительно")]
    ]
    keyboard = ReplyKeyboardMarkup(keyboard=kb, resize_keyboard=True)
    await message.answer(text='Выберете что-нибудь:', reply_markup=keyboard)