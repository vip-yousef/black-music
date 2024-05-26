import os
#os.system("pip install pyrogram && pip install tgcrypto && pip install pyromod && clear")

from pyrogram import Client, filters, idle
from pyromod import Zelzaly
from MatrixMusic import app
from pyrogram.enums import ParseMode, ChatMemberStatus

LOG = -1002001981301

def get_rd(text, id):
    chat_id = str(id)
    text = text
    with open("getrdod.txt", "r+") as f:
       x = f.readlines()
       final = f"{chat_id}#{text}"
       for a in x:
         if final in a:
            return int(a.split(f"{final}ATARI")[1].replace("\n",""))
    return False


def add_rd(text, id, rd) -> bool:
    chat_id = str(id)
    with open("getrdod.txt", "a+") as f:
       x = f.readlines()
       for a in x:
         if f"{chat_id}#{text}" in a:
           return False
       f.write(f"{chat_id}#{text}ATARI{rd}\n")
    return True


def del_rd(x):
   word = str(x).replace("\n","")
   with open("getrdod.txt", "r+") as fp:
      lines = fp.readlines()
   with open("getrdod.txt", "w+") as fp:
          for line in lines:
            line = line.replace("\n","")
            if word != line:
              fp.write(line+"\n")
          return



def del_rdod(id) -> bool:
    chat_id = str(id)
    gps = open("getrdod.txt").read()
    if chat_id not in gps:
      return False
    with open("getrdod.txt", "r+") as fp:
      lines = fp.readlines()
    with open("getrdod.txt", "w+") as fp:
          for line in lines:
            line = line.replace("\n","")
            if chat_id not in line:
              fp.write(line+"\n")
          return


def get_rdod(chat_id):
   with open("getrdod.txt", "r+") as f:
       lines = f.readlines()
   text = "≭︰الردود بهذه المجموعة : \n"
   for line in lines:
     if str(chat_id) in line:
       a = line.split("#")[1]
       b = a.split("ATARI")[0]
       text += f"{b}\n"
   if text == "≭︰الردود بهذه المجموعة : \n": return False
   else: return f"**{text}**"
       
async def get_rtba(chat_id: int, user_id: int) -> bool:
    get = await app.get_chat_member(chat_id, user_id)
    if not get.status in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR]:
      return False
    else: return True
    


@app.on_message(filters.regex("^اضف رد$") & filters.group)
async def adf_rd(app,message):
    get = await get_rtba(message.chat.id, message.from_user.id)
    if not get: return await message.reply("≭︰هذا االأمر لا يخصك")
    ask1 = await app.ask(
    message.chat.id, "ارسل كلمة الرد", reply_to_message_id=message.id, filters=filters.text & filters.user(message.from_user.id))
    text = ask1.text
    ask2 = await app.ask(
    message.chat.id, "ارسل جواب الرد", reply_to_message_id=ask1.id, filters=filters.user(message.from_user.id))
    copy = await ask2.copy(LOG)
    rd = copy.id
    a = add_rd(text, message.chat.id, rd)
    if a: return await ask2.reply("تم اضافة الرد بنجاح")
    else: return await ask2.reply("حدث خطأ")


@app.on_message(filters.regex("^مسح رد$") & filters.group)
async def delete_rd(app,message):
   get = await get_rtba(message.chat.id, message.from_user.id)
   if not get: return await message.reply("≭︰هذا االأمر لا يخصك")
   ask = await app.ask(
     message.chat.id, "ارسل الرد الآن", filters=filters.text & filters.user(message.from_user.id), reply_to_message_id=message.id)
   a = get_rd(ask.text, message.chat.id)
   if not a:
     return await ask.reply("الرد غير موجود")
   x = f"{message.chat.id}#{ask.text}ATARI{a}"
   b = del_rd(x)
   await ask.reply("≭︰تم مسح الرد")
   


@app.on_message(filters.regex("^مسح الردود$") & filters.group)
async def delrdood(app,message):
   get = await get_rtba(message.chat.id, message.from_user.id)
   if not get: return await message.reply("≭︰هذا االأمر لا يخصك")
   a = del_rdod(message.chat.id)
   print(a)
   if not a : return await message.reply("≭︰تم مسح الردود هنا")
   else: return await message.reply("≭︰لاتوجد ردود هنا")



@app.on_message(filters.regex("^الردود$") & filters.group)
async def get_rdodd(app,message):
    get = await get_rtba(message.chat.id, message.from_user.id)
    if not get: return await message.reply("≭︰هذا االأمر لا يخصك")
    a = get_rdod(message.chat.id)
    if not a: return await message.reply("≭︰لا توجد ردود هنا")
    else: return await message.reply(a)


@app.on_message(filters.text & filters.group, group=1)
async def gettt_rd(app, message):
   a = get_rd(message.text, message.chat.id)
   if a: return await app.copy_message(message.chat.id, LOG, a, reply_to_message_id=message.id)
   else: return
