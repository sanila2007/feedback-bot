# Copyright ©️ 2022 Sanila Ranatunga. All Rights Reserved
# You are free to use this code in any of your project, but you MUST include the following in your README.md (Copy & paste)
# ##Credits - [feedback-bot] (https://github.com/sanila2007/feedback-bot)

# Read GNU General Public License v3.0: https://github.com/sanila2007/feedback-bot/blob/mai/LICENSE
# Don't forget to follow github.com/sanila2007 because I'm doing these things for free and open source
# Star and fork and enjoy!


from pyrogram import Client, filters
from pyrogram.types import ReplyKeyboardMarkup, ForceReply

from helper import buttons, messages


@Client.on_message(filters.regex(pattern="Feedbacks"))
def reply_to_Feedback(bot, message):
    text = messages.FEEDBACK_REPLY_TEXT
    reply_markup = ReplyKeyboardMarkup(buttons.FEEDBACK_REPLY_BUTTONS, one_time_keyboard=True, resize_keyboard=True)
    message.reply(
        text=text,
        reply_markup=reply_markup
    )


# Assistant Bot Feedback/Report bugs centre

@Client.on_message(filters.regex(pattern="Sanila Assistant Bot"))
async def reply_to_Assistant(bot, message):
    reply_markup = ForceReply(message.chat.id)
    await bot.send_message(message.chat.id, messages.SANILA_ASSISTANT_TEXT,
                           reply_markup=reply_markup
                           , disable_web_page_preview=True)


# Reporting area - Song Downloader bot

@Client.on_message(filters.regex("Song Downloader Bot"))
def reply_to_Song(bot, message):
    reply_markup = ForceReply(message.chat.id)
    text = messages.SONG_DOWNLOADER_TEXT
    message.reply(
        text=text,
        reply_markup=reply_markup,
        disable_web_page_preview=True
    )


# Reporting area - Torrent downloader bot

@Client.on_message(filters.regex(pattern="Torrent Downloader Bot"))
async def reply_to_Torrent(bot, message):
    reply_markup = ForceReply(message.chat.id)
    text = messages.TORRENT_DOWNLOADER_TEXT
    await message.reply(
        text=text,
        reply_markup=reply_markup,
        disable_web_page_preview=True
    )


# Reporting area - Telegraph uploader bot


@Client.on_message(filters.regex(pattern="Telegraph Uploader Bot"))
def reply_to_Youtube(bot, message):
    text = messages.TELEGRAPH_UPLOADER_TEXT
    reply_markup = ForceReply(message.chat.id)
    message.reply(
        text=text,
        reply_markup=reply_markup,
        disable_web_page_preview=True
    )
