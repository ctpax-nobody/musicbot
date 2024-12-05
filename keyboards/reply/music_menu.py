from aiogram.utils.keyboard import ReplyKeyboardBuilder
from aiogram.types import KeyboardButton

def music_category():
    builder = ReplyKeyboardBuilder()

    builder.row(
        KeyboardButton(text="Aralash musiqalar 🎵"),
        KeyboardButton(text="Peaceful 💆🏻‍♂️")
    )
    builder.row(
        KeyboardButton(text="Phonklar ☠️"),
        KeyboardButton(text="Orqaga qaytish 🔙")
    )
    
    return builder.as_markup(resize_keyboard=True)
