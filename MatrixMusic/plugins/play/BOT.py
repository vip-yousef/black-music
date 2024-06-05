import asyncio
import random
from pyrogram import enums
from pyrogram import types
from MatrixMusic.misc import SUDOERS
from pyrogram.types import (Message,InlineKeyboardButton,InlineKeyboardMarkup,CallbackQuery,ChatPrivileges)
from pyrogram import filters, Client
from MatrixMusic import app
from config import *

bot_name = {}

name = "بلاك"

@app.on_message(filters.regex("تعيين اسم البوت")& filters.private & SUDOERS, group=7113)
async def set_bot_name(client, message):
    global name
    ask = await app.ask(message.chat.id, "ارسل الاسم الجديد", timeout=300)
    name = ask.text
    await message.reply_text("تم تعيين الاسم بنجاح")

caesar_responses = [
    "اسمي {name} يصحبي 💘 ⋅",
    "يحبيبي قلتلك اسمي {name } 🙂",
    "ايه يا يارفيقي 😂♥️ ،",
    "قلب البوت 🥹💘 ⋅",
    "ثانية بشقط واحدة تانية 😂💘 ،",
    "ياخي والله بحبك بس ناديلي بـ {name} 🙂",
    "شو يا معلم مين مزعلك",
    "ايوه جاي 😂♥️ ،",
    "تًبا لك ماذا تريد من امي 🙂",
    " هوا عشان بحبك تصدعني؟",
    "تعرف بالله هحبك أكتر لو ناديتلي {name} 🥹💘",
    "اي ي معلم مين مزعلك؟",
    "متصلي على النبي 💘 ⋅",
    "مش فاضيلك نص ساعه وحكيني ☺ .",
    "انجز عايزني أشقطلك مين؟",
    "شكلها منكدا عليك وجاي تطلعهم علينا 😂♥ ,",
]

@app.on_message(filters.command(["بوت", "بلاك"], ""), group=71135)
async def caesar_bot(client, message):
    global name
    bot_username = (await app.get_me()).username
    bar = random.choice(caesar_responses).format(name=name)
    keyboard = InlineKeyboardMarkup([
        [InlineKeyboardButton("خدني لجروبك 🌚", url=f"https://t.me/{bot_username}?startgroup=True")]
    ])
    
    await message.reply_text(
        text=f"**[{bar}](https://t.me/{bot_username}?startgroup=True)**",
        disable_web_page_preview=True,
        reply_markup=keyboard,
    parse_mode=enums.ParseMode.MARKDOWN)
