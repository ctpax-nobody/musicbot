from aiogram.types import Message
from aiogram import F

from router import router
from keyboards.reply.music_menu import music_menu

@router.message(F.text == "Musiqalar menyusi 🎧")
async def music_menu(message: Message):
    await message.answer(text="Kategoriyani tanlang", reply_markup=music_menu())
