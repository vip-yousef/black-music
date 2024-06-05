import os
import time
from asyncio import sleep
from pyrogram import Client, filters
from pyrogram import enums, filters
from strings.filters import command
from MatrixMusic import app
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram.enums import ChatMemberStatus

@app.on_message(~filters.private & command(["المالك","المنشئ"]), group=222)
def owner(app, message):
  for owner in app.get_chat_members(message.chat.id, filter=enums.ChatMembersFilter.ADMINISTRATORS):
    if owner.status == enums.ChatMemberStatus.OWNER:
      saidi = app.get_users(owner.user.id)
      JABWA = InlineKeyboardMarkup([[InlineKeyboardButton(saidi.first_name, url=f"https://t.me/{saidi.username}")]])
      for x in app.get_chat_photos(saidi.id, limit=1):
        photo = x.file_id
      message.reply_photo(photo,caption=f"𝅄 𓏺 𝙾𝚆𝙽𝙴𝚁 𝖭𝖺𝗆𝖾 : {saidi.first_name}\n𝅄 𓏺 𝙾𝚆𝙽𝙴𝚁 𝚄𝚂𝙴𝚁 : [@{saidi.username}]\n𝅄 𓏺 𝙾𝚆𝙽𝙴𝚁 𝗂𝖽 : {saidi.id}",reply_markup=JABWA,quote=True)
