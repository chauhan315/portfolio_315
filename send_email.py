import smtplib as email
import ssl

host = "smtp.gmail.com"
port = 465


USERNAME = "ankur2k15ak47@gmail.com"
PASSWORD = "andtmtedmqzqpjvf"

context = ssl.create_default_context()

message = """\
Subject: Hi!
How are you?
Bye!
"""

with email.SMTP_SSL(host=host, port=port, context=context) as server:
    server.login(user=USERNAME, password=PASSWORD)
    server.sendmail(from_addr=USERNAME, to_addrs=USERNAME, msg=message)
