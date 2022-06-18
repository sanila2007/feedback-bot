# Copyright ©️ 2022 Sanila Ranatunga. All Rights Reserved
# You are free to use this code in any of your project, but you MUST include the following in your README.md (Copy & paste)
# ##Credits - [Sanila-Assistant-Bot] (https://github.com/sanila2007/Sanila-Assistant-Bot)

# Read GNU General Public License v3.0: https://github.com/sanila2007/Sanila-Assistant-Bot/blob/mai/LICENSE
# Don't forget to follow github.com/sanila2007 because I'm doing these things for free and open source
# Star and fork and enjoy!



import datetime
from datetime import timedelta

# %a = weekday(short)
# %A = weekday(full)
# %b = month name(short)
# %B = month name(full)
# %y = year(short)
# %Y = year(full)
# %d = day
# %H = hour(00-23)
# %I = hour(00-12)
# %S = second
# %f = microsecond
# %p = AM/PM


POSTED_DATE = datetime.date.today()

time = datetime.datetime.now()

POSTED_TIME = time.strftime("%I.%M %p")

replydate = datetime.datetime.now() + timedelta(days=2)

DATE_OF_REPLY = replydate.strftime("%Y-%m-%d")

CAPTCHA_DATE = datetime.datetime.now() + timedelta(seconds=1)