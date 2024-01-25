import requests
from send_mail import send_mail

request = requests.get('https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL')

request_dic = request.json()
dolar_price = float(request_dic["USDBRL"]["bid"])
euro_price = float(request_dic["EURBRL"]["bid"])
btc_price = float(request_dic["BTCBRL"]["bid"])

print('Cotação feita!')

send_mail(dolar_price, euro_price, btc_price)