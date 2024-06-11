import math

from pyrogram.types import InlineKeyboardButton

from MatrixMusic.utils.formatters import time_to_seconds


def track_markup(_, videoid, user_id, channel, fplay):
    buttons = [
        [
            InlineKeyboardButton(
                text=_["P_B_1"],
                callback_data=f"MusicStream {videoid}|{user_id}|a|{channel}|{fplay}",
            ),
            InlineKeyboardButton(
                text=_["P_B_2"],
                callback_data=f"MusicStream {videoid}|{user_id}|v|{channel}|{fplay}",
            ),
        ],
        [
            InlineKeyboardButton(
                text=_["CLOSE_BUTTON"],
                callback_data=f"forceclose {videoid}|{user_id}",
            )
        ],
    ]
    return buttons


def stream_markup_timer(_, chat_id, played, dur):
    played_sec = time_to_seconds(played)
    duration_sec = time_to_seconds(dur)
    percentage = (played_sec / duration_sec) * 100
    umm = math.floor(percentage)
    if 0 < umm <= 10:
        bar = "◉—————————"
    elif 10 < umm < 20:
        bar = "—◉————————"
    elif 20 <= umm < 30:
        bar = "——◉———————"
    elif 30 <= umm < 40:
        bar = "———◉——————"
    elif 40 <= umm < 50:
        bar = "————◉—————"
    elif 50 <= umm < 60:
        bar = "—————◉————"
    elif 60 <= umm < 70:
        bar = "——————◉———"
    elif 70 <= umm < 80:
        bar = "———————◉——"
    elif 80 <= umm < 95:
        bar = "————————◉—"
    else:
        bar = "—————————◉"
    buttons = [
        [
            InlineKeyboardButton(text="ᎡᎬՏႮᎷᎬ", callback_data=f"ADMIN Resume|{chat_id}"),
            InlineKeyboardButton(text="ᏢᎪႮՏᎬ", callback_data=f"ADMIN Pause|{chat_id}"),
            InlineKeyboardButton(text="ᎬŃᎠ", callback_data=f"ADMIN Stop|{chat_id}"),
            
        ],
        [
            
        ],
        [InlineKeyboardButton(text="ᏟᎻᎪΝΝᎬᏞ", url=f"https://t.me/KKC8C"), InlineKeyboardButton(text="ᏟᎻᎪΝΝᎬᏞ²", url=f"https://t.me/cecrr")],
        
        [InlineKeyboardButton("⏤͟͞ َِ⍣⃟َ𝐓𝐇ِ𝐄 𓆩ََِِ𝐘َِْ𝐎ِِ𝐔ًٌُ𝐒𝐄ُِ𝐅𓆪", url=f"https://t.me/y_o_v")],
        [InlineKeyboardButton(text="اضف البوت الي مجموعتك او قناتك ⚡️", url=f"https://t.me/Gor_Genabot?startgroup=True")],
    ]
    return buttons


def stream_markup(_, chat_id):
    buttons = [
        [
            InlineKeyboardButton(text="ᎡᎬՏႮᎷᎬ", callback_data=f"ADMIN Resume|{chat_id}"),
            InlineKeyboardButton(text="ᏢᎪႮՏᎬ", callback_data=f"ADMIN Pause|{chat_id}"),
            InlineKeyboardButton(text="ᎬŃᎠ", callback_data=f"ADMIN Stop|{chat_id}"),
            
    
        ],
        [InlineKeyboardButton(text="ᏟᎻᎪΝΝᎬᏞ", url=f"https://t.me/KKC8C"), InlineKeyboardButton(text="ᏟᎻᎪΝΝᎬᏞ²", url=f"https://t.me/cecrr")],
        [InlineKeyboardButton("⏤͟͞ َِ⍣⃟َ𝐓𝐇ِ𝐄 𓆩ََِِ𝐘َِْ𝐎ِِ𝐔ًٌُ𝐒𝐄ُِ𝐅𓆪", url=f"https://t.me/y_o_v")],
        [InlineKeyboardButton(text="اضف البوت الي مجموعتك او قناتك ⚡️", url=f"https://t.me/Gor_Genabot?startgroup=True")],
    ]
    return buttons


def playlist_markup(_, videoid, user_id, ptype, channel, fplay):
    buttons = [
        [
            InlineKeyboardButton(
                text=_["P_B_1"],
                callback_data=f"AnonyPlaylists {videoid}|{user_id}|{ptype}|a|{channel}|{fplay}",
            ),
            InlineKeyboardButton(
                text=_["P_B_2"],
                callback_data=f"AnonyPlaylists {videoid}|{user_id}|{ptype}|v|{channel}|{fplay}",
            ),
        ],
        [
            InlineKeyboardButton(
                text=_["CLOSE_BUTTON"],
                callback_data=f"forceclose {videoid}|{user_id}",
            ),
        ],
    ]
    return buttons


def livestream_markup(_, videoid, user_id, mode, channel, fplay):
    buttons = [
        [
            InlineKeyboardButton(
                text=_["P_B_3"],
                callback_data=f"LiveStream {videoid}|{user_id}|{mode}|{channel}|{fplay}",
            ),
        ],
        [
            InlineKeyboardButton(
                text=_["CLOSE_BUTTON"],
                callback_data=f"forceclose {videoid}|{user_id}",
            ),
        ],
    ]
    return buttons


def slider_markup(_, videoid, user_id, query, query_type, channel, fplay):
    query = f"{query[:20]}"
    buttons = [
        [
            InlineKeyboardButton(
                text=_["P_B_1"],
                callback_data=f"MusicStream {videoid}|{user_id}|a|{channel}|{fplay}",
            ),
            InlineKeyboardButton(
                text=_["P_B_2"],
                callback_data=f"MusicStream {videoid}|{user_id}|v|{channel}|{fplay}",
            ),
        ],
        [
            InlineKeyboardButton(
                text="◁",
                callback_data=f"slider B|{query_type}|{query}|{user_id}|{channel}|{fplay}",
            ),
            InlineKeyboardButton(
                text=_["CLOSE_BUTTON"],
                callback_data=f"forceclose {query}|{user_id}",
            ),
            InlineKeyboardButton(
                text="▷",
                callback_data=f"slider F|{query_type}|{query}|{user_id}|{channel}|{fplay}",
            ),
        ],
    ]
    return buttons
