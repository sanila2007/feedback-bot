
<h1 align= left><a href="https://t.me/sanilaassistant_bot">feedback bot</a> </h1>

> Multi functional bot that can give & collect feedbacks from users and broadcast replies to them with cool functions such as rating bots, completing captchas & etc...

    
<p align="center">
<a href="https://python.org"><img src="http://forthebadge.com/images/badges/made-with-python.svg" alt="made-with-python"></a>
<br>
    <img src="https://img.shields.io/github/stars/sanila2007/Sanila-Assistant-Bot?style=for-the-badge" alt="Stars">
    <img src="https://img.shields.io/github/forks/sanila2007/Sanila-Assistant-Bot?style=for-the-badge" alt="Forks">
    <img src="https://img.shields.io/github/watchers/sanila2007/Sanila-Assistant-Bot?style=for-the-badge" alt="Watchers"> 
<br>
    <img src="https://img.shields.io/github/license/sanila2007/Sanila-Assistant-Bot?style=for-the-badge" alt="License">
    <img src="https://img.shields.io/github/repo-size/sanila2007/Sanila-Assistant-Bot?style=for-the-badge" alt="Repository Size">
    <img src="https://img.shields.io/github/contributors/sanila2007/Sanila-Assistant-Bot?style=for-the-badge" alt="Contributors">
    <img src="https://img.shields.io/github/issues/sanila2007/Sanila-Assistant-Bot?style=for-the-badge" alt="Issues">
</p>  


## Config Vars
1. `API_ID` : Telegram API_ID, get it from my.telegram.org/apps
2. `API_HASH` : Telegram API_HASH, get it from my.telegram.org/apps
3. `BOT_TOKEN` : A Valid Telegram Bot Token, get it from @Botfather
4. `LOG_CHANNEL` : Create a Telegram channel and enter the username 
5. `FEEDBACK_CHANNEL` : Create a Telegram channel and enter the username

## Learn more about this repository

This is a multi functional telegram bot that can collect feedbacks from users. This bot was created using pyrogram library.<br>
features of this bot,<br>
       ● Give feedbacks<br>
       ● Collect feedbacks `admin(s) only`<br>
       ● Broadcast `admin(s) only`<br>
       ● Rate bots <br>
       ● Captcha `/captcha`<br>
       ● Learn projects<br>
       
`Collect feedbacks`<br>

When a user sent a feedback, it will send to the channels that added on `bot.py`. There are two channels added in `bot.py` to get 
logs and feedbacks in default. You can add or remove those as your need but you MUST put credits for this repository in your `README.md`. When you are adding or removing those you must edit `config.py`, `bot.py`, `docker-compose.yml`, `app.json`. else you will generate errors. for those don't tag admin. It should fix by yourself.<br>
```yml
version: "3.10"
services:
  worker:
    build: .
    environment:
      API_HASH: $API_HASH
      API_ID: $API_ID
      BOT_TOKEN: $BOT_TOKEN
      LOG_CHANNEL: $LOG_CHANNEL
      FEEDBACK_CHANEL: $FEEDBACK_CHANNEL
```
<br>

`Broadcast to user feedback`

This feature is still testing on beta version. still developing. It will be available here soon on next updates.<br>

```python
"Admin message\n\nThanks for your feedback."
```

`Captcha`

This feature is not for anything but to enjoy. users can enjoy this by completing captcha. You can use `/captcha` command in this bot to prove yourself that you are a human. 

`Deploying methods`

I have added two methods to host this bot. for that you can use either Heroku or Okteto. I recommend you to use Heroku because this bot had been faced issues when
deploying to Okteto. but you can deploy it as your choice,<br><br>
● Heroku - Easiest way to deloy<br>
● Okteto - Create variables exactly<br> 

  
## Deployment Methods

### Heroku

[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy?template=https://github.com/sanila2007/Sanila-Assistant-Bot)
   
### Okteto

[![Develop on Okteto](https://okteto.com/develop-okteto.svg)](https://cloud.okteto.com)
     
<br>

### What's new in this v0.8.0
<details>

|   **Version**     |       **Release Notes**  |
| ---------------- | ---------------------------------------- |
| v0.7 |⁕Now you can't send feedbacks empty |
| | ⁕Removed unnecessary features |
| | ⁕Improved feedback centre |
| | ⁕Improved report bugs centre|
| | ⁕Improved contact section and added features |
| | ⁕Improved changelog section |
| | ⁕Improvements in repository |
| | ⁕Minor bugs fixes |
| v0.6 |  ⁕Improvements in Feedback Centre |
| |    ⁕Fixed major problem in Contact Centre |
| |  ⁕Fixed major problem in Feedback Centre |
| | ⁕Removed some commands |
| |  ⁕Minor bugs fixes |
| | ⁕Optimizations |
| v0.5 | ⁕100% works with Inline & Reply KeyboardButtons |
| |  ⁕Improved the feedback and bugs reporting section |
| |  ⁕Added ability to learn how bots works using images |
| | ⁕Added Help Centre |
| | ⁕Added learning centre |
| | ⁕Added Contact facility |
| | ⁕Optimization |
| | ⁕Minor bug fixes |
| v0.4 |  ⁕Added InlineKeyboardButtons |
| | ⁕ Added ReplyKeyboardButtons |
| | ⁕Optimizations and minor bug fixes |
| v0.3 |  ⁕Fixed errors in v0.2 |
| | ⁕Changed the welcome msg |
| | ⁕Optimizations and bug fixes |
| v0.2 |  ⁕Changed the interface much attractive |
| | ⁕What's new changed to Changelog |
| | ⁕Minor bugs fixes |
| v0.1 |  ⁕Added Some Commands |
| | ⁕Made much easier to use |
| | ⁕Improved Chat Facilities |
</details>   
<br>    
   
## ⚠️ Warning
 ⁕This is under <b>GNU General Public License v3.0.</b><br><br>
 ⁕You are free to use this code in any of your projects, but you MUST include the following in your `README.md` (Copy & paste)<br>

```
## 💡 Credits
 
-[feedback-bot] (https://github.com/sanila2007/feedback-bot)

```

## ⚠️ Note: <br>

<pre> I don't officially support forks / Clones for this feedback bot,
So don't tag admins for errors of your deploy/code, 
If any errors you should fix it yourself!!</pre>
<br>


 
## 💖 Credits: <br>
 •[Sanila Ranatunga] (https://github.com/sanila2007) <br>
 •[Pyrogram] (https://github.com/pyrogram) 
    
