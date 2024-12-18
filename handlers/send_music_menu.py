from aiogram.types import Message
from aiogram import F
from router import router
from keyboards.reply.send_musics import sending_musics
from keyboards.reply.music_menu import music_category
from keyboards.reply.main_menu import main_menu

async def send_music_page(message: Message, start_id: int):
    musics_sent = 0
    skip_count = start_id

    async for msg in message.chat.iter_history(reverse=True):
        if skip_count > 0:
            skip_count -= 1
            continue
        if musics_sent >= 10:
            break
        if msg.audio:
            await message.answer_audio(audio=msg.audio.file_id)
            musics_sent += 1

    await message.answer("Musiqalar ro'yxati:", reply_markup=sending_musics())

@router.message(F.text == "Musiqalar menyusi 🎧")
async def send_categoryes(message: Message):
    await message.answer("Kategoriyani tanlang:", reply_markup=music_category())

@router.message(F.text == "Aralash musiqalar 🎵")
async def send_all_musics(message: Message):
    await send_music_page(message, start_id=0)

@router.message(F.text == "Keyingi 10 ta musiqa 🎵")
async def send_next_music(message: Message):
    await send_music_page(message, start_id=10)

@router.message(F.text == "Olidingi 10 ta musiqa 🎵")
async def send_previous_music(message: Message):
    await send_music_page(message, start_id=0)

@router.message(F.text == "Ortga 🔙")
async def go_back(message: Message):
    await message.answer("Asosiy menyuga qaytdingiz.", reply_markup=main_menu())
