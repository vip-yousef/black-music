import json
from pyrogram import Client, filters
from pyrogram.enums import ChatMembersFilter
from pyrogram import enums
import json
from pyrogram import Client, filters
from MatrixMusic import app







@app.on_message(filters.command("رفع مالك", ""))
def promote_owner(client, message):
    if message.reply_to_message and message.reply_to_message.from_user:
        target = message.reply_to_message.from_user.id
        user_id = str(target)
    elif message.reply_to_message is None:
        target = message.text.split()[2]
        user = app.get_users(target)
        if user:
            user_id = str(user.id)
        else:
            message.reply_text("لا يمكن العثور على المستخدم")
            return
    else:
        target = message.text.split()[1].strip("@")
        user = app.get_users(target)
        if user:
            user_id = str(user.id)
        else:
            message.reply_text("لا يمكن العثور على المستخدم")
            return

    chat_id = str(message.chat.id)
    tom_owners = load_tom_owners()

    if (not TOM(client, message, message) and not basic_dev(client, message, message) and not OWNER_ID(client, message, message) and not dev(client, message, message) and not is_basic_creator(client, message, message)):
        message.reply_text("""◍ انت لست المنشئ الاساسي
√""")
        return
    if chat_id not in tom_owners['owners']:
        tom_owners['owners'][chat_id] = {'owner_id': []}

    if user_id in tom_owners['owners'][chat_id]['owner_id']:
        message.reply_text("""◍ هذا المستخدم مالك بالفعل
√""")
    else:
        tom_owners['owners'][chat_id]['owner_id'].append(user_id)
        dump_tom_owners(tom_owners)
        message.reply_text("""◍ تم رفع المستخدم ليصبح مالك
√""")


@app.on_message(filters.command("تنزيل مالك", ""))
def demote_owner(client, message):
    if message.reply_to_message and message.reply_to_message.from_user:
        target = message.reply_to_message.from_user.id
        user_id = str(target)
    elif message.reply_to_message is None:
        target = message.text.split()[2]
        user = app.get_users(target)
        if user:
            user_id = str(user.id)
        else:
            message.reply_text("لا يمكن العثور على المستخدم")
            return
    else:
        target = message.text.split()[1].strip("@")
        user = app.get_users(target)
        if user:
            user_id = str(user.id)
        else:
            message.reply_text("لا يمكن العثور على المستخدم")
            return

    chat_id = str(message.chat.id)

    tom_owners = load_tom_owners()
    if (not TOM(client, message, message) and not basic_dev(client, message, message) and not OWNER_ID(client, message, message) and not dev(client, message, message) and not is_basic_creator(client, message, message)):
        message.reply_text("""◍ انت لست المنشئ الاساسي
√""")
        return
    if chat_id not in tom_owners['owners']:
        message.reply_text("لا يوجد مالكين في هذه الدردشة حتى الأن")
        return

    if user_id not in tom_owners['owners'][chat_id]['owner_id']:
        message.reply_text("""◍ هذا المستخدم ليس مالك لتنزيله
√""")
    else:
        tom_owners['owners'][chat_id]['owner_id'].remove(user_id)
        dump_tom_owners(tom_owners)
        message.reply_text("""◍ تم تنزيل المستخدم من المالكين بنجاح
√""")


@app.on_message(filters.command("مسح المالكين", ""))
def clear_owner(client, message):
    chat_id = str(message.chat.id)
    tom_owners = load_tom_owners()
    if (not TOM(client, message, message) and not basic_dev(client, message, message) and not OWNER_ID(client, message, message) and not dev(client, message, message) and not is_basic_creator(client, message, message)):
        message.reply_text("""◍ انت لست المنشئ الاساسي
√""")
        return
    if chat_id in tom_owners['owners']:
        tom_owners['owners'][chat_id]['owner_id'] = []
        dump_tom_owners(tom_owners)
        message.reply_text("""◍ تم مسح المالكين بنجاح
√""")
    else:
        message.reply_text("لا يوجد مالكين ليتم مسحهم")





@app.on_message(filters.command("المالكين", ""))
def get_owner(client, message):
    chat_id = str(message.chat.id)
    tom_owners = load_tom_owners()
    if (not TOM(client, message, message) and not basic_dev(client, message, message) and not OWNER_ID(client, message, message) and not dev(client, message, message) and not is_basic_creator(client, message, message) and not owner(client, message, message)):
        message.reply_text("""◍ يجب ان تكون مالك على الاقل لستخدام الامر
√""")
        return
    if chat_id not in tom_owners['owners']:
        message.reply_text("لا يوجد مالكين حتى الأن")
        return

    admins = tom_owners['owners'][chat_id]['owner_id']
    if not admins:
        message.reply_text("لا يوجد مالكين حتى الأن")
    else:
        admin_names = []
        for admin_id in admins:
            user = app.get_users(int(admin_id))
            if user:
                admin_names.append(f"[{user.first_name}](tg://user?id={user.id})")

        if admin_names:
            admin_list = "\n".join(admin_names)
            message.reply_text(f"◍ قائمة المالكين:\n\n{admin_list}")
        else:
            message.reply_text("تعذر العثور على معلومات المالكين")






@app.on_message(filters.command("رفع ادمن", ""))
def promote_admin(client, message):
    if message.reply_to_message and message.reply_to_message.from_user:
        target = message.reply_to_message.from_user.id
        user_id = str(target)
    elif message.reply_to_message is None:
        target = message.text.split()[2]
        user = app.get_users(target)
        if user:
            user_id = str(user.id)
        else:
            message.reply_text("لا يمكن العثور على المستخدم")
            return
    else:
        target = message.text.split()[1].strip("@")
        user = app.get_users(target)
        if user:
            user_id = str(user.id)
        else:
            message.reply_text("لا يمكن العثور على المستخدم")
            return

    chat_id = str(message.chat.id)
    tom_admin = load_tom_admin()

    if (not TOM(client, message, message) and not basic_dev(client, message, message) and not OWNER_ID(client, message, message) and not dev(client, message, message) and not is_basic_creator(client, message, message) and not owner(client, message, message) and not creator(client, message, message)):
        message.reply_text("""◍ يجب ان تكون منشئ على الاقل لكى تستطيع رفع ادمن
√""")
        return

    if chat_id not in tom_admin['admin']:
        tom_admin['admin'][chat_id] = {'admin_id': []}

    if user_id in tom_admin['admin'][chat_id]['admin_id']:
        message.reply_text("""◍ هذا المستخدم ادمن بالفعل
√""")
    else:
        tom_admin['admin'][chat_id]['admin_id'].append(user_id)
        dump_tom_admin(tom_admin)
        message.reply_text("""◍ تم رفع المستخدم ليصبح ادمن
√""")




@app.on_message(filters.command("تنزيل ادمن", ""))
def demote_admin(client, message):
    if message.reply_to_message and message.reply_to_message.from_user:
        target = message.reply_to_message.from_user.id
        user_id = str(target)
    elif message.reply_to_message is None:
        target = message.text.split()[2]
        user = app.get_users(target)
        if user:
            user_id = str(user.id)
        else:
            message.reply_text("لا يمكن العثور على المستخدم")
            return
    else:
        target = message.text.split()[1].strip("@")
        user = app.get_users(target)
        if user:
            user_id = str(user.id)
        else:
            message.reply_text("لا يمكن العثور على المستخدم")
            return
    chat_id = str(message.chat.id)
    

    tom_admin = load_tom_admin()
    if (not TOM(client, message, message) and not basic_dev(client, message, message) and not OWNER_ID(client, message, message) and not dev(client, message, message) and not is_basic_creator(client, message, message) and not owner(client, message, message) and not creator(client, message, message)):
        message.reply_text("""◍ يجب ان تكون منشئ على الاقل لكى تستطيع تنزيل ادمن
√""")
        return
    if chat_id not in tom_admin['admin']:
        message.reply_text("لا يوجد مشرفين حتى الأن")
        return

    if user_id not in tom_admin['admin'][chat_id]['admin_id']:
        message.reply_text("""◍ هذا المستخدم ليس ادمن لتنزيله
√""")
    else:
        tom_admin['admin'][chat_id]['admin_id'].remove(user_id)
        dump_tom_admin(tom_admin)
        message.reply_text("""◍ تم تنزيل المستخدم من الادمن بنجاح
√""")



@app.on_message(filters.command("مسح الادمنيه", ""))
def clear_admins(client, message):
    chat_id = str(message.chat.id)
    tom_admin = load_tom_admin()
    if (not TOM(client, message, message) and not basic_dev(client, message, message) and not OWNER_ID(client, message, message) and not dev(client, message, message) and not is_basic_creator(client, message, message) and not owner(client, message, message) and not creator(client, message, message)):
        message.reply_text("""◍ يجب ان تكون منشئ على الاقل لستخدام الامر
√""")
        return
    if chat_id in tom_admin['admin']:
        tom_admin['admin'][chat_id]['admin_id'] = []
        dump_tom_admin(tom_admin)
        message.reply_text("""◍ تم مسح الادمنيه بنجاح
√""")
    else:
        message.reply_text("لا يوجد ادمنيه ليتم مسحهم")






@app.on_message(filters.command("الادمنيه", ""))
def get_admins(client, message):
    chat_id = str(message.chat.id)
    tom_admin = load_tom_admin()

    if chat_id not in tom_admin['admin']:
        message.reply_text("لا يوجد مشرفين في هذه الدردشة")
        return

    admins = tom_admin['admin'][chat_id]['admin_id']
    if not admins:
        message.reply_text("لا يوجد مشرفين في هذه الدردشة")
    else:
        admin_names = []
        for admin_id in admins:
            user = app.get_users(int(admin_id))
            if user:
                admin_names.append(f"[{user.first_name}](tg://user?id={user.id})")

        
        if admin_names:
            admin_list = "\n".join(admin_names)
            message.reply_text(f"◍ قائمة المشرفين:\n\n{admin_list}")
        else:
            message.reply_text("تعذر العثور على معلومات المشرفين")






@app.on_message(filters.command("رفع ثانوي", ""))
def promote_basic_dev(client, message):
    if message.reply_to_message and message.reply_to_message.from_user:
        target = message.reply_to_message.from_user.id
        user_id = str(target)
    elif message.reply_to_message is None:
        target = message.text.split()[2]
        user = app.get_users(target)
        if user:
            user_id = str(user.id)
        else:
            message.reply_text("لا يمكن العثور على المستخدم")
            return
    else:
        target = message.text.split()[1].strip("@")
        user = app.get_users(target)
        if user:
            user_id = str(user.id)
        else:
            message.reply_text("لا يمكن العثور على المستخدم")
            return

    tom_basic_devs = load_tom_basic_devs()

    if (not TOM(client, message, message) and not OWNER_ID(client, message, message)):
        message.reply("""◍ انت لست المطور الاساسي
√""")
    elif user_id in tom_basic_devs['basic_devs']:
        message.reply_text("""◍ هذا المستخدم مطور ثانوي بالفعل
√""")
    else:
        tom_basic_devs['basic_devs'][user_id] = True
        dump_tom_basic_devs(tom_basic_devs)
        message.reply_text("""◍ تم رفع المستخدم ليصبح مطور ثانوي
√""")





@app.on_message(filters.command("الثانويين", ""))
def list_basic_devs(client, message):
    tom_basic_devs = load_tom_basic_devs()

    if (not TOM(client, message, message) and not basic_dev(client, message, message) and not OWNER_ID(client, message, message)):
        message.reply("""◍ انت لست المطور الثانوي
√""")
        return

    basic_devs = tom_basic_devs['basic_devs']
    if not basic_devs:
        message.reply_text("لا يوجد مطورين ثانويين")
    else:
        basic_dev_names = []
        for basic_dev_id in basic_devs:
            user = app.get_users(int(basic_dev_id))
            if user:
                basic_dev_names.append(f"[{user.first_name}](tg://user?id={user.id})")

        if basic_dev_names:
            basic_dev_list = "\n".join(basic_dev_names)
            message.reply_text(f"◍ قائمة الثانويين:\n\n{basic_dev_list}")
        else:
            message.reply_text("تعذر العثور على معلومات المطورين الثانويين")


@app.on_message(filters.command("تنزيل ثانوي", ""))
def demote_basic_dev(client, message):
    if message.reply_to_message and message.reply_to_message.from_user:
        target = message.reply_to_message.from_user.id
        user_id = str(target)
    elif message.reply_to_message is None:
        target = message.text.split()[2]
        user = app.get_users(target)
        if user:
            user_id = str(user.id)
        else:
            message.reply_text("لا يمكن العثور على المستخدم")
            return
    else:
        target = message.text.split()[1].strip("@")
        user = app.get_users(target)
        if user:
            user_id = str(user.id)
        else:
            message.reply_text("لا يمكن العثور على المستخدم")
            return

    tom_basic_devs = load_tom_basic_devs()
    if (not TOM(client, message, message) and not OWNER_ID(client, message, message)):
        message.reply_text("""◍ انت لست المطور الاساسي
√""")
        return

    if user_id not in tom_basic_devs['basic_devs']:
        message.reply_text("""◍ هذا المستخدم ليس ثانويا لتنزيله
√""")
    else:
        del tom_basic_devs['basic_devs'][user_id]
        dump_tom_basic_devs(tom_basic_devs)
        message.reply_text("""◍ تم تنزيل المستخدم من الثانويين بنجاح
√""")


@app.on_message(filters.command("مسح الثانويين", ""))
def clear_basic_devs(client, message):
    tom_basic_devs = load_tom_basic_devs()
    if (not TOM(client, message, message) and not OWNER_ID(client, message, message)):
        message.reply_text("""◍ انت لست المطور الاساسي
√""")
        return
    if 'basic_devs' in tom_basic_devs:
        tom_basic_devs['basic_devs'] = {}
        dump_tom_basic_devs(tom_basic_devs)
        message.reply_text("""◍ تم مسح الثانويين بنجاح
√""")
    else:
        message.reply_text("لا يوجد ثانويين ليتم مسحهم")







@app.on_message(filters.command("رفع مطور", ""))
def promote_devs(client, message):
    if message.reply_to_message and message.reply_to_message.from_user:
        target = message.reply_to_message.from_user.id
        user_id = str(target)
    elif message.reply_to_message is None:
        target = message.text.split()[2]
        user = app.get_users(target)
        if user:
            user_id = str(user.id)
        else:
            message.reply_text("لا يمكن العثور على المستخدم")
            return
    else:
        target = message.text.split()[1].strip("@")
        user = app.get_users(target)
        if user:
            user_id = str(user.id)
        else:
            message.reply_text("لا يمكن العثور على المستخدم")
            return

    tom_devs = load_tom_devs()

    if (not TOM(client, message, message) and not basic_dev(client, message, message) and not OWNER_ID(client, message, message)):
        message.reply_text("""◍ انت لست المطور الثانوي
√""")
        return

    if user_id in tom_devs['devs']:
        message.reply_text("""◍ هذا المستخدم مطور بالفعل
√""")
    else:
        tom_devs['devs'][user_id] = True
        dump_tom_devs(tom_devs)
        message.reply_text("""◍ تم رفع المستخدم ليصبح مطور
√""")



@app.on_message(filters.command("المطورين", ""))
def get_devs(client, message):
    chat_id = str(message.chat.id)
    tom_devs = load_tom_devs()
    if (not TOM(client, message, message) and not basic_dev(client, message, message) and not OWNER_ID(client, message, message) and not dev(client, message, message)):
        message.reply_text("""◍ انت لست المطور
√""")
        return

    if 'devs' not in tom_devs:
        message.reply_text("لا يوجد مطورين حتى الأن")
        return

    admins = tom_devs['devs']
    if not admins:
        message.reply_text("لا يوجد مطورين حتى الأن")
    else:
        admin_names = []
        for admin_id in admins:
            user = app.get_users(int(admin_id))
            if user:
                admin_names.append(f"[{user.first_name}](tg://user?id={user.id})")

        if admin_names:
            admin_list = "\n".join(admin_names)
            message.reply_text(f"◍ قائمة المطورين:\n\n{admin_list}")
        else:
            message.reply_text("تعذر العثور على معلومات المطورين")



@app.on_message(filters.command("تنزيل مطور", ""))
def demote_devs(client, message):
    if message.reply_to_message and message.reply_to_message.from_user:
        target = message.reply_to_message.from_user.id
        user_id = str(target)
    elif message.reply_to_message is None:
        target = message.text.split()[2]
        user = app.get_users(target)
        if user:
            user_id = str(user.id)
        else:
            message.reply_text("لا يمكن العثور على المستخدم")
            return
    else:
        target = message.text.split()[1].strip("@")
        user = app.get_users(target)
        if user:
            user_id = str(user.id)
        else:
            message.reply_text("لا يمكن العثور على المستخدم")
            return
    chat_id = str(message.chat.id)

    tom_devs = load_tom_devs()
    if (not TOM(client, message, message) and not basic_dev(client, message, message) and not OWNER_ID(client, message, message)):
        message.reply_text("""◍ انت لست المطور الثانوي
√""")
        return

    if user_id not in tom_devs['devs']:
        message.reply_text("""◍ هذا المستخدم ليس مطور لتنزيله
√""")
    else:
        del tom_devs['devs'][user_id]
        dump_tom_devs(tom_devs)
        message.reply_text("""◍ تم تنزيل المستخدم من المطورين بنجاح
√""")

@app.on_message(filters.command("مسح المطورين", ""))
def clear_devs(client, message):
    chat_id = str(message.chat.id)
    tom_devs = load_tom_devs()
    if (not TOM(client, message, message) and not basic_dev(client, message, message) and not OWNER_ID(client, message, message)):
        message.reply_text("""◍ انت لست المطور الثانوي
√""")
        return

    if 'devs' in tom_devs:
        tom_devs['devs'] = {}
        dump_tom_devs(tom_devs)
        message.reply_text("""◍ تم مسح المطورين بنجاح
√""")
    else:
        message.reply_text("لا يوجد مطورين ليتم مسحهم")












@app.on_message(filters.command("رفع مميز", ""))
def promote_distinct(client, message):
    if message.reply_to_message and message.reply_to_message.from_user:
        target = message.reply_to_message.from_user.id
        user_id = str(target)
    elif message.reply_to_message is None:
        target = message.text.split()[2]
        user = app.get_users(target)
        if user:
            user_id = str(user.id)
        else:
            message.reply_text("لا يمكن العثور على المستخدم")
            return
    else:
        target = message.text.split()[1].strip("@")
        user = app.get_users(target)
        if user:
            user_id = str(user.id)
        else:
            message.reply_text("لا يمكن العثور على المستخدم")
            return

    chat_id = str(message.chat.id)
    tom_distinct = load_tom_distinct()

    if (not TOM(client, message, message) and not basic_dev(client, message, message) and not OWNER_ID(client, message, message) and not dev(client, message, message) and not is_basic_creator(client, message, message) and not owner(client, message, message) and not creator(client, message, message) and not admin(client, message, message)):
        message.reply_text("""◍ يجب ان تكون ادمن على الاقل لكى تستطيع رفع مميز
√""")
        return

    if chat_id not in tom_distinct['admin']:
        tom_distinct['admin'][chat_id] = {'admin_id': []}

    if user_id in tom_distinct['admin'][chat_id]['admin_id']:
        message.reply_text("""◍ هذا المستخدم مميز بالفعل
√""")
    else:
        tom_distinct['admin'][chat_id]['admin_id'].append(user_id)
        dump_tom_distinct(tom_distinct)
        message.reply_text("""◍ تم رفع المستخدم ليصبح مميز
√""")


@app.on_message(filters.command("تنزيل مميز", ""))
def demote_distinct(client, message):
    if message.reply_to_message and message.reply_to_message.from_user:
        target = message.reply_to_message.from_user.id
        user_id = str(target)
    elif message.reply_to_message is None:
        target = message.text.split()[2]
        user = app.get_users(target)
        if user:
            user_id = str(user.id)
        else:
            message.reply_text("لا يمكن العثور على المستخدم")
            return
    else:
        target = message.text.split()[1].strip("@")
        user = app.get_users(target)
        if user:
            user_id = str(user.id)
        else:
            message.reply_text("لا يمكن العثور على المستخدم")
            return
    chat_id = str(message.chat.id)

    tom_distinct = load_tom_distinct()
    if (not TOM(client, message, message) and not basic_dev(client, message, message) and not OWNER_ID(client, message, message) and not dev(client, message, message) and not is_basic_creator(client, message, message) and not owner(client, message, message) and not creator(client, message, message) and not admin(client, message, message)):
        message.reply_text("""◍ يجب ان تكون ادمن على الاقل لكى تستطيع تنزيل مميز
√""")
        return
    if chat_id not in tom_distinct['admin']:
        message.reply_text("لا يوجد مميزين حتى الأن")
        return

    if user_id not in tom_distinct['admin'][chat_id]['admin_id']:
        message.reply_text("""◍ هذا المستخدم ليس مميز لتنزيله
√""")
    else:
        tom_distinct['admin'][chat_id]['admin_id'].remove(user_id)
        dump_tom_distinct(tom_distinct)
        message.reply_text("""◍ تم تنزيل المستخدم من المميزين بنجاح
√""")


@app.on_message(filters.command("مسح المميزين", ""))
def clear_distinct(client, message):
    chat_id = str(message.chat.id)
    tom_distinct = load_tom_distinct()
    if (not TOM(client, message, message) and not basic_dev(client, message, message) and not OWNER_ID(client, message, message) and not dev(client, message, message) and not is_basic_creator(client, message, message) and not owner(client, message, message) and not creator(client, message, message) and not admin(client, message, message)):
        message.reply_text("""◍ يجب ان تكون ادمن على الاقل لكى تستطيع استخدام الأمر
√""")
        return

    if chat_id in tom_distinct['admin']:
        tom_distinct['admin'][chat_id]['admin_id'] = []
        dump_tom_distinct(tom_distinct)
        message.reply_text("""◍ تم مسح المميزين بنجاح
√""")
    else:
        message.reply_text("لا يوجد مميزين ليتم مسحهم")


@app.on_message(filters.command("المميزين", ""))
def get_distinct(client, message):
    chat_id = str(message.chat.id)
    tom_distinct = load_tom_distinct()

    if chat_id not in tom_distinct['admin']:
        message.reply_text("لا يوجد مميزين في هذه الدردشة")
        return

    admins = tom_distinct['admin'][chat_id]['admin_id']
    if not admins:
        message.reply_text("لا يوجد مميزين في هذه الدردشة")
    else:
        admin_names = []
        for admin_id in admins:
            user = app.get_users(int(admin_id))
            if user:
                admin_names.append(f"[{user.first_name}](tg://user?id={user.id})")

        if admin_names:
            admin_list = "\n".join(admin_names)
            message.reply_text(f"◍ قائمة المميزين:\n\n{admin_list}")
        else:
            message.reply_text("تعذر العثور على معلومات المميزين")











@app.on_message(filters.command("رفع منشئ اساسي", ""))
def promote_basic_creator(client, message):
    if message.reply_to_message and message.reply_to_message.from_user:
        target = message.reply_to_message.from_user.id
        user_id = str(target)
    elif message.reply_to_message is None:
        target = message.text.split()[3]
        user = app.get_users(target)
        if user:
            user_id = str(user.id)
        else:
            message.reply_text("لا يمكن العثور على المستخدم")
            return
    else:
        target = message.text.split()[2].strip("@")
        user = app.get_users(target)
        if user:
            user_id = str(user.id)
        else:
            message.reply_text("لا يمكن العثور على المستخدم")
            return

    if (not TOM(client, message, message) and not basic_dev(client, message, message) and not OWNER_ID(client, message, message) and not dev(client, message, message)):
        message.reply_text("""◍ انت لست المطور
√""")
        return
    tom_basic_creators = load_tom_basic_creators()

    if user_id in tom_basic_creators['basic_creators']:
        message.reply_text("""◍ هذا المستخدم منشئ اساسي بالفعل
√""")
    else:
        tom_basic_creators['basic_creators'][user_id] = True
        dump_tom_basic_creators(tom_basic_creators)
        message.reply_text("""◍ تم رفع المستخدم ليصبح منشئ اساسي
√""")



@app.on_message(filters.command("تنزيل منشئ اساسي", ""))
def demote_basic_creator(client, message):
    if message.reply_to_message and message.reply_to_message.from_user:
        target = message.reply_to_message.from_user.id
        user_id = str(target)
    elif message.reply_to_message is None:
        target = message.text.split()[3]
        user = app.get_users(target)
        if user:
            user_id = str(user.id)
        else:
            message.reply_text("لا يمكن العثور على المستخدم")
            return
    else:
        target = message.text.split()[2].strip("@")
        user = app.get_users(target)
        if user:
            user_id = str(user.id)
        else:
            message.reply_text("لا يمكن العثور على المستخدم")
            return

    if (not TOM(client, message, message) and not basic_dev(client, message, message) and not OWNER_ID(client, message, message) and not dev(client, message, message)):
        message.reply_text("""◍ انت لست المطور
√""")
        return
        
    tom_basic_creators = load_tom_basic_creators()

    if user_id not in tom_basic_creators['basic_creators']:
        message.reply_text("""◍ هذا المستخدم ليس منشئ اساسي لتنزيله
√""")
    else:
        del tom_basic_creators['basic_creators'][user_id]
        dump_tom_basic_creators(tom_basic_creators)
        message.reply_text("""◍ تم تنزيل المستخدم من المنشئين الاساسيين بنجاح
√""")


@app.on_message(filters.command("المنشئين الاساسيين", ""))
def get_basic_creators(client, message):
    tom_basic_creators = load_tom_basic_creators()
    if (not TOM(client, message, message) and not basic_dev(client, message, message) and not OWNER_ID(client, message, message) and not dev(client, message, message) and not is_basic_creator(client, message, message)):
        message.reply_text("""◍ انت لست المنشئ الاساسي
√""")
        return

    if 'basic_creators' not in tom_basic_creators:
        message.reply_text("لا يوجد منشئين اساسيين حتى الأن")
        return

    basic_creators = tom_basic_creators['basic_creators']
    if not basic_creators:
        message.reply_text("لا يوجد منشئين اساسيين حتى الأن")
    else:
        creator_names = []
        for creator_id in basic_creators:
            user = app.get_users(int(creator_id))
            if user:
                creator_names.append(f"[{user.first_name}](tg://user?id={user.id})")

        if creator_names:
            creator_list = "\n".join(creator_names)
            message.reply_text(f"◍ قائمة المنشئين الاساسيين:\n\n{creator_list}")
        else:
            message.reply_text("تعذر العثور على معلومات المنشئين الاساسيين")

@app.on_message(filters.command("مسح المنشئين الاساسيين", ""))
def clear_basic_creators(client, message):
    tom_basic_creators = load_tom_basic_creators()
    if (not TOM(client, message, message) and not basic_dev(client, message, message) and not OWNER_ID(client, message, message) and not dev(client, message, message)):
        message.reply_text("""◍ انت لست المطور
√""")
        return

    if 'basic_creators' in tom_basic_creators:
        tom_basic_creators['basic_creators'] = {}
        dump_tom_basic_creators(tom_basic_creators)
        message.reply_text("""◍ تم مسح المنشئين الاساسيين بنجاح
√""")
    else:
        message.reply_text("لا يوجد منشئين اساسيين ليتم مسحهم")





@app.on_message(filters.command("رفع منشئ", ""))
def promote_creator(client, message):
    if message.reply_to_message and message.reply_to_message.from_user:
        target = message.reply_to_message.from_user.id
        user_id = str(target)
    elif message.reply_to_message is None:
        target = message.text.split()[2]
        user = app.get_users(target)
        if user:
            user_id = str(user.id)
        else:
            message.reply_text("لا يمكن العثور على المستخدم")
            return
    else:
        target = message.text.split()[1].strip("@")
        user = app.get_users(target)
        if user:
            user_id = str(user.id)
        else:
            message.reply_text("لا يمكن العثور على المستخدم")
            return

    chat_id = str(message.chat.id)
    tom_creators = load_tom_creators()

    if (not TOM(client, message, message) and not basic_dev(client, message, message) and not OWNER_ID(client, message, message) and not dev(client, message, message) and not is_basic_creator(client, message, message) and not owner(client, message, message)):
        message.reply_text("""◍ يجب ان تكون مالك حتى تستطيع رفع منشئ
√""")
        return
    if chat_id not in tom_creators['creators']:
        tom_creators['creators'][chat_id] = {'creator_id': []}

    if user_id in tom_creators['creators'][chat_id]['creator_id']:
        message.reply_text("""◍ هذا المستخدم منشئ بالفعل
√""")
    else:
        tom_creators['creators'][chat_id]['creator_id'].append(user_id)
        dump_tom_creators(tom_creators)
        message.reply_text("""◍ تم رفع المستخدم ليصبح منشئ
√""")




@app.on_message(filters.command("تنزيل منشئ", ""))
def demote_creator(client, message):
    if message.reply_to_message and message.reply_to_message.from_user:
        target = message.reply_to_message.from_user.id
        user_id = str(target)
    elif message.reply_to_message is None:
        target = message.text.split()[2]
        user = app.get_users(target)
        if user:
            user_id = str(user.id)
        else:
            message.reply_text("لا يمكن العثور على المستخدم")
            return
    else:
        target = message.text.split()[1].strip("@")
        user = app.get_users(target)
        if user:
            user_id = str(user.id)
        else:
            message.reply_text("لا يمكن العثور على المستخدم")
            return
    chat_id = str(message.chat.id)
    
    tom_creators = load_tom_creators()
    if (not TOM(client, message, message) and not basic_dev(client, message, message) and not OWNER_ID(client, message, message) and not dev(client, message, message) and not is_basic_creator(client, message, message) and not owner(client, message, message)):
        message.reply_text("""◍ يجب ان تكون مالك حتى تستطيع تنزيل منشئ
√""")
        return
    if chat_id not in tom_creators['creators']:
        message.reply_text("لا يوجد منشئين حتى الأن")
        return

    if user_id not in tom_creators['creators'][chat_id]['creator_id']:
        message.reply_text("""◍ هذا المستخدم ليس منشئ لتنزيله
√""")
    else:
        tom_creators['creators'][chat_id]['creator_id'].remove(user_id)
        dump_tom_creators(tom_creators)
        message.reply_text("""◍ تم تنزيل المستخدم من المنشئين بنجاح
√""")



@app.on_message(filters.command("مسح المنشئين", ""))
def clear_creators(client, message):
    chat_id = str(message.chat.id)
    tom_creators = load_tom_creators()
    if (not TOM(client, message, message) and not basic_dev(client, message, message) and not OWNER_ID(client, message, message) and not dev(client, message, message) and not is_basic_creator(client, message, message) and not owner(client, message, message)):
        message.reply_text("""◍ يجب ان تكون مالك حتى تستطيع حذف المنشئين
√""")
        return
    if chat_id in tom_creators['creators']:
        tom_creators['creators'][chat_id]['creator_id'] = []
        dump_tom_creators(tom_creators)
        message.reply_text("""◍ تم حذف المنشئين
√""")
    else:
        message.reply_text("""◍ لا يوجد منشئين
√""")






@app.on_message(filters.command("المنشئين", ""))
def get_creators(client, message):
    chat_id = str(message.chat.id)
    tom_creators = load_tom_creators()
    if (not TOM(client, message, message) and not basic_dev(client, message, message) and not OWNER_ID(client, message, message) and not dev(client, message, message) and not is_basic_creator(client, message, message) and not owner(client, message, message) and not creator(client, message, message)):
        message.reply_text("""◍ يجب ان تكون منشئ على الاقل لستخدام الامر
√""")
        return
    if chat_id not in tom_creators['creators']:
        message.reply_text("""◍ لا يوجد منشئين
√""")
        return
    admins = tom_creators['creators'][chat_id]['creator_id']
    if not admins:
        message.reply_text("""◍ لا يوجد منشئين
√""")
    else:
        admin_names = []
        for admin_id in admins:
            user = app.get_users(int(admin_id))
            if user:
                admin_names.append(f"[{user.first_name}](tg://user?id={user.id})")

        
        if admin_names:
            admin_list = "\n".join(admin_names)
            message.reply_text(f"◍ قائمة المنشئين:\n\n{admin_list}")
        else:
            message.reply_text("تعذر العثور على معلومات المنشئين")
