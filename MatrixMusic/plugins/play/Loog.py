from pyrogram import enums
from pyrogram.enums import ChatType
from pyrogram import filters, Client
from MatrixMusic import app
from config import OWNER_ID
from pyrogram.types import Message
from MatrixMusic.utils.admin_check import admin_filter
from pyrogram.types import Message, CallbackQuery, InlineKeyboardMarkup, InlineKeyboardButton



# ------------------------------------------------------------------------------- #


@app.on_message(filters.command("تثبيت", [".", ""]) & admin_filter)
async def pin(_, message):
    replied = message.reply_to_message
    chat_title = message.chat.title
    chat_id = message.chat.id
    user_id = message.from_user.id
    name = message.from_user.mention
    
    if message.chat.type == enums.ChatType.PRIVATE:
        await message.reply_text("**↢ هذا مو كروب يا حلو**")
    elif not replied:
        await message.reply_text("**⋙ رد على الرسالـة علمود تكدر تثبتها !**")
    else:
        user_stats = await app.get_chat_member(chat_id, user_id)
        if user_stats.privileges.can_pin_messages and message.reply_to_message:
            try:
                await message.reply_to_message.pin()
                await message.reply_text(f"**⋙ أبشر ثبتت الرسالـة **\n\n**المجموعـة:** {chat_title}\n**المُشرف:** {name}", reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton(" 📝 ᴠɪᴇᴡs ᴍᴇssᴀɢᴇ ", url=replied.link)]]))
            except Exception as e:
                await message.reply_text(str(e))


@app.on_message(filters.command("المثبتات", [".", ""]))
async def pinned(_, message):
    chat = await app.get_chat(message.chat.id)
    if not chat.pinned_message:
        return await message.reply_text("**↢ ما بيه رسائل مثبتة.**")
    try:        
        await message.reply_text("هُنا آخر الرسائل المثبتة",reply_markup=
        InlineKeyboardMarkup([[InlineKeyboardButton(text="↢عرض الرسالة",url=chat.pinned_message.link)]]))  
    except Exception as er:
        await message.reply_text(er)


# ------------------------------------------------------------------------------- #

@app.on_message(filters.command("الغاء التثبيت", [".", ""]) & admin_filter)
async def unpin(_, message):
    replied = message.reply_to_message
    chat_title = message.chat.title
    chat_id = message.chat.id
    user_id = message.from_user.id
    name = message.from_user.mention
    
    if message.chat.type == enums.ChatType.PRIVATE:
        await message.reply_text("**↢هذا مو كروب يا حلو !**")
    elif not replied:
        await message.reply_text("**↢ رُد على الرسالـة علمود تكدر تلغي تثبيتـهــا!**")
    else:
        user_stats = await app.get_chat_member(chat_id, user_id)
        if user_stats.privileges.can_pin_messages and message.reply_to_message:
            try:
                await message.reply_to_message.unpin()
                await message.reply_text(f"**↢تم إلغاء تثبيت الرسالة بنجاح**\n\n**المجموعـة:** {chat_title}\n**المُشرف:** {name}", reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton(" 📝 ᴠɪᴇᴡs ᴍᴇssᴀɢᴇ ", url=replied.link)]]))
            except Exception as e:
                await message.reply_text(str(e))




# --------------------------------------------------------------------------------- #

@app.on_message(filters.command("مسح الصورة", [".", ""]) & admin_filter)
async def deletechatphoto(_, message):
      
      chat_id = message.chat.id
      user_id = message.from_user.id
      msg = await message.reply_text("**جاري المسـح....**")
      admin_check = await app.get_chat_member(chat_id, user_id)
      if message.chat.type == enums.ChatType.PRIVATE:
           await msg.edit("**ما تكدر تستخدم هالأمر إلّا بالمجموعات !**") 
      try:
         if admin_check.privileges.can_change_info:
             await app.delete_chat_photo(chat_id)
             await msg.edit("**↢أبشـر مسحـت صورة المجموعة !\nمن 🕊️** {}".format(message.from_user.mention))    
      except:
          await msg.edit("**↢ما عندي صلاحية ( تعديل معلومات المجموعة ) علمود كذا ما يمديني أحذف الصورة، آسف .**")


# --------------------------------------------------------------------------------- #

@app.on_message(filters.command("وضع صورة", [".", ""])& admin_filter)
async def setchatphoto(_, message):
      reply = message.reply_to_message
      chat_id = message.chat.id
      user_id = message.from_user.id
      msg = await message.reply_text("جـاري...")
      admin_check = await app.get_chat_member(chat_id, user_id)
      if message.chat.type == enums.ChatType.PRIVATE:
           await msg.edit("`ما يمديك تستخدم هالأمر إلّا بالمجموعات !`") 
      elif not reply:
           await msg.edit("**↢بالرد على صورة معينة.**")
      elif reply:
          try:
             if admin_check.privileges.can_change_info:
                photo = await reply.download()
                await message.chat.set_photo(photo=photo)
                await msg.edit_text("**↢ أبشر غيرت صورة المجموعة\nمن 🕊️** {}".format(message.from_user.mention))
             else:
                await msg.edit("**↢خطـأ، جرب صورة ثانية.**")
     
          except:
              await msg.edit("**↢ ما عندي صلاحية ( تغيير معلومات المجموعة ) عشان كذا ما أقدر أحط صورة للمجموعة، آسف**")


# --------------------------------------------------------------------------------- #

@app.on_message(filters.command("وضع اسم", [".", ""])& admin_filter)
async def setgrouptitle(_, message):
    reply = message.reply_to_message
    chat_id = message.chat.id
    user_id = message.from_user.id
    msg = await message.reply_text("جاري...")
    if message.chat.type == enums.ChatType.PRIVATE:
          await msg.edit("**ما يمديك تستخدم هالأمر إلّا بالمجموعات !**")
    elif reply:
          try:
            title = message.reply_to_message.text
            admin_check = await app.get_chat_member(chat_id, user_id)
            if admin_check.privileges.can_change_info:
               await message.chat.set_title(title)
               await msg.edit("**↢أبشر حطيت اسم جديد للمجموعة !\nمن 🕊️** {}".format(message.from_user.mention))
          except AttributeError:
                await msg.edit("**ما عندي الصلاحية عشان أغير اسم المجموعة**")   
    elif len(message.command) >1:
        try:
            title = message.text.split(None, 1)[1]
            admin_check = await app.get_chat_member(chat_id, user_id)
            if admin_check.privileges.can_change_info:
               await message.chat.set_title(title)
               await msg.edit("**أبشر غيرت اسم المجموعة !\nمن 🕊️** {}".format(message.from_user.mention))
        except AttributeError:
               await msg.edit("**ما عندي الصلاحية عشان أغير اسم المجموعة**")
          

    else:
       await msg.edit("**↢امنحني الاسم أو الصورة جنب الأمر أو بالرد على الأمر .**")


# --------------------------------------------------------------------------------- #



@app.on_message(filters.command("وضع وصف", [".", ""]) & admin_filter)
async def setg_discription(_, message):
    reply = message.reply_to_message
    chat_id = message.chat.id
    user_id = message.from_user.id
    msg = await message.reply_text("**جاري...**")
    if message.chat.type == enums.ChatType.PRIVATE:
        await msg.edit("**↢هذا الأمر يعمل في المجموعات!**")
    elif reply:
        try:
            discription = message.reply_to_message.text
            admin_check = await app.get_chat_member(chat_id, user_id)
            if admin_check.privileges.can_change_info:
                await message.chat.set_description(discription)
                await msg.edit("**↢أبشر غيرت وصف المجموعة!**\nمن 🕊️ {}".format(message.from_user.mention))
        except AttributeError:
            await msg.edit("**↢ما يمي الصلاحية عشان أغير الوصف .**")   
    elif len(message.command) > 1:
        try:
            discription = message.text.split(None, 1)[1]
            admin_check = await app.get_chat_member(chat_id, user_id)
            if admin_check.privileges.can_change_info:
                await message.chat.set_description(discription)
                await msg.edit("**تم تغيير وصف المجموعة!**\nمن 🕊️ {}".format(message.from_user.mention))
        except AttributeError:
            await msg.edit("**↢ليس لدي الصلاحية لأغير الوصف**")
    else:
        await msg.edit("**↢رُد على الوصف المراد أو اكتب الوصف المراد جنب الأمر**")


# --------------------------------------------------------------------------------- #

@app.on_message(filters.command("غادر", [".", ""])& filters.user(OWNER_ID))
async def bot_leave(_, message):
    chat_id = message.chat.id
    text = "**↢أنا مغادر، سلام 🚶....**"
    await message.reply_text(text)
    await app.leave_chat(chat_id=chat_id, delete=True)


# -----------------------------------------------------تعريب - @NUNUU---------------------------- #
