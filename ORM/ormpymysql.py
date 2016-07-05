# -*- coding: utf-8 -*-
__author__ = 'Administrator'


# -*- coding: utf-8 -*-

import logging
import pymysql
import threading

__author__ = 'Administrator'


def log(sql, args=()):
    logging.info('SQL:%s' % sql)


class LazyConnection:
    def __init__(self, **kw):
        self._kw = kw
        self._local = threading.local()

    def __enter__(self):
        if hasattr(self._local, 'connection'):
            raise RuntimeError('Already connected')
        self._local.connection = pymysql.connect(**self._kw)
        return self._local.connection

    def __exit__(self, exc_type, exc_val, exc_tb):
        self._local.connection.close()
        del self._local.connection


def create_connect(**kw):
    logging.info('create database connection')
    conn = LazyConnection(host=kw.get('host', '127.0.0.1'),
                          port=kw.get('port', 3306),
                          user=kw.get('user', 'xiaoabiang'),
                          password=kw.get('password', 'xiaoabiang'),
                          db=kw.get('db', 'awesome'),
                          charset=kw.get('charset', 'utf8mb4'),
                          cursorclass=pymysql.cursors.DictCursor)
    return conn


def select(sql, args, size=None):
    log(sql, args)
    try:
        with create_connect() as conn:
            with conn.cursor() as cur:
                cur.execute(sql.replace('?', '%s'), args)
                if size:
                    rs = cur.fetchmany(size)
                else:
                    rs = cur.fetchall()
            logging.info('rows returned: %s' % len(rs))
            return rs
    except:
        return None


def execute(sql, args, autocommit=False):
    log(sql)
    try:
        with create_connect() as conn:
            if not autocommit:
                conn.begin()
            try:
                cur = conn.cursor()
                cur.execute(sql.replace('?', '%s'), args)
                affected = cur.rowcount
                cur.close()
                if not autocommit:
                    conn.commit()
            except BaseException as e:
                logging.log(1, e.args)
                if not autocommit:
                    conn.rollback()
                raise
            return affected
    except:
        return None




