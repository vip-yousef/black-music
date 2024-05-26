from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup



def botplaylist_markup(_):
    buttons = [
        [
            InlineKeyboardButton(text=_["PL_B_1"],callback_data="get_playlist_playmode"),
            InlineKeyboardButton(text=_["PL_B_8"], callback_data="get_top_playlists"),
            InlineKeyboardButton(text=_["PL_B_4"], callback_data="PM"),
            InlineKeyboardButton(text=_["CLOSE_BUTTON"], callback_data="close"),
        ],
    ]
    return buttons

def close_markup(_):
    upl = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(
                    text=_["CLOSE_BUTTON"],
                    callback_data="close",
                ),
            ]
        ]
    )
    return upl
