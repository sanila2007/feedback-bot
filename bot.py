#Copyright ©️ 2022 Sanila Ranatunga. All Rights Reserved
#You are free to use this code in any of your project, but you MUST include the following in your README.md (Copy & paste)
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

DONE_MESSAGE = "Thanks for collaboration to make Sanila's bots much better! You will get reply to yur feedback by this bot around **48hours** till then have some patient\n"


@bot.on_message(filters.command("start") & filters.private)
def command1(bot, message):
    text = "Click any button from ReplyKeyboard as your choice..."
    reply_markup = ReplyKeyboardMarkup(buttons.REPLY_BUTTONS)
    bot.send_photo(message.chat.id, "https://telegra.ph/file/f7dc9203585394d0595b1.jpg",
                   caption=messages.START_TEXT_CAPTION_TEXT),
    message.reply(
        text=text,
        reply_markup=reply_markup,
        disable_web_page_preview=True
    )


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


@bot.on_message(filters.regex("About Bot"))
def reply_to_AboutBot(bot, message):
    bot.send_message(message.chat.id, "<ins>**About Bot**</ins>\n\n"
                                      "Name: <a href=https://t.me/sanilaassistant_bot>Sanila's Assistant Bot ✨</a>\n\n"
                                      "Created on: 11/21/2021🎂\n\n"
                                      "Latest Version:  v0.6\n\n"
                                      "Language: <a href=www.python.org>Python</a>\n\n"
                                      "Framework: <a href=https://docs.pyrogram.org/>Pyrogram</a> ✌️\n\n"
                                      "Developer: <a href=https://github.com/sanila2007>Sanila Ranatunga\n\n</a>"
                                      "Source: 🔓\n\n", disable_web_page_preview=True)


@bot.on_message(filters.regex("Contact📞"))
def reply_to_Contact(bot, message):
    text = messages.CONTACT_TEXT
    reply_markup = ReplyKeyboardMarkup(buttons.SEND_CONTACT_BUTTON, one_time_keyboard=False, resize_keyboard=True)
    message.reply(
        text=text,
        reply_markup=reply_markup,
        disable_web_page_preview=True
    )


@bot.on_message(filters.regex("Send Message"))
def reply_to_Contact_send_message(bot, message):
    bot.send_message(message.chat.id,
                     "☑️You request has been accepted!\n\n🚶 Please have some patience until Sanila's reply.\n\nSanila's Contact Centre.")


@bot.on_message(filters.regex("About Sanila"))
def reply_to_About(bot, message):
    bot.send_message(message.chat.id,
                     "**<ins>About Sanila</ins>**\n\n""❖ Name : Sanila Ranatunga😎\n\n""❖ Age : 15 Years (2022) 🙃\n\n""❖ Birthday : 09.01.2007🎂\n\n""❖ From : Sri Lanka🇱🇰\n\n""❖ Skills : Programmer , Developer😏\n\n""❖ Ambition : Be a software engineer😊\n\n""❖ Languages : Python, HTML, CSS🙃\n\n❖ Still Learning : C++, JS, Java")


@bot.on_message(filters.regex("♻️Done & give more feedbacks"))
def reply_to_Done_Feedback(bot, message):
    text = messages.REPORT_BUGS_TEXT
    reply_markup = ReplyKeyboardMarkup(buttons.REPORT_BUGS_BUTTONS, one_time_keyboard=False, resize_keyboard=True)
    message.reply(
        text=text,
        reply_markup=reply_markup
    )


@bot.on_message(filters.regex("Home"))
def greet(bot, message):
    text = messages.REPLY_MESSAGE
    reply_markup = ReplyKeyboardMarkup(buttons.REPLY_BUTTONS, one_time_keyboard=False, resize_keyboard=True)
    message.reply(
        text=text,
        reply_markup=reply_markup,
        disable_web_page_preview=True

    )


@bot.on_message(filters.regex("Help Centre💁"))
def reply_to_Help_Centre(bot, message):
    text = messages.HELP_CENTRE_TEXT
    reply_markup = ReplyKeyboardMarkup(buttons.HELP_CENTRE_DONE_BUTTONS, one_time_keyboard=False, resize_keyboard=True)
    message.reply(
        text=text,
        reply_markup=reply_markup,
        disable_web_page_preview=True
    )


@bot.on_message(filters.regex("Feedback"))
def reply_to_Feedback(bot, message):
    text = messages.FEEDBACK_REPLY_TEXT
    reply_markup = ReplyKeyboardMarkup(buttons.FEEDBACK_REPLY_BUTTONS, one_time_keyboard=True, resize_keyboard=True)
    message.reply(
        text=text,
        reply_markup=reply_markup
    )


@bot.on_message(filters.regex("Send📩"))
def reply_to_send(bot, message):
    text = messages.SEND_TEXT
    reply_markup = ReplyKeyboardMarkup(buttons.REPLY_BUTTONS, one_time_keyboard=False, resize_keyboard=True)
    message.reply(
        text=text,
        reply_markup=reply_markup,
        disable_web_page_preview=True
    )


@bot.on_message(filters.regex("Report Bugs"))
def reply_to_Report(bot, message):
    text = messages.REPORT_BUGS_TEXT
    reply_markup = ReplyKeyboardMarkup(buttons.REPORT_BUGS_BUTTONS, one_time_keyboard=True, resize_keyboard=True)
    message.reply(
        text=text,
        reply_markup=reply_markup
    )



@bot.on_message(filters.regex("Sanila Assistant Bot🤖💖"))
def reply_to_Assistant(bot, message):
    text = "Reporting Area‼️\n\nBot = <a href=https://t.me/sanilaassistant_bot> Sanila's Assistant Bot</a>\n\n≡ Type your report here and send it\n\n≡ Then Click <<**Done**>>\n\n≡ You will get answer for your feedback/report around <b><b>48hours.</b></b>\n\n" \
           "||**Thank you for your collaboration to make us much better!💖**||"
    reply_markup = ReplyKeyboardMarkup(buttons.DONE_REPLY_KEYBORD, one_time_keyboard=False, resize_keyboard=True)
    message.reply(
        text=text,disable_web_page_preview=True,
        reply_markup=reply_markup
    )


@bot.on_message(filters.regex("Done"))
def reply_to_Done(bot, message):
    text = messages.SEND_TEXT_FEEDBACK
    reply_markup = ReplyKeyboardMarkup(buttons.REPLY_BUTTONS, one_time_keyboard=False, resize_keyboard=True)
    message.reply(
        text=text,
        reply_markup=reply_markup

    )


@bot.on_message(filters.regex("Song Downloader Bot"))
def reply_to_Song(bot, message):
    text = "Reporting Area‼️\n\nBot = <a href=https://t.me/songdownload597_bot> Song Downloader Bot</a>\n\n≡ Type your report here and send it\n\n≡ Then Click <<**Done**>>\n\n≡ You will get answer for your feedback/report around <b><b>48hours.</b></b>\n\n" \
           "||**Thank you for your collaboration to make us much better!💖**||"
    reply_markup = ReplyKeyboardMarkup(buttons.DONE_REPLY_KEYBORD, one_time_keyboard=False, resize_keyboard=True)
    message.reply(
        text=text,disable_web_page_preview=True,
        reply_markup=reply_markup
    )


@bot.on_message(filters.regex("Torrent Downloader Bot"))
def reply_to_Torrent(bot, message):
    text = "Reporting Area‼️\n\nBot = <a href=https://t.me/torrentdownloader88_bot> Torrent Downloader Bot</a>\n\n≡ Type your report here and send it\n\n≡ Then Click <<**Done**>>\n\n≡ You will get answer for your feedback/report around <b><b>48hours.</b></b>\n\n" \
           "||**Thank you for your collaboration to make us much better!💖**||"
    reply_markup = ReplyKeyboardMarkup(buttons.DONE_REPLY_KEYBORD, one_time_keyboard=False, resize_keyboard=True)
    message.reply(
        text=text,disable_web_page_preview=True,
        reply_markup=reply_markup
    )


@bot.on_message(filters.regex("Youtube Video Downloader Bot"))
def reply_to_Youtube(bot, message):
    text = "Reporting Area‼️\n\nBot = <a href=https://t.me/youtubevideodownloader45_bot>Youtube Video Downloader Bot</a>\n\n≡ Type your report here and send it\n\n≡ Then Click <<**Done**>>\n\n≡ You will get answer for your feedback/report around <b><b>48hours.</b></b>\n\n" \
           "||**Thank you for your collaboration to make us much better!💖**||"
    reply_markup = ReplyKeyboardMarkup(buttons.DONE_REPLY_KEYBORD, one_time_keyboard=False, resize_keyboard=True)
    message.reply(
        text=text,disable_web_page_preview=True,
        reply_markup=reply_markup
    )


@bot.on_message(filters.regex("Github"))
def reply_to_Github(bot, message):
    bot.send_message(message.chat.id,
                     "Check out the projects of me on <a href=https://github.com/sanila2007>GitHub.</a>",
                     disable_web_page_preview=True)


@bot.on_message(filters.regex("Changelog"))
def reply_to_Changelog(bot, message):
    bot.send_message(message.chat.id, messages.CHANGELOG_TEXT)


print("Bot is alive📶✨")

bot.run()
