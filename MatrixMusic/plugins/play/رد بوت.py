import asyncio
from MatrixMusic import app 
from strings.filters import command
import random
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup


atari = ["وبعدين وياك ؟", "عندي اسم ترا", "زعلت !", "وياك القميل بلاك"]

@app.on_message(filters.text & filters.regex(r"(^|\W)بوت(\W|$)"))
async def atari(client, message):
    if "بوت" in message.text:
        response = random.choice(atari)
        await message.reply(response)
