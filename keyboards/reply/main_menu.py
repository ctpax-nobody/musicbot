from aiogram.utils.keyboard import ReplyKeyboardBuilder
from aiogram.types import KeyboardButton

def generate_main_menu():
    builder = ReplyKeyboardBuilder()

    builder.row(
        KeyboardButton(text="Musiqalar menyusi 🎧")
    )
    builder.row(
        KeyboardButton(text="Video yuklash 📹"),
        KeyboardButton(text="Musiqa qidirish 🔍"),
        KeyboardButton(text="Aloqa uchun 📞")
    )
