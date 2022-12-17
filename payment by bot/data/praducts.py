from aiogram import types
from aiogram.types import LabeledPrice

from utils.misc.product import Product
from .config import PROVIDER_TOKEN_CLICK, PROVIDER_TOKEN_PAYME

communicator = Product(
    title="E-pos systems",
    description="To'lov qilish uchun quyidagi tugmani bosing",
    currency="UZS",
    provider_token=PROVIDER_TOKEN_CLICK,
    prices=[
        LabeledPrice(
            label="Har bir oy uchun to'lov",
            amount=7000000, #70 ming so'm
        ),
    ],
    start_parameter="create_invoice_mt_payment",
    photo_url='http://telegra.ph//file/29fcc004b39bf4f6c5f90.jpg',
    photo_width=1280,
    photo_height=564,
    # photo_size=600,
    need_name=True,
    need_phone_number=True,
)


