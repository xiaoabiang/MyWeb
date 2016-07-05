# -*- coding: utf-8 -*-
import json
from werkzeug.utils import secure_filename

__author__ = 'Administrator'


from flask import render_template, flash, request, redirect, g, url_for, session, send_from_directory
from www import app, lm, oid
from www.forms import LoginForm, RegisterForm, BlogForm, UserInfoEditForm, ShowBlogForm
from ORM.models import User, Blog, Comment, RoleMap
from flask_login import login_user, current_user, logout_user, login_required
from logging import warning, log
from werkzeug.security import generate_password_hash, check_password_hash
from www.smtpemail.mailserver import send_email
import time, os
from www.decorators import admin_required, permission_required
from www.apis import get_page_index, Page
from config import PRE_PAGE_NUMBER, UPLOAD_FOLDER, IMAGE_SIZE, ALLOWED_TAGS
from PIL import Image



@app.route('/')
@app.route('/index')
def index():
    page = request.values.get('page', '1')
    page_index = get_page_index(page)
    if g.user is not None and g.user.is_authenticated:
        return render_template('index.html', user=g.user, page_index=page_index)
    return render_template('index.html', page_index=page_index)


@app.route('/login', methods=['GET', 'POST'])
def login():
    if g.user is not None and g.user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User()
        user.name = form.name.data
        user.passwd = form.password.data.strip()
        users = User.find_all('name=?', [user.name])
        if users is None or len(users) == 0:
            log(level=1, msg="用户名不存在!")
            return redirect(url_for('login'))
        elif not check_password_hash(users[0].passwd, user.passwd):
            log(level=1, msg="密码错误!")
            return redirect(url_for('login'))
        login_user(users[0], remember=True)
        return redirect(request.args.get('next') or url_for('index'))
    return render_template('login.html', title='Sign in', form=form)


@lm.user_loader
def load_user(id):
    return User.find(id)


@app.before_request
def before_request():
    g.user = current_user


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))


@app.route('/user/<id>')
@login_required
def user(id):
    user = User.find(id)
    form = UserInfoEditForm()
    if len(user) == 0:
        flash('User not found')
        return redirect(url_for('index'))
    if form.validate_on_submit():
        user.name = form.name.data
        user.email = form.name.email
        user.update()
        return redirect(url_for('index'))
    return render_template('user.html',
                           user=user,
                           form=form)


@app.route('/register', methods=['GET', 'POST'])
def register():
    if g.user is not None and g.user.is_authenticated:
        return redirect(url_for('index'))
    form = RegisterForm()
    if form.validate_on_submit():
        # return oid.try_login(form.openid.data, ask_for=['name', 'email'])
        user = User()
        user.name = form.name.data
        user.email = form.email.data
        user.isconfirmed = False
        user.passwd = generate_password_hash(form.password.data.strip())
        rows = user.save()
        if rows != 1:
            return redirect(url_for('register'))
        else:
            send_email(to=user.email, subject='确认注册信息!', template='/email/confirm', user=user, id=user.id)
            # login_user(user, remember=True)
            return redirect(url_for('index'))
    return render_template('register.html',
                           title='Sign in',
                           form=form,
                           providers=app.config['OPENID_PROVIDERS'])


@app.route('/confirm/<id>', methods=['GET', 'POST'])
def confirm(id):
    if g.user is not None and g.user.is_authenticated:
        return redirect(url_for('index'))
    user = User.find(id)
    if not user:
        return redirect(url_for('register'))
    elif int(time.time()) - user.created_at > 3600:
        user.remove()
        return redirect(url_for('register'))
    elif user.id != id:
        return redirect(url_for('register'))
    # 验证正确,将数据保存到数据库
    user.isconfirmed = True
    user.update()

    login_user(user, remember=True)
    return redirect(url_for('index'))


@app.route('/admin')
@login_required
@admin_required
def for_admins_only():
    return "For administrators!"


# @app.route('/blog/edit/<id>')
# @login_required
# def blog_edit_id(id):
#     blog = Blog.find(id)
#     return blog


@app.route('/blog/create', methods=['GET', 'POST'])
@login_required
def blog_create():
    form = BlogForm()
    blog = Blog(user_id=g.user.id, user_name=g.user.name, user_image=g.user.image)
    if form.validate_on_submit():
        blog.name = form.name.data
        blog.summary = form.summary.data
        blog.content = form.content.data
        rownumber = blog.save()
        if rownumber != 1:
            return render_template('blog_edit.html',
                                   user=g.user,
                                   form=form,
                                   blog=blog)
        return redirect(url_for('blog_manage'))
    return render_template('blog_edit.html',
                           user=g.user,
                           form=form,
                           blog=blog)


@app.route('/blog/edit/<id>', methods=['GET', 'POST'])
@login_required
def blog_edit(id):
    form = BlogForm()
    blog = Blog.find(id)
    if form.validate_on_submit():
        blog.name = form.name.data
        blog.summary = form.summary.data
        blog.content = form.content.data
        # blog = Blog(user_id=g.user.id, user_name=g.user.name, user_image=g.user.image,
        #             name=form.name.data, summary=form.summary.data, content=form.content.data)
        rownumber = blog.update()
        if rownumber != 1:
            return render_template('blog_edit.html',
                                   user=g.user,
                                   form=form,
                                   blog=blog)
        return redirect(url_for('blog_manage'))
    return render_template('blog_edit.html',
                           user=g.user,
                           form=form,
                           blog=blog)


@app.route('/blog/manage', methods=['GET', 'POST'])
@login_required
def blog_manage():
    # blogs = Blog.find_all('user_id = ?', g.user.id)
    page = request.values.get('page', '1')
    page_index = get_page_index(page)
    return render_template('blog_manage.html', user=g.user, page_index=page_index)


@login_required
@app.route('/blog/view/')
def blog_view():
    '''
    :param page: 获取分页数
    :param user_id 用户ID
    :return: 返回读取的结果
    '''
    page = request.values.get('page', '1')
    user_id = request.values.get('user_id', None)
    page_index = get_page_index(page)
    if user_id:
        num = Blog.find_number('count(id)', where='user_id=?', args=(user_id,))
    else:
        num = Blog.find_number('count(id)')
    p = Page(num, page_index, page_size=PRE_PAGE_NUMBER)
    if num == 0:
        json.dumps(dict(page=p, blogs=()), ensure_ascii=False, default=lambda o: o.__dict__).encode('utf-8')
    if user_id:
        blogs = Blog.find_all('user_id=?', [user_id], orderBy='created_at desc', limit=(p.offset, p.limit))
    else:
        blogs = Blog.find_all(orderBy='created_at desc', limit=(p.offset, p.limit))
    return json.dumps(dict(page=p, blogs=blogs), ensure_ascii=False, default=lambda o: o.__dict__).encode('utf-8')


@login_required
@app.route('/blog/<id>/delete', methods=['POST'])
def blog_delete(id):
    blog = Blog.find(id)
    blog.remove()
    return json.dumps(dict(id=id), ensure_ascii=False, default=lambda o: o.__dict__).encode('utf-8')


@login_required
@app.route('/user/image/update', methods=['POST'])
def user_image_update():
    ''' 更新用户头像并修改成指定大小保存
    :return:
    '''
    file = request.files['files[]']
    if file:
        try:
            filename = secure_filename(file.filename)
            *test, extends = filename.split('.')
            filename = g.user.id + str(int(time.time()*1000)) + "." + extends
            im = Image.open(file)
            im.thumbnail(IMAGE_SIZE)
            im.save(os.path.join(os.getcwd(), 'www', *(app.config['UPLOAD_FOLDER'].split('/')), filename))
            g.user.image = '/' + os.path.join(*(app.config['UPLOAD_FOLDER'].split('/')), filename).replace('\\', '/')
            g.user.update()
            return json.dumps(dict(flag=True, userimage=g.user.image), ensure_ascii=False, default=lambda o: o.__dict__).encode('utf-8')
        except BaseException as e:
            Warning(e)
    return json.dumps(dict(flag=False), ensure_ascii=False, default=lambda o: o.__dict__).encode('utf-8')


@app.route('/blogshow/<id>')
def blog_show(id):
    blog = Blog.find(id)
    blog.created_at = time.strftime('%Y-%m-%d %H:%M:%S', time.gmtime(blog.created_at))
    return render_template('blog_show.html', user=g.user, blog=blog)


@app.route('/blog/comments', methods=['GET'])
def blog_comments():
    blog_id = request.values.get('blog_id', None)
    if not blog_id:
        return json.dumps(None).encode('utf-8')
    else:
        comments = Comment.find_all('blog_id=?', args=[blog_id])
        return json.dumps(dict(comments=comments), ensure_ascii=False, default=lambda o: o.__dict__).encode('utf-8')


@app.route('/comments/update', methods=['POST'])
@login_required
def comments_update():
    '''
    保存评论
    :return:
    '''
    try:
        commentdata = json.loads(request.data.decode('utf-8'))
        comment = Comment(blog_id=commentdata['blog_id'], user_id=g.user.id,
                          user_name=g.user.name, user_image=g.user.image,
                          content=commentdata['content'], title=commentdata['title'])
        comment.save()
        comments = Comment.find_all('blog_id=?', args=[comment.blog_id])
        return json.dumps(dict(comments=comments), ensure_ascii=False, default=lambda o: o.__dict__).encode('utf-8')
    except BaseException as e:
        warning(e)
        return json.dumps(None).encode('utf-8')


@app.route('/test')
def test():
    '''
    用来做测试的
    :return:
    '''
    return render_template('test.html')
