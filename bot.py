import requests
import json
from dotenv import load_dotenv
import os

load_dotenv()
USDT = os.environ["USDT"]
MEP = os.environ["MEP"]


def get_usdt(url: str) -> str:
    req = requests.get(url).text
    res = json.loads(req)
    value_usdt = res.get('ask')
    print("The usdt value is: " + str(value_usdt))


def get_mep(url: str) -> str:
    req = requests.get(url).json()[4]
    value_mep = req.get('casa').get('compra')
    print("The USDMep value is: " + str(value_mep))


def get_tsla():
    pass





get_usdt(USDT)
get_mep(MEP)