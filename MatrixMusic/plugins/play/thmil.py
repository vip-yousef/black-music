import os
import future
import asyncio
import requests
import wget
import time
import yt_dlp
from urllib.parse import urlparse
from MatrixMusic import app
from pyrogram import Client, filters
from pyrogram.types import Message

@app.on_message(filters.command(["انستا"], ["."]))
async def download_instareels(c: app, m: Message):
    try:
        reel_ = m.command[1]
    except IndexError:
        await m.reply_text("≭︰إرسل رابط المقطع في الانستا .")
        return
    if not reel_.startswith("https://www.instagram.com/reel/"):
        await m.reply_text("≭︰عذراً ~ الرابط غير صالح .")
        return
    OwO = reel_.split(".",1)
    Reel_ = ".dd".join(OwO)
    try:
        await m.reply_video(Reel_)
        return
    except Exception:
        try:
            await m.reply_photo(Reel_)
            return
        except Exception:
            try:
                await m.reply_document(Reel_)
                return
            except Exception:
                await m.reply_text("Error")
