from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

meny_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="🛍Menu"),
            KeyboardButton(text="💾Info"),
        ],
    ],
    resize_keyboard=True
)