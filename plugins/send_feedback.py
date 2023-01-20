# Copyright ©️ 2022 Sanila Ranatunga. All Rights Reserved
# You are free to use this code in any of your project, but you MUST include the following in your README.md (Copy & paste)
# ##Credits - [feedback-bot] (https://github.com/sanila2007/feedback-bot)

# Read GNU General Public License v3.0: https://github.com/sanila2007/feedback-bot/blob/mai/LICENSE
# Don't forget to follow github.com/sanila2007 because I'm doing these things for free and open source
# Star and fork and enjoy!


from pyrogram import Client, filters
from pyrogram import enums
from pyrogram.types import ReplyKeyboardMarkup, ForceReply

from config import Config
from helper import buttons
from util import date_info


@Client.on_message(filters.reply & filters.private)
def fbb(bot, message):
    bot.send_chat_action(message.chat.id, enums.ChatAction.TYPING)
    tet = f"**<u>Feedback Information</u>**\n\nMessage - `{message.text}`\nWord count - {len(message.text.split())}\nPosted by - {message.from_user.first_name}\nUser ID - {message.from_user.id}\nUsername - @{message.chat.username}\nLanguage - {message.from_user.language_code}\nChat type - {message.chat.type}\nPosted date - {date_info.POSTED_DATE}\nPosted time - {date_info.POSTED_TIME}\nDate of reply - {date_info.DATE_OF_REPLY}\n\n<i>*Note: Add more feedbacks or click finish</i>"
    reply_markup = ReplyKeyboardMarkup(buttons.FINISH_FEEDBACK_BUTTONS, one_time_keyboard=True, resize_keyboard=True)
    message.reply(
        text=tet,
        reply_markup=reply_markup,
        quote=True,
        protect_content=True
    )
    global vaar
    vaar = message.chat.id
    try:
        bot.send_message(Config.FEEDBACK_GROUP, "**New feedback available!**\n\n" + tet, protect_content=True,
                         reply_markup=ForceReply(message.chat.id))
    except Exception as e:
        bot.send_message(message.chat.id,
                         f"**Oops!! error occurred while sending feedback to the admin.**\n\n<i>Reason: {e}</i> ")


@Client.on_message(filters.group & filters.reply & filters.user(Config.ADMIN))
def do_nothing(bot, message):
    try:
        bot.send_message(vaar,
                         f"**Admin message** #admin_msg:\n➖➖➖➖➖➖➖➖➖➖\n{message.text}\n\n~Powered by <a href=https://github.com/sanila2007/Feedback-Bot>Feedback Bot</a>",
                         disable_web_page_preview=True, protect_content=True)
        bot.send_message(Config.FEEDBACK_GROUP, f"Your reply have been sent to the user successfully.",
                         protect_content=True)
    except Exception as error_nothing:
        print(f"Error occurred: {error_nothing}")
