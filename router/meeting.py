from aiogram import Router
from aiogram.types import Message, ReplyKeyboardRemove, KeyboardButton, ReplyKeyboardMarkup
from aiogram.filters import Text

router = Router()

@router.message(Text("Коллектив"))
async def meeting(message: Message):
    kb = [
        [
            KeyboardButton(text="Амфитеатр"),
            KeyboardButton(text="Зал трансформер"),
            KeyboardButton(text="Галерея")
        ]
    ]
    keyboard = ReplyKeyboardMarkup(keyboard=kb, resize_keyboard=True)
    await message.answer(text='Выберете что-нибудь:', reply_markup=keyboard)