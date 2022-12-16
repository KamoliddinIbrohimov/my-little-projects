from aiogram import types
from loader import dp


@dp.message_handler(commands="info_html")
async def html_texts(message: types.Message):
    await message.answer(f"Hello {message.from_user.full_name}!\n")
    text = "This is <b> bold text</b>\n"
    text += "This is <i>italic text</i>\n"
    text += "This is <u>underlined text</u>\n"
    text += "This is <s>deleted text</s>\n"
    text += "This is <a href='https://mohirdev.uz/courses/telegram/lesson/matnlarni-formatlash/'>Link text</a>\n"
    text += "This is <code>print('Hello world')</code> code\n"

    await message.answer(text)

