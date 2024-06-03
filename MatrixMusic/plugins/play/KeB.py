#
# Copyright (C) 2024-2026 by JUSTATARI@Github, < https://github.com/JUSTATARI >.
#
# This file is part of < https://github.com/JUSTATARI/VBTB > project,
# and is released under the "GNU v3.0 License Agreement".
# Please see < https://github.com/JUSTATARI/VBTB/blob/master/LICENSE >
#
# All rights reserved.

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
from MatrixMusic.utils.decorators import AdminActual
from MatrixMusic import (Apple, Resso, SoundCloud, Spotify, Telegram, YouTube, app)
from MatrixMusic import app
from random import  choice, randint
#اتار.ي
lnk= "" +config.SUPPORT_CHANNEL

REPLY_MESSAGE = "<b>- اهلا بك عزيزي اليك قائمة اوامر التسلية .\n- اصدار السورس ~ 5.8V .\n- اصدار الكيبورد ~ 5.8V .</b>"

#اتاري
#v..vi.zi.n.n

REPLY_MESSAGE_BUTTONS = [

          [

             ("‹ غنيلي ›"),

             ("‹ شعر ›")
          ],

          [

             ("‹ صور ›"),

             ("‹ انمي ›")

          ],

          [

             ("‹ متحركة ›"),

             ("‹ اقتباسات ›")

          ],

          [

             ("‹ افتارات شباب ›"),

             ("‹ افتار بنات ›")

          ],

          [

             ("‹ هيدرات ›"),

             ("‹ قران ›")

          ],
    
          [

            ("‹ جداريات ›"),

            ("‹ لوكيت ›")
  #ا..تاري
#v..v....i.zi..n.n            
          ],
          [
            ("‹ افتارات سينمائية ›"),

            ("‹ افتارات فنانين ›")
              
          ],
          [
            ("‹ افلام ›"),

            ("‹ قيفات كوكسال ›")
              
          ],
          [
            ("‹ قيفات شباب ›"),

            ("‹ قيفات بنات ›")
              
          ],
          [
            ("‹ قيفات قطط ›"),

            ("‹ قيفات اطفال ›")
              
          ],
          [
            ("‹ قيفات رومانسية ›"),

            ("‹ قيفات كيبوب ›")
          ],
          [
             ("‹ ستوري ›"),

             ("‹ راب ›")
          ],
          [
             ("‹ فيديو ›"),

             ("‹ ريمكس ›")
          ],
          [
             ("‹ فويز ›"),
             ("• اخفاء الكيبورد •")

          ]

]




  

@app.on_message(filters.regex("^/cmds$") & filters.private & filters.group)
async def cpanel(_, message: Message):             
        text = REPLY_MESSAGE
        reply_markup = ReplyKeyboardMarkup(REPLY_MESSAGE_BUTTONS, resize_keyboard=True, selective=True)
        await message.reply(
              text=text,
              reply_markup=reply_markup
        )

@app.on_message(filters.regex("• اخفاء الكيبورد •") & filters.private & filters.group)
async def down(client, message):
          m = await message.reply("<b>- تم اغلاق الكيبورد .</b>", reply_markup= ReplyKeyboardRemove(selective=True))
          
@app.on_message(command(["غنيلي","‹ غنيلي ›"]) & filters.private & filters.group)
async def aTari(client: Client, message: Message):
    rl = random.randint(2,2301)
    url = f"https://t.me/AudiosWaTaN/{rl}"
    await message.reply_voice(url,caption="≭︰تم اختيار اغنية لك .",
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        text=config.CHANNEL_NAME, url=lnk)
                ],
            ]
        )
                             )
#.حقو.ق س.ورس بلا.ك. اتار.ي
@app.on_message(command(["فويز","‹ فويز ›"]) & filters.private & filters.group)
async def aTari(client: Client, message: Message):
    rl = random.randint(2,580)
    url = f"https://t.me/AudiosWaTaN/{rl}"
    await message.reply_voice(url,caption="≭︰تم اختيار فويز لك .",
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        text=config.CHANNEL_NAME, url=lnk)
                ],
            ]
        )
                             )

@app.on_message(command(["ريمكس","‹ ريمكس ›"]) & filters.private & filters.group)
async def aTari(client: Client, message: Message):
    rl = random.randint(2,279)
    url = f"https://t.me/remixsource/{rl}"
    await message.reply_voice(url,caption="≭︰تم اختيار ريمكس لك .",
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        text=config.CHANNEL_NAME, url=lnk)
                ],
            ]
        )
                             )

@app.on_message(command(["راب","‹ راب ›"]) & filters.private & filters.group)
async def aTari(client: Client, message: Message):
    rl = random.randint(2,86)
    url = f"https://t.me/RapEthan/{rl}"
    await message.reply_voice(url,caption="≭︰تم اختيار الراب لك .",
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        text=config.CHANNEL_NAME, url=lnk)
                ],
            ]
        )
                             )


#اتاري
#v..vi-.zi.n.n
@app.on_message(command(["‹ صور ›","صور"]) & filters.private & filters.group)
async def aTari(client: Client, message: Message):
    rl = random.randint(1,107)
    url = f"https://t.me/LKKKKV/{rl}"
    await message.reply_photo(url,caption="≭︰تم اختيار صورة لك .",
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        text=config.CHANNEL_NAME, url=lnk)
                ],
            ]
        )
    )


@app.on_message(command(["‹ انمي ›", "انمي"]) & filters.private & filters.group)
async def aTari(client: Client, message: Message):
    rl = random.randint(2,999)
    url = f"https://t.me/AnimeWaTaN/{rl}"
    await message.reply_photo(url,caption="≭︰تم اختيار انمي لك .",
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        text=config.CHANNEL_NAME, url=lnk)
                ],
            ]
        )
    )

#اتاري
#v..vi.+zi.n.n
@app.on_message(command(["‹ متحركة ›", "متحركة"]) & filters.private & filters.group)
async def aTari(client: Client, message: Message):
    rl = random.randint(2,925)
    url = f"https://t.me/GifWaTaN/{rl}"
    await message.reply_animation(url,caption="≭︰تم اختيار المتحركة لك .",
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        text=config.CHANNEL_NAME, url=lnk)
                ],
            ]
        )
    )

@app.on_message(command(["‹ اقتباسات ›", "اقتباسات"]) & filters.private & filters.group)
async def aTari(client: Client, message: Message):
    rl = random.randint(2,90)
    url = f"https://t.me/LoreBots9/{rl}"
    await message.reply_photo(url,caption="≭︰تم اختيار اقتباس لك .",
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        text=config.CHANNEL_NAME, url=lnk)
                ],
            ]
        )
    )
#اتاري
#v..vi.zi.n.;n
@app.on_message(command(["هيدرات", "‹ هيدرات ›"]) & filters.private & filters.group)
async def aTari(client: Client, message: Message):
    rl = random.randint(2,90)
    url = f"https://t.me/flflfldld/{rl}"
    await message.reply_photo(url,caption="≭︰تم اختيار هيدرات لك .",
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        text=config.CHANNEL_NAME, url=lnk)
                ],
            ]
        )
    )

@app.on_message(command(["‹ افتارات شباب ›","افتارات شباب"]) & filters.private & filters.group)
async def aTari(client: Client, message: Message):
    rl = random.randint(2,90)
    url = f"https://t.me/QrQsQ/{rl}"
    await message.reply_photo(url,caption="≭︰تم اختيار صورة لك .",
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        text=config.CHANNEL_NAME, url=lnk)
                ],
            ]
        )
    )

@app.on_message(command(["‹ افتار بنات ›","افتارات بنات"]) & filters.private & filters.group)
async def aTari(client: Client, message: Message):
    rl = random.randint(2,90)
    url = f"https://t.me/vvyuol/{rl}"
    await message.reply_photo(url,caption="≭︰تم اختيار صورة لك .",
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        text=config.CHANNEL_NAME, url=lnk)
                ],
            ]
        )
    )


@app.on_message(command(["‹ قران ›", "قران"]) & filters.private & filters.group)
async def aTari(client: Client, message: Message):
    rl = random.randint(1,90)
    url = f"https://t.me/lllIIlIllIlIIlI/{rl}"
    await message.reply_voice(url,caption="≭︰تم اختيار اية قرآنية لك .",
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        text=config.CHANNEL_NAME, url=lnk)
                ],
            ]
        )
    )

@app.on_message(command(["‹ جداريات ›","جداريات"]) & filters.private & filters.group)
async def aTari(client: Client, message: Message):
    rl = random.randint(2,61)
    url = f"https://t.me/flflflgktl/{rl}"
    await message.reply_photo(url,caption="≭︰تم اختيار جدارية لك .",
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        text=config.CHANNEL_NAME, url=lnk)
                ],
            ]
        )
                           )

@app.on_message(command(["‹ لوكيت ›","لوكيت"]) & filters.private & filters.group)
async def aTari(client: Client, message: Message):
    rl = random.randint(4,281)
    url = f"https://t.me/kabsjjwbs/{rl}"
    await message.reply_photo(url,caption="≭︰تم اختيار لوكيت لك .",
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        text=config.CHANNEL_NAME, url=lnk)
                ],
            ]
        )
                           )

@app.on_message(command(["‹ افلام ›","افلام"]) & filters.private & filters.group)
async def aTari(client: Client, message: Message):
    rl = random.randint(2,326)
    url = f"https://t.me/Ntsjcdz/{rl}"
    await message.reply_video(url,caption="≭︰تم اختيار فلم لك .",
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        text=config.CHANNEL_NAME, url=lnk)
                ],
            ]
        )
                           )

@app.on_message(command(["‹ فيديو ›","فيديو"]) & filters.private & filters.group)
async def aTari(client: Client, message: Message):
    rl = random.randint(1,78)
    url = f"https://t.me/LKKKKT/{rl}"
    await message.reply_video(url,caption="≭︰تم اختيار فيديو التمبلر لك .",
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        text=config.CHANNEL_NAME, url=lnk)
                ],
            ]
        )
                           )

@app.on_message(command(["‹ ستوري ›","ستوري"]) & filters.private & filters.group)
async def aTari(client: Client, message: Message):
    rl = random.randint(1,379)
    url = f"https://t.me/storryr/{rl}"
    await message.reply_video(url,caption="≭︰تم اختيار ستوري لك .",
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        text=config.CHANNEL_NAME, url=lnk)
                ],
            ]
        )
                           )
    #
# Copyright (C) 2024-2026 by JUSTATARI@Github, < https://github.com/JUSTATARI >.
#
# This file is part of < https://github.com/JUSTATARI/VBTB > project,
# and is released under the "GNU v3.0 License Agreement".
# Please see < https://github.com/JUSTATARI/VBTB/blob/master/LICENSE >
#
# All rights reserved.

@app.on_message(command(["‹ شعر ›","شعر"]) & filters.private & filters.group)
async def aTari(client: Client, message: Message):
    rl = random.randint(7,622)
    url = f"https://t.me/L1BBBL/{rl}"
    await message.reply_voice(url,caption="≭︰تم اختيار شعر لك .",
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        text=config.CHANNEL_NAME, url=lnk)
                ],
            ]
        )
                           )

@app.on_message(command(["‹ افتارات سينمائية ›","افتارات سينمائية"]) & filters.private & filters.group)
async def aTari(client: Client, message: Message):
    rl = random.randint(3,218)
    url = f"https://t.me/IIYIZ/{rl}"
    await message.reply_photo(url,caption="≭︰تم اختيار افتار سينمائي لك .",
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        text=config.CHANNEL_NAME, url=lnk)
                ],
            ]
        )
                           )
#اتاري
#v..vi......zi.n.n
@app.on_message(command(["‹ افتارات فنانين ›","افتارات فنانين"]) & filters.private & filters.group)
async def aTari(client: Client, message: Message):
    rl = random.randint(3,214)
    url = f"https://t.me/FPPPH/{rl}"
    await message.reply_photo(url,caption="≭︰تم اختيار افتار فنان لك .",
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        text=config.CHANNEL_NAME, url=lnk)
                ],
            ]
        )
                           )
#اتاري
#v..vi.zi....n.n.......
@app.on_message(command(["‹ قيفات شباب ›","قيفات شباب","متحركات شباب"]) & filters.private & filters.group)
async def aTari(client: Client, message: Message):
    rl = random.randint(2,21)
    url = f"https://t.me/dldldldlgt/{rl}"
    await message.reply_animation(url,caption="≭︰تم اختيار قيف شباب لك .",
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        text=config.CHANNEL_NAME, url=lnk)
                ],
            ]
        )
                           )

@app.on_message(command(["‹ قيفات بنات ›","قيفات بنات","متحركات بنات"]) & filters.private & filters.group)
async def aTari(client: Client, message: Message):
    rl = random.randint(2,22)
    url = f"https://t.me/lflflrofo/{rl}"
    await message.reply_animation(url,caption="≭︰تم اختيار قيف بنات لك .",
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        text=config.CHANNEL_NAME, url=lnk)
                ],
            ]
        )
                               )
#اتاري
#.......v.....vi.zi.n.n......
@app.on_message(command(["‹ قيفات قطط ›","قيفات قطط","متحركات قطط"]) & filters.private & filters.group)
async def aTari(client: Client, message: Message):
    rl = random.randint(2,101)
    url = f"https://t.me/gsgjituops/{rl}"
    await message.reply_animation(url,caption="≭︰تم اختيار قيف قطط لك .",
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        text=config.CHANNEL_NAME, url=lnk)
                ],
            ]
        )
                               )

@app.on_message(command(["‹ قيفات اطفال ›","قيفات اطفال","متحركات اطفال"]) & filters.private & filters.group)
async def aTari(client: Client, message: Message):
    rl = random.randint(2,24)
    url = f"https://t.me/fmgngoclr/{rl}"
    await message.reply_animation(url,caption="≭︰تم اختيار قيف اطفال لك .",
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        text=config.CHANNEL_NAME, url=lnk)
                ],
            ]
        )
                               )

@app.on_message(command(["‹ قيفات رومانسية ›","قيفات رومانسية","متحركات رومانسية"]) & filters.private & filters.group)
async def aTari(client: Client, message: Message):
    rl = random.randint(2,21)
    url = f"https://t.me/romansiaaa/{rl}"
    await message.reply_animation(url,caption="≭︰تم اختيار قيف رومانسي لك .",
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        text=config.CHANNEL_NAME, url=lnk)
                ],
            ]
        )
                               )

@app.on_message(command(["‹ قيفات كيبوب ›","قيفات كيبوب","متحركات كيبوب"]) & filters.private & filters.group)
async def aTari(client: Client, message: Message):
    rl = random.randint(2,25)
    url = f"https://t.me/kibobg/{rl}"
    await message.reply_animation(url,caption="≭︰تم اختيار قيف كيبوب لك .",
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        text=config.CHANNEL_NAME, url=lnk)
                ],
            ]
    )    
                               )

@app.on_message(command(["‹ قيفات كوكسال ›","قيفات كوكسال","متحركات كوكسال"]) & filters.private & filters.group)
async def aTari(client: Client, message: Message):
    rl = random.randint(2,59)
    url = f"https://t.me/koksalt/{rl}"
    await message.reply_animation(url,caption="≭︰تم اختيار قيف كوكسال لك .",
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        text=config.CHANNEL_NAME, url=lnk)
                ],
            ]
    )
                               )

@app.on_message(command(["‹ هامستر ›","هامستر"]) & filters.private & filters.group)
async def aTari(client: Client, message: Message):
    rl = random.randint(2,3)
    url = f"https://t.me/asoein/{rl}"
    await message.reply_animation(url,caption="≭︰تم اختيار هامستر لك .",
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        text=config.CHANNEL_NAME, url=lnk)
                ],
            ]
    )
                               )

@app.on_message(command(["‹ هامستر ›","هامستر"]) & filters.private & filters.group)
async def aTari(client: Client, message: Message):
    rl = random.randint(4,5)
    url = f"https://t.me/asoein/{rl}"
    await message.reply_voice(url,caption="≭︰تم اختيار اغنية لك .",
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        text=config.CHANNEL_NAME, url=lnk)
                ],
            ]
        )
                           )
####################اتاري
#v..vi.z###i.###n.n####
                           
#
# Copyright (C) 2024-2026 by JUSTATARI@Github, < https://github.com/JUSTATARI >.
#
# This file is part of < https://github.com/JUSTATARI/VBTB > project,
# and is released under the "GNU v3.0 License Agreement".
# Please see < https://github.com/JUSTATARI/VBTB/blob/master/LICENSE >
#
# All rights reserved.