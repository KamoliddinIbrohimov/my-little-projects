from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from .callback_data import course_callback, book_callback

# The first method
products_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="💻Course", callback_data="course"),
            InlineKeyboardButton(text="📚Books", callback_data="books"),
        ],
        [
            InlineKeyboardButton(text="🔗Link", url="https://www.youtube.com/watch?v=pqPWXBRqp3Y"),
        ],
        [
            InlineKeyboardButton(text="🔍Sorch", switch_inline_query_current_chat=""),
        ],
        [
            InlineKeyboardButton(text="📤To share", switch_inline_query="Nice bot"),
        ],
    ])

# The second method
course_menu = InlineKeyboardMarkup(row_width=2)

python = InlineKeyboardButton(text="🐍Python", callback_data=course_callback.new(item_name="python"))
course_menu.insert(python)

java = InlineKeyboardButton(text="💻Java", callback_data=course_callback.new(item_name="java"))
course_menu.insert(java)

flutter = InlineKeyboardButton(text="📱Flutter", callback_data="course:flutter")
course_menu.insert(flutter)

go = InlineKeyboardButton(text="💎GO", callback_data="course:go")
course_menu.insert(go)

telegram_bot = InlineKeyboardButton(text="🤖Telegram bot", callback_data="course:telegram_bot")
course_menu.insert(telegram_bot)

back_button = InlineKeyboardButton(text="🔙Back", callback_data="back")
course_menu.insert(back_button)


# The third method
books = {
    "Python.fundamentals of programming": "python_book",
    "C++.Programming language": "cpp_book",
    "Perfect programming. JavaScript": "js_book",
}

book_menu = InlineKeyboardMarkup(row_width=1)
for key, value in books.items():
    book_menu.insert(InlineKeyboardButton(text=key, callback_data=book_callback.new(item_name=value)))
book_menu.insert(back_button)


telegram_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="🛒\nShopping", callback_data="shopping")
        ],
    ])