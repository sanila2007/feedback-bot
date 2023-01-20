# Copyright ©️ 2022 Sanila Ranatunga. All Rights Reserved
# You are free to use this code in any of your project, but you MUST include the following in your README.md (Copy & paste)
# ##Credits - [feedback-bot] (https://github.com/sanila2007/feedback-bot)

# Read GNU General Public License v3.0: https://github.com/sanila2007/feedback-bot/blob/mai/LICENSE
# Don't forget to follow github.com/sanila2007 because I'm doing these things for free and open source
# Star and fork and enjoy!


from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup

from config import Config
from helper import buttons, messages
from util import date_info

INLINE_BB = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton("Inline Mode Bot list 🔎", switch_inline_query_current_chat="")
        ]
    ]
)


# START MESSAGE

@Client.on_message(filters.command("start") & filters.private)
async def command1(bot, message):
    text = f"Hello **{message.from_user.first_name}!**\n\n" + messages.START_TEXT_CAPTION_TEXT
    reply_markup = INLINE_BB
    await message.reply(
        text=text,
        reply_markup=reply_markup,
        disable_web_page_preview=True
    )
    await message.reply(
        "Use ReplyKeyboard or Inline Mode...",
        reply_markup=ReplyKeyboardMarkup(buttons.REPLY_BUTTONS, one_time_keyboard=False, resize_keyboard=True)
    )
    try:
        await bot.send_message(Config.LOG_CHANNEL,
                             f"New User!\n\n◉ User - {message.from_user.first_name}\n◉ Joined time - {date_info.POSTED_TIME}\n◉ Joined date - {date_info.POSTED_DATE}")
    except Exception as er:
        print(f"Unable to send the logs to the channel.\nReason: {er}")
