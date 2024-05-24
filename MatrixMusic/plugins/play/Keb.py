import asyncio
from pyrogram import Client, filters
from strings.filters import command
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
from MatrixMusic import app


REPLY_MESSAGE = "<b>- اهلا بك عزيزي اليك قائمه الاوامر</b>"




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
             ("‹ اخفاء الكيبورد ›")

          ]

]




  

@app.on_message(filters.regex("^/cmds$") & filters.private)
async def cpanel(_, message: Message):             
        text = REPLY_MESSAGE
        reply_markup = ReplyKeyboardMarkup(REPLY_MESSAGE_BUTTONS, resize_keyboard=True, selective=True)
        await message.reply(
              text=text,
              reply_markup=reply_markup
        )

@app.on_message(filters.regex("‹ اخفاء الكيبورد ›") & filters.private)
async def down(client, message):
          m = await message.reply("<b>- تم اغلاق الكيبورد.</b>", reply_markup= ReplyKeyboardRemove(selective=True))
