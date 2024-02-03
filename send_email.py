import smtplib as email
import ssl
import os

__USERNAME__ = "ankur2k15ak47@gmail.com"
__PASSWORD__ = os.getenv("__PASSWORD__")


def send_email(message):
    host = "smtp.gmail.com"
    port = 465

    context = ssl.create_default_context()

    with email.SMTP_SSL(host=host, port=port, context=context) as server:
        server.login(user=__USERNAME__, password=__PASSWORD__)
        server.sendmail(from_addr=__USERNAME__, to_addrs=__USERNAME__, msg=message)
