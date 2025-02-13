from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup, KeyboardButton
from database import *


async def main_menu():
    return ReplyKeyboardMarkup([
        [KeyboardButton(text='MENU')],
        [KeyboardButton(text='1-Manzil 📍'), KeyboardButton(text='2-Manzil 📍')]

    ], resize_keyboard=True)


def generate_category_menu():
    markup = InlineKeyboardMarkup(row_width=2)

    categories = get_all_categories()
    buttons = []
    for category in categories:
        btn = InlineKeyboardButton(text=category[1], callback_data=f'category_{category[0]}')
        buttons.append(btn)
    markup.add(*buttons)
    return markup


def products_by_category(category_id):
    markup = InlineKeyboardMarkup(row_width=2)
    products = get_products_by_category_id(category_id)
    buttons = []
    for product in products:
        btn = InlineKeyboardButton(text=product[1], callback_data=f'product_{product[0]}')
        buttons.append(btn)
    markup.add(*buttons)
    markup.row(
        InlineKeyboardButton(text='🔙 Ortga',callback_data='main_menu')
    )
    return markup
