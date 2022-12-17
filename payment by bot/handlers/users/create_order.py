from aiogram import types
import logging
from data.config import ADMINS
from loader import dp, bot
from aiogram.types import CallbackQuery, ContentTypes

from keyboards.inline.product_keys import build_keyboard
from data.praducts import communicator


@dp.message_handler(text="To'lov")
async def invoice(message: types.Message):
    msg = "<b>E-pos systems uchun oylik to'lov</b>\n\n"
    await message.reply_photo(photo="http://telegra.ph//file/6f5e750a2a7300eb9a875.jpg", caption=msg, reply_markup=build_keyboard("invoice"))



@dp.callback_query_handler(text="product:invoice")
async def comunicator_invoice(call: CallbackQuery):
    res = await bot.send_invoice(chat_id=call.from_user.id,
                           **communicator.generate_invoice(),
                           payload="payload:comunicator")
    logging.info(f"{res}")
    await call.answer()
    await call.message.delete()


@dp.pre_checkout_query_handler()
async def process_pre_checkout_query(pre_checkout_query: types.PreCheckoutQuery):
    await bot.answer_pre_checkout_query(pre_checkout_query_id=pre_checkout_query.id,
                                        ok=True)


@dp.message_handler(content_types=ContentTypes.SUCCESSFUL_PAYMENT)
async def process_pos(message: types.Message):
    await bot.send_message(chat_id=message.from_user.id,
                           text="Xaridingiz uchun rahmat!")
    await bot.send_message(chat_id=ADMINS[0],
                           text=f"Quyidagi mahsulot sotildi:\n"
                                f"ID: \n"
                                f"Telegram user:\n"                                
                                f"Xaridor:")
