from aiogram import Router
from aiogram.types import Message, ReplyKeyboardRemove, KeyboardButton, ReplyKeyboardMarkup, InlineKeyboardMarkup, \
    InlineKeyboardButton
from aiogram.filters import Text

router = Router()

@router.message(Text("Туалеты"))
async def tualet(message: Message):
    await message.answer(text='1 этаж')
    await message.answer_photo(photo=open('assets/tualet.png', 'rb'), caption="here's an image!")

