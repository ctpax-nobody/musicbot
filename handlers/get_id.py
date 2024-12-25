from aiogram import Bot, Dispatcher, types
from aiogram.types import Message
from aiogram.fsm.context import FSMContext
import logging
from aiogram import Router

# Tokenni kiriting
API_TOKEN = "7765933698:AAGPvP5wdy_PZ9xiQHn3SRxNDEuIHmFSohw"

# Botni yaratish
bot = Bot(token=API_TOKEN)
router = Router()

# Loglarni sozlash
logging.basicConfig(level=logging.INFO)

# Bot guruhga xabar yuborilganida, chat.id ni chiqarish
@router.message()
async def get_group_id(message: Message, state: FSMContext):
    # Agar xabar guruhdan bo'lsa, guruhning chat.id sini olish
    if message.chat.type in ['group', 'supergroup']:
        chat_id = message.chat.id
        await message.answer(f"Guruhning chat ID si: {chat_id}")

# Asosiy loop
async def main():
    # Dispatcher yaratish
    dp = Dispatcher()

    # Routerni qo'shish
    dp.include_router(router)

    # Pollingni boshlash
    await dp.start_polling(bot)

if __name__ == "__main__":
    import asyncio
    asyncio.run(main())
