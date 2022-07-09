# Copyright ©️ 2022 Sanila Ranatunga. All Rights Reserved
# You are free to use this code in any of your project, but you MUST include the following in your README.md (Copy & paste)
# ##Credits - [feedback-bot] (https://github.com/sanila2007/feedback-bot)

# Read GNU General Public License v3.0: https://github.com/sanila2007/feedback-bot/blob/mai/LICENSE
# Don't forget to follow github.com/sanila2007 because I'm doing these things for free and open source
# Star and fork and enjoy!

import random
import pyrogram

QUOTE1 = '<i> **“You only live once, but if you do it right, once is enough.”**\n\n — Mae West</i>'

QUOTE2 = '<i>**“Many of life’s failures are people who did not realize how close they were to success when they gave up.”**\n\n– Thomas A. Edison</i>'

QUOTE3 = '<i>**“Money and success don’t change people; they merely amplify what is already there.”**\n\n — Will Smith</i>'

QUOTE4 = '<i>**"Your time is limited, so don’t waste it living someone else’s life. Don’t be trapped by dogma – which is living with the results of other people’s thinking.”**\n\n – Steve Jobs</i>'

QUOTE5 = '<i>**“In order to write about life first you must live it.”**\n\n– Ernest Hemingway</i>'

QUOTE6 = '<i>**“Turn your wounds into wisdom.”** \n\n— Oprah Winfrey</i>'

ALL_QUOTE = QUOTE1, QUOTE2, QUOTE3, QUOTE6, QUOTE5, QUOTE4
length = 1

GENERATED_QUOTE1 = "".join(random.sample(ALL_QUOTE, length))
GENERATED_QUOTE2 = "".join(random.sample(ALL_QUOTE, length))
GENERATED_QUOTE3 = "".join(random.sample(ALL_QUOTE, length))
GENERATED_QUOTE4 = "".join(random.sample(ALL_QUOTE, length))
GENERATED_QUOTE5 = "".join(random.sample(ALL_QUOTE, length))
GENERATED_QUOTE6 = "".join(random.sample(ALL_QUOTE, length))

