from pyrogram import Client, filters
from pyrogram.types import Message
from MatrixMusic import app
from MatrixMusic.utils.database import get_served_chats
from config import LOGGER_ID


async def lul_message(chat_id: int, message: str):
    await app.send_message(chat_id=chat_id, text=message)


@app.on_message(filters.new_chat_members)
async def on_new_chat_members(client: Client, message: Message):
    if (await client.get_me()).id in [user.id for user in message.new_chat_members]:
        added_by = message.from_user.first_name if message.from_user else "مستخدم غير معروف"
        added_id = message.from_user.id

        matlabi_jhanto = message.chat.title
        served_chats = len(await get_served_chats())
        chat_id = message.chat.id

        chat = await client.get_chat(int(chat_id))
        cont = chat.members_count
        
        if message.chat.username:
            chatusername = f"@{message.chat.username}"
        else:
            chatusername = "القروب خاص"
        lemda_text = f"≭︰تم اضافة البوت الى قروب جديد .\n⎯ ⎯ ⎯ ⎯ ⎯ ⎯ ⎯ ⎯\n≭︰<b>القروب</b> › : {matlabi_jhanto}\n≭︰<b>ايدي القروب</b> › : {chat_id}\n≭︰<b>اسم القروب</b> › : {chatusername}\n≭︰<b>عدد الاعضاء</b> › : {cont}\n≭︰<b>مجموع القروب</b> › : {served_chats}\n≭︰<b>تم اضافة البوت بواسطة</b> › :\n⎯ ⎯ ⎯ ⎯ ⎯ ⎯ ⎯ ⎯<a href='tg://user?id={added_id}'>{added_by}</a>"
        await lul_message(LOGGER_ID, lemda_text)
