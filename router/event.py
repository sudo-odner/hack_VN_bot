from aiogram import Router
from aiogram.types import Message, ReplyKeyboardRemove, KeyboardButton, ReplyKeyboardMarkup
from aiogram.filters import Text

router = Router()
@router.message(Text("Мероприятие"))
async def events(message: Message):
    kb = [
        [KeyboardButton(text="ПИШ")],
        [KeyboardButton(text="Школа 21")],
        [KeyboardButton(text="Физ мат лицей")],
        [KeyboardButton(text="Точка кипения")]
    ]
    keyboard = ReplyKeyboardMarkup(keyboard=kb, resize_keyboard=True)
    await message.answer(text='Выберете что-нибудь:', reply_markup=keyboard)