import asyncio
from pyrogram import Client, filters
from typing import Union
from pyrogram.types import Message, VoiceChatStarted, VoiceChatEnded
from MatrixMusic import app

@app.on_message(filters.voice_chat_started)
async def babloo(client: Client, message: Message): 
      Startt = "- صعدوا نسمع أغاني 🫂"
      await message.reply_text(Startt)

@app.on_message(filters.voice_chat_ended)
async def bablo(client: Client, message: Message): 
      Enddd = "- أصلاً مليت ☹"
      await message.reply_text(Enddd)
