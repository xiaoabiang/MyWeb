# -*- coding: utf-8 -*-
import hashlib
import time
import uuid
import asyncio
from ORM.field import StringField, BooleanField, FloatField, TextField, IntegerField
# from ORM.metaclass import Model
# from ORM.orm import create_pool

from ORM.metaclasspymysql import Model
from flask_login import UserMixin
from hashlib import md5

__author__ = 'Administrator'


def next_id():
    return '%015d%s000' % (int(time.time() * 1000), uuid.uuid4().hex)


class User(Model, UserMixin, ):
    __table__ = 'users'
    id = StringField(primary_key=True, default=next_id, ddl='varchar(50)')
    email = StringField(ddl='varchar(50)')
    passwd = StringField(ddl='varchar(100)')
    admin = BooleanField()
    role_id = IntegerField(default=3)
    isconfirmed = BooleanField()
    name = StringField(ddl='varchar(50)')
    image = StringField(ddl='varchar(500)')
    created_at = FloatField(default=time.time)


class Blog(Model):
    __table__ = 'blogs'

    id = StringField(primary_key=True, default=next_id, ddl='varchar(50)')
    user_id = StringField(ddl='varchar(50)')
    user_name = StringField(ddl='varchar(50)')
    user_image = StringField(ddl='varchar(500)')
    name = StringField(ddl='varchar(50)')
    summary = StringField(ddl='varchar(200)')
    content = TextField()
    created_at = FloatField(default=time.time)


class Comment(Model):
    __table__ = 'comments'

    id = StringField(primary_key=True, default=next_id, ddl='varchar(50)')
    blog_id = StringField(ddl='varchar(50)')
    user_id = StringField(ddl='varchar(50)')
    user_name = StringField(ddl='varchar(50)')
    user_image = StringField(ddl='varchar(500)')
    title = StringField(ddl='varchar(50)')
    content = TextField()
    created_at = FloatField(default=time.time)


class Roles(Model):
    __table__ = 'roles'
    id = StringField(primary_key=True)
    role_name = StringField(ddl='varchar(100)')
    role_comment = StringField(ddl='varchar(100)')
    created_at = FloatField(default=time.time)


class RoleMap(Model):
    __table__ = 'rolemap'
    user_id = StringField(primary_key=True, ddl='varchar(50)')
    role_id = IntegerField()
    created_at = FloatField(default=time.time)


# @asyncio.coroutine
def test(loop=None):


    users = User.findAll()
    # users.send(None)
    for user in users:
        print(user)
    # yield from u.save()
    # yield from u.remove()


if __name__ == '__main__':
    test()




