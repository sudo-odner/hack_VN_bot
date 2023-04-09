import logging
import os
import io
from aiogram import Bot, Dispatcher, types
from aiogram.types import ParseMode
from aiogram.dispatcher.filters import Command, Text
from aiogram.dispatcher import FSMContext
from aiogram.contrib.fsm_storage.memory import MemoryStorage    
logging.basicConfig(level=logging.INFO)
from aiogram.utils import executor
from aiogram.types import InputFile, Message
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

API_TOKEN = '6192900694:AAGh8mvOwOyrT6x4M0hFv5CX9ilNXmloK84' # токен бота
bot = Bot(token=API_TOKEN, parse_mode=ParseMode.HTML)
dp = Dispatcher(bot, storage=MemoryStorage())

@dp.message_handler(Command("start"))
async def cmd_start(message: types.Message):
    """
    Обработчик команды /start. Отправляет приветственное сообщение и кнопки для запуска гида.
    """
    keyboard_markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    #info_button = types.KeyboardButton('Информация')
    info_button = types.KeyboardButton('Выберите язык')
    keyboard_markup.add(info_button)
    await message.answer('Бот гид НТШ\n'
                         'Сайт НТШ - <a href ="https://novtechschool.ru/?ysclid=lg7tljhcuc753613716">перейти</a>.', reply_markup=keyboard_markup, parse_mode='HTML')

@dp.message_handler(Text(equals="Выберите язык"))
async def choose_lang(message: types.Message):

    keyboard_markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    russian = types.KeyboardButton('Русский')
    english = types.KeyboardButton('English')
    keyboard_markup.add(russian, english)
    await message.answer('Выбери язык:', reply_markup=keyboard_markup)


@dp.message_handler(Text(equals="Русский"))
async def if_russian(message: types.Message):
    keyboard_markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    back = types.KeyboardButton('Смена языка')
    info_key = types.KeyboardButton('Перемещение')
    adres_key = types.KeyboardButton('Место положение')
    keyboard_markup.add(info_key,adres_key, back)
    await message.answer('Представленные опции:',reply_markup=keyboard_markup)


@dp.message_handler(Text(equals="English"))
async def if_russian(message: types.Message):
    keyboard_markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    back = types.KeyboardButton('Choose the language')
    info_key = types.KeyboardButton('Movements')
    adres_key = types.KeyboardButton('Address')
    keyboard_markup.add(info_key,adres_key, back)
    await message.answer('Choose:',reply_markup=keyboard_markup)
        

@dp.message_handler(Text(equals="Choose the language"))
async def choose_lang_back(message: types.Message):

    keyboard_markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    russian = types.KeyboardButton('Русский')
    english = types.KeyboardButton('English')
    keyboard_markup.add(russian, english)
    await message.answer('Выбери язык:', reply_markup=keyboard_markup)



@dp.message_handler(Text(equals="Смена языка"))
async def choose_lang_back(message: types.Message):

    keyboard_markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    russian = types.KeyboardButton('Русский')
    english = types.KeyboardButton('English')
    keyboard_markup.add(russian, english)
    await message.answer('Выбери язык:', reply_markup=keyboard_markup)


@dp.message_handler(Text(equals="Место положение"))
async def addres(message: types.Message):
    keyboard_markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    await message.answer('НТШ находится по адресу: Великая ул., 18А, Софийская сторона, Великий Новгород\n <a href ="https://yandex.ru/maps/org/novgorodskaya_tekhnicheskaya_shkola/245430995911/?ll=31.278521%2C58.538530&z=17.03">Смотреть на Яндекс Картах</a>', parse_mode='HTML')

@dp.message_handler(Text(equals="Address"))
async def addres(message: types.Message):
    keyboard_markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    await message.answer('NTSH is located at: Velikaya Street, 18A, Sophia Side, Veliky Novgorod <a href ="https://yandex.ru/maps/org/novgorodskaya_tekhnicheskaya_shkola/245430995911/?ll=31.278521%2C58.538530&z=17.03">View on Yandex Maps</a>', parse_mode='HTML')

@dp.message_handler(Text(equals="Перемещение"))
async def navigation(message: types.Message):
    keyboard_markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    one_days = types.KeyboardButton('Основные места')
    toulets = types.KeyboardButton('Туалеты')
    quiets = types.KeyboardButton('Выходы')
    dop_veshi = types.KeyboardButton('Сервисы')
    back = types.KeyboardButton('Смена языка')
    keyboard_markup.add(one_days, toulets, quiets, dop_veshi, back)
    await message.answer('ч:',reply_markup=keyboard_markup)

@dp.message_handler(Text(equals="Movements"))
async def navigation(message: types.Message):
    keyboard_markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    one_days = types.KeyboardButton('Events')
    toulets = types.KeyboardButton('bathrooms')
    quiets = types.KeyboardButton('exits')
    dop_veshi = types.KeyboardButton('Service areas')
    back = types.KeyboardButton('Choose the languages')
    keyboard_markup.add(one_days, toulets, quiets, dop_veshi, back)
    await message.answer('Choose:',reply_markup=keyboard_markup)





@dp.message_handler(Text(equals="Основные места"))
async def info_of_floors(message: types.Message):
    keyboard_markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    pish= types.KeyboardButton('ПИШ')
    school_21 = types.KeyboardButton('Школа №21')
    phismath_licey = types.KeyboardButton('Физ. Мат. Лицей')
    residents_intc = types.KeyboardButton('Резиденты ИНТЦ')
    point_of_boil = types.KeyboardButton('Точка кипения')
    #publish_zone = types.KeyboardButton('Выставочная зона')
    back = types.KeyboardButton('Смена языка')
    keyboard_markup.add(pish, school_21, phismath_licey, residents_intc, point_of_boil, back)
    await message.answer('Выберите зону:', reply_markup=keyboard_markup)


@dp.message_handler(Text(equals="Events"))
async def info_of_floors(message: types.Message):
    keyboard_markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    pish= types.KeyboardButton('PISH')
    school_21 = types.KeyboardButton('School №21')
    phismath_licey = types.KeyboardButton('Phys. Math. Lyceum')
    residents_intc = types.KeyboardButton('INTC Residents')
    point_of_boil = types.KeyboardButton('Boiling Point')
    #publish_zone = types.KeyboardButton('Выставочная зона')
    back = types.KeyboardButton('Choose the languages')
    keyboard_markup.add(pish, school_21, phismath_licey, residents_intc, point_of_boil, back)
    await message.answer('Choose:', reply_markup=keyboard_markup)



@dp.message_handler(Text(equals="ПИШ"))
async def send_image_1(message: types.Message):
    photo = InputFile('2 этаж/ПИШ.png')
    photo_1 = InputFile('1 этаж/ПИШ.png')
    await bot.send_photo(chat_id=message.from_user.id, photo=photo_1, caption='Нахождение ПИШ в планировке здания на первом этаже')
    await bot.send_photo(chat_id=message.from_user.id, photo=photo, caption='Нахождение ПИШ в планировке здания на втором этаже')

@dp.message_handler(Text(equals="PISH"))
async def send_image_1(message: types.Message):
    photo = InputFile('2 этаж/ПИШ.png')
    photo_1 = InputFile('1 этаж/ПИШ.png')
    await bot.send_photo(chat_id=message.from_user.id, photo=photo_1, caption='Locating the NSP in the building layout on the first floor')
    await bot.send_photo(chat_id=message.from_user.id, photo=photo, caption='Finding the NSP in the layout of the building on the second floor')


@dp.message_handler(Text(equals="Школа №21"))
async def send_image_2(message: types.Message):
    photo = InputFile('1 этаж/Школа 21.png')
    await bot.send_photo(chat_id=message.from_user.id, photo=photo, caption='Нахождение Школы №21 в планировке здания') 

@dp.message_handler(Text(equals="School №21"))
async def send_image_2(message: types.Message):
    photo = InputFile('1 этаж/Школа 21.png')
    await bot.send_photo(chat_id=message.from_user.id, photo=photo, caption='Finding School No. 21 in the layout of the building')

@dp.message_handler(Text(equals="Физ. Мат. Лицей"))
async def send_image_3(message: types.Message):
    photo = InputFile('1 этаж/Физ. мат. лицей.png')
    photo_1 = InputFile('2 этаж/Физ. мат. лицей.png')
    await bot.send_photo(chat_id=message.from_user.id, photo=photo, caption='Нахождение Физ. Мат. Лицея в планировке здания на первом этаже') 
    await bot.send_photo(chat_id=message.from_user.id, photo=photo_1, caption='Нахождение Физ. Мат. Лицея в планировке здания на втором этаже') 

@dp.message_handler(Text(equals="Phys. Math. Lyceum"))
async def send_image_3(message: types.Message):
    photo = InputFile('1 этаж/Физ. мат. лицей.png')
    photo_1 = InputFile('2 этаж/Физ. мат. лицей.png')
    await bot.send_photo(chat_id=message.from_user.id, photo=photo, caption='Finding the Phys. Math. Lyceum in the layout of the building on the first floor') 
    await bot.send_photo(chat_id=message.from_user.id, photo=photo_1, caption='Finding the Phys. Math. Lyceum in the layout of the building on the second floor') 


@dp.message_handler(Text(equals="Резиденты ИНТЦ"))
async def send_image_4(message: types.Message):
    photo_1 = InputFile('2 этаж/Резиденты ИНТЦ.png')
    await bot.send_photo(chat_id=message.from_user.id, photo=photo_1, caption='Нахождение Резидентов ИНТЦ в планировке здания на втором этаже') 

@dp.message_handler(Text(equals="INTC Residents"))
async def send_image_4(message: types.Message):
    photo_1 = InputFile('2 этаж/Резиденты ИНТЦ.png')
    await bot.send_photo(chat_id=message.from_user.id, photo=photo_1, caption='Locating INTC Residents in the building layout on the second floor')     

@dp.message_handler(Text(equals="Точка кипения"))
async def send_image_5(message: types.Message):
    photo = InputFile('1 этаж/Точка кипения.png')
    photo_1 = InputFile('2 этаж/Точка кипения.png')
    await bot.send_photo(chat_id=message.from_user.id, photo=photo_1, caption='Нахождение Точки кипения в планировке здания на втором этаже')
    await bot.send_photo(chat_id=message.from_user.id, photo=photo, caption='Нахождение Точки кипения в планировке здания на первом этаже')  

@dp.message_handler(Text(equals="Boiling Point"))
async def send_image_5(message: types.Message):
    photo = InputFile('1 этаж/Точка кипения.png')
    photo_1 = InputFile('2 этаж/Точка кипения.png')
    await bot.send_photo(chat_id=message.from_user.id, photo=photo_1, caption='Finding the Boiling Point in the Building Layout on the Second Floor')
    await bot.send_photo(chat_id=message.from_user.id, photo=photo, caption='Finding the Boiling Point in the Building Layout on the Ground Floor')  


@dp.message_handler(Text(equals="Туалеты"))
async def send_image_7(message: types.Message):
    photo = InputFile('2 этаж/Туалет.png')
    photo_1 = InputFile('1 этаж/Туалет.png')
    await bot.send_photo(chat_id=message.from_user.id, photo=photo_1, caption='Нахождение туалета в планировке здания на первом этаже')
    await bot.send_photo(chat_id=message.from_user.id, photo=photo, caption='Нахождение туалета в планировке здания на втором этаже')

@dp.message_handler(Text(equals="Toilet locations"))
async def send_image_7(message: types.Message):
    photo = InputFile('2 этаж/Туалет.png')
    photo_1 = InputFile('1 этаж/Туалет.png')
    await bot.send_photo(chat_id=message.from_user.id, photo=photo_1, caption='Locating the toilet in the layout of the building on the first floor')
    await bot.send_photo(chat_id=message.from_user.id, photo=photo, caption='Locating the toilet in the layout of the building on the second floor')



@dp.message_handler(Text(equals="Выходы"))
async def send_image_8(message: types.Message):
    photo_1 = InputFile('1 этаж/Выход-Вход.png')
    await bot.send_photo(chat_id=message.from_user.id, photo=photo_1, caption='Нахождение выхода/входа в планировке здания на первом этаже')

@dp.message_handler(Text(equals="exits"))
async def send_image_8(message: types.Message):
    photo_1 = InputFile('1 этаж/Выход-Вход.png')
    await bot.send_photo(chat_id=message.from_user.id, photo=photo_1, caption='Finding an exit/entrance in the building layout on the first floor')



@dp.message_handler(Text(equals="Сервисы"))
async def navigation(message: types.Message):
    keyboard_markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    hall = types.KeyboardButton('Холл')
    voice_hall = types.KeyboardButton('Переговорные')
    halerelya = types.KeyboardButton('Галерея')
    amphtheatre = types.KeyboardButton('Амфитеатр')
    zal_trans = types.KeyboardButton('Зал-трансформер')
    back = types.KeyboardButton('Choose the languages')
    keyboard_markup.add(hall,voice_hall, halerelya, amphtheatre, zal_trans, back)
    await message.answer('Choose:',reply_markup=keyboard_markup)

@dp.message_handler(Text(equals="Service areas"))
async def navigation(message: types.Message):
    keyboard_markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    hall = types.KeyboardButton('Hall')
    voice_hall = types.KeyboardButton('Negotiations')
    halerelya = types.KeyboardButton('Gallery')
    amphtheatre = types.KeyboardButton('Amphitheater')
    zal_trans = types.KeyboardButton('Transformer Room')
    back = types.KeyboardButton('Choose the languages')
    keyboard_markup.add(hall,voice_hall, halerelya, amphtheatre, zal_trans, back)
    await message.answer('Choose:',reply_markup=keyboard_markup)



@dp.message_handler(Text(equals="Холл"))
async def send_image_9(message: types.Message):
    photo_1 = InputFile('1 этаж/Хол.png')
    await bot.send_photo(chat_id=message.from_user.id, photo=photo_1, caption='Нахождение хола в планировке здания на первом этаже')

@dp.message_handler(Text(equals="Hall"))
async def send_image_9(message: types.Message):
    photo_1 = InputFile('1 этаж/Хол.png')
    await bot.send_photo(chat_id=message.from_user.id, photo=photo_1, caption='Locating the hall in the building layout on the first floor')

@dp.message_handler(Text(equals="Переговорные"))
async def send_image_10(message: types.Message):
    photo_1 = InputFile('2 этаж/4 переговорные.png')
    await bot.send_photo(chat_id=message.from_user.id, photo=photo_1, caption='Нахождение хола в планировке здания на втором этаже')

@dp.message_handler(Text(equals="Negotiations"))
async def send_image_10(message: types.Message):
    photo_1 = InputFile('2 этаж/4 переговорные.png')
    await bot.send_photo(chat_id=message.from_user.id, photo=photo_1, caption='Locating the hall in the building layout on the second floor')

@dp.message_handler(Text(equals="Галерея"))
async def send_image_11(message: types.Message):
    photo_1 = InputFile('2 этаж/Галерея.png')
    await bot.send_photo(chat_id=message.from_user.id, photo=photo_1, caption='Нахождение Галереи в планировке здания на втором этаже')

@dp.message_handler(Text(equals="Gallery"))
async def send_image_11(message: types.Message):
    photo_1 = InputFile('2 этаж/Галерея.png')
    await bot.send_photo(chat_id=message.from_user.id, photo=photo_1, caption='Finding the Gallery in the layout of the building on the second floor')

@dp.message_handler(Text(equals="Амфитеатр"))
async def send_image_11(message: types.Message):
    photo_1 = InputFile('1 этаж/Амфитеатр.png')
    await bot.send_photo(chat_id=message.from_user.id, photo=photo_1, caption='Нахождение Амфитеатра в планировке здания на первом этаже')

@dp.message_handler(Text(equals="Amphitheater"))
async def send_image_11(message: types.Message):
    photo_1 = InputFile('1 этаж/Амфитеатр.png')
    await bot.send_photo(chat_id=message.from_user.id, photo=photo_1, caption='Finding the Amphitheater in the layout of the building on the first floor')

@dp.message_handler(Text(equals="Зал-трансформер"))
async def send_image_11(message: types.Message):
    photo_1 = InputFile('2 этаж/Трансформер зал.png')
    photo = InputFile('1 этаж/Трансформер зал.png')
    await bot.send_photo(chat_id=message.from_user.id, photo=photo_1, caption='Нахождение Зала-трансформера в планировке здания на втором этаже')
    await bot.send_photo(chat_id=message.from_user.id, photo=photo, caption='Нахождение Зала-трансформера в планировке здания на первом этаже')

@dp.message_handler(Text(equals="Transformer Room"))
async def send_image_11(message: types.Message):
    photo_1 = InputFile('2 этаж/Трансформер зал.png')
    photo = InputFile('1 этаж/Трансформер зал.png')
    await bot.send_photo(chat_id=message.from_user.id, photo=photo_1, caption='Finding the Transformer Room in the layout of the building on the second floor')
    await bot.send_photo(chat_id=message.from_user.id, photo=photo, caption='Finding the Transformer Room in the building layout on the first floor')    





if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)