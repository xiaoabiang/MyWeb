# -*- coding: utf-8 -*-
__author__ = 'Administrator'
import os, configparser


configini = configparser.ConfigParser()

'''
项目路径
'''
basedir = os.path.abspath(os.path.dirname(__file__))

'''
配置文件
'''
configini.read(os.path.join(basedir, 'config.ini'))


CSRF_ENABLED = True
SECRET_KEY = 'you-will-never-guess'


OPENID_PROVIDERS = [
    { 'name': 'Google', 'url': 'https://www.google.com/accounts/o8/id' },
    { 'name': 'Yahoo', 'url': 'https://me.yahoo.com' },
    { 'name': 'AOL', 'url': 'http://openid.aol.com/<username>' },
    { 'name': 'Flickr', 'url': 'http://www.flickr.com/<username>' },
    { 'name': 'MyOpenID', 'url': 'https://www.myopenid.com' }]

'''
分页中每页的默认数量
'''
PRE_PAGE_NUMBER = 10

'''
图片存储的相对路径
'''
UPLOAD_FOLDER = '/static/img/'

'''
将头像转换成指定大小存储
'''
IMAGE_SIZE = (100, 100)


'''
STMP配置
'''
MAIL_SEVER_INFO = dict()
MAIL_SEVER_INFO['MAIL_SERVER'] = configini['MAIL_SEVER_INFO']['MAIL_SERVER']
MAIL_SEVER_INFO['MAIL_PORT'] = configini.getint('MAIL_SEVER_INFO', 'MAIL_PORT')
MAIL_SEVER_INFO['MAIL_USERNAME'] = configini['MAIL_SEVER_INFO']['MAIL_USERNAME']
MAIL_SEVER_INFO['MAIL_PASSWORD'] = configini['MAIL_SEVER_INFO']['MAIL_PASSWORD']
MAIL_SEVER_INFO['MAIL_USE_TLS'] = configini.getboolean('MAIL_SEVER_INFO', 'MAIL_USE_TLS')

'''
数据库配置
'''
DBINFO = dict()
DBINFO['host'] = configini['DB_INFO']['host']
DBINFO['port'] = configini.getint('DB_INFO', 'port')
DBINFO['user'] = configini['DB_INFO']['user']
DBINFO['password'] = configini['DB_INFO']['password']
DBINFO['db'] = configini['DB_INFO']['db']
DBINFO['charset'] = configini['DB_INFO']['charset']
