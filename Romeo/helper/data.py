from pyrogram.types import InlineKeyboardButton, WebAppInfo

class Data:

    text_help_menu = (
        "**DEVILBOT PLUGINS**\n**COMMAND PREFIX;-** `.`"
        .replace(",", "")
        .replace("[", "")
        .replace("]", "")
        .replace("'", "")
    )
    reopen = [[InlineKeyboardButton("Re-Open", callback_data="reopen")]]
