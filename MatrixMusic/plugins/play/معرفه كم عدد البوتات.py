import os
import asyncio
from pyrogram import Client, filters
from pyrogram.types import Message
from pyrogram import enums
from strings.filters import command
from pyrogram.enums import ChatMemberStatus
from pyrogram.errors import FloodWait
from MatrixMusic import app


@app.on_message(command(["bots","البوتات","/bots"]))
async def bots(client, message):  
  try:    
    botList = []
    async for bot in app.get_chat_members(message.chat.id, filter=enums.ChatMembersFilter.BOTS):
      botList.append(bot.user)
    lenBotList = len(botList) 
    text3  = f"قائمة البوتات - {message.chat.title}\n\n🤖 البوتات\n"
    while len(botList) > 1:
      bot = botList.pop(0)
      text3 += f"├ @{bot.username}\n"    
    else:    
      bot = botList.pop(0)
      text3 += f"└ @{bot.username}\n\n"
      text3 += f"✅ | اجمالي البوتات: {lenBotList}"  
      await app.send_message(message.chat.id, text3)
  except FloodWait as e:
    await asyncio.sleep(e.value)
    
