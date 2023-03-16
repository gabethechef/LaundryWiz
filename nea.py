import requests, json
import telebot
from apikey import API

def getnowcast():
        response = requests.get("https://api.data.gov.sg/v1/environment/2-hour-weather-forecast")
        cat = response.json()
        jurong_east = cat["items"][0]["forecasts"][16]
        return jurong_east


API_KEY = API
bot = telebot.TeleBot(API_KEY)

@bot.message_handler(commands=['hello', 'start'])
def welcome(message):
    bot.send_message(message.chat.id, "Hello there, I'm the weather wizard:/n '/laundry' should you need my opinion.")

@bot.message_handler(commands=['laundry'])
def welcome(message):
    bot.send_message(message.chat.id, f"The 2-hour now casts suggests, {getnowcast()}")


bot.polling()




