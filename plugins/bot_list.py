# Copyright ©️ 2022 Sanila Ranatunga. All Rights Reserved
# You are free to use this code in any of your project, but you MUST include the following in your README.md (Copy & paste)
# ##Credits - [feedback-bot] (https://github.com/sanila2007/feedback-bot)

# Read GNU General Public License v3.0: https://github.com/sanila2007/feedback-bot/blob/mai/LICENSE
# Don't forget to follow github.com/sanila2007 because I'm doing these things for free and open source
# Star and fork and enjoy!


from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from pyrogram import Client
from pyrogram.types import InlineQueryResultArticle, InputTextMessageContent


@Client.on_inline_query()
def inlinequery(client, inline_query):
    inline_query.answer(
        results=[
            InlineQueryResultArticle(
                title="Telegraph Uploader Bot",
                description="A telegram bot which can upload media such as images, videos & animations to the telegra.ph",
                thumb_url="https://telegra.ph/file/8edc5c1131bcc8a691a3c.jpg",
                input_message_content=InputTextMessageContent(
                    "**Telegraph Uploader**\n\nA telegram bot which can upload media such as images, videos & animations to the telegra.ph",

                ),
                url="https://t.me/telegraph200_bot",
                reply_markup=InlineKeyboardMarkup(
                    [
                        [
                            InlineKeyboardButton("Reach the Bot", url="https://t.me/telegraph200_bot")
                        ],
                        [
                            InlineKeyboardButton("Repository here",
                                                 url="https://github.com/sanila2007/telegraph-uploader-bot")
                        ],
                        [
                            InlineKeyboardButton("Inline again 🔎", switch_inline_query_current_chat="")
                        ]
                    ]
                ),
            ),
            InlineQueryResultArticle(
                title="Feedback Bot",
                thumb_url="https://telegra.ph/file/e997ee0ea8bc354e77d3d.jpg",
                description="Multi functional bot that can give & collect feedbacks from users and broadcast replies to them with cool functions such as rating bots, completing captchas & etc...",
                input_message_content=InputTextMessageContent(
                    "**Feedback Bot**\n\nMulti functional bot that can give & collect feedbacks from users and broadcast replies to them with cool functions such as rating bots, completing captchas & etc...\n\nDeveloper : <a href=https://github.com/sanila2007>Sanila Ranatunga</a>",
                    disable_web_page_preview=True
                ),
                url="https://t.me/sanilaassistant_bot",
                reply_markup=InlineKeyboardMarkup(
                    [
                        [
                            InlineKeyboardButton("Reach the Bot", url="https://t.me/sanilaassistant_bot")
                        ],
                        [

                            InlineKeyboardButton("Repository here", url="https://github.com/sanila2007/feedback-bot")
                        ],
                        [
                            InlineKeyboardButton("Inline again 🔎", switch_inline_query_current_chat="")
                        ]
                    ]
                ),
            ),
            InlineQueryResultArticle(
                title="Song Downloader Bot",
                thumb_url="https://telegra.ph/file/79f269c5db774fb4e732d.jpg",
                description="One of the most powerful song download bot found on Telegram...",
                input_message_content=InputTextMessageContent(
                    "**Music Download Bot**\n\nOne of the most powerful Song download bot found on Telegram...\n\nDeveloper : <a href=https://github.com/sanila2007>Sanila Ranatunga</a>",
                    disable_web_page_preview=True
                ),
                url="https://t.me/songdownload597_bot",
                reply_markup=InlineKeyboardMarkup(
                    [
                        [
                            InlineKeyboardButton("Reach the Bot", url="https://t.me/songdownload597_bot")
                        ],
                        [

                            InlineKeyboardButton("Repository here",
                                                 url="https://github.com/sanila2007/Telegram-Song-Downloader-Bot")
                        ],
                        [
                            InlineKeyboardButton("Inline again 🔎", switch_inline_query_current_chat="")
                        ]
                    ]
                ),
            ),
            InlineQueryResultArticle(
                title="Text to File Bot",
                thumb_url="https://telegra.ph/file/cc1c4c375f60c649a70a7.jpg",
                description="Send any code or text message to this bot then it will convert it into file...",
                input_message_content=InputTextMessageContent(
                    "**Text to File Bot**\n\nTEXT TO FILE BOT JUST SENT YOUR CODE OR TEXT MESSAGE THEN I WILL CONVERT IT INTO FILE\n\nDEVELOPER : <a href=https://github.com/hbbots>Amal Mohan</a>",
                    disable_web_page_preview=True
                ),
                url="https://t.me/hb_text_to_file_bot",
                reply_markup=InlineKeyboardMarkup(
                    [
                        [
                            InlineKeyboardButton("Reach the Bot", url="https://t.me/hb_text_to_file_bot")
                        ],
                        [

                            InlineKeyboardButton("Repository here", url="https://github.com/hbbots/TEXT-TO-FILE-BOT")
                        ],
                        [
                            InlineKeyboardButton("Inline again 🔎", switch_inline_query_current_chat="")
                        ]
                    ]
                ),
            ),

            InlineQueryResultArticle(
                title="QR Code Generator Bot",
                thumb_url="https://telegra.ph/file/cc1c4c375f60c649a70a7.jpg",
                description="Telegram Bot that can generate QR codes",
                input_message_content=InputTextMessageContent(
                    "**QR Code Generator Bot**\n\nTelegram Bot that can generate QR codes\n\nDEVELOPER : <a href=https://github.com/hbbots>Amal Mohan</a>",
                    disable_web_page_preview=True
                ),
                url="https://t.me/HB_QR_CODE_BOT",
                reply_markup=InlineKeyboardMarkup(
                    [
                        [
                            InlineKeyboardButton("Reach the Bot", url="https://t.me/HB_QR_CODE_BOT")
                        ],
                        [

                            InlineKeyboardButton("Repository here", url="https://github.com/hbbots/QR-COD-EBOT")
                        ],
                        [
                            InlineKeyboardButton("Inline again 🔎", switch_inline_query_current_chat="")
                        ]
                    ]
                ),
            ),

            InlineQueryResultArticle(
                title="Youtube Video Downloader Bot",
                thumb_url="https://telegra.ph/file/c846b61802788f8d6af86.jpg",
                description="Telegram bot that can download videos, thumbnail and playlist videos from Youtube",
                input_message_content=InputTextMessageContent(
                    "**Youtube Video Bot**\n\nTelegram bot that can download videos, thumbnail and playlist videos from Youtube VERY QUICKLY.\n\nDEVELOPER : <a href=https://github.com/hbbots>Amal Mohan</a>",
                    disable_web_page_preview=True
                ),
                url="https://t.me/HB_YOUTUBE_BOT",
                reply_markup=InlineKeyboardMarkup(
                    [
                        [
                            InlineKeyboardButton("Reach the Bot", url="https://t.me/HB_YOUTUBE_BOT")
                        ],
                        [

                            InlineKeyboardButton("Repository here", url="https://github.com/hbbots/YOUTUBE-BOT")
                        ],
                        [
                            InlineKeyboardButton("Inline again 🔎", switch_inline_query_current_chat="")
                        ]
                    ]
                ),
            ),
            InlineQueryResultArticle(
                title="Torrent Search Bot",
                thumb_url="https://telegra.ph/file/89639d2a177ba4a4e8ea3.jpg",
                description="Telegram Bot that can search & download torrents from YTS, Piratebay, Anime, etc...",
                input_message_content=InputTextMessageContent(
                    "**Torrent Search Bot**\n\nTelegram Bot that can search & download torrents from YTS, Piratebay, Anime, etc...\n\nDEVELOPER : <a href=https://github.com/sanila2007>Sanila Ranatunga</a>",
                    disable_web_page_preview=True
                ),
                url="https://t.me/torrentdownload88_bot",
                reply_markup=InlineKeyboardMarkup(
                    [
                        [
                            InlineKeyboardButton("Reach the Bot", url="https://t.me/torrentdownload88_bot")
                        ],
                        [

                            InlineKeyboardButton("Inline again 🔎", switch_inline_query_current_chat="")
                        ]
                    ]
                ),
            ),
            InlineQueryResultArticle(
                title="Random Name Generator Bot",
                thumb_url="https://telegra.ph/file/cc1c4c375f60c649a70a7.jpg",
                description="A bot that can generate random name for you",
                input_message_content=InputTextMessageContent(
                    "**Random Name Generator Bot**\n\nTelegram bot that can generate random names for their users.\n\nDEVELOPER : <a href=https://github.com/hbbots>Amal Mohan</a>",
                    disable_web_page_preview=True
                ),
                url="https://t.me/HB_RANDOM_NAME_GENERATOR_BOT",
                reply_markup=InlineKeyboardMarkup(
                    [
                        [
                            InlineKeyboardButton("Reach the Bot", url="https://t.me/HB_RANDOM_NAME_GENERATOR_BOT"),
                            InlineKeyboardButton("Repository here", url="https://github.com/hbbots?tab=repositories"),
                            InlineKeyboardButton("Inline again 🔎", switch_inline_query_current_chat="")
                        ]
                    ]
                ),
            )
        ],
        cache_time=1
    )
