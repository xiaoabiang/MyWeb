# -*- coding: utf-8 -*-
__author__ = 'Administrator'

import os
from flask import Flask
from flask_login import LoginManager
from flask_openid import OpenID
from config import basedir
from flask_pagedown import PageDown

app = Flask(__name__)
pagedown = PageDown(app)
app.config.from_object('config')


# db = SQLAlchemy(app)
lm = LoginManager()
lm.init_app(app)
lm.login_view = 'login'
oid = OpenID(app, os.path.join(basedir, 'tmp'))

from www import views
