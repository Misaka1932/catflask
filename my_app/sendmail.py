from flask_mail import Message
from flask import render_template
import os
import threading
from my_app import app, mail

def send_async_email(app, msg):
    with app.app_context():
        mail.send(msg)

def send_mail(subject, sender, recipients, text_body, html_body):
    msg = Message(subject, sender=sender, recipients=recipients)
    msg.body = text_body
    msg.html = html_body

    thr1 = threading.Thread(target=send_async_email)
    thr1.start()

