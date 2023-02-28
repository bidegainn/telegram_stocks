from dotenv import load_dotenv
import os
import telebot


from stocks import get_usdt, get_mep, get_tsla

load_dotenv()
BOT_TOKEN = os.environ["TOKEN_TELEGRAM"]
USDT = os.environ["USDT"]
MEP = os.environ["MEP"]





bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(commands=['start', 'price'])
def send_welcome(message):
    usdt =  get_usdt(USDT)
    mep = get_mep(MEP)
    tsla = get_tsla()
    bot.reply_to(message, f"USDT: {usdt} \nMEP:  {mep}\nTSLA: {tsla}")

bot.infinity_polling()