# -*- coding: utf-8 -*-
__author__ = 'Administrator'

from flask_wtf import Form
from wtforms import StringField, BooleanField, PasswordField, TextAreaField
from wtforms.validators import DataRequired, Email, Regexp, EqualTo, Length
from flask_pagedown.fields import PageDownField


class NewStringField(StringField):
    pass


class LoginForm(Form):
    name = StringField('名字', validators=(DataRequired(),))
    password = PasswordField('输入口令')


class RegisterForm(Form):
    name = StringField('名字', validators=(DataRequired(), Length(1, 50),))
    email = StringField('电子邮件', validators=(Email(), Length(1, 50),))
    password = PasswordField('输入口令', validators=(Regexp('[a-z0-9A-Z\-\_]{6,18}'),))
    passwordagain = PasswordField('重复口令', validators=(EqualTo('password', message='密码不一致!'),))


class UserInfoEditForm(Form):
    name = StringField('名字', validators=(DataRequired(), Length(1, 50),))
    email = StringField('电子邮件', validators=(Email(), Length(1, 50),))
    image = StringField('头像')


class BlogForm(Form):
    '''
    编辑blog
    '''
    name = NewStringField('标题', validators=(DataRequired(), Length(1, 50),))
    summary = PageDownField('摘要', validators=(Length(0, 200),))
    content = PageDownField('内容', validators=(DataRequired(),))


class ShowBlogForm(Form):
    '''
    博客展示页
    '''
    user_id = StringField('编号', validators=(DataRequired(),))
    user_name = StringField('博主', validators=(DataRequired(),))
    name = NewStringField('标题', validators=(DataRequired(), Length(1, 50),))
    summary = PageDownField('摘要', validators=(Length(0, 200),))
    content = PageDownField('内容', validators=(DataRequired(),))



if __name__ == '__main__':
    aa = NewStringField()
    print(help(aa))




