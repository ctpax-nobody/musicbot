from aiogram.types import Message
from aiogram import F
from router import router
from keyboards.reply.main_menu import generate_main_menu

@router.message(F.text == "Orqaga qaytish 🔙")
async def back_one_step(message: Message):
    await message.answer(text="Bosh menyuga chiqildi", 
                         reply_markup=generate_main_menu)
