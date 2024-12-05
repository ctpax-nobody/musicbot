from aiogram.types import Message
from aiogram.enums.parse_mode import ParseMode
from aiogram import F
from router import router
from keyboards.reply.music_menu import music_category

@router.message(F.text == "Musiqalar menyusi 🎧")
async def send_categoryes(message: Message):
    await message.answer(text="Kategoriyani tanlang", 
                         reply_markup=music_category())

@router.message(F.text == "Aralash musiqalar 🎵")
async def send_random_music(message: Message):
    url = "https://t.me/mymuzzzzzzzzzzzzzzzz"
    await message.reply(text=f"Guruxga kirish uchun [Muz]({url}) bosing", parse_mode=ParseMode.MARKDOWN)

@router.message(F.text == "Phonklar ☠️")
async def send_phonk_music(message: Message):
    url = "https://t.me/anomalyphonk"
    await message.reply(text=f"Guruxga kirish uchun [Zal time]({url}) bosing", parse_mode=ParseMode.MARKDOWN)

@router.message(F.text == "Peaceful 💆🏻‍♂️")
async def send_peaceful_music(message: Message):
    url = "https://t.me/+oNZhavnX3RM4ZjY6"
    await message.reply(text=f"Guruxga kirish uchun [Peaceful]({url}) bosing", parse_mode=ParseMode.MARKDOWN)
