from pyrogram.types import InlineKeyboardButton

import config
from DAXXMUSIC import app


def start_panel(_):
    buttons = [
        [
            InlineKeyboardButton(
                text=_["S_B_1"], url=f"https://t.me/{app.username}?startgroup=true"
            ),
            InlineKeyboardButton(text=_["S_B_2"], url=config.SUPPORT_CHAT),
        ],
    ]
    return buttons


def private_panel(_):
    buttons = [
        [
            InlineKeyboardButton(
                text="➕ ᴀᴅᴅ ᴍᴇ ➕",
                url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
            )
        ],
        [
            InlineKeyboardButton(
                text="✭ʜᴇʟᴘ & ᴄᴏᴍᴍᴀɴᴅs✭", callback_data="settings_back_helper"
            )
        ],
        [
            InlineKeyboardButton(
                text="✭ ᴜᴘᴅᴀᴛᴇs ✭", url=config.SUPPORT_CHANNEL
            ),
            InlineKeyboardButton(
                text="✭ sᴜᴘᴘᴏʀᴛ ✭", url=config.SUPPORT_GROUP
            )
        ],
        [
            InlineKeyboardButton(
                text="✮💞 ᴍᴀɪɴᴛᴀɪɴᴇʀ 💞✮", url=f"tg://openmessage?user_id=6910477574"
            )
        ]
     ]
    return buttons
