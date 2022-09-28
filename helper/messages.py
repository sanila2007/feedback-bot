# Copyright ©️ 2022 Sanila Ranatunga. All Rights Reserved
# You are free to use this code in any of your project, but you MUST include the following in your README.md (Copy & paste)
# ##Credits - [feedback-bot] (https://github.com/sanila2007/feedback-bot)

# Read GNU General Public License v3.0: https://github.com/sanila2007/feedback-bot/blob/mai/LICENSE
# Don't forget to follow github.com/sanila2007 because I'm doing these things for free and open source
# Star and fork and enjoy!


import pyrogram
from plugins import quotes_text

FEEDBACK_REPLY_TEXT = "First please select a bot!!👮"

CONTACT_TEXT = "**Contact**\n\n√ You can connect with the admin from here.\n\n√ Type your message here and send.\n\n√ After you finish click <<**Finish📩**>>"

REPLY_MESSAGE = "Click any button from ReplyKeyboard as your choice. Don't send feedbacks directly. Use contact or feedback sections. **WE DO NOT COLLECT DIRECT FEEDBACKS.**\n\nUse `@sanilaassistant_bot` for get the BOT LIST in inline mode."

LEARN_TEXT = "Please select the bot that you want to learn!!👨‍🏫"

START_TEXT_CAPTION_TEXT = "This is a multi functional bot that can give & collect feedbacks from" \
                          " users and broadcast replies to them.\n\n" \
                          "⚠️Warning - Heroku has been stopped giving free dyno bundles. Therefore the bots may be unstable for some days. We appreciate your patience in these kinds of situations.\n\n" \
                          "Use `@sanilaassistant_bot` for get the BOT LIST in inline mode."

REPORT_BUGS_TEXT = "Please select a bot!!👮"

CHANGELOG_TEXT = "<u>**Changelog**</u>\n\n" \
                 "🆅1.9.0\n **-New features**\n ⁕Added possibility to broadcast replies to the users\n ⁕Broadcast replies anonymously\n ⁕Added possibility to broadcast replies only by the admin in the group. Other members would not be able to reply.\n\n **-Security improvements**\n ⁕No one can copy feedbacks from feedback group\n ⁕Getting screenshots is restricted in the both group and bot\n<i>*Note: feedback messages only, group messages can read anyone but cannot share those</i>\n\n **-Improved features**\n ⁕Redesigned texts\n ⁕And other minor bug fixes\n\n" \
                 "🆅1.8.0\n **-New features**\n ⁕Added CAPTCHA /captcha\n ⁕Added facility to rate bots\n ⁕Added log channel (admin only)\n ⁕Instant view supports\n ⁕Added ForceReply\n\n **-Improved features**\n ⁕Feedback improvements\n ⁕Stickers has been restricted\n ⁕Minor bug fixes\n\n  " \
                 "<a href=https://github.com/sanila2007/feedback-bot/blob/mai/release%20notes/release_notes.txt>see more...</a>\n\n" \
                 "*Note: Every version releases aren't available here. Just major updates only. If you want to get the minor releases," \
                 "you can check <a href=https://github.com/sanila2007/feedback-bot/releases>Releases</a>"

SANILA_ASSISTANT_TEXT = "Reporting Area‼️\n\nBot = <a href=https://t.me/sanilaassistant_bot> Sanila's Assistant Bot</a>\n\n" \
                        "◉ Type your report here and send it\n\n" \
                        "◉ After you finish click <<**Finish📩**>>\n\n" \
                        "◉ You will get answer for your feedback around <b><b>24hours.</b></b>"

SONG_DOWNLOADER_TEXT = "Reporting Area‼️\n\nBot = <a href=https://t.me/songdownload597_bot> Song Downloader Bot</a>\n\n" \
                       "◉ Type your report here and send it\n\n" \
                       "◉ After you finish click <<**Finish📩**>>\n\n" \
                       "◉ You will get answer for your feedback around <b><b>24hours.</b></b>"

TORRENT_DOWNLOADER_TEXT = "Reporting Area‼️\n\nBot = <a href=https://t.me/torrentdownloader88_bot> Torrent Downloader Bot</a>\n\n" \
                          "◉ Type your report here and send it\n\n" \
                          "◉ After you finish click <<**Finish📩**>>\n\n" \
                          "◉ You will get answer for your feedback around <b><b>24hours.</b></b>"

YOUTUBE_VIDEO_DOWNLOADER_TEXT = "Reporting Area‼️\n\nBot = <a href=https://t.me/youtubevideodownloader45_bot>Youtube Video Downloader Bot</a>\n\n" \
                                "◉ Type your report here and send it\n\n" \
                                "◉ After you finish click <<**Finish📩**>>\n\n" \
                                "◉ You will get answer for your feedback around <b><b>24hours.</b></b>"

TELEGRAPH_UPLOADER_TEXT = "Reporting Area‼️\n\nBot = <a href=https://t.me/telgeraph200_bot>Telegraph Uploader Bot</a>\n\n" \
                          "◉ Type your report here and send it\n\n" \
                          "◉ After you finish click <<**Finish📩**>>\n\n" \
                          "◉ You will get answer for your feedback around <b><b>24hours.</b></b>"

FEEDBACK_FINISH_TEXT = "Thanks for your feedback!\n\nYour valuable feedbacks help us to build our bots much friendly. When you sending your feedback please include a screenshot of it because it helps us to decide what is the error.\n\nIt usually takes about 48 hours to get back to you, please accept our apologies in advance for any reply that exceeds this time frame.\n\nFeedback Centre."

DONT_SEND = "Telegraph Uploader\n\nA telegram bot which can upload media such as images, videos & animations to the telegra.ph"

DONT_SEND2 = "Feedback Bot\n\nMulti functional bot that can give & collect feedbacks from users and broadcast replies to them with cool functions such as rating bots, completing captchas & etc...\n\nDeveloper : <a href=https://github.com/sanila2007>Sanila Ranatunga</a>"

DONT_SEND3 = "Music Download Bot\n\nOne of the most powerful Song download bot found on Telegram...\n\nDeveloper : <a href=https://github.com/sanila2007>Sanila Ranatunga</a>"

DONT_SEND4 = "Text to File Bot\n\nTEXT TO FILE BOT JUST SENT YOUR CODE OR TEXT MESSAGE THEN I WILL CONVERT IT INTO FILE\n\nDEVELOPER : <a href=https://github.com/hbbots>Amal Mohan</a>"

DONT_SEND5 = "QR Code Generator Bot\n\nTelegram Bot that can generate QR codes\n\nDEVELOPER : <a href=https://github.com/hbbots>Amal Mohan</a>"

DONT_SEND6 = "Youtube Video Bot\n\nTelegram bot that can download videos, thumbnail and playlist videos from Youtube VERY QUICKLY.\n\nDEVELOPER : <a href=https://github.com/hbbots>Amal Mohan</a>"

DONT_SEND7 = "Torrent Search Bot\n\nTelegram Bot that can search & download torrents from YTS, Piratebay, Anime, etc...\n\nDEVELOPER : <a href=https://github.com/sanila2007>Sanila Ranatunga</a>"

DONT_SEND8 = "Random Name Generator Bot\n\nTelegram bot that can generate random names for their users.\n\nDEVELOPER : <a href=https://github.com/hbbots>Amal Mohan</a>"

# Copyright ©️ 2022 Sanila Ranatunga. All Rights Reserved
