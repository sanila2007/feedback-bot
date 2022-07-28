
<h1 align= left><a href="https://t.me/sanilaassistant_bot">feedback bot</a> </h1>

> Multi functional bot that can give & collect feedbacks from users and broadcast replies to them with cool features such as rating bots, completing captchas & etc...

----

    
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
<br>

## Learn more about this repository

This is a multi functional telegram bot that can collect feedbacks from users. This bot was created using pyrogram library.
features of this bot,<br>
       ● Give feedbacks<br>
       ● Collect feedbacks `admin(s) only`<br>
       ● Broadcast `admin(s) only`<br>
       ● Rate bots <br>
       ● Captcha<br>
       ● Learn projects<br>
       ● Inline Bot list<br>
       
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

`Inline Bot list`

Using Inline mode, you can get the all the bot projects of me by using ```@sanilaassistant_bot``` in any chat. Very easy to share and get the bot repositories and the bot links.

`Deploying methods` <br><br>
There are two ways that you can deploy this bot to cloud. Those are Okteto & Heroku. Heroku is the easiest way to deploy. If you are using Otketo you must create variables EXACTLY. Unless it will generate errors. For those don't tag the developer. You can deploy it as your choice,<br><br>
● Heroku - Easiest way to deloy<br>
● Okteto - Create variables exactly<br>

<u><b>Variables for Okteto (Copy & Paste)</b></u><br><br>
```
API_ID
``` 
```
API_HASH
```
```
BOT_TOKEN
``` 
```
LOG_CHANNEL
```
```
FEEDBACK_CHANNEL
``` 
  
## Deployment Methods

### Heroku

[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy?template=https://github.com/sanila2007/Sanila-Assistant-Bot)
   
### Okteto

[![Develop on Okteto](https://okteto.com/develop-okteto.svg)](https://cloud.okteto.com)
     
<br>

## What's new in this v0.8.0

● Added CAPTCHA /captcha<br>
● Added facility to rate bots<br>
● Added log channel (admin only)<br>
● Instant view supports<br>
● Added ForceReply<br>
● Feedback improvements<br>
● Stickers have been restricted<br>
● Minor bug fixes<br>

<a href="https://github.com/sanila2007/feedback-bot/blob/mai/release%20notes/release_notes.txt">Read more...</a>

  
   
## Warning
 ● This is under <b>GNU General Public License v3.0.</b><br><br>
 ● You are free to use this code in any of your projects, but you MUST include the following in your `README.md` (Copy & paste)<br>

```
## Credits
 
-[feedback-bot] (https://github.com/sanila2007/feedback-bot)

```

## Note: <br>

<pre>I don't officially support forks / Clones for this feedback bot,
So don't tag admins for errors of your deploy/code, 
If any errors you should fix it yourself!!</pre>


## Credits: <br>
 • <a href="https://github.com/sanila2007">Sanila Ranatunga</a> <br>
 • <a href="https://github.com/pyrogram/pyrogram">Pyrogram</a> 
  
[![Open Source Love svg2](https://badges.frapsoft.com/os/v2/open-source.svg?v=103)](https://github.com/sanila2007/feedback-bot)   
