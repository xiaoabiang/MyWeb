##项目简介
这是一个采用flask+vue+uikit实现的简单的博客网站,主要实现了如下功能点:
#### 后端API包括：
- **获取日志**：GET /blog/view/
- **创建日志**：POST /blog/create
- **修改日志**：POST /blog/edit/:log_id
- **删除日志**：POST /blog/:blog_id/delete
- **获取评论**：GET /blog/comments
- **创建评论**：POST /comments/update
- **验证新用户**：POST /confirm/:user_id
- **更新头像**：POST /user/image/update
#### 管理页面包括：
- **评论列表页**：GET /manage/comments
- **日志列表页**：GET /blog/manage
- **创建日志页**：GET /blog/create
- **修改日志页**：GET /blog/edit/:log_id
- **用户信息修改页**：GET /manage/users
#### 用户浏览页面包括：
- **注册页**：GET /register
- **登录页**：GET /login
- **注销页**：GET /logout
- **首页**：GET /: /index
- **日志详情页**：GET /blogshow/:blog_id
- **用户信息页**：GET /userview/:user_id

## 模块

- **flask**：主模块
- **flask_login**：为 Flask 提供了会话管理。它处理日常的登入、登出并长期保留用户会话
- **flask_pagedown**：Flask的MarkDown支持
- **flask_wtf**：提供了简单的 WTForms 集成
- **flask_mail**：Flask框架下收发电子邮件

- **markdown**： 富文本处理 
- **pymysql**： 数据库处理 
- **Pillow**： 头像处理

## 项目移植简介
1.从github上下载项目
2.创建数据库,该项目使用的是mysql数据库,sql脚本在migration文件夹下
3.配置config.ini
4.安装所需模块,创建表,运行migration下setups.py
5.启动run.py进行测试

