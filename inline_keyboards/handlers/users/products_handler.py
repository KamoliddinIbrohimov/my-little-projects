from aiogram import types

from keyboards.inline.callback_data import course_callback, book_callback
from loader import dp
import logging
from keyboards.inline.products_keyboard import products_keyboard, course_menu, book_menu, telegram_keyboard


@dp.callback_query_handler(text="back")
async def back(call: types.CallbackQuery):
    """Back button"""
    callback_data = call.data
    logging.info(f"{callback_data=}")
    logging.info(f"{call.from_user.id=}")
    await call.message.edit_reply_markup(reply_markup=products_keyboard)
    await call.answer(cache_time=60)


@dp.message_handler(text="🛍Menu")
async def menu(message: types.Message):
    """Take the user to the menu"""
    await message.answer("Choose", reply_markup=products_keyboard)
    await message.delete()


@dp.callback_query_handler(text="course")
async def course(call: types.CallbackQuery):
    """Course is a function that generates menus"""
    await call.message.edit_reply_markup(reply_markup=course_menu)
    await call.answer(cache_time=60)


@dp.callback_query_handler(text="books")
async def books(call: types.CallbackQuery):
    """Book is a function that generates menus"""
    callback_data = call.data
    logging.info(f"{callback_data=}")
    logging.info(f"{call.from_user.id=}")
    await call.message.answer("Books", reply_markup=book_menu)
    await call.message.delete()
    await call.answer(cache_time=60)


@dp.callback_query_handler(course_callback.filter(item_name="telegram_bot"))
async def telegram(call: types.CallbackQuery, callback_data: dict):
    """Telegram bot is a function that generates menus"""
    logging.info(f'{callback_data=}')
    await call.message.answer("You have selected the telegram bot course", reply_markup=telegram_keyboard)
    await call.answer(cache_time=60)


@dp.callback_query_handler(book_callback.filter(item_name="python_book"))
async def python_book(call: types.CallbackQuery, callback_data: dict):
    logging.info(f"{callback_data=}")
    await call.answer("Your order has been accepted😉", cache_time=60, show_alert=True)







