from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

loc_phone = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="🕹Location", request_location=True),
            KeyboardButton(text="📱Phone number", request_contact=True),
        ],
        [
            KeyboardButton(text="◀️Back")
        ]
    ],
    resize_keyboard=True
)