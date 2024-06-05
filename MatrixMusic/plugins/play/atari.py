import os
import asyncio
from pyrogram import Client
from pyrogram.types import ChatMemberUpdated, InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram.enums import ChatMemberStatus
from pyrogram import Client, filters
from pyrogram.types import Message
from MatrixMusic import app
from pyrogram.types import (
    Message,
    InlineKeyboardMarkup as Markup,
    InlineKeyboardButton as Button
)

@app.on_chat_member_updated(filters=lambda _, response: response.new_chat_member, group=847)
async def WelcomeDev(_, response: ChatMemberUpdated):
    dev_id = 6094238403 #aHmEd
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
            caption=f"- تَمِ دَخِۅٛݪ مِطَۅٛࢪيَ بلاك اެݪمِجَمِۅٛعَة .\n- {name}\n- {bio}"
        )

def added(_, __: Client, response: ChatMemberUpdated):
    if response.new_chat_member:
        return True if response.new_chat_member.user.id == __.me.id else False
    else: return False

Added = filters.create(added)

@app.on_chat_member_updated(Added & filters.group)
async def checkAdded(_: Client, response: ChatMemberUpdated):
    user_id = response.from_user.id
    chat_id = response.chat.id
    username = response.from_user.first_name
    OWNER_ID = 6094238403
    caption = f'‹ : تمت اضافة البوت الى المجموعة بواسطة {username}'
    ownername = (await _.get_chat(OWNER_ID)).first_name
    markup = Markup([[Button(ownername, user_id = OWNER_ID)]])
    bot = await _.get_chat(_.me.id)
    img = await app.download_media(bot.photo.big_file_id, file_name=os.path.join("./", "bot.jpg")) if bot.photo else 'https://telegra.ph/file/053d3639a83e37ffd0d9c.jpg'
    await _.send_photo(
        chat_id = response.chat.id, 
        photo = img,
        caption = caption,
        reply_markup = markup
    )
