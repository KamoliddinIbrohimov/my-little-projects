from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

menu_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="🛍Menu"),
            KeyboardButton(text="💾Info"),
        ],
    ],
    resize_keyboard=True
)