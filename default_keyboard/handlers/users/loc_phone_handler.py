from aiogram import types
from loader import dp

from keyboards.default.loc_phon_keyboard import loc_phone


@dp.message_handler(text="💾Info")
async def loc_phone_info(message: types.Message):
    """"""
    await message.delete()
    await message.answer("Send your phone number and location", reply_markup=loc_phone)