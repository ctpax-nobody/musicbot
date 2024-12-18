from aiogram.utils.keyboard import ReplyKeyboardBuilder
from aiogram.types import KeyboardButton

def sending_musics():
    builder = ReplyKeyboardBuilder()

    builder.row(
        KeyboardButton(text="Olidingi 10 ta musiqa 🎵"),
        KeyboardButton(text="Keyingi 10 ta musiqa 🎵")
    )
    builder.row(
        KeyboardButton(text="Ortga 🔙")
    )
    return builder.as_markup(resize_keyboard=True)
