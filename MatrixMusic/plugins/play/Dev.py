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
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from random import  choice, randint
from MatrixMusic import app
from pyrogram import Client, filters
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

    
    usm = await app.get_users(user_ids=[OWNER_ID])
    mname = "usm.first_name"
    musrnam = "usm.username"


    chat = query.message.chat.id
    gti = query.message.chat.title
    chatusername = f"@{query.message.chat.username}"
    chatprivatename = await app.export_chat_invite_link(chat)
    user_id = query.from_user.id
    user_ab = query.from_user.username
    user_name = query.from_user.first_name
    
    await app.send_message(OWNER_ID, f"<b>≭︰قام ~ ⦗ {query.from_user.mention} ⦘ .\n</b>"
                                     f"<b>≭︰بمناداتك عزيزي المطور .\n</b>"
                                     f"<b>≭︰الأيدي ~ ⦗ {user_id} ⦘ .\n</b>"
                                     f"<b>≭︰اليوزر ~ ⦗ @{user_ab} ⦘ .\n</b>"
                                     f"<b>≭︰يوزر المجموعة العام ~ ⦗ {chatusername} ⦘ .\n</b>"
                                     f"<b>≭︰يوزر المجموعة الخاص ~ ⦗ {chatprivatename} ⦘ .\n</b>"
                                     f"<b>≭︰ايدي المجموعة ~ ⦗ {chat} ⦘ .\n</b>")


    await query.message.reply_text(f"<b>≭︰تم إرسال استدعائك إلى مطور البوت .\n\n≭︰Black Team ~ ⦗ @vvizinn ⦘ .\n≭︰Black Updates ~ ⦗ @ExP_Black ⦘ .\n≭︰Dev ~ ⦗ @A1RTR ⦘ .</b>")

@app.on_message(
    command(["المطور"])
    & filters.group
  
)
async def rsexs(client, message):
    usr = await app.get_chat("A1RTR")
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


from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

app = Client("my_account")

@app.on_message(filters.command(["تخ"]) & filters.group)
async def huhh(client, message):
    user = message.from_user
    await message.reply_animation(
        animation="https://telegra.ph/file/5a18fe591860a8a98f39f.mp4",
        caption=f"""≭︰قتل ↫ ⦗ {message.from_user.mention} ⦘\n≭︰الضحيه دا 😢 ↫ ⦗ [{user.first_name}](tg://user?id={user.id}) ⦘\nانا لله وانـا اليـه راجعـون 😢😢""",
        reply_markup=InlineKeyboardMarkup(
            [
               [
                   InlineKeyboardButton(
                       "‹ 𝐁𝐥𝐚𝐜𝐤 𝐓𝐞𝐀𝐦 ›", url="https://t.me/vvizinn"),
               ],
           ]
        )
    )
