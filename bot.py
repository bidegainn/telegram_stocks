import requests
import json
from dotenv import load_dotenv
import os
import telebot


load_dotenv()
USDT = os.environ["USDT"]
MEP = os.environ["MEP"]
BOT_TOKEN = os.environ["TOKEN_TELEGRAM"]



bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(commands=['start', 'hello'])
def send_welcome(message):
    bot.reply_to(message, "Howdy, how are you doing?")

bot.infinity_polling()