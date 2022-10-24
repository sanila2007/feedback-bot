# Copyright ©️ 2022 Sanila Ranatunga. All Rights Reserved
# You are free to use this code in any of your project, but you MUST include the following in your README.md (Copy & paste)
# ##Credits - [feedback-bot] (https://github.com/sanila2007/feedback-bot)

# Read GNU General Public License v3.0: https://github.com/sanila2007/feedback-bot/blob/mai/LICENSE
# Don't forget to follow github.com/sanila2007 because I'm doing these things for free and open source
# Star and fork and enjoy!

from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup


RATINGS_TEXT = "Please select the bot that you want to rate!"

RATINGS_BUTTONS = [
    [
        ("Song Bot ✨"),
        ("Assistant Bot ✨")
    ],
    [
        ("Torrent Bot ✨"),
        ("Telegraph Bot ✨")
    ]
]

# Assistant bot rating


RATING_BOT_FEEDBACK_BOT = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton("⭐", callback_data="one_star")
        ],
        [
            InlineKeyboardButton("⭐⭐", callback_data="two_star")
        ],
        [
            InlineKeyboardButton("⭐⭐⭐", callback_data="three_star")],
        [
            InlineKeyboardButton("⭐⭐⭐⭐", callback_data="four_star")

        ],
        [

            InlineKeyboardButton("⭐⭐⭐⭐⭐", callback_data="five_star")
        ]
    ]
)


RATING_BOT_TELEGRAPH = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton("⭐", callback_data="one_star_telegraph")
        ],
        [
            InlineKeyboardButton("⭐⭐", callback_data="two_star_telegraph")
        ],
        [
            InlineKeyboardButton("⭐⭐⭐", callback_data="three_star_telegraph")],
        [
            InlineKeyboardButton("⭐⭐⭐⭐", callback_data="four_star_telegraph")

        ],
        [

            InlineKeyboardButton("⭐⭐⭐⭐⭐", callback_data="five_star_telegraph")
        ]
    ]
)

RATING_BOT_SONG = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton("⭐", callback_data="one_star_song")
        ],
        [
            InlineKeyboardButton("⭐⭐", callback_data="two_star_song")
        ],
        [
            InlineKeyboardButton("⭐⭐⭐", callback_data="three_star_song")],
        [
            InlineKeyboardButton("⭐⭐⭐⭐", callback_data="four_star_song")

        ],
        [

            InlineKeyboardButton("⭐⭐⭐⭐⭐", callback_data="five_star_song")
        ]
    ]
)


RATING_BOT_TORRENT = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton("⭐", callback_data="one_star_torrent")
        ],
        [
            InlineKeyboardButton("⭐⭐", callback_data="two_star_torrent")
        ],
        [
            InlineKeyboardButton("⭐⭐⭐", callback_data="three_star_torrent")],
        [
            InlineKeyboardButton("⭐⭐⭐⭐", callback_data="four_star_torrent")

        ],
        [

            InlineKeyboardButton("⭐⭐⭐⭐⭐", callback_data="five_star_torrent")
        ]
    ]
)


# Copyright ©️ 2022 Sanila Ranatunga. All Rights Reserved
