import os
import asyncio
import requests
import config
import random
import time
from config import START_IMG_URL
from pyrogram import filters
from pyrogram import Client
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup
from strings.filters import command
from MatrixMusic import (Apple, Resso, SoundCloud, Spotify, Telegram, YouTube, app)
from MatrixMusic import app
from random import  choice, randint


lnk= "" +config.SUPPORT_CHANNEL
@app.on_message(command(["غنيلي","‹ غنيلي ›"]))
async def aTari(client: Client, message: Message):
    rl = random.randint(2,90)
    url = f"https://t.me/BE_19/{rl}"
    await client.send_voice(message.chat.id,url,caption="↯︙تم اختيار اغنية لك .",
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        text=config.CHANNEL_NAME, url=lnk)
                ],
            ]
        )
    )



@app.on_message(command(["‹ صور ›","صور"]) & filters.private)
async def aTari(client: Client, message: Message):
    rl = random.randint(2,50)
    url = f"https://t.me/vnnkli/{rl}"
    await client.send_photo(message.chat.id,url,caption="↯︙تم اختيار صورة لك .",
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        text=config.CHANNEL_NAME, url=lnk)
                ],
            ]
        )
    )


@app.on_message(command(["‹ انمي ›", "انمي"]) & filters.private)
async def aTari(client: Client, message: Message):
    rl = random.randint(2,90)
    url = f"https://t.me/LoreBots7/{rl}"
    await client.send_photo(message.chat.id,url,caption="↯︙تم اختيار انمي لك .",
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        text=config.CHANNEL_NAME, url=lnk)
                ],
            ]
        )
    )


@app.on_message(command(["‹ متحركة ›", "متحركة"]) & filters.private)
async def aTari(client: Client, message: Message):
    rl = random.randint(2,90)
    url = f"https://t.me/GifWaTaN/{rl}"
    await client.send_animation(message.chat.id,url,caption="↯︙تم اختيار المتحركة لك .",
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        text=config.CHANNEL_NAME, url=lnk)
                ],
            ]
        )
    )

@app.on_message(command(["‹ اقتباسات ›", "اقتباسات"]) & filters.private)
async def aTari(client: Client, message: Message):
    rl = random.randint(2,90)
    url = f"https://t.me/LoreBots9/{rl}"
    await client.send_photo(message.chat.id,url,caption="↯︙تم اختيار اقتباس لك .",
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        text=config.CHANNEL_NAME, url=lnk)
                ],
            ]
        )
    )

@app.on_message(command(["هيدرات", "‹ هيدرات ›"]) & filters.private)
async def aTari(client: Client, message: Message):
    rl = random.randint(2,90)
    url = f"https://t.me/flflfldld/{rl}"
    await client.send_photo(message.chat.id,url,caption="↯︙تم اختيار هيدرات لك .",
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        text=config.CHANNEL_NAME, url=lnk)
                ],
            ]
        )
    )

@app.on_message(command(["‹ افتارات شباب ›"]) & filters.private)
async def aTari(client: Client, message: Message):
    rl = random.randint(2,90)
    url = f"https://t.me/QrQsQ/{rl}"
    await client.send_photo(message.chat.id,url,caption="↯︙تم اختيار صورة لك .",
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        text=config.CHANNEL_NAME, url=lnk)
                ],
            ]
        )
    )

@app.on_message(command(["‹ افتار بنات ›"]) & filters.private)
async def aTari(client: Client, message: Message):
    rl = random.randint(2,90)
    url = f"https://t.me/vvyuol/{rl}"
    await client.send_photo(message.chat.id,url,caption="↯︙تم اختيار صورة لك .",
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        text=config.CHANNEL_NAME, url=lnk)
                ],
            ]
        )
    )


@app.on_message(command(["‹ قران ›", "قران"]) & filters.private)
async def aTari(client: Client, message: Message):
    rl = random.randint(1,90)
    url = f"https://t.me/lllIIlIllIlIIlI/{rl}"
    await client.send_voice(message.chat.id,url,caption="↯︙تم اختيار اية قرآنية لك .",
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        text=config.CHANNEL_NAME, url=lnk)
                ],
            ]
        )
    )

@app.on_message(command(["‹ جداريات ›"]) & filters.private)
async def aTari(client: Client, message: Message):
    rl = random.randint(2,61)
    url = f"https://t.me/flflflgktl/{rl}"
    await client.send_photo(message.chat.id,url,caption="↯︙تم اختيار جدارية لك .",
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        text=config.CHANNEL_NAME, url=lnk)
                ],
            ]
        )
                           )

@app.on_message(command(["‹ لوكيت ›"]) & filters.private)
async def aTari(client: Client, message: Message):
    rl = random.randint(4,281)
    url = f"https://t.me/kabsjjwbs/{rl}"
    await client.send_photo(message.chat.id,url,caption="↯︙تم اختيار لوكيت لك .",
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        text=config.CHANNEL_NAME, url=lnk)
                ],
            ]
        )
                           )

@app.on_message(command(["‹ افلام ›"]) & filters.private)
async def aTari(client: Client, message: Message):
    rl = random.randint(2,326)
    url = f"https://t.me/Ntsjcdz/{rl}"
    await client.send_video(message.chat.id,url,caption="↯︙تم اختيار فلم لك .",
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        text=config.CHANNEL_NAME, url=lnk)
                ],
            ]
        )
                           )


@app.on_message(command(["‹ شعر ›"]) & filters.private)
async def aTari(client: Client, message: Message):
    rl = random.randint(2,30)
    url = f"https://t.me/lflfltnt/{rl}"
    await client.send_voice(message.chat.id,url,caption="↯︙تم اختيار شعر لك .",
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        text=config.CHANNEL_NAME, url=lnk)
                ],
            ]
        )
                           )

@app.on_message(command(["‹ افتارات سينمائية ›"]) & filters.private)
async def aTari(client: Client, message: Message):
    rl = random.randint(3,218)
    url = f"https://t.me/IIYIZ/{rl}"
    await client.send_photo(message.chat.id,url,caption="↯︙تم اختيار افتار سينمائي لك .",
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        text=config.CHANNEL_NAME, url=lnk)
                ],
            ]
        )
                           )

@app.on_message(command(["‹ افتارات فنانين ›"]) & filters.private)
async def aTari(client: Client, message: Message):
    rl = random.randint(3,214)
    url = f"https://t.me/FPPPH/{rl}"
    await client.send_photo(message.chat.id,url,caption="↯︙تم اختيار افتار فنان لك .",
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        text=config.CHANNEL_NAME, url=lnk)
                ],
            ]
        )
                           )

@app.on_message(command(["‹ قيفات شباب ›"]) & filters.private)
async def aTari(client: Client, message: Message):
    rl = random.randint(2,21)
    url = f"https://t.me/dldldldlgt/{rl}"
    await client.send_animation(message.chat.id,url,caption="↯︙تم اختيار قيف شباب لك .",
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        text=config.CHANNEL_NAME, url=lnk)
                ],
            ]
        )
                           )

@app.on_message(command(["‹ قيفات بنات ›"]) & filters.private)
async def aTari(client: Client, message: Message):
    rl = random.randint(2,22)
    url = f"https://t.me/lflflrofo/{rl}"
    await client.send_animation(message.chat.id,url,caption="↯︙تم اختيار قيف بنات لك .",
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        text=config.CHANNEL_NAME, url=lnk)
                ],
            ]
        )
                               )

@app.on_message(command(["‹ قيفات قطط ›"]) & filters.private)
async def aTari(client: Client, message: Message):
    rl = random.randint(2,101)
    url = f"https://t.me/gsgjituops/{rl}"
    await client.send_animation(message.chat.id,url,caption="↯︙تم اختيار قيف قطط لك .",
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        text=config.CHANNEL_NAME, url=lnk)
                ],
            ]
        )
                               )

@app.on_message(command(["‹ قيفات اطفال ›"]) & filters.private)
async def aTari(client: Client, message: Message):
    rl = random.randint(2,24)
    url = f"https://t.me/fmgngoclr/{rl}"
    await client.send_animation(message.chat.id,url,caption="↯︙تم اختيار قيف اطفال لك .",
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        text=config.CHANNEL_NAME, url=lnk)
                ],
            ]
        )
                               )

@app.on_message(command(["‹ قيفات رومانسية ›"]) & filters.private)
async def aTari(client: Client, message: Message):
    rl = random.randint(2,21)
    url = f"https://t.me/romansiaaa/{rl}"
    await client.send_animation(message.chat.id,url,caption="↯︙تم اختيار قيف رومانسي لك .",
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        text=config.CHANNEL_NAME, url=lnk)
                ],
            ]
        )
                               )

@app.on_message(command(["‹ قيفات كيبوب ›"]) & filters.private)
async def aTari(client: Client, message: Message):
    rl = random.randint(2,25)
    url = f"https://t.me/kibobg/{rl}"
    await client.send_animation(message.chat.id,url,caption="↯︙تم اختيار قيف كيبوب لك .",
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        text=config.CHANNEL_NAME, url=lnk)
                ],
            ]
    )    
                               )

@app.on_message(command(["‹ قيفات كوكسال ›"]) & filters.private)
async def aTari(client: Client, message: Message):
    rl = random.randint(2,59)
    url = f"https://t.me/koksalt/{rl}"
    await client.send_animation(message.chat.id,url,caption="↯︙تم اختيار قيف كوكسال لك .",
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        text=config.CHANNEL_NAME, url=lnk)
                ],
            ]
    )
                               )
