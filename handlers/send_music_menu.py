from aiogram.types import Message
from aiogram import F
from router import router
from keyboards.reply.music_menu import sending_musics

# Musiqa fayllarini yuborish funksiyasi
async def send_music_page(message: Message, start_id: int):
    musics_sent = 0

    # Guruhdagi xabarlar tarixini olish
    async for msg in message.chat.iter_history():
        if musics_sent >= 10:
            break  # Faqat 10 ta musiqani yuborish
        if msg.audio:
            await message.answer_audio(audio=msg.audio.file_id)
            musics_sent += 1

    # Yuborish tugadi, tugmalarni qaytarish
    await message.answer("Musiqalar ro'yxati:", reply_markup=sending_musics())

# "Aralash musiqalar 🎵" tugmasi ishlatilganda
@router.message(F.text == "Aralash musiqalar 🎵")
async def send_all_musics(message: Message):
    await send_music_page(message, start_id=0)

# Keyingi 10 ta musiqa tugmasi
@router.message(F.text == "Keyingi 10 ta musiqa 🎵")
async def send_next_music(message: Message):
    await send_music_page(message, start_id=10)

# Oldingi 10 ta musiqa tugmasi
@router.message(F.text == "Olidingi 10 ta musiqa 🎵")
async def send_previous_music(message: Message):
    await send_music_page(message, start_id=0)

# Ortga tugmasi uchun handler
@router.message(F.text == "Ortga 🔙")
async def go_back(message: Message):
    await message.answer("Asosiy menyuga qaytdingiz.")
