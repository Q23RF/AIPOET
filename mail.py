import os
import smtplib
from email.mime.text import MIMEText
from email.header import Header


def send(message):
    password = os.environ['MAIL_PASSWORD']
    mail = MIMEText(message, 'plain', 'utf-8')
    mail['Subject'] = Header('New Feedback!', 'utf-8')
    server = smtplib.SMTP('smtp.gmail.com')
    server.starttls()
    server.login("aip.mailbot@gmail.com", password)
    server.sendmail("aip.mailbot@gmail.com", "elsie094081@gmail.com",
                    mail.as_string())
    server.quit()
