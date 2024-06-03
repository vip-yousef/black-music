from pyrogram import Client, filters
from random import  choice, randint
from MatrixMusic import app
from pyrogram.types import (
    CallbackQuery,
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    ReplyKeyboardMarkup,
    ReplyKeyboardRemove,
    InputMediaPhoto,
    Message,
)

@app.on_message(filters.command("تخ", [".", ""]) & filters.group & filters.reply)
async def huhh(client, message):
    user = message.from_user
    await message.reply_animation(
        animation="https://telegra.ph/file/b90d4b29a715fb542544a.mp4",
        caption=f"""≭︰قتل ↫ ⦗ {message.from_user.mention} ⦘\n≭︰الضحيه دا 😢 ↫ ⦗ {message.reply_to_message.from_user.mention} ⦘\nانا لله وانـا اليـه راجعـون 😢😢""",
        reply_markup=InlineKeyboardMarkup(
            [
               [
                   InlineKeyboardButton(
                       "المقتول 🔪", url=f"https://t.me/{message.reply_to_message.from_user.username}"
                   )],[
                   InlineKeyboardButton(
                       "‹ 𝐁𝐥𝐚𝐜𝐤 𝐓𝐞𝐀𝐦 ›", url="https://t.me/vvizinn"),
               ],
           ]
        )
    )
    

@app.on_message(filters.command("تف", [".", ""]) & filters.group & filters.reply)
async def huhh(client, message):
    user = message.from_user
    await message.reply_animation(
        animation="https://telegra.ph/file/4a1f6a9bacb1a863f03f1.mp4",
        caption=f"""≭︰تف ↫ ⦗ {message.from_user.mention} ⦘\n≭︰علي الضحيه دا 😢 ↫ ⦗ {message.reply_to_message.from_user.mention} ⦘\nاععع اي القرف دا""",
        reply_markup=InlineKeyboardMarkup(
            [
               [
                   InlineKeyboardButton(
                       "المجني عليه 😢", url=f"https://t.me/{message.reply_to_message.from_user.username}"
                  )],[
                   InlineKeyboardButton(
                       "‹ 𝐁𝐥𝐚𝐜𝐤 𝐓𝐞𝐀𝐦 ›", url="https://t.me/vvizinn"),
               ],
           ]
        )
    )
