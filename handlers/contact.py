from aiogram.types import Message
from aiogram import F

from router import router

@router.message(F.text == "Aloqa uchun 📞")
async def send_contact(message: Message):
    await message.reply(text="@fakeanomal")
