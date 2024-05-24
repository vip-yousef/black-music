from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
import os
import asyncio
import time
import requests
from strings.filters import command
from MatrixMusic import app

hmses = {}

@app.on_message(filters.reply & filters.regex("اهمس") & filters.group)
def reply_with_link(client, message):
    user_id = message.reply_to_message.from_user.id
    my_id = message.from_user.id
    bar_id = message.chat.id
    start_link = f"https://t.me/{(app.get_me()).username}?start=hms{my_id}to{user_id}in{bar_id}"
    reply_markup = InlineKeyboardMarkup(
        [
            [InlineKeyboardButton("‹ اضغط هنا ›", url=start_link)]
        ]
    )
    message.reply_text("↯︙اضـغط هنا ↫ ⦗ لإرسال الهمسة السرية ⦘", reply_markup=reply_markup)

waiting_for_hms = False
@app.on_message(filters.command("start"))
def hms_start(client, message):
  
  if message.text.split(" ", 1)[-1].startswith("hms"):
    global waiting_for_hms, hms_ids
    hms_ids = message.text
    waiting_for_hms = True
    message.reply_text(
      "↯︙ارسل رسالتك",
      reply_markup = InlineKeyboardMarkup ([[
        InlineKeyboardButton ("‹ إلغاء ›", callback_data="hms_cancel")
      ]])
    )
    return

@app.on_message(filters.private & filters.text & ~filters.command("start"))
def send_hms(client, message):
  
  global waiting_for_hms
  if waiting_for_hms:    
    to_id = int(hms_ids.split("to")[-1].split("in")[0])
    from_id = int(hms_ids.split("hms")[-1].split("to")[0])
    in_id = int(hms_ids.split("in")[-1])
    to_url = f"tg://openmessage?user_id={to_id}"
    from_url = f"tg://openmessage?user_id={from_id}"
    
    hmses[str(to_id)] = { "hms" : message.text, "bar" : in_id }
    
    message.reply_text("↯︙تم إرسال الهمسة")
    
    app.send_message(
      chat_id = in_id,
      text = f"↯︙هذي الهمسة للحلو ↬ [{app.get_chat(to_id).first_name}]({to_url})\n[{app.get_chat(from_id).first_name}]({from_url})\n↯︙هو اللي يقدر يشوفها ↬",
      reply_markup = InlineKeyboardMarkup ([[InlineKeyboardButton("- اضغط لرؤية الهمسه 👀", callback_data = "hms_answer")]])
    )
    
    waiting_for_hms = False
  
@app.on_callback_query(filters.regex("hms_answer"))
def display_hms(client, callback):
  
  in_id = callback.message.chat.id
  who_id = callback.from_user.id
  
  if hmses.get(str(who_id)) is not None:
    if hmses.get(str(who_id))["bar"] == in_id:
      callback.answer( hmses.get(str(who_id))["hms"], show_alert = True )
  else:
    callback.answer( "هذا الأمر لايخصك", show_alert = True )
    
@app.on_callback_query(filters.regex("hms_cancel"))
def cancel_hms(client, callback):
  
  global waiting_for_hms
  waiting_for_hms = False
  
  client.edit_message_text(
  chat_id = callback.message.chat.id,
  message_id = callback.message.id,
  text = "↯︙تم الغاء ↫ ⦗ الهمسة ⦘")
  
if __name__ == "__main__":
  app.run()
