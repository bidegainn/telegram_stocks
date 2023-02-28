from dotenv import load_dotenv
import os
import telebot


from stocks import get_usdt

load_dotenv()
BOT_TOKEN = os.environ["TOKEN_TELEGRAM"]
USDT = os.environ["USDT"]
MEP = os.environ["MEP"]





bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(commands=['start', 'hello'])
def send_welcome(message):
    usdt =  get_usdt(USDT)
    print(usdt)
    bot.reply_to(message, f"The value of usdt: {usdt}")

bot.infinity_polling()