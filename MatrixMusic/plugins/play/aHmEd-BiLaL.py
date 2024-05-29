import os, webbrowser
import asyncio
import requests
from pyrogram import Client
import aiohttp
import aiofiles
from pyrogram import enums
from pyrogram.enums import ChatMembersFilter, ChatMemberStatus , ChatType
from pyrogram.types import ChatPermissions, ChatPrivileges
import yt_dlp
from yt_dlp import YoutubeDL
from pyrogram import Client, filters
from pyrogram.errors import FloodWait
from pyrogram.types import Message, InputTextMessageContent
from youtube_search import YoutubeSearch
from pyrogram.types import ChatMemberUpdated, InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram.enums import ChatMemberStatus
from pyrogram import Client, filters
from pyrogram.types import Message
from pyrogram.types import CallbackQuery, InputMediaPhoto, InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram.types import CallbackQuery, InlineKeyboardMarkup, InlineKeyboardButton
from MatrixMusic import app



last_clicked_button = {}
welcome_enabled = True

@app.on_message(filters.command(["الرابط","/link"], "") & filters.group & ~filters.private)
async def invitelink(client, message):
    chid = message.chat.id
    try: #BILAL
        invitelink = await client.export_chat_invite_link(chid)
    except:
        return await message.reply_text("قم برفعي مسؤول في المجموعة أولا ؟")
    await message.reply_text(f"**تم إنشاء رابط الدعوة بنجاح :**\n {invitelink}")
    


@app.on_message(filters.command("رفع مشرف", "") & filters.group)
def promote_g_admin(client, message):
    if message.reply_to_message and message.reply_to_message.from_user:
        target = message.reply_to_message.from_user.id
        user_id = str(target)
    elif message.reply_to_message is None:
        target = message.text.split()[2]
        user = app.get_users(target)
        if user:
            user_id = str(user.id)
        else:
            message.reply_text("↯︙لا يمكن العثور على المستخدم .")
            return
    else:
        target = message.text.split()[1].strip("@")
        user = app.get_users(target)
        if user:
            user_id = str(user.id)
        else:
            message.reply_text("لا يمكن العثور على المستخدم")
            return

    tom_id = message.from_user.id
    chat_id = message.chat.id
    ToM= ChatPrivileges(
                    can_manage_chat=True,
                    can_delete_messages=True,
                    can_manage_video_chats=True,
                    can_restrict_members=True,
                    can_promote_members=True,
                    can_change_info=True,
                    can_post_messages=False,
                    can_edit_messages=False,
                    can_invite_users=True,
                    can_pin_messages=True,
                    is_anonymous=False
                )
    tooom = client.get_chat_members(chat_id, filter=ChatMembersFilter.ADMINISTRATORS)
    for tom in tooom:
    	if tom.user.id == tom_id and (tom.status == enums.ChatMemberStatus.OWNER or tom.status == enums.ChatMemberStatus.ADMINISTRATOR):
    		client.promote_chat_member(chat_id, user_id, ToM)
    		message.reply(f"↯︙تم رفع ⦗ {user_id} ⦘ مشرف بنجاح")
