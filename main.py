import os
import requests
from send_mail import send_mail
from dotenv import load_dotenv

load_dotenv()
pass_google = os.environ.get('PASS_GOOGLE_AUTHENTICATION')
sender_gmail = os.environ.get('SENDER_GMAIL')
email_recipient = os.environ.get('EMAIL_RECIPIENT').split(', ')

print('print', pass_google)
print(sender_gmail)
print(email_recipient)

request = requests.get('https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL')

request_dic = request.json()
dolar_price = float(request_dic["USDBRL"]["bid"])
euro_price = float(request_dic["EURBRL"]["bid"])
btc_price = float(request_dic["BTCBRL"]["bid"])

print('Cotação feita!')

send_mail(dolar_price, euro_price, btc_price)
