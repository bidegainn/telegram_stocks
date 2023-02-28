import requests
import json
from dotenv import load_dotenv
import os

from yahoo_fin import stock_info as si


load_dotenv()
USDT = os.environ["USDT"]
MEP = os.environ["MEP"]
BOT_TOKEN = os.environ["TOKEN_TELEGRAM"]

def get_usdt(url: str) -> int:
    req = requests.get(url).text
    res = json.loads(req)
    value_usdt = res.get('ask')
    return value_usdt

def get_mep(url: str) -> str:
    req = requests.get(url).json()[4]
    value_mep = req.get('casa').get('compra')
    return value_mep


def get_tsla():
    ticker_price = si.get_live_price("TSLA")
    return round(ticker_price, 2)





