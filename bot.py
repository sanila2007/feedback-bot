import os
import pyrogram
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup
from config import Config

bot = Client("bot", api_id=Config.API_ID, api_hash=Config.API_HASH, bot_token=Config.BOT_TOKEN)

STICKER_MESSAGE = "https://telegra.ph/file/0a7f2e9ffab72fcc400f8.png"

START_MESSAGE = "**𝐒𝐚𝐧𝐢𝐥𝐚'𝐬 𝐀𝐬𝐬𝐢𝐬𝐭𝐚𝐧𝐭 𝐁𝐨𝐭**\n\n🙋‍♂Hello, This is Sanila's Telegram Assistant bot™. This bot was created to collect your feedbacks, bugs and ideas about Sanila's bots😊. 𝐂𝐥𝐢𝐜𝐤 /help 𝐟𝐨𝐫 𝐦𝐨𝐫𝐞 𝐭𝐡𝐢𝐧𝐠𝐬.\n\n" \
                "**These are the bots that created by Sanila🙇‍♂.**\n\n" \
                "▬▬▬▬ ◈ @songdownload597_bot\n" \
                "▬▬▬▬ ◈ @torrentdownloader88_bot\n" \
                "▬▬▬▬ ◈ @useful_powerful_chat_bot\n" \
                "▬▬▬▬ ◈ @youtubevideodownloader45_bot\n\n" \
                "**✨𝐃𝐞𝐯𝐞𝐥𝐨𝐩𝐞𝐫𝐬**\n\n" \
                "➥  Sanila Ranatunga\n\n" \
                "**𝟸𝟶𝟸𝟷-𝟸𝟶𝟸𝟸©**"

START_MESSAGE_BUTTONS = [
    [
        InlineKeyboardButton("Github", url="https://github.com/sanila2007"),
        InlineKeyboardButton("Source Code", url="https://github.com/sanila2007/Sanila-Ranatunga-Assistant-Bot")
    ]
]


@bot.on_message(filters.command("start") & filters.private)
def start(bot, message):
    sticker = STICKER_MESSAGE
    text = START_MESSAGE
    reply_markup = InlineKeyboardMarkup(START_MESSAGE_BUTTONS)
    message.reply(
        sticker=sticker
        text=text,
        reply_markup=reply_markup,
        disable_web_page_preview=True
    )


REPLY_MESSAGE = "✍️Hello \n\n🌺You Can Contact Sanila Using This BOT 💁‍♂\n========================\n\n- ғeel ғree тo reporт вυɢѕ 🐞.\n- ѕυɢɢeѕтιoɴѕ αre welcoмe 🐣.\n- coɴтαcт αɴy вoт proвleм 🐍.\n αѕĸ αɴy qυeѕтιoɴѕ 🦑.\n\n========================\n\nCheck my projects using (Github)[https://t.me/sanilaranatunga]\n",parse_mode="markdown")

REPLY_BUTTONS = [
    [
        ("About Sanila"),
        ("Feedback")
    ],
    [
        ("Report Bugs"),
        ("Github")
    ],
    [
        ("Changelog")
    ]
]


@bot.on_message(filters.command("help"))
def greet(bot, message):
    text = REPLY_MESSAGE
    reply_markup = ReplyKeyboardMarkup(REPLY_BUTTONS, one_time_keyboard=True, resize_keyboard=True)
    message.reply(
        text=text,
        reply_markup=reply_markup

    )


@bot.on_message(filters.regex("About Sanila"))
def reply_to_About(bot, message):
    bot.send_message(message.chat.id,
                     "𝗔𝗯𝗼𝘂𝘁 𝗦𝗮𝗻𝗶𝗹𝗮\n\n""❖ Name : Sanila Ranatunga😎\n\n""❖ Age : 14 Years (2021) 🙃\n\n""❖ Birthday : 09.01.2007 (2021)\n\n""❖ From : Sri Lanka🇱🇰\n\n""❖ Skills : Programmer , Developer😏\n\n""❖ Ambition : Be a software engineer😊\n\n""❖ Programming Languages : Python, HTML🙃\n\n❖ Still Learning : C++, JS, Java")


@bot.on_message(filters.regex("Feedback"))
def reply_to_Feedback(bot, message):
    bot.reply_sticker("https://telegra.ph/file/393ef93bf57458d541da6.png")
    bot.send_message(message.chat.id,
                     "Sanila welcome your valuable feedbacks about his bots💖 Send your feedback to me now and I will send it to Sanila🙂")


@bot.on_message(filters.regex("Report Bugs"))
def reply_to_Report(bot, message):
    bot.reply_sticker("https://telegra.ph/file/e40644b121bafa74aaf4d.png")
    bot.send_message(message.chat.id,
                     "I am sorry to hear that you have faced issues in Sanila's bots😶 Send me your issue and I will send it to Sanila🥲")


@bot.on_message(filters.regex("Github"))
def reply_to_Github(bot, message):
    bot.reply_sticker("https://telegra.ph/file/3145f61ab7e2fc45ee768.png")
    bot.send_message(message.chat.id,
                     "Sanila not only creates bots but also so many projects😉✌️You can check those by clicking this link👇\nhttps://github.com/sanila2007")


@bot.on_message(filters.regex("Changelog"))
def reply_to_Changelog(bot, message):
    bot.send_message(message.chat.id,
                     "𝐂𝐡𝐚𝐧𝐠𝐞𝐥𝐨𝐠\n\n🆅0.7\n -Added InlineKeyboardButtons\n -Added ReplyKeyboardButtons\n -Optimizations and minor bug fixes\n\n 🆅0.6\n -Fixed errors in v0.5\n -Optimizations\n -Minor bug fixes\n\n🆅0.5\n -Bug fixes and optimizations\n\n""🆅0.4\n"" -Changed the interface\n\n""🆅0.3\n"" -Added time (US Time)\n\n""🆅0.2\n"" -Changed the interface much attractive\n"" -What's new changed to Changelog\n"" -Added time\n"" -Minor bugs fixes\n\n""🆅0.1\n"" -Added Some Commands\n"" -Made much easier to use\n"" -Improved Chat Facilities\n")


print("still good 693")

bot.run()
