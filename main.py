from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import Message, CallbackQuery
from keyboards import *
from database import *
from dotenv import load_dotenv
import os


load_dotenv()

TOKEN = os.getenv('TOKEN')

bot = Bot(TOKEN, parse_mode='html')

dp: Dispatcher = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def command_start(message: Message):
    await message.answer(f'Salom ! Abuzar Besh botiga xush kelibsiz !', reply_markup=await main_menu())
    await message.answer('Kategoriyani tanlang  📑 !')


@dp.message_handler(lambda message: 'MENU' in message.text)
async def open_menu(message: Message):
    await message.answer('Kategoriyani tanlang',reply_markup=generate_category_menu())





@dp.message_handler(regexp='1-Manzil 📍')
async def send_location(message: types.Message):
    latitude = 41.280476006242054
    longitude = 69.19760963071913
    await bot.send_location(chat_id=message.chat.id, latitude=latitude, longitude=longitude)


@dp.message_handler(regexp='2-Manzil 📍')
async def send_2_location(message: types.Message):
    latitude = 41.280476006242054
    longitude = 69.19760963071915
    await bot.send_location(chat_id=message.chat.id, latitude=latitude, longitude=longitude)


@dp.callback_query_handler(lambda call: 'category' in call.data)
async def show_products(call:CallbackQuery):
    chat_id =call.message.chat.id
    message_id =call.message.message_id
    _,category_id = call.data.split('_')
    category_id = int(category_id)
    await bot.edit_message_text('Maxsulotni tanlang',chat_id,message_id,reply_markup=products_by_category(category_id))


@dp.callback_query_handler(lambda call: 'main_menu' in call.data)
async def return_to_main_menu(call:CallbackQuery):
    chat_id=call.message.chat.id
    message_id =call.message.message_id
    await bot.edit_message_text(chat_id=chat_id,
                                message_id=message_id,
                                text='Kategoriyani tanlang',
                                reply_markup=generate_category_menu())


@dp.callback_query_handler(lambda call: 'product' in call.data)
async def show_detail_product(call:CallbackQuery):
    chat_id =call.message.chat.id
    message_id = call.message.message_id
    _,product_id = call.data.split('_')
    product_id =int(product_id)

    product = get_product_detail(product_id)
    await bot.delete_message(chat_id,message_id)
    with open(product[-1],mode='rb') as img:
        await bot.send_photo(chat_id=chat_id,photo=img,caption=f'''{product[2]}

Tarif: {product[4]}

Narxi: {product[3]} so`m
Malumot uchun:''')



executor.start_polling(dp)