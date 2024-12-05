from aiogram.utils.keyboard import ReplyKeyboardBuilder
from aiogram.types import KeyboardButton

def generate_main_menu():
    builder = ReplyKeyboardBuilder()

    builder.row(
        KeyboardButton(text="Musiqalar menyusi 🎧"),
        KeyboardButton(text="Musiqa qidirish 🔍")
    )
    builder.row(
        KeyboardButton(text="Video yuklash 📹"),
        KeyboardButton(text="Aloqa uchun 📞")
    )
    return builder.as_markup(resize_keyboard=True)
