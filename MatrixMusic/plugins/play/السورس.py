#_____كسمك تحياتي 
#_____@EU_TM

import asyncio
import os
import time
import requests
from config import START_IMG_URL
from pyrogram import filters
import random
from pyrogram import Client
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup
from strings.filters import command
from MatrixMusic import (Apple, Resso, Spotify, Telegram, YouTube, app)
from MatrixMusic import app
from random import  choice, randint

                
@app.on_message(
    command(["سورس","السورس"])
    
)
async def huhh(client: Client, message: Message):
    await message.reply_video(
        video=f"https://graph.org/file/9e4fbd7e83b5f7a30b04c.mp4",
        caption=f"𖥻 WelCoMe To SoUrCe black Music .",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "𖥻 GrOuP .", url=f"https://t.me/KKC8C"), 
                 InlineKeyboardButton(
                   "𖥻 SoUrCe .",       url=f"https://t.me/KKC8C"), 
                 
             ],[ 
            InlineKeyboardButton(
                        "⏤͟͞ َِ⍣⃟َ𝐓𝐇ِ𝐄 𓆩ََِِ𝐘َِْ𝐎ِِ𝐔ًٌُ𝐒𝐄ُِ𝐅𓆪", url=f"https://t.me/y_o_v"), 
                      
             ],[ 
            InlineKeyboardButton(
                      "لتنصيب بوت", url=f"https://t.me/y_o_v"), 
                      
             ],[ 
                  InlineKeyboardButton(
                text="𖥻 AdD Me To YoUr GrOuP .",
                url=f"https://t.me/{app.username}?startgroup=true"),
                ],

            ]

        ),

    )


@app.on_message(filters.command(["مطور السورس","يوسف","بلاك","اوس"], ""), group=73) 
async def deev(client: Client, message: Message):
     user = await client.get_chat(chat_id="y_o_v")
     name = user.first_name
     username = user.username 
     bio = user.bio
     user_id = user.id
     photo = user.photo.big_file_id
     photo = await client.download_media(photo)
     link = f"https://t.me/{message.chat.username}"
     title = message.chat.title if message.chat.title else message.chat.first_name
     chat_title = f"User : {message.from_user.mention} \nChat Name : {title}" if message.from_user else f"Chat Name : {message.chat.title}"
     try:
      await client.send_message(username, f"**هناك شخص بالحاجه اليك عزيزي المطور**\n{chat_title}\nChat Id : `{message.chat.id}`",
      reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton(f"{title}", url=f"{link}")]]))
     except:
       pass
     await message.reply_photo(
     photo=photo,
     caption=f"**𝙳𝚎𝚟𝚎𝚕𝚘𝚙𝚎𝚛 𝙽𝚊𝚖𝚎 : {name}** \n**𝚍𝚎𝚟 𝚞𝚜𝚎𝚛 𝚗𝚊𝚖𝚎 : @{username}**\n**{bio}**",
     reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton(f"{name}", user_id=f"{user_id}")]]))
     try:
       os.remove(photo)
     except:
        pass

@app.on_message(filters.command(["مبرمج السورس","لين","لينو","لينوو"], ""), group=73) 
async def deev(client: Client, message: Message):
     user = await client.get_chat(chat_id="o_v_31")
     name = user.first_name
     username = user.username 
     bio = user.bio
     user_id = user.id
     photo = user.photo.big_file_id
     photo = await client.download_media(photo)
     link = f"https://t.me/{message.chat.username}"
     title = message.chat.title if message.chat.title else message.chat.first_name
     chat_title = f"User : {message.from_user.mention} \nChat Name : {title}" if message.from_user else f"Chat Name : {message.chat.title}"
     try:
      await client.send_message(username, f"**هناك شخص بالحاجه اليك عزيزي المطور**\n{chat_title}\nChat Id : `{message.chat.id}`",
      reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton(f"{title}", url=f"{link}")]]))
     except:
       pass
     await message.reply_photo(
     photo=photo,
     caption=f"**𝙳𝚎𝚟𝚎𝚕𝚘𝚙𝚎𝚛 𝙽𝚊𝚖𝚎 : {name}** \n**𝚍𝚎𝚟 𝚞𝚜𝚎𝚛 𝚗𝚊𝚖𝚎 : @{username}**\n**{bio}**",
     reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton(f"{name}", user_id=f"{user_id}")]]))
     try:
       os.remove(photo)
     except:
        pass
