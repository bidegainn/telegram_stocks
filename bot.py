import requests
import json


BELO_USDT = "https://criptoya.com/api/belo/usdt/ars/0.5"


def get_mep():
    pass

def get_usdt(url: str) -> str:
    req = requests.get(url).text
    res = json.loads(req)
    value_usdt = res.get('ask')
    print("The usdt value is: " + str(value_usdt))


def get_tsla():
    pass





get_usdt(BELO_USDT)