import telebot
import requests
import json

BOT_TOKEN = '6076907632:AAFt5Mf63hm3Sxakw8OFQJkqolwaKLnGrCQ'
bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(commands=['ask'])
def gpt_answer(message):
    

    url = "https://api.writesonic.com/v2/business/content/chatsonic?engine=premium"

    payload = {
        "enable_google_results": "true",
        "enable_memory": False,
        "input_text": message.text
    }
    headers = {
        "accept": "application/json",
        "content-type": "application/json",
        "X-API-KEY": "490c8dc4-31c9-44ce-bd86-c561cd0d2d72"
    }

    response = requests.post(url, json=payload, headers=headers)
    json_answer = response.json()

    bot.reply_to(message, json_answer['message'])

bot.infinity_polling()
