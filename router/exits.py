from aiogram import Router
from aiogram.types import Message, ReplyKeyboardRemove, KeyboardButton, ReplyKeyboardMarkup
from aiogram.filters import Text

router = Router()

@router.message(Text("Выходы"))
async def exists(message:Message):
    await message.answer(text='1 фотка')
    await message.answer(text='2 фотка')
