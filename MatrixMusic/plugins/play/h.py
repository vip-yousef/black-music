import random
from MatrixMusic import app
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message
from strings.filters import command
from pyrogram import Client
from config import OWNER_ID

txt = [
    "؏ـيوٍڼ ماتركس 😻🫶",
    "ﻧ؏ـ۾ 🥺❤",
    "هہذآ آڛـﻤــي 🫶😻",
    f"ضـوꪆ ماتريكس،💗🧸!َ''))",
    "ها ضلعي سولفلي",
    "خخـير حبيـبي ؟"
    "اههـوو ترا اسمي ماتركس 🙂"
]

txt1 = [
    "**؏ـيوٍڼ ماتركس 😻🫶 يا مطوريي**",
    "**ﻧ؏ـم يامطوريي**",
    "**امرني يا مطوري الحبيب**"
]

@app.on_message(command(["بوت"]))
async def cutt(client: Client, message: Message):
    dev = [OWNER_ID]
    text = random.choice(txt1) if message.from_user.id in dev else random.choice(txt)
    await message.reply(text)


