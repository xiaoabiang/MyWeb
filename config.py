# -*- coding: utf-8 -*-
__author__ = 'Administrator'

import os

basedir = os.path.abspath(os.path.dirname(__file__))


CSRF_ENABLED = True
SECRET_KEY = 'you-will-never-guess'


OPENID_PROVIDERS = [
    { 'name': 'Google', 'url': 'https://www.google.com/accounts/o8/id' },
    { 'name': 'Yahoo', 'url': 'https://me.yahoo.com' },
    { 'name': 'AOL', 'url': 'http://openid.aol.com/<username>' },
    { 'name': 'Flickr', 'url': 'http://www.flickr.com/<username>' },
    { 'name': 'MyOpenID', 'url': 'https://www.myopenid.com' }]

PRE_PAGE_NUMBER = 10

UPLOAD_FOLDER = '/static/img/'
IMAGE_SIZE = (100, 100)


ALLOWED_TAGS = ['a', 'abbr', 'acronym', 'b', 'blockquote', 'code',
'em', 'i', 'li', 'ol', 'pre', 'strong', 'ul',
'h1', 'h2', 'h3', 'p']