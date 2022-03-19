import os
import pyrogram
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup

bot = Client(
    "bot",
    api_id=7263889,
    api_hash="89c452ed35062d2d31922e6d8d069c90",
    bot_token="2031117879:AAG5kJt7xsyMkD8EPcep9TVjXyqoFcgcTiA"
)

START_MESSAGE = "**Sanila's Assistant Bot**\n\n🙋‍♂Hello, This is Sanila's Telegram Assistant bot™. **Click /help for more settings**\n\n" \
                "**These are the bots that created by Sanila🙇‍♂.**\n\n" \
                "▬▬▬▬ ◈ @songdownload597_bot\n" \
                "▬▬▬▬ ◈ @torrentdownloader88_bot\n" \
                "▬▬▬▬ ◈ @useful_powerful_chat_bot\n" \
                "▬▬▬▬ ◈ @youtubevideodownloader45_bot\n\n" \
                "**✨Developer**\n\n" \
                "➥  Sanila Ranatunga\n\n" \
                "**𝟸𝟶𝟸𝟷-𝟸𝟶𝟸𝟸©**"

START_MESSAGE_BUTTONS = [
    [
        InlineKeyboardButton("Github", url="https://github.com/sanila2007"),
        InlineKeyboardButton("Source Code", url="https://github.com/sanila2007/Sanila-Ranatunga-Assistant-Bot")
    ]
]
REPLY_BUTTONS = [
    [
        ("About Sanila☘️"),
        ("About Bot🤖")
    ],
    [
        ("Report Bugs👮"),
        ("Feedback📝")
    ],
    [
        ("Learn Bots👨‍🏫"),
        ("Github🔓")
    ],
    [
        ("Help Centre💁"),
        ("Contact📞")
    ],
    [
        ("Changelog ♾️")
    ]
]

HELP_CENTRE_TEXT = "**Help Centre**\n\n" \
                   "√ This help centre was created to ask questions about bots or to fix your problems about those.\n\n " \
                   "√ You can ask them here and after you sent your " \
                   "message click <<<b>Send📩</b>>> \n\n" \
                   "√ You will receive your answer for your question through this bot around <b>48 hours.</b>\n\n" \
                   "||<b>Please accept my apologies in advance if my reply was exceeded the time period.</b>||"

HELP_CENTRE_DONE_BUTTONS = [
    [
        ("Send📩")
    ]
]

DONE_MESSAGE = "Thanks for collaboration to make Sanila's bots much better! You will get reply to yur feedback by this bot around **48hours** till then have some patient\n"

DONE_REPLY_KEYBORD = [
    [
        ("✅Done"),
        ("♻️Done & give more feedbacks")
    ]
]


@bot.on_message(filters.command("start") & filters.private)
def command1(bot, message):
    text = START_MESSAGE
    reply_markup = InlineKeyboardMarkup(START_MESSAGE_BUTTONS)
    message.reply(
        text=text,
        reply_markup=reply_markup,
        disable_web_page_preview=True
    )


LEARN_TEXT = "Please select the bot that you want to learn!!👨‍🏫"

LEARN_REPLY_BUTTONS = [
    [
        ("Song Download Bot🤖💖")
    ],
    [
        ("Torrent Download Bot🤖💖")
    ],
    [
        ("Home 🔙"),
        ("Youtube Video Download Bot🤖💖")
    ]
]


@bot.on_message(filters.regex("Learn Bots"))
def reply_to_Learn_Bots(bot, message):
    text = LEARN_TEXT
    reply_markup = ReplyKeyboardMarkup(LEARN_REPLY_BUTTONS, one_time_keyboard=False, resize_keyboard=True)
    message.reply(
        text=text,
        reply_markup=reply_markup,
        disable_web_page_preview=True
    )


@bot.on_message(filters.regex("Song Download Bot🤖💖"))
def reply_to_utube(bot, message):
    bot.send_message(message.chat.id, "Song Downloader bot!!")
    bot.send_photo(message.chat.id, "https://telegra.ph/file/87ce14694a8c1d65cffaf.jpg", caption="<b>Step 1</b>")
    bot.send_photo(message.chat.id,"https://telegra.ph/file/13218e7e5fb04f37d555e.jpg", caption="<b>Step 2\nYou must send the song like this👇👇\n   ️/song Senorita</b>")
    bot.send_photo(message.chat.id, "https://telegra.ph/file/a3de0355d3fa67676e680.jpg", caption="<b>Step 3</b>")


@bot.on_message((filters.regex("Torrent Download Bot🤖💖")))
def reply_to_s_ong(bot, message):
    bot.send_message(message.chat.id, "Torrent downloader bot!")
    bot.send_photo(message.chat.id, "https://telegra.ph/file/cedb06244d2f74979095f.jpg", caption="<b>Step 1</b>")
    bot.send_photo(message.chat.id, "https://telegra.ph/file/b5956b401cb68cd7b8d2f.jpg",caption="<b>Step 2</b>")
    bot.send_photo(message.chat.id, "https://telegra.ph/file/a3d2f02b3c7e4ab742bc8.jpg", caption="<b>Step 3</b>")
    bot.send_photo(message.chat.id, "https://telegra.ph/file/17f2f0820c5007b136086.jpg", caption="<b>Step 4</b>")


@bot.on_message((filters.regex("Youtube Video Download Bot🤖💖")))
def reply_to_s_ong(bot, message):
    bot.send_message(message.chat.id, "Youtube Video Downloader bot!!!")
    bot.send_photo(message.chat.id, "https://telegra.ph/file/81aab8398259866256409.jpg", caption="<b>Step 1</b>")
    bot.send_photo(message.chat.id, "https://telegra.ph/file/e1c08af0c0e5f28053855.jpg",caption="<b>Step 2</b>")
    bot.send_photo(message.chat.id, "https://telegra.ph/file/3fc72cf3f77f4e4c3d28f.jpg", caption="<b>Step 3</b>")



REPLY_MESSAGE = "Hello dear, You can ue this bot to✨,\n\n" \
                "    -Give feedbacks  🐞.\n\n" \
                "    -Give suggestions🐣.\n\n" \
                "    -Contact with Sanila🐍.\n\n" \
                "    -Ask any questions 🦑.\n\n" \
                "    -Learn how bots work🤖.\n\n✅️Note: Select your need from the ReplyKeyboard and click it!"


@bot.on_message(filters.command("help"))
def greet(bot, message):
    text = REPLY_MESSAGE
    reply_markup = ReplyKeyboardMarkup(REPLY_BUTTONS, one_time_keyboard=False, resize_keyboard=True)
    message.reply(
        text=text,
        reply_markup=reply_markup

    )


@bot.on_message(filters.regex("About Bot"))
def reply_to_AboutBot(bot, message):
    bot.send_message(message.chat.id, "<ins>**About Bot**</ins>\n\n"
                                      "Name: <a href=https://t.me/sanilaassistant_bot>Sanila's Assistant Bot ✨</a>\n\n"
                                      "Created on: 11/21/2021🎂\n\n"
                                      "Latest Version:  v0.5.2️\n\n"
                                      "Language: <a href=www.python.org>Python</a>\n\n"
                                      "Framework: <a href=https://docs.pyrogram.org/>Pyrogram</a> ✌️\n\n"
                                      "Developer: <a href=https://github.com/sanila2007>Sanila Ranatunga\n\n</a>"
                                      "Source: 🔓\n\n", disable_web_page_preview=True)


CONTACT_TEXT = "**Contact**\n\n√ You can connect with Sanila from here.\n\n√ Type your message and click **<<Send📩>>**"


@bot.on_message(filters.regex("Contact📞"))
def reply_to_Contact(bot, message):
    text = CONTACT_TEXT
    reply_markup = ReplyKeyboardMarkup(HELP_CENTRE_DONE_BUTTONS, one_time_keyboard=False, resize_keyboard=True)
    message.reply(
        text=text,
        reply_markup=reply_markup,
        disable_web_page_preview=True
    )


@bot.on_message(filters.regex("About Sanila"))
def reply_to_About(bot, message):
    bot.send_message(message.chat.id,
                     "**<ins>About Sanila</ins>**\n\n""❖ Name : Sanila Ranatunga😎\n\n""❖ Age : 15 Years (2022) 🙃\n\n""❖ Birthday : 09.01.2007🎂\n\n""❖ From : Sri Lanka🇱🇰\n\n""❖ Skills : Programmer , Developer😏\n\n""❖ Ambition : Be a software engineer😊\n\n""❖ Languages : Python, HTML, CSS🙃\n\n❖ Still Learning : C++, JS, Java")


FEEDBACK_REPLY_BUTTONS = [
    [
        ("Sanila Assistant Bot🤖💖")
    ],
    [
        ("Song Downloader Bot🤖💖")
    ],
    [
        ("Torrent Downloader Bot🤖💖")
    ],
    [
        ("Home 🔙"),
        ("Youtube Video Downloader Bot🤖💖")
    ]
]

FEEDBACK_REPLY_TEXT = "First please select a bot!!👮"


@bot.on_message(filters.regex("♻️Done & give more feedbacks"))
def reply_to_Done_Feedback(bot, message):
    text = REPORT_BUGS_TEXT
    reply_markup = ReplyKeyboardMarkup(REPORT_BUGS_BUTTONS, one_time_keyboard=False, resize_keyboard=True)
    message.reply(
        text=text,
        reply_markup=reply_markup
    )


@bot.on_message(filters.regex("Home"))
def greet(bot, message):
    text = REPLY_MESSAGE
    reply_markup = ReplyKeyboardMarkup(REPLY_BUTTONS, one_time_keyboard=False, resize_keyboard=True)
    message.reply(
        text=text,
        reply_markup=reply_markup,
        disable_web_page_preview=True

    )


@bot.on_message(filters.regex("Help Centre💁"))
def reply_to_Help_Centre(bot, message):
    text = HELP_CENTRE_TEXT
    reply_markup = ReplyKeyboardMarkup(HELP_CENTRE_DONE_BUTTONS, one_time_keyboard=False, resize_keyboard=True)
    message.reply(
        text=text,
        reply_markup=reply_markup,
        disable_web_page_preview=True
    )


@bot.on_message(filters.regex("Feedback"))
def reply_to_Feedback(bot, message):
    text = FEEDBACK_REPLY_TEXT
    reply_markup = ReplyKeyboardMarkup(FEEDBACK_REPLY_BUTTONS, one_time_keyboard=True, resize_keyboard=True)
    message.reply(
        text=text,
        reply_markup=reply_markup
    )


REPORT_BUGS_TEXT = "Please select a bot!!👮"

REPORT_BUGS_BUTTONS = [
    [
        ("Sanila Assistant Bot🤖💖")
    ],
    [
        ("Song Downloader Bot🤖💖")
    ],
    [
        ("Torrent Downloader Bot🤖💖")
    ],
    [
        ("Home 🔙"),
        ("Youtube Video Downloader Bot🤖💖")
    ]
]

SEND_TEXT = "☑️You request has been accepted!\n\n🚶 Please have some patience until Sanila's reply.\n\nHelp Centre."


@bot.on_message(filters.regex("Send📩"))
def reply_to_send(bot, message):
    text = SEND_TEXT
    reply_markup = ReplyKeyboardMarkup(REPLY_BUTTONS, one_time_keyboard=False, resize_keyboard=True)
    message.reply(
        text=text,
        reply_markup=reply_markup,
        disable_web_page_preview=True
    )


@bot.on_message(filters.regex("Report Bugs"))
def reply_to_Report(bot, message):
    text = REPORT_BUGS_TEXT
    reply_markup = ReplyKeyboardMarkup(REPORT_BUGS_BUTTONS, one_time_keyboard=True, resize_keyboard=True)
    message.reply(
        text=text,
        reply_markup=reply_markup
    )


@bot.on_message(filters.regex("Sanila Assistant Bot🤖💖"))
def reply_to_Assistant(bot, message):
    text = "Reporting Area‼️\n\nBot = ` Sanila's Assistant Bot`\n\n≡ Type your report here and send it\n\n≡ Then Click <<**Done**>>\n\n≡ You will get answer for your feedback/report around <b><b>48hours.</b></b>\n\n" \
           "||**Thank you for your collaboration to make us much better!💖**||"
    reply_markup = ReplyKeyboardMarkup(DONE_REPLY_KEYBORD, one_time_keyboard=False, resize_keyboard=True)
    message.reply(
        text=text,
        reply_markup=reply_markup
    )


@bot.on_message(filters.regex("Done"))
def reply_to_Done(bot, message):
    text = SEND_TEXT
    reply_markup = ReplyKeyboardMarkup(REPLY_BUTTONS, one_time_keyboard=False, resize_keyboard=True)
    message.reply(
        text=text,
        reply_markup=reply_markup

    )


@bot.on_message(filters.regex("Song Downloader Bot"))
def reply_to_Song(bot, message):
    text = "Reporting Area‼️\n\nBot = ` Song Downloader Bot`\n\n≡ Type your report here and send it\n\n≡ Then Click <<**Done**>>\n\n≡ You will get answer for your feedback/report around <b><b>48hours.</b></b>\n\n" \
           "||**Thank you for your collaboration to make us much better!💖**||"
    reply_markup = ReplyKeyboardMarkup(DONE_REPLY_KEYBORD, one_time_keyboard=False, resize_keyboard=True)
    message.reply(
        text=text,
        reply_markup=reply_markup
    )


@bot.on_message(filters.regex("Torrent Downloader Bot"))
def reply_to_Torrent(bot, message):
    text = "Reporting Area‼️\n\nBot = ` Torrent Downloader Bot`\n\n≡ Type your report here and send it\n\n≡ Then Click <<**Done**>>\n\n≡ You will get answer for your feedback/report around <b><b>48hours.</b></b>\n\n" \
           "||**Thank you for your collaboration to make us much better!💖**||"
    reply_markup = ReplyKeyboardMarkup(DONE_REPLY_KEYBORD, one_time_keyboard=False, resize_keyboard=True)
    message.reply(
        text=text,
        reply_markup=reply_markup
    )


@bot.on_message(filters.regex("Youtube Video Downloader Bot"))
def reply_to_Youtube(bot, message):
    text = "Reporting Area‼️\n\nBot = ` Youtube Video Downloader Bot`\n\n≡ Type your report here and send it\n\n≡ Then Click <<**Done**>>\n\n≡ You will get answer for your feedback/report around <b><b>48hours.</b></b>\n\n" \
           "||**Thank you for your collaboration to make us much better!💖**||"
    reply_markup = ReplyKeyboardMarkup(DONE_REPLY_KEYBORD, one_time_keyboard=False, resize_keyboard=True)
    message.reply(
        text=text,
        reply_markup=reply_markup
    )


@bot.on_message(filters.regex("Github"))
def reply_to_Github(bot, message):
    bot.send_message(message.chat.id,
                     "Check out the projects of me on <a href=https://github.com/sanila2007>GitHub.</a>",
                     disable_web_page_preview=True)


@bot.on_message(filters.regex("Changelog"))
def reply_to_Changelog(bot, message):
    bot.send_message(message.chat.id,
                     "**Changelog**\n\n"
                     "🆅0.5\n -100% works with Inline & Reply KeyboardButtons\n -Improved the feedback and bugs reporting section\n -Added ability to learn how bots works using images\n -Added Help Centre\n -Added learning centre\n -Added Contact facility\n -Optimization\n -Minor bug fixes\n\n"
                     "🆅0.4\n -Added InlineKeyboardButtons\n -	Added ReplyKeyboardButtons\n -Optimizations and minor bug fixes\n\n"""
                     "🆅0.3\n -Fixed errors in v0.2\n -Changed the welcome msg\n -Optimizations and bug fixes\n\n"""
                     "🆅0.2\n -Changed the interface much attractive\n"" -What's new changed to Changelog\n -Minor bugs fixes\n\n"""
                     "🆅0.1\n -Added Some Commands\n"" -Made much easier to use\n"" -Improved Chat Facilities\n\n||<i>More features coming on v0.6 update...</i>||")


print("Bot is alive📶✨")

bot.run()
