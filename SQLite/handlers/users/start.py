from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart

from loader import dp, db, bot
from data.config import ADMINS
import sqlite3


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    name = message.from_user.full_name
    id = message.from_user.id
    try:
        db.add_user(id=id,
                    name=name)
    except sqlite3.IntegrityError as err:
        pass

    count = db.count_users()[0]
    await message.answer(f"Hello, {message.from_user.full_name}!")


    msg = f"{name} bazaga qo'shildi.\nBazada {count} ta foydalanuvchi bor."
    await bot.send_message(chat_id=ADMINS[0], text=msg)

# import sqlite3
#
# from aiogram import types
# from aiogram.dispatcher.filters.builtin import CommandStart
#
# from data.config import ADMINS
# from loader import dp, db, bot


# @dp.message_handler(CommandStart())
# async def bot_start(message: types.Message):
#     name = message.from_user.full_name
#     # Foydalanuvchini bazaga qo'shamiz
#     try:
#         db.add_user(id=id,
#                     name=name)
#     except sqlite3.IntegrityError as err:
#         await bot.send_message(chat_id=ADMINS[0], text=err)

    # await message.answer("Xush kelibsiz!")
    # # Adminga xabar beramiz
    # count = db.count_users()[0]
    # msg = f"{message.from_user.full_name} bazaga qo'shildi.\nBazada {count} ta foydalanuvchi bor."
    # await bot.send_message(chat_id=ADMINS[0], text=msg)