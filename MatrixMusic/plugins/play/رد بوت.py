import asyncio
from MatrixMusic import app 
from strings.filters import command
import random
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup


italy = ["ممكن تسميني باسمي!", "اسمي القميل ماتركس", "شوي واجيك", "عنديہ آسم ترۿ", "ياروحه اسمـي ماتركس 🧸♥️؟!"]

@app.on_message(filters.text & filters.regex(r"(^|\W)بوت(\W|$)"))
async def Italymusic(client, message):
    if "بوت" in message.text:
        response = random.choice(italy)
        keyboard = InlineKeyboardMarkup([[InlineKeyboardButton("قناة السورس", url="https://t.me/XMATTMX")]])
        await message.reply(response, reply_markup=keyboard)
