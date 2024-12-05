from aiogram.utils.keyboard import ReplyKeyboardBuilder
from aiogram.types import KeyboardButton

builder = ReplyKeyboardBuilder()

def music_category():
    builder.row(
        KeyboardButton(text="Aralash musiqalar 🎵")
    )
    builder.row(
        KeyboardButton(text="Phonklar ☠️"),
        KeyboardButton(text="Peaceful 💆🏻‍♂️")
    )
    return builder.as_markup(resize_keyboard=True)
