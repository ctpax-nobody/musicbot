from aiogram import types
from aiogram.filters.command import CommandStart

from router import router
from loader import db
from keyboards.reply.main_menu import generate_main_menu

@router.message(CommandStart())
async def start(message: types.Message):
    telegram_id = message.from_user.id
    fullname = message.from_user.full_name
    username = message.from_user.username

    try:
        # Agar bu guruhda bo'lsa
        if message.chat.type in ['group', 'supergroup']:
            group_id = message.chat.id
            await message.reply(
                text=f"Guruhning ID si: {group_id}",
                reply_markup=generate_main_menu()
            )

        # Agar username bo'lsa, uni ro'yxatdan o'tkazish
        if username:
            db.register_user(telegram_id, fullname, username)
            await message.reply(
                text=f"Assalomu aleykum, {fullname}, muvaffaqiyatli ro'yxatdan o'tdingiz ✅",
                reply_markup=generate_main_menu()
            )
        else:
            db.register_user2(telegram_id, fullname)
            await message.reply(
                text=f"Assalomu aleykum, {fullname}, muvaffaqiyatli ro'yxatdan o'tdingiz ✅",
                reply_markup=generate_main_menu()
            )
    except Exception as e:
        await message.reply(
            text=f"Xush kelibsiz, {fullname} 🤝",
            reply_markup=generate_main_menu()
        )
