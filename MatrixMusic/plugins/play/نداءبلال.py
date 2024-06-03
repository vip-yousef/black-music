import asyncio
import random
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram import filters, Client
from MatrixMusic import app
from config import OWNER_ID

@app.on_message(filters.command(['نداء'], prefixes=""))
def call_random_member(client, message):
    chat_id = message.chat.id
    members = [
        member for member in client.iter_chat_members(chat_id)
        if not member.user.is_bot
    ]
    random_member = random.choice(members)
    random_member_mention = f"[{random_member.user.first_name}](tg://user?id={random_member.user.id})"
    random_message = random.choice([
        f"تبغى عصير ؟  {random_member_mention}",
        f"• ممـڪن نتعــرف؟ :   {random_member_mention}",
        f"حياتـي تاتـي  :  {random_member_mention}",
        f"جمالك ذوبني  :  {random_member_mention}",
        f"ويــن طامــس يحـلــو : غسان  :  {random_member_mention}",
        f"ويــن طامــس يحـلــو  :  {random_member_mention}",
        f"حبــي الـڪ ادمان :  {random_member_mention}",
        f"تع ابوسـڪ يعسل :✨🤍  :  {random_member_mention}",
        f"• تعـا نورنـھَہّ يقمر : {random_member_mention}",
        f"• تعـال شارڪ ويانھَہّ   ♥ {random_member_mention}"
    ])
    client.send_message(chat_id, random_message, reply_to_message_id=message.message_id, parse_mode='markdown')



@app.on_message(filters.command(['الزواج'], prefixes=""))
def call_random_member(client, message):
    chat_id = message.chat.id
    members = [
        member for member in client.iter_chat_members(chat_id)
        if not member.user.is_bot
    ]
    random_member = random.choice(members)
    random_member_mention = f"[{random_member.user.first_name}](tg://user?id={random_member.user.id})"
    random_message = random.choice([
        f"**• اخترت لك هذا الشخص** {random_member_mention} \n **اعلنكم الان امام الجروب زوجاً وزوجه يلا روحو بف اعملو واحد🙈♥**",
        f"**• اخترت لك هذا الشخص** \n {random_member_mention} \n **انتم الان متزوجين رسميا يلا روحو بف اعملو واحد🌚♥**"
    ])
    client.send_message(chat_id, random_message, reply_to_message_id=message.message_id, parse_mode='markdown')

print("OKAY ITALY MUSIC CODE WORKING NOW⚡")
