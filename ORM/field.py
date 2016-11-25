# -*- coding: utf-8 -*-
__author__ = 'Administrator'


class Field(object):
    def __init__(self, name, col_type, primary_key, default):
        self.name = name
        self.col_type =col_type
        self.primary_key = primary_key
        self.default = default

    def __str__(self):
        return '<%s, %s : %s>' % (self.__class__.__name__, self.col_type, self.name)


class StringField(Field):

    def __init__(self, name=None, primary_key=False, default='', ddl='varchar(100)'):
        super().__init__(name, ddl, primary_key, default)


class BooleanField(Field):

    def __init__(self, name=None, default=False):
        super(BooleanField, self).__init__(name, 'boolean', False, default)


class IntegerField(Field):

    def __init__(self, name=None, primary_key=False, default=0):
        super().__init__(name, 'bigint', primary_key, default)


class FloatField(Field):

    def __init__(self, name=None, primary_key=False, default=0.0):
        super().__init__(name, 'real', primary_key, default)


class TextField(Field):

    def __init__(self, name=None, default=None):
        super().__init__(name, 'text', False, default)

