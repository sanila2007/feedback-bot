# Copyright ©️ 2022 Sanila Ranatunga. All Rights Reserved
# You are free to use this code in any of your project, but you MUST include the following in your README.md (Copy & paste)
# ##Credits - [Sanila-Assistant-Bot] (https://github.com/sanila2007/Sanila-Assistant-Bot)

# Changing the code is not allowed! Read GNU General Public License v3.0: https://github.com/sanila2007/Sanila-Assistant-Bot/blob/mai/LICENSE


import os
import buttons
import messages
import pyrogram
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup

from configs import Config

bot = Client(
    "bot",
    api_id=Config.API_ID,
    api_hash=Config.API_HASH,
    bot_token=Config.BOT_TOKEN
)


# START MESSAGE

@bot.on_message(filters.command("start") & filters.private)
def command1(bot, message):
    text = "Use ReplyKeyboard..."
    reply_markup = ReplyKeyboardMarkup(buttons.REPLY_BUTTONS)
    bot.send_photo(message.chat.id, "https://telegra.ph/file/f7dc9203585394d0595b1.jpg",
                   caption=messages.START_TEXT_CAPTION_TEXT),
    message.reply(
        text=text,
        reply_markup=reply_markup,
        disable_web_page_preview=True
    )



# Learn bots section

@bot.on_message(filters.regex("Learn Bots"))
def reply_to_Learn_Bots(bot, message):
    text = messages.LEARN_TEXT
    reply_markup = ReplyKeyboardMarkup(buttons.LEARN_REPLY_BUTTONS, one_time_keyboard=False, resize_keyboard=True)
    message.reply(
        text=text,
        reply_markup=reply_markup,
        disable_web_page_preview=True
    )


@bot.on_message(filters.regex("Song Download Bot🤖💖"))
def reply_to_utube(bot, message):
    bot.send_message(message.chat.id, "Song Downloader bot!!")
    bot.send_photo(message.chat.id, "https://telegra.ph/file/87ce14694a8c1d65cffaf.jpg", caption="<b>Step 1</b>")
    bot.send_photo(message.chat.id, "https://telegra.ph/file/13218e7e5fb04f37d555e.jpg",
                   caption="<b>Step 2\nYou must send the song like this👇👇\n   ️/song Senorita</b>")
    bot.send_photo(message.chat.id, "https://telegra.ph/file/a3de0355d3fa67676e680.jpg", caption="<b>Step 3</b>")


@bot.on_message((filters.regex("Torrent Download Bot🤖💖")))
def reply_to_s_ong(bot, message):
    bot.send_message(message.chat.id, "Torrent downloader bot!")
    bot.send_photo(message.chat.id, "https://telegra.ph/file/cedb06244d2f74979095f.jpg", caption="<b>Step 1</b>")
    bot.send_photo(message.chat.id, "https://telegra.ph/file/b5956b401cb68cd7b8d2f.jpg", caption="<b>Step 2</b>")
    bot.send_photo(message.chat.id, "https://telegra.ph/file/a3d2f02b3c7e4ab742bc8.jpg", caption="<b>Step 3</b>")
    bot.send_photo(message.chat.id, "https://telegra.ph/file/17f2f0820c5007b136086.jpg", caption="<b>Step 4</b>")


@bot.on_message((filters.regex("Youtube Video Download Bot🤖💖")))
def reply_to_s_ong(bot, message):
    bot.send_message(message.chat.id, "Youtube Video Downloader bot!!!")
    bot.send_photo(message.chat.id, "https://telegra.ph/file/81aab8398259866256409.jpg", caption="<b>Step 1</b>")
    bot.send_photo(message.chat.id, "https://telegra.ph/file/e1c08af0c0e5f28053855.jpg", caption="<b>Step 2</b>")
    bot.send_photo(message.chat.id, "https://telegra.ph/file/3fc72cf3f77f4e4c3d28f.jpg", caption="<b>Step 3</b>")


# About bot section

@bot.on_message(filters.regex("About Bot"))
def reply_to_AboutBot(bot, message):
    bot.send_message(message.chat.id, "<ins>**About Bot**</ins>\n\n"
                                      "Name: <a href=https://t.me/sanilaassistant_bot>Sanila's Assistant Bot ✨</a>\n\n"
                                      "Created on: 11/21/2021🎂\n\n"
                                      "Latest Version:  v0.7.3\n\n"
                                      "Language: <a href=www.python.org>Python</a>\n\n"
                                      "Framework: <a href=https://docs.pyrogram.org/>Pyrogram</a> ✌️\n\n"
                                      "Server: <a href=https://heroku.com>Heroku</a>\n\n"
                                      "Developer: <a href=https://github.com/sanila2007>Sanila Ranatunga\n\n</a>"
                                      "Source: 🔓\n\n", disable_web_page_preview=True)


# Contact section

@bot.on_message(filters.regex("Contact 📞"))
def reply_to_Contact(bot, message):
    bot.send_message(message.chat.id, messages.CONTACT_TEXT)


# About Developer

@bot.on_message(filters.regex("About Developer"))
def reply_to_About(bot, message):
    bot.send_message(message.chat.id,
                     "**<ins>About Developer</ins>**\n\n""❖ Name : Sanila Ranatunga😎\n\n""❖ Age : 15 Years (2022) 🙃\n\n""❖ Birthday : 09.01.2007🎂\n\n""❖ From : Sri Lanka🇱🇰\n\n""❖ Skills : Programmer , Developer😏\n\n""❖ Ambition : Be a software engineer😊\n\n""❖ Languages : Python, HTML, CSS🙃\n\n❖ Still Learning : C++, JS, Java")


# Home

@bot.on_message(filters.regex("Home"))
def greet(bot, message):
    text = messages.REPLY_MESSAGE
    reply_markup = ReplyKeyboardMarkup(buttons.REPLY_BUTTONS, one_time_keyboard=False, resize_keyboard=True)
    message.reply(
        text=text,
        reply_markup=reply_markup,
        disable_web_page_preview=True

    )


# Feedbacks section

@bot.on_message(filters.regex("Feedback"))
def reply_to_Feedback(bot, message):
    text = messages.FEEDBACK_REPLY_TEXT
    reply_markup = ReplyKeyboardMarkup(buttons.FEEDBACK_REPLY_BUTTONS, one_time_keyboard=True, resize_keyboard=True)
    message.reply(
        text=text,
        reply_markup=reply_markup
    )


# Credits

@bot.on_message(filters.regex("Credits"))
def reply_to_Credits(bot, message):
    text = messages.CREDITS_TEXT
    reply_markup = ReplyKeyboardMarkup(buttons.HOME_BUTTON_CR, one_time_keyboard=False, resize_keyboard=True)
    message.reply(
        text=text,
        reply_markup=reply_markup,
        disable_web_page_preview=True
    )


# Finish button and text

@bot.on_message(filters.regex("Finish"))
def reply_to_finish(bot, message):
    text = messages.FINISH_TEXT
    reply_markup = ReplyKeyboardMarkup(buttons.REPLY_BUTTONS, resize_keyboard=True, one_time_keyboard=False)
    message.reply(
        text=text,
        reply_markup=reply_markup,
        disable_web_page_preview=True
    )


# Report bugs section

@bot.on_message(filters.regex("Report Bugs"))
def reply_to_Report(bot, message):
    text = messages.REPORT_BUGS_TEXT
    reply_markup = ReplyKeyboardMarkup(buttons.REPORT_BUGS_BUTTONS, one_time_keyboard=True, resize_keyboard=True)
    message.reply(
        text=text,
        reply_markup=reply_markup
    )


# Changelog Section

@bot.on_message(filters.regex("Changelog"))
def reply_to_Changelog(bot, message):
    bot.send_message(message.chat.id, messages.CHANGELOG_TEXT, disable_web_page_preview=True)


# Assistant Bot Feedback/Report bugs centre

@bot.on_message(filters.regex("Sanila Assistant Bot"))
def reply_to_Assistant(bot, message):
    text = messages.SANILA_ASSISTANT_TEXT
    reply_markup = None
    message.reply(
        text=text, disable_web_page_preview=True,
        reply_markup=reply_markup
    )


# Reporting area - Song Downloader bot

@bot.on_message(filters.regex("Song Downloader Bot"))
def reply_to_Song(bot, message):
    text = messages.SONG_DOWNLOADER_TEXT
    message.reply(
        text=text,
        disable_web_page_preview=True
    )


# Reporting area - Torrent downloader bot

@bot.on_message(filters.regex("Torrent Downloader Bot"))
def reply_to_Torrent(bot, message):
    text = messages.TORRENT_DOWNLOADER_TEXT
    message.reply(
        text=text,
        disable_web_page_preview=True
    )


# Reporting area - Youtube video downloader bot

@bot.on_message(filters.regex("Youtube Video Downloader Bot"))
def reply_to_Youtube(bot, message):
    text = messages.YOUTUBE_VIDEO_DOWNLOADER_TEXT
    message.reply(
        text=text,
        disable_web_page_preview=True
    )


@bot.on_message(filters.private)
async def hello(bot, message):
    text = messages.SEND_TEXT_FEEDBACK
    reply_markup = ReplyKeyboardMarkup(buttons.FINISH_FEEDBACK_BUTTONS, resize_keyboard=True,
                                       one_time_keyboard=False)
    await message.reply(
        text=text,
        reply_markup=reply_markup)


print("Bot is alive📶✨")

bot.run()
