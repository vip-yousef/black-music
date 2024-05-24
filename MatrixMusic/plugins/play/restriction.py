import asyncio
from pyrogram import Client, filters
from pyrogram.types import Message, ChatPermissions
from pyrogram.enums import ChatMemberStatus
from datetime import datetime, timedelta
from MatrixMusic import app

@app.on_message(filters.command("تقييد", "") & filters.group & filters.reply)
async def restriction(_: Client, message: Message):
    chat_id = message.chat.id
    user_id = message.from_user.id 
    reply_to = message.reply_to_message
    replied_id = reply_to.from_user.id
    admin = ChatMemberStatus.ADMINISTRATOR
    owner = ChatMemberStatus.OWNER
    memberA = await app.get_chat_member(chat_id, user_id)
    memberB = await app.get_chat_member(chat_id, replied_id)
    if memberA.status not in [admin, owner]: return await message.reply("- يجب أن تكون مشرف في المجموعه على الأقل لإستخدام هذا الأمر .", reply_to_message_id=message.id)
    elif memberB.status in [admin, owner]: return await message.reply(f"- لا يمكنك تقييد {'المالك' if memberB.status == owner else 'المشرف'}.", reply_to_message_id=message.id)
    text = message.text.split()
    timer = datetime.now() + timedelta(seconds=int(text[1])) if len(text) > 1 else datetime.now() + timedelta(seconds=30)
    try:await app.restrict_chat_member(chat_id=chat_id, user_id=replied_id, until_date=timer, permissions=ChatPermissions(can_send_messages=False))
    except TypeError: pass
    await message.reply(f"- تم تقييدك حتى {timer.strftime('%H:%M:%S')}", reply_to_message_id=reply_to.id)
    asyncio.create_task(checker(chat_id, replied_id, timer))

            
async def checker(chat_id, user_id, until_date):
    current = datetime.now().strftime('%H:%M:%S')
    while current != until_date.strftime('%H:%M:%S'):
        current = datetime.now().strftime('%H:%M:%S')
    await app.restrict_chat_member(chat_id, user_id, permissions=ChatPermissions(can_send_messages=True))
    return
