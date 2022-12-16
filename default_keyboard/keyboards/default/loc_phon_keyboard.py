from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

loc_phone = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="🕹Location", request_location=True),
            KeyboardButton(text="📱Phone number", request_contact=True),
        ],
    ],
    resize_keyboard=True
)