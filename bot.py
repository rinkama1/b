

import telebot, requests
from pprint import pprint

bot = telebot.TeleBot('8674705784:AAHz5GVmwm9yZWseDwt9MRLpk5_bwRqyAB0')

def get_fiat_price():
    response = requests.get('https://www.cbr-xml-daily.ru/daily_json.js')
    response.raise_for_status()
    valute = response.json()['Valute']


    euro_n = valute['EUR']['Name']
    euro = valute['EUR']['Value']

    dollar_n = valute['USD']['Name']
    dollar = valute['USD']['Value']

    uan_n = valute['CNY']['Name']
    uan = valute['CNY']['Value']

    yen_n = valute['JPY']['Name']
    yen = valute['JPY']['Value']

    d = {euro_n:euro,dollar_n:dollar,uan_n:uan,yen_n:yen}
    ans = ''

    for k in d:
        ans += (f'{k}: {d[k]}\n')
    return ans


def get_crypto_price():
    params = {
        'symbol': 'BTCUSDT'
    }

    response = requests.get('https://api.binance.com/api/v3/avgPrice', params = params)
    response.raise_for_status()
    crypto = response.json()['price']

    return crypto

@bot.message_handler(commands=['start'])
def send_message(message):
    ans = get_fiat_price()
    crypto_valute = get_crypto_price()

    ans += f"Solana: {crypto_valute}"
    bot.send_message(message.chat.id, ans)

bot.polling(True)