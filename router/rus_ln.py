from aiogram import Router
from aiogram.types import Message, ReplyKeyboardRemove, KeyboardButton, ReplyKeyboardMarkup
from aiogram.filters import Text

router = Router()
const = 'Привет, Snikky☕️!😊Я бот-справочник о городе Иннополис!😉 Если ты не нашел нужной информации, то можешь позвонить в Консьерж-сервис:☎️: 8-800-222-22-87📩: helpme@innopolis.rutelegram: @InnopolisHelp!'
@router.message(Text("Русский"))
async def rus_lang(message: Message):
    kb = [
        [
            KeyboardButton(text="Навигация"),
            KeyboardButton(text="Адрес")
        ]
    ]
    keyboard = ReplyKeyboardMarkup(keyboard=kb, resize_keyboard=True)
    await message.answer(text = const, reply_markup = keyboard)