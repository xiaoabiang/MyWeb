# -*- coding: utf-8 -*-
__author__ = 'Administrator'


from flask_mail import Mail, Message
from flask import render_template
from www import app
from config import MAIL_SEVER_INFO
from threading import Thread
from logging import warning


app.config['MAIL_SERVER'] = MAIL_SEVER_INFO['MAIL_SERVER']
app.config['MAIL_PORT'] = MAIL_SEVER_INFO['MAIL_PORT']
app.config['MAIL_USERNAME'] = MAIL_SEVER_INFO['MAIL_USERNAME']
app.config['MAIL_PASSWORD'] = MAIL_SEVER_INFO['MAIL_PASSWORD']
app.config['MAIL_USE_TLS'] =  MAIL_SEVER_INFO['MAIL_USE_TLS']


mail = Mail(app)


# for register
def send_email(to, subject, template, **kwargs):
    try:
        msg = Message(subject,
                      sender=app.config['MAIL_USERNAME'], recipients=[to])
        msg.body = render_template(template + '.txt', **kwargs)
        # msg.html = render_template(template + '.html', **kwargs)
        thread = Thread(target=send_async_email, args=(app, msg))
        thread.start()
    except BaseException as e:
        warning('send mail failed!')


def send_async_email(app, msg):
    with app.app_context():
        mail.send(msg)



