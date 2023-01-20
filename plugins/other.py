# Copyright ©️ 2022 Sanila Ranatunga. All Rights Reserved
# You are free to use this code in any of your project, but you MUST include the following in your README.md (Copy & paste)
# ##Credits - [feedback-bot] (https://github.com/sanila2007/feedback-bot)

# Read GNU General Public License v3.0: https://github.com/sanila2007/feedback-bot/blob/mai/LICENSE
# Don't forget to follow github.com/sanila2007 because I'm doing these things for free and open source
# Star and fork and enjoy!


from pyrogram import Client, filters
from pyrogram import enums
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup, ForceReply

from config import Config
from helper import buttons, messages
from util import date_info

VERSION = "v1.9.3"

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


@Client.on_message(filters.regex(pattern="Changelog"))
def reply_to_Changelog(bot, message):
    reply_markup = ReplyKeyboardMarkup(buttons.HOME_BUTTON_CR, resize_keyboard=True, one_time_keyboard=False)
    bot.send_message(message.chat.id, messages.CHANGELOG_TEXT, disable_web_page_preview=True, reply_markup=reply_markup)


@Client.on_message(filters.regex(pattern="Finish"))
def reply_finish(bot, message):
    bot.send_message(message.chat.id, messages.FEEDBACK_FINISH_TEXT,
                     reply_markup=ReplyKeyboardMarkup(buttons.REPLY_BUTTONS, resize_keyboard=True,
                                                      one_time_keyboard=False))


# Contact section

@Client.on_message(filters.regex(pattern="Contact 📞"))
def reply_to_Contact(bot, message):
    bot.send_message(message.chat.id, messages.CONTACT_TEXT, reply_markup=ForceReply(message.chat.id))


# Home

@Client.on_message(filters.regex(pattern="Home"))
def greet(bot, message):
    text = messages.REPLY_MESSAGE
    reply_markup = INLINE_BB
    message.reply(
        text=text,
        reply_markup=reply_markup,
        disable_web_page_preview=True
    )
    message.reply(
        text="Use ReplyKeyboards or Inline Mode...",
        reply_markup=ReplyKeyboardMarkup(buttons.REPLY_BUTTONS, one_time_keyboard=False, resize_keyboard=True)
    )


@Client.on_message(filters.regex(pattern="About Bot"))
def reply_to_AboutBot(bot, message):
    bot.send_message(message.chat.id, "<ins>**About Bot**</ins>\n\n"
                                      "Name: <a href=https://t.me/sanilaassistant_bot>Sanila's Assistant Bot</a>\n\n"
                                      "Created on: `11/21/2021`\n\n"
                                      f"Latest Version:  `{VERSION}`\n\n"
                                      "Language: <a href=www.python.org>Python</a>\n\n"
                                      "Framework: <a href=https://docs.pyrogram.org/>Pyrogram</a>\n\n"
                                      "Server: <a href=https://heroku.com>Heroku</a>\n\n"
                                      "Developer: <a href=https://github.com/sanila2007>Sanila Ranatunga\n\n</a>"
                                      "Source: 🔓\n\n", disable_web_page_preview=True)


@Client.on_message(filters.sticker)
async def restric_sticker(bot, message):
    await bot.send_chat_action(message.chat.id, enums.ChatAction.CANCEL)
    await bot.send_message(message.chat.id, "Oops!\n\nStickers has been restricted")
