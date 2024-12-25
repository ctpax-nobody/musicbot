from aiogram.types import Message
from aiogram import F
from router import router
from keyboards.reply.send_musics import sending_musics
from keyboards.reply.music_menu import music_category
from keyboards.reply.main_menu import main_menu

GROUP_CHAT_ID = "--1001829104884"  # Guruh ID ni kiriting
audio_list = []  # Guruhdan kelgan musiqalarni saqlash uchun ro'yxat

# Musiqa kategoriyalari menyusi
@router.message(F.text == "Musiqalar menyusi 🎧")
async def send_categoryes(message: Message):
    await message.answer(
        text="Kategoriyani tanlang:", 
        reply_markup=music_category()
    )

# "Aralash musiqalar 🎵" tugmasi bosilganda barcha musiqalarni yuborish
@router.message(F.text == "Aralash musiqalar 🎵")
async def send_all_musics(message: Message):
    global audio_list

    if not audio_list:
        await message.answer("Guruhdan hali musiqalar kelib tushmagan.")
        return

    # Ro'yxatdagi musiqalarni yuborish (10 tadan)
    batch = audio_list[:10]  # Dastlabki 10 ta musiqani oling
    for audio_id in batch:
        await message.answer_audio(audio_id)

    # Yuborilgan musiqalarni ro'yxatdan o'chirish
    audio_list = audio_list[10:]

# Guruhdan musiqalarni yig'ish
@router.message(F.chat.id == GROUP_CHAT_ID, F.audio)
async def save_audio(message: Message):
    global audio_list
    audio_list.append(message.audio.file_id)
    
    # Ro'yxatni cheklash (masalan, 100 ta faylni saqlash)
    if len(audio_list) > 100:
        audio_list.pop(0)
