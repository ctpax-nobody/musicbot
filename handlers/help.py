from aiogram import types
from aiogram.filters.command import Command

from router import router

@router.message(Command("help"))
async def start(message: types.Message):
    await message.answer("Murojat uchun @geneticanomal")
