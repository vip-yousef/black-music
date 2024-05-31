from typing import List, Union

from pyrogram import filters


other_filters = filters.group  & ~filters.via_bot & ~filters.forwarde
other_filters2 = (
    filters.private  & ~filters.via_bot & ~filters.forwarded & ~filters.regex
)


def command(commands: Union[str, List[str]]):
    return filters.command(commands, "")
