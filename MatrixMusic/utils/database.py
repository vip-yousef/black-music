import random
from typing import Dict, List, Union
from MatrixMusic import userbot
from MatrixMusic.core.mongo import mongodb
from dbh import dbcGeneral, dbGeneral

authdb = mongodb.adminauth
authuserdb = mongodb.authuser
autoenddb = mongodb.autoend
assdb = mongodb.assistants
blacklist_chatdb = mongodb.blacklistChat
blockeddb = mongodb.blockedusers
chatsdb = mongodb.chats
channeldb = mongodb.cplaymode
countdb = mongodb.upcount
gbansdb = mongodb.gban
langdb = mongodb.language
onoffdb = mongodb.onoffper
playmodedb = mongodb.playmode
playtypedb = mongodb.playtypedb
skipdb = mongodb.skipmode
sudoersdb = mongodb.sudoers
usersdb = mongodb.tgusersdb

# Shifting to memory [mongo sucks often]
active = []
activevideo = []
assistantdict = {}
autoend = {}
count = {}
channelconnect = {}
langm = {}
loop = {}
maintenance = []
nonadmin = {}
pause = {}
playmode = {}
playtype = {}
skipmode = {}


async def get_assistant_number(chat_id: int) -> str:
    assistant = assistantdict.get(chat_id)
    return assistant


async def get_client(assistant: int):
    if int(assistant) == 1:
        return userbot.one
    elif int(assistant) == 2:
        return userbot.two
    elif int(assistant) == 3:
        return userbot.three
    elif int(assistant) == 4:
        return userbot.four
    elif int(assistant) == 5:
        return userbot.five


async def set_assistant_new(chat_id, number):
    number = int(number)
    await assdb.update_one(
        {"chat_id": chat_id},
        {"$set": {"assistant": number}},
        upsert=True,
    )


async def set_assistant(chat_id):
    from MatrixMusic.core.userbot import assistants

    ran_assistant = random.choice(assistants)
    assistantdict[chat_id] = ran_assistant
    await assdb.update_one(
        {"chat_id": chat_id},
        {"$set": {"assistant": ran_assistant}},
        upsert=True,
    )
    userbot = await get_client(ran_assistant)
    return userbot


async def get_assistant(chat_id: int) -> str:
    from MatrixMusic.core.userbot import assistants

    assistant = assistantdict.get(chat_id)
    if not assistant:
        dbassistant = await assdb.find_one({"chat_id": chat_id})
        if not dbassistant:
            userbot = await set_assistant(chat_id)
            return userbot
        else:
            got_assis = dbassistant["assistant"]
            if got_assis in assistants:
                assistantdict[chat_id] = got_assis
                userbot = await get_client(got_assis)
                return userbot
            else:
                userbot = await set_assistant(chat_id)
                return userbot
    else:
        if assistant in assistants:
            userbot = await get_client(assistant)
            return userbot
        else:
            userbot = await set_assistant(chat_id)
            return userbot


async def set_calls_assistant(chat_id):
    from MatrixMusic.core.userbot import assistants

    ran_assistant = random.choice(assistants)
    assistantdict[chat_id] = ran_assistant
    await assdb.update_one(
        {"chat_id": chat_id},
        {"$set": {"assistant": ran_assistant}},
        upsert=True,
    )
    return ran_assistant


async def group_assistant(self, chat_id: int) -> int:
    from MatrixMusic.core.userbot import assistants

    assistant = assistantdict.get(chat_id)
    if not assistant:
        dbassistant = await assdb.find_one({"chat_id": chat_id})
        if not dbassistant:
            assis = await set_calls_assistant(chat_id)
        else:
            assis = dbassistant["assistant"]
            if assis in assistants:
                assistantdict[chat_id] = assis
                assis = assis
            else:
                assis = await set_calls_assistant(chat_id)
    else:
        if assistant in assistants:
            assis = assistant
        else:
            assis = await set_calls_assistant(chat_id)
    if int(assis) == 1:
        return self.one
    elif int(assis) == 2:
        return self.two
    elif int(assis) == 3:
        return self.three
    elif int(assis) == 4:
        return self.four
    elif int(assis) == 5:
        return self.five


async def is_skipmode(chat_id: int) -> bool:
    mode = skipmode.get(chat_id)
    if not mode:
        user = await skipdb.find_one({"chat_id": chat_id})
        if not user:
            skipmode[chat_id] = True
            return True
        skipmode[chat_id] = False
        return False
    return mode


async def skip_on(chat_id: int):
    skipmode[chat_id] = True
    user = await skipdb.find_one({"chat_id": chat_id})
    if user:
        return await skipdb.delete_one({"chat_id": chat_id})


async def skip_off(chat_id: int):
    skipmode[chat_id] = False
    user = await skipdb.find_one({"chat_id": chat_id})
    if not user:
        return await skipdb.insert_one({"chat_id": chat_id})


async def get_upvote_count(chat_id: int) -> int:
    mode = count.get(chat_id)
    if not mode:
        mode = await countdb.find_one({"chat_id": chat_id})
        if not mode:
            return 5
        count[chat_id] = mode["mode"]
        return mode["mode"]
    return mode


async def set_upvotes(chat_id: int, mode: int):
    count[chat_id] = mode
    await countdb.update_one(
        {"chat_id": chat_id}, {"$set": {"mode": mode}}, upsert=True
    )


async def is_autoend() -> bool:
    chat_id = 1234
    user = await autoenddb.find_one({"chat_id": chat_id})
    if not user:
        return False
    return True


async def autoend_on():
    chat_id = 1234
    await autoenddb.insert_one({"chat_id": chat_id})


async def autoend_off():
    chat_id = 1234
    await autoenddb.delete_one({"chat_id": chat_id})


async def get_loop(chat_id: int) -> int:
    lop = loop.get(chat_id)
    if not lop:
        return 0
    return lop


async def set_loop(chat_id: int, mode: int):
    loop[chat_id] = mode


async def get_cmode(chat_id: int) -> int:
    mode = channelconnect.get(chat_id)
    if not mode:
        mode = await channeldb.find_one({"chat_id": chat_id})
        if not mode:
            return None
        channelconnect[chat_id] = mode["mode"]
        return mode["mode"]
    return mode


async def set_cmode(chat_id: int, mode: int):
    channelconnect[chat_id] = mode
    await channeldb.update_one(
        {"chat_id": chat_id}, {"$set": {"mode": mode}}, upsert=True
    )


async def get_playtype(chat_id: int) -> str:
    mode = playtype.get(chat_id)
    if not mode:
        mode = await playtypedb.find_one({"chat_id": chat_id})
        if not mode:
            playtype[chat_id] = "Everyone"
            return "Everyone"
        playtype[chat_id] = mode["mode"]
        return mode["mode"]
    return mode


async def set_playtype(chat_id: int, mode: str):
    playtype[chat_id] = mode
    await playtypedb.update_one(
        {"chat_id": chat_id}, {"$set": {"mode": mode}}, upsert=True
    )


async def get_playmode(chat_id: int) -> str:
    mode = playmode.get(chat_id)
    if not mode:
        mode = await playmodedb.find_one({"chat_id": chat_id})
        if not mode:
            playmode[chat_id] = "Direct"
            return "Direct"
        playmode[chat_id] = mode["mode"]
        return mode["mode"]
    return mode


async def set_playmode(chat_id: int, mode: str):
    playmode[chat_id] = mode
    await playmodedb.update_one(
        {"chat_id": chat_id}, {"$set": {"mode": mode}}, upsert=True
    )


async def get_lang(chat_id: int) -> str:
    mode = langm.get(chat_id)
    if not mode:
        lang = await langdb.find_one({"chat_id": chat_id})
        if not lang:
            langm[chat_id] = "en"
            return "en"
        langm[chat_id] = lang["lang"]
        return lang["lang"]
    return mode


async def set_lang(chat_id: int, lang: str):
    langm[chat_id] = lang
    await langdb.update_one({"chat_id": chat_id}, {"$set": {"lang": lang}}, upsert=True)


async def is_music_playing(chat_id: int) -> bool:
    mode = pause.get(chat_id)
    if not mode:
        return False
    return mode


async def music_on(chat_id: int):
    pause[chat_id] = True


async def music_off(chat_id: int):
    pause[chat_id] = False


async def get_active_chats() -> list:
    return active


async def is_active_chat(chat_id: int) -> bool:
    if chat_id not in active:
        return False
    else:
        return True


async def add_active_chat(chat_id: int):
    if chat_id not in active:
        active.append(chat_id)


async def remove_active_chat(chat_id: int):
    if chat_id in active:
        active.remove(chat_id)


async def get_active_video_chats() -> list:
    return activevideo


async def is_active_video_chat(chat_id: int) -> bool:
    if chat_id not in activevideo:
        return False
    else:
        return True


async def add_active_video_chat(chat_id: int):
    if chat_id not in activevideo:
        activevideo.append(chat_id)


async def remove_active_video_chat(chat_id: int):
    if chat_id in activevideo:
        activevideo.remove(chat_id)


async def check_nonadmin_chat(chat_id: int) -> bool:
    user = await authdb.find_one({"chat_id": chat_id})
    if not user:
        return False
    return True


async def is_nonadmin_chat(chat_id: int) -> bool:
    mode = nonadmin.get(chat_id)
    if not mode:
        user = await authdb.find_one({"chat_id": chat_id})
        if not user:
            nonadmin[chat_id] = False
            return False
        nonadmin[chat_id] = True
        return True
    return mode


async def add_nonadmin_chat(chat_id: int):
    nonadmin[chat_id] = True
    is_admin = await check_nonadmin_chat(chat_id)
    if is_admin:
        return
    return await authdb.insert_one({"chat_id": chat_id})


async def remove_nonadmin_chat(chat_id: int):
    nonadmin[chat_id] = False
    is_admin = await check_nonadmin_chat(chat_id)
    if not is_admin:
        return
    return await authdb.delete_one({"chat_id": chat_id})


async def is_on_off(on_off: int) -> bool:
    onoff = await onoffdb.find_one({"on_off": on_off})
    if not onoff:
        return False
    return True


async def add_on(on_off: int):
    is_on = await is_on_off(on_off)
    if is_on:
        return
    return await onoffdb.insert_one({"on_off": on_off})


async def add_off(on_off: int):
    is_off = await is_on_off(on_off)
    if not is_off:
        return
    return await onoffdb.delete_one({"on_off": on_off})


async def is_maintenance():
    if not maintenance:
        get = await onoffdb.find_one({"on_off": 1})
        if not get:
            maintenance.clear()
            maintenance.append(2)
            return True
        else:
            maintenance.clear()
            maintenance.append(1)
            return False
    else:
        if 1 in maintenance:
            return False
        else:
            return True


async def maintenance_off():
    maintenance.clear()
    maintenance.append(2)
    is_off = await is_on_off(1)
    if not is_off:
        return
    return await onoffdb.delete_one({"on_off": 1})


async def maintenance_on():
    maintenance.clear()
    maintenance.append(1)
    is_on = await is_on_off(1)
    if is_on:
        return
    return await onoffdb.insert_one({"on_off": 1})


async def is_served_user(user_id: int) -> bool:
    user = await usersdb.find_one({"user_id": user_id})
    if not user:
        return False
    return True


async def get_served_users() -> list:
    users_list = []
    async for user in usersdb.find({"user_id": {"$gt": 0}}):
        users_list.append(user)
    return users_list


async def add_served_user(user_id: int):
    is_served = await is_served_user(user_id)
    if is_served:
        return
    return await usersdb.insert_one({"user_id": user_id})


async def get_served_chats() -> list:
    chats_list = []
    async for chat in chatsdb.find({"chat_id": {"$lt": 0}}):
        chats_list.append(chat)
    return chats_list


async def is_served_chat(chat_id: int) -> bool:
    chat = await chatsdb.find_one({"chat_id": chat_id})
    if not chat:
        return False
    return True


async def add_served_chat(chat_id: int):
    is_served = await is_served_chat(chat_id)
    if is_served:
        return
    return await chatsdb.insert_one({"chat_id": chat_id})


async def blacklisted_chats() -> list:
    chats_list = []
    async for chat in blacklist_chatdb.find({"chat_id": {"$lt": 0}}):
        chats_list.append(chat["chat_id"])
    return chats_list


async def blacklist_chat(chat_id: int) -> bool:
    if not await blacklist_chatdb.find_one({"chat_id": chat_id}):
        await blacklist_chatdb.insert_one({"chat_id": chat_id})
        return True
    return False


async def whitelist_chat(chat_id: int) -> bool:
    if await blacklist_chatdb.find_one({"chat_id": chat_id}):
        await blacklist_chatdb.delete_one({"chat_id": chat_id})
        return True
    return False


async def _get_authusers(chat_id: int) -> Dict[str, int]:
    _notes = await authuserdb.find_one({"chat_id": chat_id})
    if not _notes:
        return {}
    return _notes["notes"]


async def get_authuser_names(chat_id: int) -> List[str]:
    _notes = []
    for note in await _get_authusers(chat_id):
        _notes.append(note)
    return _notes


async def get_authuser(chat_id: int, name: str) -> Union[bool, dict]:
    name = name
    _notes = await _get_authusers(chat_id)
    if name in _notes:
        return _notes[name]
    else:
        return False


async def save_authuser(chat_id: int, name: str, note: dict):
    name = name
    _notes = await _get_authusers(chat_id)
    _notes[name] = note

    await authuserdb.update_one(
        {"chat_id": chat_id}, {"$set": {"notes": _notes}}, upsert=True
    )


async def delete_authuser(chat_id: int, name: str) -> bool:
    notesd = await _get_authusers(chat_id)
    name = name
    if name in notesd:
        del notesd[name]
        await authuserdb.update_one(
            {"chat_id": chat_id},
            {"$set": {"notes": notesd}},
            upsert=True,
        )
        return True
    return False


async def get_gbanned() -> list:
    results = []
    async for user in gbansdb.find({"user_id": {"$gt": 0}}):
        user_id = user["user_id"]
        results.append(user_id)
    return results


async def is_gbanned_user(user_id: int) -> bool:
    user = await gbansdb.find_one({"user_id": user_id})
    if not user:
        return False
    return True


async def add_gban_user(user_id: int):
    is_gbanned = await is_gbanned_user(user_id)
    if is_gbanned:
        return
    return await gbansdb.insert_one({"user_id": user_id})


async def remove_gban_user(user_id: int):
    is_gbanned = await is_gbanned_user(user_id)
    if not is_gbanned:
        return
    return await gbansdb.delete_one({"user_id": user_id})


async def get_sudoers() -> list:
    sudoers = await sudoersdb.find_one({"sudo": "sudo"})
    if not sudoers:
        return []
    return sudoers["sudoers"]


async def add_sudo(user_id: int) -> bool:
    sudoers = await get_sudoers()
    sudoers.append(user_id)
    await sudoersdb.update_one(
        {"sudo": "sudo"}, {"$set": {"sudoers": sudoers}}, upsert=True
    )
    return True


async def remove_sudo(user_id: int) -> bool:
    sudoers = await get_sudoers()
    sudoers.remove(user_id)
    await sudoersdb.update_one(
        {"sudo": "sudo"}, {"$set": {"sudoers": sudoers}}, upsert=True
    )
    return True


async def get_banned_users() -> list:
    results = []
    async for user in blockeddb.find({"user_id": {"$gt": 0}}):
        user_id = user["user_id"]
        results.append(user_id)
    return results


async def get_banned_count() -> int:
    users = blockeddb.find({"user_id": {"$gt": 0}})
    users = await users.to_list(length=100000)
    return len(users)


async def is_banned_user(user_id: int) -> bool:
    user = await blockeddb.find_one({"user_id": user_id})
    if not user:
        return False
    return True


async def add_banned_user(user_id: int):
    is_gbanned = await is_banned_user(user_id)
    if is_gbanned:
        return
    return await blockeddb.insert_one({"user_id": user_id})


async def remove_banned_user(user_id: int):
    is_gbanned = await is_banned_user(user_id)
    if not is_gbanned:
        return
    return await blockeddb.delete_one({"user_id": user_id})







######################
def set_db_checkgroup(key: str, chat_id: int, name: str):
    dbcGeneral.execute("INSERT INTO groupcheck(key,chat_id,name) VALUES(?,?,?)", (key, chat_id, name))
    dbGeneral.commit()


def del_db_checkgroup(chat_id: int):
    dbcGeneral.execute("DELETE FROM groupcheck WHERE chat_id = ? ", (chat_id,))
    dbGeneral.commit()


def get_db_checkgroup(chat_id: int) -> str:
    dbcGeneral.execute("SELECT key FROM groupcheck WHERE chat_id = ?", (chat_id,))
    ul = dbcGeneral.fetchall()
    return ul if ul else None


def get_db_checkgroupall() -> str:
    dbcGeneral.execute("SELECT * FROM groupcheck")
    ul = dbcGeneral.fetchall()
    return ul if ul else None


#######################################################################################################
#######################################################################################################

def set_db_checkuser(key: str, user_id: int, name: str):
    dbcGeneral.execute("INSERT INTO usercheck(key,user_id,name) VALUES(?,?,?)", (key, user_id, name))
    dbGeneral.commit()


def del_db_checkuser(chat_id: int):
    dbcGeneral.execute("DELETE FROM usercheck WHERE user_id = ? ", (chat_id,))
    dbGeneral.commit()


def get_db_checkuser(user_id: int) -> str:
    dbcGeneral.execute("SELECT key FROM usercheck WHERE user_id = ?", (user_id,))
    ul = dbcGeneral.fetchall()
    return ul if ul else None


def get_db_checkuserall() -> str:
    dbcGeneral.execute("SELECT * FROM usercheck")
    ul = dbcGeneral.fetchall()
    return ul if ul else None


#######################################################################################################
#######################################################################################################

def set_db_gban(user_id: int, firstname: str):
    dbcGeneral.execute("INSERT INTO generalban(user_id,firstname) VALUES(?,?)", (user_id, firstname))
    dbGeneral.commit()


def del_db_gban(user_id: int):
    dbcGeneral.execute("DELETE FROM generalban WHERE user_id = ?", (user_id,))
    dbGeneral.commit()


def del_db_gbanall():
    dbcGeneral.execute("DELETE FROM generalban")
    dbGeneral.commit()


def get_db_gban() -> str:
    dbcGeneral.execute("SELECT * FROM generalban")
    ul = dbcGeneral.fetchall()
    return ul if ul else None


#######################################################################################################
#######################################################################################################

def set_db_gmute(user_id: int, firstname: str):
    dbcGeneral.execute("INSERT INTO generalmute(user_id,firstname) VALUES(?,?)", (user_id, firstname))
    dbGeneral.commit()


def del_db_gmute(user_id: int):
    dbcGeneral.execute("DELETE FROM generalmute WHERE user_id = ?", (user_id,))
    dbGeneral.commit()


def del_db_gmuteall():
    dbcGeneral.execute("DELETE FROM generalmute")
    dbGeneral.commit()


def get_db_gmute() -> str:
    dbcGeneral.execute("SELECT * FROM generalmute")
    ul = dbcGeneral.fetchall()
    return ul if ul else None


#######################################################################################################
#######################################################################################################

def set_db_privban(user_id: int, firstname: str, chat_id: int):
    dbcGeneral.execute("INSERT INTO priban(user_id,firstname,chat_id) VALUES(?,?,?)", (user_id, firstname, chat_id))
    dbGeneral.commit()


def del_db_priban(user_id: int, chat_id: int):
    dbcGeneral.execute("DELETE FROM priban WHERE user_id = ? and chat_id = ?", (user_id, chat_id))
    dbGeneral.commit()


def del_db_pribanall(chat_id: int):
    dbcGeneral.execute("DELETE FROM priban WHERE chat_id = ?", (chat_id,))
    dbGeneral.commit()


def drop_db_pribanallall():
    dbcGeneral.execute("DROP TABLE priban")
    dbcGeneral.execute("""CREATE TABLE IF NOT EXISTS priban (user_id,
                                                     firstname, chat_id INTEGER)""")
    dbGeneral.commit()


def get_db_priban(chat_id: int) -> str:
    dbcGeneral.execute("SELECT * FROM priban WHERE chat_id = ?", (chat_id,))
    ul = dbcGeneral.fetchall()
    return ul if ul else None


#######################################################################################################
#######################################################################################################

def set_db_greply(text: str, reply: str):
    dbcGeneral.execute("INSERT INTO generalreply (text,reply) VALUES(?,?)", (text, reply))
    dbGeneral.commit()


def del_db_greply(text: str):
    dbcGeneral.execute("DELETE FROM generalreply WHERE text = ?", (text,))
    dbGeneral.commit()


def del_db_grepall():
    dbcGeneral.execute("DELETE FROM generalreply")
    dbGeneral.commit()


def get_db_greply() -> str:
    dbcGeneral.execute("SELECT * FROM generalreply")
    ul = dbcGeneral.fetchall()
    return ul if ul else None


#######################################################################################################
#######################################################################################################

def set_db_wait(key: str, user_id: int, chat_id: int):
    dbcGeneral.execute("INSERT INTO wait (key,user_id,chat_id) VALUES(?,?,?)", (key, user_id, chat_id))
    dbGeneral.commit()


def del_db_wait(key: str):
    dbcGeneral.execute("DELETE FROM wait WHERE key = ?", (key,))
    dbGeneral.commit()


def get_db_wait() -> str:
    dbcGeneral.execute("SELECT * FROM wait")
    ul = dbcGeneral.fetchall()
    return ul if ul else None


def drop_db_wait():
    dbcGeneral.execute("DROP TABLE wait")
    dbcGeneral.execute("""CREATE TABLE IF NOT EXISTS wait (key,
                                                     user_id INTEGER, chat_id INTEGER)""")
    dbGeneral.commit()


def set_db_waitg(key: str, gamekey: str, chat_id: int):
    dbcGeneral.execute("INSERT INTO waitg (key,gamekey,chat_id) VALUES(?,?,?)", (key, gamekey, chat_id))
    dbGeneral.commit()


def del_db_waitg(key: str):
    dbcGeneral.execute("DELETE FROM waitg WHERE key = ?", (key,))
    dbGeneral.commit()


def get_db_waitg(chat_id: int) -> str:
    dbcGeneral.execute("SELECT * FROM waitg WHERE chat_id = ?", (chat_id,))
    ul = dbcGeneral.fetchall()
    return ul if ul else None


def drop_db_waitq():
    dbcGeneral.execute("DROP TABLE waitg")
    dbcGeneral.execute("""CREATE TABLE IF NOT EXISTS waitg (key,
                                                     gamekey, chat_id INTEGER)""")
    dbGeneral.commit()


#######################################################################################################
#######################################################################################################

def set_db_botname(botname: str):
    dbcGeneral.execute("INSERT INTO botname(name) VALUES(?)", (botname,))
    dbGeneral.commit()


def del_db_botname():
    dbcGeneral.execute("DELETE FROM botname")
    dbGeneral.commit()


def get_db_botname() -> str:
    dbcGeneral.execute("SELECT name FROM botname")
    ul = dbcGeneral.fetchone()
    return ul[0] if ul else None


#######################################################################################################
#######################################################################################################

def set_db_general_rtb(databasename, user_id: int, firstname: str):
    dbcGeneral.execute("INSERT INTO " + databasename + "(user_id,firstname) VALUES(?,?)", (user_id, firstname))
    dbGeneral.commit()


def del_db_general_rtb(databasename, user_id: int):
    dbcGeneral.execute("DELETE FROM " + databasename + " WHERE user_id = ?", (user_id,))
    dbGeneral.commit()


def del_db_general_rtball(databasename):
    dbcGeneral.execute("DELETE FROM " + databasename)
    dbGeneral.commit()


def get_db_general_rtb(databasename) -> str:
    dbcGeneral.execute("SELECT * FROM " + databasename)
    ul = dbcGeneral.fetchall()
    return ul if ul else None


#######################################################################################################
#######################################################################################################

def set_db_manager(firstname: str, user_id: int, chat_id: int):
    dbcGeneral.execute("INSERT INTO manager(firstname,user_id,chat_id) VALUES(?,?,?)", (firstname, user_id, chat_id))
    dbGeneral.commit()


def del_db_manager(user_id: int, chat_id: int):
    dbcGeneral.execute("DELETE FROM manager WHERE user_id = ? and chat_id = ?", (user_id, chat_id))
    dbGeneral.commit()


def del_db_managerall(chat_id: int):
    dbcGeneral.execute("DELETE FROM manager WHERE chat_id = ?", (chat_id,))
    dbGeneral.commit()


def get_db_manager(chat_id: int) -> str:
    dbcGeneral.execute("SELECT * FROM manager WHERE chat_id = ?", (chat_id,))
    ul = dbcGeneral.fetchall()
    return ul if ul else None


#######################################################################################################
#######################################################################################################

def set_db_constractors(firstname: str, user_id: int, chat_id: int):
    dbcGeneral.execute("INSERT INTO constructor(firstname,user_id,chat_id) VALUES(?,?,?)",
                       (firstname, user_id, chat_id))
    dbGeneral.commit()


def del_db_constractors(user_id: int, chat_id: int):
    dbcGeneral.execute("DELETE FROM constructor WHERE user_id = ? and chat_id = ?", (user_id, chat_id))
    dbGeneral.commit()


def del_db_constractorsall(chat_id: int):
    dbcGeneral.execute("DELETE FROM constructor WHERE chat_id = ?", (chat_id,))
    dbGeneral.commit()


def get_db_constractors(chat_id: int) -> str:
    dbcGeneral.execute("SELECT * FROM constructor WHERE chat_id = ?", (chat_id,))
    ul = dbcGeneral.fetchall()
    return ul if ul else None


#######################################################################################################
#######################################################################################################

def set_db_admin(firstname: str, user_id: int, chat_id: int):
    dbcGeneral.execute("INSERT INTO admin(firstname,user_id,chat_id) VALUES(?,?,?)", (firstname, user_id, chat_id))
    dbGeneral.commit()


def del_db_admin(user_id: int, chat_id: int):
    dbcGeneral.execute("DELETE FROM admin WHERE user_id = ? and chat_id = ?", (user_id, chat_id))
    dbGeneral.commit()


def del_db_adminall(chat_id: int):
    dbcGeneral.execute("DELETE FROM admin WHERE chat_id = ?", (chat_id,))
    dbGeneral.commit()


def get_db_admin(chat_id: int) -> str:
    dbcGeneral.execute("SELECT * FROM admin WHERE chat_id = ?", (chat_id,))
    ul = dbcGeneral.fetchall()
    return ul if ul else None


#######################################################################################################
#######################################################################################################

def set_db_special(firstname: str, user_id: int, chat_id: int):
    dbcGeneral.execute("INSERT INTO special(firstname,user_id,chat_id) VALUES(?,?,?)", (firstname, user_id, chat_id))
    dbGeneral.commit()


def del_db_special(user_id: int, chat_id: int):
    dbcGeneral.execute("DELETE FROM special WHERE user_id = ? and chat_id = ?", (user_id, chat_id))
    dbGeneral.commit()


def del_db_specialall(chat_id: int):
    dbcGeneral.execute("DELETE FROM special WHERE chat_id = ?", (chat_id,))
    dbGeneral.commit()


def get_db_special(chat_id: int) -> str:
    dbcGeneral.execute("SELECT * FROM special WHERE chat_id = ?", (chat_id,))
    ul = dbcGeneral.fetchall()
    return ul if ul else None


#######################################################################################################
#######################################################################################################

def set_db_locktext(key: str, chat_id: int):
    dbcGeneral.execute("INSERT INTO locktext(key,chat_id) VALUES(?,?)", (key, chat_id))
    dbGeneral.commit()


def del_db_locktext(chat_id: int):
    dbcGeneral.execute("DELETE FROM locktext WHERE chat_id = ?", (chat_id,))
    dbGeneral.commit()


def get_db_locktext(chat_id: int) -> str:
    dbcGeneral.execute("SELECT key FROM locktext WHERE chat_id = ?", (chat_id,))
    ul = dbcGeneral.fetchall()
    return ul if ul else None


def drop_db_locktext():
    dbcGeneral.execute("DROP TABLE locktext")
    dbcGeneral.execute("""CREATE TABLE IF NOT EXISTS locktext (key, chat_id)""")
    dbGeneral.commit()


#######################################################################################################
#######################################################################################################

def set_db_lockmnshn(key: str, chat_id: int):
    dbcGeneral.execute("INSERT INTO lockmnshn(key,chat_id) VALUES(?,?)", (key, chat_id))
    dbGeneral.commit()


def del_db_lockmnshn(chat_id: int):
    dbcGeneral.execute("DELETE FROM lockmnshn WHERE chat_id = ?", (chat_id,))
    dbGeneral.commit()


def get_db_lockmnshn(chat_id: int) -> str:
    dbcGeneral.execute("SELECT key FROM lockmnshn WHERE chat_id = ?", (chat_id,))
    ul = dbcGeneral.fetchall()
    return ul if ul else None


#######################################################################################################
#######################################################################################################

def set_db_locklink(key: str, chat_id: int):
    dbcGeneral.execute("INSERT INTO locklink(key,chat_id) VALUES(?,?)", (key, chat_id))
    dbGeneral.commit()


def del_db_locklink(chat_id: int):
    dbcGeneral.execute("DELETE FROM locklink WHERE chat_id = ?", (chat_id,))
    dbGeneral.commit()


def get_db_locklink(chat_id: int) -> str:
    dbcGeneral.execute("SELECT key FROM locklink WHERE chat_id = ?", (chat_id,))
    ul = dbcGeneral.fetchall()
    return ul if ul else None


def set_db_locklink_ban(key: str, chat_id: int):
    dbcGeneral.execute("INSERT INTO locklinkban(key,chat_id) VALUES(?,?)", (key, chat_id))
    dbGeneral.commit()


def del_db_locklink_ban(chat_id: int):
    dbcGeneral.execute("DELETE FROM locklinkban WHERE chat_id = ?", (chat_id,))
    dbGeneral.commit()


def get_db_locklink_ban(chat_id: int) -> str:
    dbcGeneral.execute("SELECT key FROM locklinkban WHERE chat_id = ?", (chat_id,))
    ul = dbcGeneral.fetchall()
    return ul if ul else None


def set_db_locklink_mute(key: str, chat_id: int):
    dbcGeneral.execute("INSERT INTO locklinkmute(key,chat_id) VALUES(?,?)", (key, chat_id))
    dbGeneral.commit()


def del_db_locklink_mute(chat_id: int):
    dbcGeneral.execute("DELETE FROM locklinkmute WHERE chat_id = ?", (chat_id,))
    dbGeneral.commit()


def get_db_locklink_mute(chat_id: int) -> str:
    dbcGeneral.execute("SELECT key FROM locklinkmute WHERE chat_id = ?", (chat_id,))
    ul = dbcGeneral.fetchall()
    return ul if ul else None


#######################################################################################################
#######################################################################################################

def set_db_lockphoto(key: str, chat_id: int):
    dbcGeneral.execute("INSERT INTO lockphoto(key,chat_id) VALUES(?,?)", (key, chat_id))
    dbGeneral.commit()


def del_db_lockphoto(chat_id: int):
    dbcGeneral.execute("DELETE FROM lockphoto WHERE chat_id = ?", (chat_id,))
    dbGeneral.commit()


def get_db_lockphoto(chat_id: int) -> str:
    dbcGeneral.execute("SELECT key FROM lockphoto WHERE chat_id = ?", (chat_id,))
    ul = dbcGeneral.fetchall()
    return ul if ul else None


#######################################################################################################
#######################################################################################################

def set_db_lockvideo(key: str, chat_id: int):
    dbcGeneral.execute("INSERT INTO lockvideo(key,chat_id) VALUES(?,?)", (key, chat_id))
    dbGeneral.commit()


def del_db_lockvideo(chat_id: int):
    dbcGeneral.execute("DELETE FROM lockvideo WHERE chat_id = ?", (chat_id,))
    dbGeneral.commit()


def get_db_lockvideo(chat_id: int) -> str:
    dbcGeneral.execute("SELECT key FROM lockvideo WHERE chat_id = ?", (chat_id,))
    ul = dbcGeneral.fetchall()
    return ul if ul else None


#######################################################################################################
#######################################################################################################

def set_db_locksticker(key: str, chat_id: int):
    dbcGeneral.execute("INSERT INTO locksticker(key,chat_id) VALUES(?,?)", (key, chat_id))
    dbGeneral.commit()


def del_db_locksticker(chat_id: int):
    dbcGeneral.execute("DELETE FROM locksticker WHERE chat_id = ?", (chat_id,))
    dbGeneral.commit()


def get_db_locksticker(chat_id: int) -> str:
    dbcGeneral.execute("SELECT key FROM locksticker WHERE chat_id = ?", (chat_id,))
    ul = dbcGeneral.fetchall()
    return ul if ul else None


#######################################################################################################
#######################################################################################################

def set_db_lockanimation(key: str, chat_id: int):
    dbcGeneral.execute("INSERT INTO lockanimation(key,chat_id) VALUES(?,?)", (key, chat_id))
    dbGeneral.commit()


def del_db_lockanimation(chat_id: int):
    dbcGeneral.execute("DELETE FROM lockanimation WHERE chat_id = ?", (chat_id,))
    dbGeneral.commit()


def get_db_lockanimation(chat_id: int) -> str:
    dbcGeneral.execute("SELECT key FROM lockanimation WHERE chat_id = ?", (chat_id,))
    ul = dbcGeneral.fetchall()
    return ul if ul else None


#######################################################################################################
#######################################################################################################

def set_db_lockaudio(key: str, chat_id: int):
    dbcGeneral.execute("INSERT INTO lockaudio(key,chat_id) VALUES(?,?)", (key, chat_id))
    dbGeneral.commit()


def del_db_lockaudio(chat_id: int):
    dbcGeneral.execute("DELETE FROM lockaudio WHERE chat_id = ?", (chat_id,))
    dbGeneral.commit()


def get_db_lockaudio(chat_id: int) -> str:
    dbcGeneral.execute("SELECT key FROM lockaudio WHERE chat_id = ?", (chat_id,))
    ul = dbcGeneral.fetchall()
    return ul if ul else None


#######################################################################################################
#######################################################################################################

def set_db_lockvoice(key: str, chat_id: int):
    dbcGeneral.execute("INSERT INTO lockvoice(key,chat_id) VALUES(?,?)", (key, chat_id))
    dbGeneral.commit()


def del_db_lockvoice(chat_id: int):
    dbcGeneral.execute("DELETE FROM lockvoice WHERE chat_id = ?", (chat_id,))
    dbGeneral.commit()


def get_db_lockvoice(chat_id: int) -> str:
    dbcGeneral.execute("SELECT key FROM lockvoice WHERE chat_id = ?", (chat_id,))
    ul = dbcGeneral.fetchall()
    return ul if ul else None


#######################################################################################################
#######################################################################################################

def set_db_lockforward(key: str, chat_id: int):
    dbcGeneral.execute("INSERT INTO lockforward(key,chat_id) VALUES(?,?)", (key, chat_id))
    dbGeneral.commit()


def del_db_lockforward(chat_id: int):
    dbcGeneral.execute("DELETE FROM lockforward WHERE chat_id = ?", (chat_id,))
    dbGeneral.commit()


def get_db_lockforward(chat_id: int) -> str:
    dbcGeneral.execute("SELECT key FROM lockforward WHERE chat_id = ?", (chat_id,))
    ul = dbcGeneral.fetchall()
    return ul if ul else None


def set_db_lockforward_ban(key: str, chat_id: int):
    dbcGeneral.execute("INSERT INTO lockforwardban(key,chat_id) VALUES(?,?)", (key, chat_id))
    dbGeneral.commit()


def del_db_lockforward_ban(chat_id: int):
    dbcGeneral.execute("DELETE FROM lockforwardban WHERE chat_id = ?", (chat_id,))
    dbGeneral.commit()


def get_db_lockforward_ban(chat_id: int) -> str:
    dbcGeneral.execute("SELECT key FROM lockforwardban WHERE chat_id = ?", (chat_id,))
    ul = dbcGeneral.fetchall()
    return ul if ul else None


def set_db_lockforward_mute(key: str, chat_id: int):
    dbcGeneral.execute("INSERT INTO lockforwardmute(key,chat_id) VALUES(?,?)", (key, chat_id))
    dbGeneral.commit()


def del_db_lockforward_mute(chat_id: int):
    dbcGeneral.execute("DELETE FROM lockforwardmute WHERE chat_id = ?", (chat_id,))
    dbGeneral.commit()


def get_db_lockforward_mute(chat_id: int) -> str:
    dbcGeneral.execute("SELECT key FROM lockforwardmute WHERE chat_id = ?", (chat_id,))
    ul = dbcGeneral.fetchall()
    return ul if ul else None


#######################################################################################################
#######################################################################################################

def set_db_lockdocument(key: str, chat_id: int):
    dbcGeneral.execute("INSERT INTO lockdocument(key,chat_id) VALUES(?,?)", (key, chat_id))
    dbGeneral.commit()


def del_db_lockdocument(chat_id: int):
    dbcGeneral.execute("DELETE FROM lockdocument WHERE chat_id = ?", (chat_id,))
    dbGeneral.commit()


def get_db_lockdocument(chat_id: int) -> str:
    dbcGeneral.execute("SELECT key FROM lockdocument WHERE chat_id = ?", (chat_id,))
    ul = dbcGeneral.fetchall()
    return ul if ul else None


#######################################################################################################
#######################################################################################################

def set_db_lockcontact(key: str, chat_id: int):
    dbcGeneral.execute("INSERT INTO lockcontact(key,chat_id) VALUES(?,?)", (key, chat_id))
    dbGeneral.commit()


def del_db_lockcontact(chat_id: int):
    dbcGeneral.execute("DELETE FROM lockcontact WHERE chat_id = ?", (chat_id,))
    dbGeneral.commit()


def get_db_lockcontact(chat_id: int) -> str:
    dbcGeneral.execute("SELECT key FROM lockcontact WHERE chat_id = ?", (chat_id,))
    ul = dbcGeneral.fetchall()
    return ul if ul else None


#######################################################################################################
#######################################################################################################

def set_db_locksendmsg(key: str):
    dbcGeneral.execute("INSERT INTO locksendmsg(key) VALUES(?)", (key,))
    dbGeneral.commit()


def del_db_locksendmsg():
    dbcGeneral.execute("DELETE FROM locksendmsg")
    dbGeneral.commit()


def get_db_locksendmsg() -> str:
    dbcGeneral.execute("SELECT key FROM locksendmsg")
    ul = dbcGeneral.fetchall()
    return ul if ul else None


#######################################################################################################
#######################################################################################################

def set_db_lockbroadcast(key: str):
    dbcGeneral.execute("INSERT INTO lockbroadcast(key) VALUES(?)", (key,))
    dbGeneral.commit()


def del_db_lockbroadcast():
    dbcGeneral.execute("DELETE FROM lockbroadcast")
    dbGeneral.commit()


def get_db_lockbroadcast() -> str:
    dbcGeneral.execute("SELECT key FROM lockbroadcast")
    ul = dbcGeneral.fetchall()
    return ul if ul else None


#######################################################################################################
#######################################################################################################

def set_db_lockgenyoutube(key: str):
    dbcGeneral.execute("INSERT INTO lockgenyoutube(key) VALUES(?)", (key,))
    dbGeneral.commit()


def del_db_lockgenyoutube():
    dbcGeneral.execute("DELETE FROM lockgenyoutube")
    dbGeneral.commit()


def get_db_lockgenyoutube() -> str:
    dbcGeneral.execute("SELECT key FROM lockgenyoutube")
    ul = dbcGeneral.fetchall()
    return ul if ul else None


#######################################################################################################
#######################################################################################################

def set_db_addlinkgroup(link: str, chat_id: int):
    dbcGeneral.execute("INSERT INTO addlinkgroup(link, chat_id) VALUES(?,?)", (link, chat_id))
    dbGeneral.commit()


def del_db_addlinkgroup(chat_id: int):
    dbcGeneral.execute("DELETE FROM addlinkgroup WHERE chat_id = ?", (chat_id,))
    dbGeneral.commit()


def get_db_addlinkgroup(chat_id: int) -> str:
    dbcGeneral.execute("SELECT * FROM addlinkgroup WHERE chat_id = ?", (chat_id,))
    ul = dbcGeneral.fetchall()
    return ul if ul else None


#######################################################################################################
#######################################################################################################

def set_db_lockwelcome(key: str, chat_id: int):
    dbcGeneral.execute("INSERT INTO lockwelcome(key, chat_id) VALUES(?,?)", (key, chat_id))
    dbGeneral.commit()


def del_db_lockwelcome(chat_id: int):
    dbcGeneral.execute("DELETE FROM lockwelcome WHERE chat_id = ?", (chat_id,))
    dbGeneral.commit()


def get_db_lockwelcome(chat_id: int) -> str:
    dbcGeneral.execute("SELECT * FROM lockwelcome WHERE chat_id = ?", (chat_id,))
    ul = dbcGeneral.fetchall()
    return ul if ul else None


def set_db_addwelcomegroup(welcome: str, chat_id: int):
    dbcGeneral.execute("INSERT INTO addwelcomegroup(welcome, chat_id) VALUES(?,?)", (welcome, chat_id))
    dbGeneral.commit()


def del_db_addwelcomegroup(chat_id: int):
    dbcGeneral.execute("DELETE FROM addwelcomegroup WHERE chat_id = ?", (chat_id,))
    dbGeneral.commit()


def get_db_addwelcomegroup(chat_id: int) -> str:
    dbcGeneral.execute("SELECT * FROM addwelcomegroup WHERE chat_id = ?", (chat_id,))
    ul = dbcGeneral.fetchall()
    return ul if ul else None


#######################################################################################################
#######################################################################################################

def set_db_lockbye(key: str, chat_id: int):
    dbcGeneral.execute("INSERT INTO lockbye(key, chat_id) VALUES(?,?)", (key, chat_id))
    dbGeneral.commit()


def del_db_lockbye(chat_id: int):
    dbcGeneral.execute("DELETE FROM lockbye WHERE chat_id = ?", (chat_id,))
    dbGeneral.commit()


def get_db_lockbye(chat_id: int) -> str:
    dbcGeneral.execute("SELECT * FROM lockbye WHERE chat_id = ?", (chat_id,))
    ul = dbcGeneral.fetchall()
    return ul if ul else None


def set_db_addbyegroup(bye: str, chat_id: int):
    dbcGeneral.execute("INSERT INTO addbyegroup(bye, chat_id) VALUES(?,?)", (bye, chat_id))
    dbGeneral.commit()


def del_db_addbyegroup(chat_id: int):
    dbcGeneral.execute("DELETE FROM addbyegroup WHERE chat_id = ?", (chat_id,))
    dbGeneral.commit()


def get_db_addbyegroup(chat_id: int) -> str:
    dbcGeneral.execute("SELECT * FROM addbyegroup WHERE chat_id = ?", (chat_id,))
    ul = dbcGeneral.fetchall()
    return ul if ul else None


#######################################################################################################
#######################################################################################################

def set_db_lockreply(key: str, chat_id: int):
    dbcGeneral.execute("INSERT INTO lockreply(key, chat_id) VALUES(?,?)", (key, chat_id))
    dbGeneral.commit()


def del_db_lockreply(chat_id: int):
    dbcGeneral.execute("DELETE FROM lockreply WHERE chat_id = ?", (chat_id,))
    dbGeneral.commit()


def get_db_lockreply(chat_id: int) -> str:
    dbcGeneral.execute("SELECT * FROM lockreply WHERE chat_id = ?", (chat_id,))
    ul = dbcGeneral.fetchall()
    return ul if ul else None


#######################################################################################################
#######################################################################################################

def set_db_lockfshar(key: str, chat_id: int):
    dbcGeneral.execute("INSERT INTO lockfshar(key,chat_id) VALUES(?,?)", (key, chat_id))
    dbGeneral.commit()


def del_db_lockfshar(chat_id: int):
    dbcGeneral.execute("DELETE FROM lockfshar WHERE chat_id = ?", (chat_id,))
    dbGeneral.commit()


def get_db_lockfshar(chat_id: int) -> str:
    dbcGeneral.execute("SELECT key FROM lockfshar WHERE chat_id = ?", (chat_id,))
    ul = dbcGeneral.fetchall()
    return ul if ul else None


def set_db_lockfshar_ban(key: str, chat_id: int):
    dbcGeneral.execute("INSERT INTO lockfsharban(key,chat_id) VALUES(?,?)", (key, chat_id))
    dbGeneral.commit()


def del_db_lockfshar_ban(chat_id: int):
    dbcGeneral.execute("DELETE FROM lockfsharban WHERE chat_id = ?", (chat_id,))
    dbGeneral.commit()


def get_db_lockfshar_ban(chat_id: int) -> str:
    dbcGeneral.execute("SELECT key FROM lockfsharban WHERE chat_id = ?", (chat_id,))
    ul = dbcGeneral.fetchall()
    return ul if ul else None


def set_db_lockfshar_mute(key: str, chat_id: int):
    dbcGeneral.execute("INSERT INTO lockfsharmute(key,chat_id) VALUES(?,?)", (key, chat_id))
    dbGeneral.commit()


def del_db_lockfshar_mute(chat_id: int):
    dbcGeneral.execute("DELETE FROM lockfsharmute WHERE chat_id = ?", (chat_id,))
    dbGeneral.commit()


def get_db_lockfshar_mute(chat_id: int) -> str:
    dbcGeneral.execute("SELECT key FROM lockfsharmute WHERE chat_id = ?", (chat_id,))
    ul = dbcGeneral.fetchall()
    return ul if ul else None


#######################################################################################################
#######################################################################################################

def set_db_locknotification(key: str, chat_id: int):
    dbcGeneral.execute("INSERT INTO locknotification(key,chat_id) VALUES(?,?)", (key, chat_id))
    dbGeneral.commit()


def del_db_locknotification(chat_id: int):
    dbcGeneral.execute("DELETE FROM locknotification WHERE chat_id = ?", (chat_id,))
    dbGeneral.commit()


def get_db_locknotification(chat_id: int) -> str:
    dbcGeneral.execute("SELECT key FROM locknotification WHERE chat_id = ?", (chat_id,))
    ul = dbcGeneral.fetchall()
    return ul if ul else None


#######################################################################################################
#######################################################################################################

def set_db_lockzhrafa(key: str, chat_id: int):
    dbcGeneral.execute("INSERT INTO lockzhrafa(key,chat_id) VALUES(?,?)", (key, chat_id))
    dbGeneral.commit()


def del_db_lockzhrafa(chat_id: int):
    dbcGeneral.execute("DELETE FROM lockzhrafa WHERE chat_id = ?", (chat_id,))
    dbGeneral.commit()


def get_db_lockzhrafa(chat_id: int) -> str:
    dbcGeneral.execute("SELECT key FROM lockzhrafa WHERE chat_id = ?", (chat_id,))
    ul = dbcGeneral.fetchall()
    return ul if ul else None


#######################################################################################################
#######################################################################################################

def set_db_lockmusic(key: str, chat_id: int):
    dbcGeneral.execute("INSERT INTO lockmusic(key,chat_id) VALUES(?,?)", (key, chat_id))
    dbGeneral.commit()


def del_db_lockmusic(chat_id: int):
    dbcGeneral.execute("DELETE FROM lockmusic WHERE chat_id = ?", (chat_id,))
    dbGeneral.commit()


def get_db_lockmusic(chat_id: int) -> str:
    dbcGeneral.execute("SELECT key FROM lockmusic WHERE chat_id = ?", (chat_id,))
    ul = dbcGeneral.fetchall()
    return ul if ul else None


#######################################################################################################
#######################################################################################################

def set_db_lockaflam(key: str, chat_id: int):
    dbcGeneral.execute("INSERT INTO lockaflam(key,chat_id) VALUES(?,?)", (key, chat_id))
    dbGeneral.commit()


def del_db_lockaflam(chat_id: int):
    dbcGeneral.execute("DELETE FROM lockaflam WHERE chat_id = ?", (chat_id,))
    dbGeneral.commit()


def get_db_lockaflam(chat_id: int) -> str:
    dbcGeneral.execute("SELECT key FROM lockaflam WHERE chat_id = ?", (chat_id,))
    ul = dbcGeneral.fetchall()
    return ul if ul else None


#######################################################################################################
#######################################################################################################

def set_db_lockyoutube(key: str, chat_id: int):
    dbcGeneral.execute("INSERT INTO lockyoutube(key,chat_id) VALUES(?,?)", (key, chat_id))
    dbGeneral.commit()


def del_db_lockyoutube(chat_id: int):
    dbcGeneral.execute("DELETE FROM lockyoutube WHERE chat_id = ?", (chat_id,))
    dbGeneral.commit()


def get_db_lockyoutube(chat_id: int) -> str:
    dbcGeneral.execute("SELECT key FROM lockyoutube WHERE chat_id = ?", (chat_id,))
    ul = dbcGeneral.fetchall()
    return ul if ul else None


#######################################################################################################
#######################################################################################################

def set_db_locktranslate(key: str, chat_id: int):
    dbcGeneral.execute("INSERT INTO locktranslate(key,chat_id) VALUES(?,?)", (key, chat_id))
    dbGeneral.commit()


def del_db_locktranslate(chat_id: int):
    dbcGeneral.execute("DELETE FROM locktranslate WHERE chat_id = ?", (chat_id,))
    dbGeneral.commit()


def get_db_locktranslate(chat_id: int) -> str:
    dbcGeneral.execute("SELECT key FROM locktranslate WHERE chat_id = ?", (chat_id,))
    ul = dbcGeneral.fetchall()
    return ul if ul else None


#######################################################################################################
#######################################################################################################

def set_db_blocktext(key: str, chat_id: int):
    dbcGeneral.execute("INSERT INTO blocktext(key,chat_id) VALUES(?,?)", (key, chat_id))
    dbGeneral.commit()


def del_db_blocktext(key: str, chat_id: int):
    dbcGeneral.execute("DELETE FROM blocktext WHERE key = ? and chat_id = ?", (key, chat_id))
    dbGeneral.commit()


def del_db_blocktextall(chat_id: int):
    dbcGeneral.execute("DELETE FROM blocktext WHERE chat_id = ?", (chat_id,))
    dbGeneral.commit()


def get_db_blocktext(chat_id: int) -> str:
    dbcGeneral.execute("SELECT * FROM blocktext WHERE chat_id = ?", (chat_id,))
    ul = dbcGeneral.fetchall()
    return ul if ul else None


def set_db_blocktext_ban(key: str, chat_id: int):
    dbcGeneral.execute("INSERT INTO blocktextban(key,chat_id) VALUES(?,?)", (key, chat_id))
    dbGeneral.commit()


def del_db_blocktext_ban(chat_id: int):
    dbcGeneral.execute("DELETE FROM blocktextban WHERE chat_id = ?", (chat_id,))
    dbGeneral.commit()


def get_db_blocktext_ban(chat_id: int) -> str:
    dbcGeneral.execute("SELECT * FROM blocktextban WHERE chat_id = ?", (chat_id,))
    ul = dbcGeneral.fetchall()
    return ul if ul else None


def set_db_blocktext_mute(key: str, chat_id: int):
    dbcGeneral.execute("INSERT INTO blocktextmute(key,chat_id) VALUES(?,?)", (key, chat_id))
    dbGeneral.commit()


def del_db_blocktext_mute(chat_id: int):
    dbcGeneral.execute("DELETE FROM blocktextmute WHERE chat_id = ?", (chat_id,))
    dbGeneral.commit()


def get_db_blocktext_mute(chat_id: int) -> str:
    dbcGeneral.execute("SELECT * FROM blocktextmute WHERE chat_id = ?", (chat_id,))
    ul = dbcGeneral.fetchall()
    return ul if ul else None


#######################################################################################################
#######################################################################################################

def set_db_lockupper(key: str, chat_id: int):
    dbcGeneral.execute("INSERT INTO lockupper(key,chat_id) VALUES(?,?)", (key, chat_id))
    dbGeneral.commit()


def del_db_lockupper(chat_id: int):
    dbcGeneral.execute("DELETE FROM lockupper WHERE chat_id = ?", (chat_id,))
    dbGeneral.commit()


def get_db_lockupper(chat_id: int) -> str:
    dbcGeneral.execute("SELECT key FROM lockupper WHERE chat_id = ?", (chat_id,))
    ul = dbcGeneral.fetchall()
    return ul if ul else None


#######################################################################################################
#######################################################################################################

def set_db_lock(databasename, key: str, chat_id: int):
    dbcGeneral.execute("INSERT INTO " + databasename + " (key,chat_id) VALUES(?,?)", (key, chat_id))
    dbGeneral.commit()


def del_db_lock(databasename, chat_id: int):
    dbcGeneral.execute("DELETE FROM " + databasename + " WHERE chat_id = ?", (chat_id,))
    dbGeneral.commit()


def get_db_lock(databasename, chat_id: int) -> str:
    dbcGeneral.execute("SELECT key FROM " + databasename + " WHERE chat_id = ?", (chat_id,))
    ul = dbcGeneral.fetchall()
    return ul if ul else None


#######################################################################################################
#######################################################################################################

def set_db_lockrwayat(key: str, chat_id: int):
    dbcGeneral.execute("INSERT INTO lockrwayat(key,chat_id) VALUES(?,?)", (key, chat_id))
    dbGeneral.commit()


def del_db_lockrwayat(chat_id: int):
    dbcGeneral.execute("DELETE FROM lockrwayat WHERE chat_id = ?", (chat_id,))
    dbGeneral.commit()


def get_db_lockrwayat(chat_id: int) -> str:
    dbcGeneral.execute("SELECT key FROM lockrwayat WHERE chat_id = ?", (chat_id,))
    ul = dbcGeneral.fetchall()
    return ul if ul else None


#######################################################################################################
#######################################################################################################

def set_db_entertainment(databasename, firstname: str, user_id: int, chat_id: int):
    dbcGeneral.execute("INSERT INTO " + databasename + "(firstname,user_id,chat_id) VALUES(?,?,?)",
                       (firstname, user_id, chat_id))
    dbGeneral.commit()


def del_db_entertainment(databasename, user_id: int, chat_id: int):
    dbcGeneral.execute("DELETE FROM " + databasename + " WHERE user_id = ? and chat_id = ?", (user_id, chat_id))
    dbGeneral.commit()


def del_db_entertainmentall(databasename, chat_id: int):
    dbcGeneral.execute("DELETE FROM " + databasename + " WHERE chat_id = ?", (chat_id,))
    dbGeneral.commit()


def get_db_entertainment(databasename, chat_id: int) -> str:
    dbcGeneral.execute("SELECT * FROM " + databasename + " WHERE chat_id = ?", (chat_id,))
    ul = dbcGeneral.fetchall()
    return ul if ul else None


#######################################################################################################
#######################################################################################################

def set_db_lockgames(key: str, chat_id: int):
    dbcGeneral.execute("INSERT INTO lockgames(key,chat_id) VALUES(?,?)", (key, chat_id))
    dbGeneral.commit()


def del_db_lockgames(chat_id: int):
    dbcGeneral.execute("DELETE FROM lockgames WHERE chat_id = ?", (chat_id,))
    dbGeneral.commit()


def get_db_lockgames(chat_id: int) -> str:
    dbcGeneral.execute("SELECT key FROM lockgames WHERE chat_id = ?", (chat_id,))
    ul = dbcGeneral.fetchall()
    return ul if ul else None


#######################################################################################################
#######################################################################################################

def set_db_locktag(key: str, chat_id: int):
    dbcGeneral.execute("INSERT INTO locktag(key,chat_id) VALUES(?,?)", (key, chat_id))
    dbGeneral.commit()


def del_db_locktag(chat_id: int):
    dbcGeneral.execute("DELETE FROM locktag WHERE chat_id = ?", (chat_id,))
    dbGeneral.commit()


def get_db_locktag(chat_id: int) -> str:
    dbcGeneral.execute("SELECT key FROM locktag WHERE chat_id = ?", (chat_id,))
    ul = dbcGeneral.fetchall()
    return ul if ul else None


#######################################################################################################
#######################################################################################################

def set_db_lockmeendafny(key: str, chat_id: int):
    dbcGeneral.execute("INSERT INTO lockmeendafny(key,chat_id) VALUES(?,?)", (key, chat_id))
    dbGeneral.commit()


def del_db_lockmeendafny(chat_id: int):
    dbcGeneral.execute("DELETE FROM lockmeendafny WHERE chat_id = ?", (chat_id,))
    dbGeneral.commit()


def get_db_lockmeendafny(chat_id: int) -> str:
    dbcGeneral.execute("SELECT key FROM lockmeendafny WHERE chat_id = ?", (chat_id,))
    ul = dbcGeneral.fetchall()
    return ul if ul else None


#######################################################################################################
#######################################################################################################

def set_db_replygroup(text: str, reply: str, chat_id: int):
    dbcGeneral.execute("INSERT INTO replygroup (text,reply,chat_id) VALUES(?,?,?)", (text, reply, chat_id))
    dbGeneral.commit()


def del_db_replygroup(text: str, chat_id: int):
    dbcGeneral.execute("DELETE FROM replygroup WHERE text = ? and chat_id = ?", (text, chat_id))
    dbGeneral.commit()


def del_db_repgroupall(chat_id: int):
    dbcGeneral.execute("DELETE FROM replygroup WHERE chat_id = ?", (chat_id,))
    dbGeneral.commit()


def get_db_replygroup(chat_id: int) -> str:
    dbcGeneral.execute("SELECT * FROM replygroup WHERE chat_id = ?", (chat_id,))
    ul = dbcGeneral.fetchall()
    return ul if ul else None


def drop_db_replygroup():
    dbcGeneral.execute("DROP TABLE replygroup")
    dbcGeneral.execute("""CREATE TABLE IF NOT EXISTS replygroup (text, reply, chat_id)""")
    dbGeneral.commit()


#######################################################################################################
#######################################################################################################

def set_db_deletelink(key: str, chat_id: int):
    dbcGeneral.execute("INSERT INTO lockdeletelink(key,chat_id) VALUES(?,?)", (key, chat_id))
    dbGeneral.commit()


def del_db_deletelink(chat_id: int):
    dbcGeneral.execute("DELETE FROM lockdeletelink WHERE chat_id = ?", (chat_id,))
    dbGeneral.commit()


def get_db_deletelink(chat_id: int) -> str:
    dbcGeneral.execute("SELECT key FROM lockdeletelink WHERE chat_id = ?", (chat_id,))
    ul = dbcGeneral.fetchall()
    return ul if ul else None


#######################################################################################################
#######################################################################################################

def set_db_lockkickme(key: str, chat_id: int):
    dbcGeneral.execute("INSERT INTO lockkickme(key,chat_id) VALUES(?,?)", (key, chat_id))
    dbGeneral.commit()


def del_db_lockkickme(chat_id: int):
    dbcGeneral.execute("DELETE FROM lockkickme WHERE chat_id = ?", (chat_id,))
    dbGeneral.commit()


def get_db_lockkickme(chat_id: int) -> str:
    dbcGeneral.execute("SELECT key FROM lockkickme WHERE chat_id = ?", (chat_id,))
    ul = dbcGeneral.fetchall()
    return ul if ul else None


#######################################################################################################
#######################################################################################################

def set_db_ban(user_id: int, firstname: str, chat_id: int):
    dbcGeneral.execute("INSERT INTO ban(user_id,firstname,chat_id) VALUES(?,?,?)", (user_id, firstname, chat_id))
    dbGeneral.commit()


def del_db_ban(user_id: int, chat_id: int):
    dbcGeneral.execute("DELETE FROM ban WHERE user_id = ? and chat_id = ?", (user_id, chat_id))
    dbGeneral.commit()


def del_db_banall(chat_id: int):
    dbcGeneral.execute("DELETE FROM ban WHERE chat_id = ?", (chat_id,))
    dbGeneral.commit()


def del_db_banallall():
    dbcGeneral.execute("DROP TABLE ban")
    dbcGeneral.execute("""CREATE TABLE IF NOT EXISTS ban (user_id,
                                                     firstname, chat_id INTEGER)""")
    dbGeneral.commit()


def get_db_ban(chat_id: int) -> str:
    dbcGeneral.execute("SELECT * FROM ban WHERE chat_id = ?", (chat_id,))
    ul = dbcGeneral.fetchall()
    return ul if ul else None


#######################################################################################################
#######################################################################################################

def set_db_mute(user_id: int, firstname: str, chat_id: int):
    dbcGeneral.execute("INSERT INTO mute(user_id,firstname,chat_id) VALUES(?,?,?)", (user_id, firstname, chat_id))
    dbGeneral.commit()


def del_db_mute(user_id: int, chat_id: int):
    dbcGeneral.execute("DELETE FROM mute WHERE user_id = ? and chat_id = ?", (user_id, chat_id))
    dbGeneral.commit()


def del_db_muteall(chat_id: int):
    dbcGeneral.execute("DELETE FROM mute WHERE chat_id = ?", (chat_id,))
    dbGeneral.commit()


def del_db_muteallall():
    dbcGeneral.execute("DROP TABLE mute")
    dbcGeneral.execute("""CREATE TABLE IF NOT EXISTS mute (user_id,
                                                     firstname, chat_id INTEGER)""")
    dbGeneral.commit()


def get_db_mute(chat_id: int) -> str:
    dbcGeneral.execute("SELECT * FROM mute WHERE chat_id = ?", (chat_id,))
    ul = dbcGeneral.fetchall()
    return ul if ul else None


#######################################################################################################
#######################################################################################################

def set_db_meendafny(user_id_add: int, firstname_add: str, user_id_added: int, chat_id: int):
    dbcGeneral.execute("INSERT INTO meendafny(user_id_add,firstname_add,user_id_added,chat_id) VALUES(?,?,?,?)",
                       (user_id_add, firstname_add, user_id_added, chat_id))
    dbGeneral.commit()


def get_db_meendafny(user_id_added: int, chat_id: int) -> str:
    dbcGeneral.execute("SELECT * FROM meendafny WHERE user_id_added = ? and chat_id = ?", (user_id_added, chat_id))
    ul = dbcGeneral.fetchall()
    return ul if ul else None


def del_db_meendafnyallall():
    dbcGeneral.execute("DROP TABLE meendafny")
    dbcGeneral.execute("""CREATE TABLE IF NOT EXISTS meendafny (user_id_add INTEGER, firstname_add,
                                                     user_id_added INTEGER, chat_id INTEGER)""")
    dbGeneral.commit()


#######################################################################################################
#######################################################################################################

def set_db_mycontact(counter, user_id, chat_id):
    dbcGeneral.execute(
        "SELECT * FROM mycontact WHERE user_id = ? AND chat_id = ?", (user_id, chat_id)
    )
    if dbcGeneral.fetchone():
        dbcGeneral.execute(
            "UPDATE mycontact SET counter = counter + ? WHERE user_id = ? AND chat_id = ?",
            (counter, user_id, chat_id),
        )
        dbGeneral.commit()
    else:
        dbcGeneral.execute(
            "INSERT INTO mycontact (counter, user_id, chat_id) VALUES (?,?,?)",
            (counter, user_id, chat_id),
        )
        dbGeneral.commit()


def del_db_mycontact(user_id: int, chat_id: int):
    dbcGeneral.execute("DELETE FROM mycontact WHERE user_id = ? and chat_id = ?", (user_id, chat_id))
    dbGeneral.commit()


def get_db_mycontact(user_id: int, chat_id: int) -> str:
    dbcGeneral.execute("SELECT counter FROM mycontact WHERE user_id = ? and chat_id = ?",
                       (user_id, chat_id))
    ul = dbcGeneral.fetchone()
    return ul[0] if ul else None


def del_db_mycontactallall():
    dbcGeneral.execute("DROP TABLE mycontact")
    dbcGeneral.execute("""CREATE TABLE IF NOT EXISTS mycontact (counter INTEGER, user_id, chat_id)""")
    dbGeneral.commit()


#######################################################################################################
#######################################################################################################

def set_db_mypointgame(counter, user_id, chat_id):
    dbcGeneral.execute(
        "SELECT * FROM mypointgame WHERE user_id = ? AND chat_id = ?", (user_id, chat_id)
    )
    if dbcGeneral.fetchone():
        dbcGeneral.execute(
            "UPDATE mypointgame SET counter = counter + ? WHERE user_id = ? AND chat_id = ?",
            (counter, user_id, chat_id),
        )
        dbGeneral.commit()
    else:
        dbcGeneral.execute(
            "INSERT INTO mypointgame (counter, user_id, chat_id) VALUES (?,?,?)",
            (counter, user_id, chat_id),
        )
        dbGeneral.commit()


def del_db_mypointgame(user_id: int, chat_id: int):
    dbcGeneral.execute("DELETE FROM mypointgame WHERE user_id = ? and chat_id = ?", (user_id, chat_id))
    dbGeneral.commit()


def get_db_mypointgame(user_id: int, chat_id: int) -> str:
    dbcGeneral.execute("SELECT counter FROM mypointgame WHERE user_id = ? and chat_id = ?",
                       (user_id, chat_id))
    ul = dbcGeneral.fetchone()
    return ul[0] if ul else None


def del_db_mypointgameallall():
    dbcGeneral.execute("DROP TABLE mypointgame")
    dbcGeneral.execute("""CREATE TABLE IF NOT EXISTS mypointgame (counter INTEGER, user_id, chat_id)""")
    dbGeneral.commit()


#######################################################################################################
#######################################################################################################

def set_db_mymessage(counter, user_id, chat_id):
    dbcGeneral.execute(
        "SELECT * FROM mymessage WHERE user_id = ? AND chat_id = ?", (user_id, chat_id)
    )
    if dbcGeneral.fetchone():
        dbcGeneral.execute(
            "UPDATE mymessage SET counter = counter + ? WHERE user_id = ? AND chat_id = ?",
            (counter, user_id, chat_id),
        )
        dbGeneral.commit()
    else:
        dbcGeneral.execute(
            "INSERT INTO mymessage (counter, user_id, chat_id) VALUES (?,?,?)",
            (counter, user_id, chat_id),
        )
        dbGeneral.commit()


def del_db_mymessage(user_id: int, chat_id: int):
    dbcGeneral.execute("DELETE FROM mymessage WHERE user_id = ? and chat_id = ?", (user_id, chat_id))
    dbGeneral.commit()


def get_db_mymessage(user_id: int, chat_id: int) -> str:
    dbcGeneral.execute("SELECT counter FROM mymessage WHERE user_id = ? and chat_id = ?",
                       (user_id, chat_id))
    ul = dbcGeneral.fetchone()
    return ul[0] if ul else None


def del_db_mymessageallall():
    dbcGeneral.execute("DROP TABLE mymessage")
    dbcGeneral.execute("""CREATE TABLE IF NOT EXISTS mymessage (counter INTEGER, user_id, chat_id)""")
    dbGeneral.commit()


#######################################################################################################
#######################################################################################################

def set_db_addcommand(command: str, newcommand: str, chat_id: int):
    dbcGeneral.execute("INSERT INTO addcomand (command,newcommand,chat_id) VALUES(?,?,?)",
                       (command, newcommand, chat_id))
    dbGeneral.commit()


def del_db_addcommand(text: str, chat_id: int):
    dbcGeneral.execute("DELETE FROM addcomand WHERE newcommand = ? and chat_id = ?", (text, chat_id))
    dbGeneral.commit()


def del_db_addcommandall(chat_id: int):
    dbcGeneral.execute("DELETE FROM addcomand WHERE chat_id = ?", (chat_id,))
    dbGeneral.commit()


def get_db_addcommand(chat_id: int) -> str:
    dbcGeneral.execute("SELECT * FROM addcomand WHERE chat_id = ?", (chat_id,))
    ul = dbcGeneral.fetchall()
    return ul if ul else None


#######################################################################################################
#######################################################################################################

def set_db_addcustomid(customid: str, chat_id: int):
    dbcGeneral.execute("INSERT INTO addcustomid(customid, chat_id) VALUES(?,?)", (customid, chat_id))
    dbGeneral.commit()


def del_db_addcustomid(chat_id: int):
    dbcGeneral.execute("DELETE FROM addcustomid WHERE chat_id = ?", (chat_id,))
    dbGeneral.commit()


def get_db_addcustomid(chat_id: int) -> str:
    dbcGeneral.execute("SELECT * FROM addcustomid WHERE chat_id = ?", (chat_id,))
    ul = dbcGeneral.fetchall()
    return ul if ul else None


#######################################################################################################
#######################################################################################################

def set_db_lockkickbotatban(key: str, chat_id: int):
    dbcGeneral.execute("INSERT INTO kickbotatban(key,chat_id) VALUES(?,?)", (key, chat_id))
    dbGeneral.commit()


def del_db_lockkickbotatban(chat_id: int):
    dbcGeneral.execute("DELETE FROM kickbotatban WHERE chat_id = ?", (chat_id,))
    dbGeneral.commit()


def get_db_lockkickbotatban(chat_id: int) -> str:
    dbcGeneral.execute("SELECT key FROM kickbotatban WHERE chat_id = ?", (chat_id,))
    ul = dbcGeneral.fetchall()
    return ul if ul else None

#######################################################################################################
#######################################################################################################
