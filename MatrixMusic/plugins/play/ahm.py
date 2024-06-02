from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
import os
import asyncio
import time
import requests
from strings.filters import command
from MatrixMusic import app

blackes = {}

@app.on_message(filters.reply & filters.regex("اهمس") & filters.group)
def reply_with_link(client, message):
    user_id = message.reply_to_message.from_user.id
    my_id = message.from_user.id
    bar_id = message.chat.id
    start_link = f"https://t.me/{(app.get_me()).username}?start=black{my_id}to{user_id}in{bar_id}"
    reply_markup = InlineKeyboardMarkup(
        [
            [InlineKeyboardButton("≭︰اضـغط هنا ↫ ⦗ لإرسال الهمسة السرية ⦘", url=start_link)]
        ]
    )
    message.reply_text("\nاضـغط هنا\n", reply_markup=reply_markup)

waiting_for_black = False
@app.on_message(filters.command("start"))
def black_start(client, message):
  
  if message.text.split(" ", 1)[-1].startswith("black"):
    global waiting_for_black, black_ids
    black_ids = message.text
    waiting_for_black = True
    message.reply_text(
      "≭︰ارسل رسالتك",
      reply_markup = InlineKeyboardMarkup ([[
        InlineKeyboardButton ("‹ إلغاء ›", callback_data="black_cancel")
      ]])
    )

@app.on_message(filters.private & filters.regex("^\/start black"))
def send_black(client, message):
  
  global waiting_for_black
  if waiting_for_black:    
    to_id = int(black_ids.split("to")[-1].split("in")[0])
    from_id = int(black_ids.split("black")[-1].split("to")[0])
    in_id = int(black_ids.split("in")[-1])
    to_url = f"tg://openmessage?user_id={to_id}"
    from_url = f"tg://openmessage?user_id={from_id}"
    
    blackes[str(to_id)] = { "black" : message.text, "bar" : in_id }
    
    message.reply_text("≭︰تم إرسال الهمسة .")
    
    app.send_message(
      chat_id = in_id,
      text = f"≭︰هذي الهمسة للحلو ~ {app.get_chat(to_id).first_name}\n≭︰من هذا الشخص ~ {app.get_chat(from_id).first_name}\n≭︰هو اللي يقدر يشوفها",
      reply_markup = InlineKeyboardMarkup ([[InlineKeyboardButton("اضـغـط هـنـا", callback_data = "black_answer")]])
    )
    
    waiting_for_black = False
  
@app.on_callback_query(filters.regex("black_answer"))
def display_black(client, callback):
  
  in_id = callback.message.chat.id
  who_id = callback.from_user.id
  
  if blackes.get(str(who_id)) is not None:
    if blackes.get(str(who_id))["bar"] == in_id:
      callback.answer( blackes.get(str(who_id))["black"], show_alert = True )
  else:
    callback.answer( "هذا الأمر لايخصك", show_alert = True )
    
@app.on_callback_query(filters.regex("black_cancel"))
def display_black(client, callback):
  
  global waiting_for_black
  waiting_for_black = False
  
  client.edit_message_text(
  chat_id = callback.message.chat.id,
  message_id = callback.message.id,
  text = "≭︰تم الغاء ↫ ⦗ الهمسة ⦘")
