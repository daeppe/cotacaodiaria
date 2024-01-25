import requests
from datetime import datetime

request = requests.get('https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL')

request_dic = request.json()
dolar_price = float(request_dic["USDBRL"]["bid"])
euro_price = float(request_dic["EURBRL"]["bid"])
btc_price = float(request_dic["BTCBRL"]["bid"])

print(f"Cotação Atualizada. {datetime.now()}\nDólar: R${dolar_price:.2f}\nEuro: R${euro_price:.2f}\nBTC: R${btc_price:.2f}")
