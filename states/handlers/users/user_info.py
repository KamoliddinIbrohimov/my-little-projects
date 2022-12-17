from aiogram import types
from loader import dp

from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command
from states.personal_data import PersonalData
from aiogram.dispatcher import filters

@dp.message_handler(Command("form"), state=None)
async def start_state(message: types.Message):
    """Function that sets the user to full name status"""
    text = "enter your full name"
    await message.answer(text)
    await PersonalData.fullname.set()


@dp.message_handler(state=PersonalData.fullname)
async def state_fullname(massage: types.Message, state: FSMContext):
    """Function that stores user input in full name status"""
    full_name = massage.text
    await state.update_data(
        {"name": full_name}
    )
    await massage.answer("Enter your email address")
    await PersonalData.next()

EMAIL_REGEX = r'[^@ \t\r\n]+@[^@ \t\r\n]+\.[^@ \t\r\n]+'


@dp.message_handler(filters.Regexp(EMAIL_REGEX), state=PersonalData.email)
async def email_state(message: types.Message, state: FSMContext):
    """Function that stores user input in email status"""
    email = message.text
    await state.update_data(
        {"email": email}
    )
    await message.answer("Enter your phone number")
    await PersonalData.next()

PHONE_NUM = r'^[\+]?[(]?[0-9]{3}[)]?[-\s\.]?[0-9]{3}[-\s\.]?[0-9]{4,6}$'


@dp.message_handler(filters.Regexp(PHONE_NUM), state=PersonalData.phone_num)
async def phone_num_state(message: types.Message, state: FSMContext):
    """Function that stores user input in phone number status"""
    phone_num = message.text
    await state.update_data(
        {"phone_num": phone_num}
    )
    # retrieve input data
    data = await state.get_data()
    name = data.get("name")
    email = data.get("email")
    phone_num = data.get("phone_num")
    # transfer data to the user
    msg = "Привет! Ты ввел следующие данные:\n"
    msg += f"Имя  - {name}\n\n"
    msg += f"Email - {email}\n\n"
    msg += f"Телефон: - {phone_num}"
    await message.answer(msg)
    await state.finish()
    #await state.reset_state(with_data=False)

@dp.message_handler(state=PersonalData.all_states)
async def error_message(message: types.Message):
    """A function that warns the user when he enters incorrect information"""
    await message.answer('You have entered incorrect information, please try again')
