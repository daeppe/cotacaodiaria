#!/usr/bin/env python
# coding: utf-8
import os
from datetime import datetime
import smtplib
import email.message
from dotenv import load_dotenv

load_dotenv()
pass_google = os.environ.get('PASS_GOOGLE_AUTHENTICATION')
sender_gmail = os.environ.get('SENDER_GMAIL')
email_recipient = os.environ.get('EMAIL_RECIPIENT').split(', ')


def send_mail(dolar_price, euro_price, btc_price):  
    body_mail = f"""
    <h2>Cotação atualizada em {datetime.now()}</h2>
    <p>Cotação do Dolar: R${dolar_price:.2f}</p>
    <p>Cotação do Euro: R${euro_price:.2f}</p>
    <p>Cotação do Bitcoin: R${btc_price:.2f}</p>
    """

    msg = email.message.Message()
    msg['Subject'] = "Cotação diaria"
    msg['From'] = f'{sender_gmail}'
    msg['To'] = ", ".join(email_recipient)
    password = f'{pass_google}' 
    msg.add_header('Content-Type', 'text/html')
    msg.set_payload(body_mail)

    s = smtplib.SMTP('smtp.gmail.com: 587')
    s.starttls()
    s.login(msg['From'], password)
    # s.sendmail(msg['From'], [msg['To']], msg.as_string().encode('utf-8'))
    s.sendmail(msg['From'], email_recipient, msg.as_string().encode('utf-8'))
    print('Email enviado')
