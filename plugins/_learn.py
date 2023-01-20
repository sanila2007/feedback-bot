# Copyright ©️ 2022 Sanila Ranatunga. All Rights Reserved
# You are free to use this code in any of your project, but you MUST include the following in your README.md (Copy & paste)
# ##Credits - [feedback-bot] (https://github.com/sanila2007/feedback-bot)

# Read GNU General Public License v3.0: https://github.com/sanila2007/feedback-bot/blob/mai/LICENSE
# Don't forget to follow github.com/sanila2007 because I'm doing these things for free and open source
# Star and fork and enjoy!


from pyrogram import Client, filters
from pyrogram import enums
from pyrogram.types import ReplyKeyboardMarkup

from helper import buttons, messages


# Learn bots section

@Client.on_message(filters.regex(pattern="Learn Bots"))
def reply_to_Learn_Bots(bot, message):
    text = messages.LEARN_TEXT
    reply_markup = ReplyKeyboardMarkup(buttons.LEARN_REPLY_BUTTONS, one_time_keyboard=False, resize_keyboard=True)
    message.reply(
        text=text,
        reply_markup=reply_markup,
        disable_web_page_preview=True
    )


@Client.on_message(filters.regex(pattern="Song Download Bot🤖💖"))
def reply_to_utube(bot, message):
    bot.send_chat_action(message.chat.id, enums.ChatAction.UPLOAD_DOCUMENT)
    bot.send_message(message.chat.id,
                     "<a href=https://telegra.ph/How-to-use-Song-Downloader-Bot-07-09>How to use Song Downloader Bot?</a>")


@Client.on_message(filters.regex(pattern="Torrent Download Bot🤖💖"))
def reply_to_s_on(bot, message):
    bot.send_chat_action(message.chat.id, enums.ChatAction.UPLOAD_DOCUMENT)
    bot.send_message(message.chat.id,
                     "<a href=https://telegra.ph/How-to-use-the-Torrent-Downloader-Bot-07-09>How to use Torrent Downloader Bot?</a>")


@Client.on_message((filters.regex(pattern="Youtube Video Download Bot🤖💖")))
def reply_to_s_ong(bot, message):
    bot.send_chat_action(message.chat.id, enums.ChatAction.UPLOAD_DOCUMENT)
    bot.send_message(message.chat.id,
                     "<a href=https://telegra.ph/How-to-use-the-Youtube-Video-Downloader-Bot-07-09>How to use YouTube Video Download Bot?</a>")


@Client.on_message((filters.regex(pattern="Telegrph Upload Bot🤖💖")))
def reply_to_s_ong(bot, message):
    bot.send_chat_action(message.chat.id, enums.ChatAction.UPLOAD_DOCUMENT)
    bot.send_message(message.chat.id,
                     "<a href=https://telegra.ph/How-to-use-Telegram-Telegraph-Uploader-Bot-08-09>How to use Telegraph uploader Bot?</a>")
