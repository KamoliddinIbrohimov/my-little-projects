from aiogram import types
from loader import dp

from keyboards.default.loc_phon_keyboard import loc_phone
from keyboards.default.menu_keyboard import menu_keyboard


@dp.message_handler(text="💾Info")
async def loc_phone_info(message: types.Message):
    """Request the user location and phone number"""
    await message.delete()
    await message.answer("Send your phone number and location", reply_markup=loc_phone)


@dp.message_handler(text="◀️Back")
async def back(message: types.Message):
    """Return to menu"""
    msg = await message.answer("Menu", reply_markup=menu_keyboard)
    await message.delete()
