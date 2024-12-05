from aiogram.types import Message
from aiogram import F
from router import router

@router.message(F.text == "Musiqa qidirish 🔍")
async def wait_music(message: Message):
    await message.reply(text="Coming soon...")
