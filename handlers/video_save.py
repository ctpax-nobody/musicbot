from aiogram.types import Message
from aiogram import F
from router import router

@router.message(F.text == "Video yuklash 📹")
async def wait_video(message: Message):
    await message.reply(text="Comming soon...")