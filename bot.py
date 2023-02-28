from dotenv import load_dotenv
import os
import telebot


from stocks import get_usdt, get_mep

load_dotenv()
BOT_TOKEN = os.environ["TOKEN_TELEGRAM"]
USDT = os.environ["USDT"]
MEP = os.environ["MEP"]





bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(commands=['start', 'price'])
def send_welcome(message):
    usdt =  get_usdt(USDT)
    mep = get_mep(MEP)
    bot.reply_to(message, f"The value of USDT: {usdt} \nThe value of MEP:  {mep}")

bot.infinity_polling()