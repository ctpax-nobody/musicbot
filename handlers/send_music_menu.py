from aiogram.types import Message
from aiogram import F

from router import router
from keyboards.reply.music_menu import music_category

@router.message(F.text == "Musiqalar menyusi 🎧")
async def send_categoryes(message: Message):
    await message.answer(text="Kategoriyani tanlang", reply_markup=music_category())
