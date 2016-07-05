# -*- coding: utf-8 -*-
__author__ = 'Administrator'


from flask_mail import Mail, Message
from flask import render_template
from www import app
from threading import Thread
from logging import warning

app.config['MAIL_SERVER'] = 'smtp.163.com'
app.config['MAIL_PORT'] = 25
app.config['MAIL_USERNAME'] = 'zhujianbang2007@163.com'
app.config['MAIL_PASSWORD'] = 'lyq220809'
app.config['MAIL_USE_TLS'] = True


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



