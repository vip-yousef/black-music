import os
import asyncio
from pyrogram import Client
from pyrogram.types import ChatMemberUpdated, InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram.enums import ChatMemberStatus
from pyrogram import Client, filters
from pyrogram.types import Message
from MatrixMusic import app

@app.on_chat_member_updated(filters=lambda _, response: response.new_chat_member, group=847)
async def WelcomeDev(_, response: ChatMemberUpdated):
    dev_id = 6855645033 #aHmEd
    if response.from_user.id == dev_id and response.new_chat_member.status == ChatMemberStatus.MEMBER:
        info = await app.get_chat(dev_id)
        name = info.first_name
        username = info.username
        bio = info.bio
        markup = InlineKeyboardMarkup([
            [InlineKeyboardButton(name, user_id=dev_id)]
        ])
        await app.download_media(info.photo.big_file_id, file_name=os.path.join("downloads", "IMG_20240529_031114_928.jpg"))
        await app.send_photo(
            chat_id=response.chat.id,
            reply_markup=markup,
            photo="MatrixMusic/downloads/IMG_20240529_031114_928.jpg", 
            caption=f"- تَمِ دَخِۅٛݪ مِطَۅٛࢪيَ اެتَاެࢪيَ اެݪمِجَمِۅٛعَة .\n- {name}\n- {bio}"
        )
