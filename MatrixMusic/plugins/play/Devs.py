import asyncio
import os
import time
import requests
from pyrogram import filters
import random
from pyrogram import Client
from MatrixMusic.utils.decorators import AdminActual
from pyrogram.types import (
    CallbackQuery,
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    ReplyKeyboardMarkup,
    ReplyKeyboardRemove,
    InputMediaPhoto,
    Message,
)
from strings.filters import command
from random import  choice, randint
from MatrixMusic import app
from config import OWNER_ID

def get_file_id(msg: Message):
    if msg.media:
        for message_type in (
            "photo",
            "animation",
            "audio",
            "document",
            "video",
            "video_note",
            "voice",
            # "contact",
            # "dice",
            # "poll",
            # "location",
            # "venue",
            "sticker",
        ):
            obj = getattr(msg, message_type)
            if obj:
                setattr(obj, "message_type", message_type)
                return obj


@app.on_callback_query(filters.regex("devatari"))
async def devatari(_, query: CallbackQuery):

    
    usm = await Client.get_users(OWNER_ID)
    mname = usm.first_name
    musrnam = usm.username
    
    chat = message.chat.id
    gti = message.chat.title
    chatusername = f"@{message.chat.username}"
    link = await app.export_chat_invite_link(chat)
    usr = await client.get_user(message.from_user.id)
    user_id = message.from_user.id
    user_ids = message.from_user.id
    user_ab = message.from_user.username
    user_name = message.from_user.first_name
    buttons = [[InlineKeyboardButton(gti, url=f"{link}")]]
    reply_markup = InlineKeyboardMarkup(buttons)
    
    await app.send_message(OWNER_ID, f"<b>≭︰قام {message.from_user.mention}\n</b>"
                                     f"<b>≭︰بمناداتك عزيزي المطور\n</b>"
                                     f"<b>≭︰الأيدي {user_id}\n</b>"
                                     f"<b>≭︰اليوزر @{user_ab}\n</b>"
                                     f"<b>≭︰ايدي المجموعة {message.chat.id}\n</b>",
                                     reply_markup=reply_markup)
    
    await message.reply_text(f"<b>≭︰تم إرسال النداء إلى مطور البوت\n\n↯︙Dᥱꪜ - @{musrnam} .</b>")

@app.on_message(
    command(["المطور"])
    & filters.group
  
)
async def rsexs(client, message):
    usr = await client.get_chat("A1RTR")
    name = usr.first_name
    photo = await app.download_media(usr.photo.big_file_id)
    await message.reply_photo(photo,       caption=f"≭︰Dev Name ↬ ⦗ {name} ⦘\n≭︰Dev User ↬ ⦗ @{usr.username} ⦘\n≭︰Dev id ↬ ⦗ {usr.id} ⦘",  
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        name, url=f"https://t.me/{usr.username}"),
                  ],[
                    InlineKeyboardButton(
                        "• استدعاء المطور •", callback_data="devatari"),
                    
                ],
            ]
        ),
    )
