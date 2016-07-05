# -*- coding: utf-8 -*-
__author__ = 'Administrator'


from flask import abort
from flask_login import current_user
from functools import wraps


def permission_required(*role_id):
    def decorator(f):
        @wraps(f)
        def decorated_function(*args, **kw):
            if not current_user.role_id in role_id:
                abort(403)
            return f(*args, **kw)
        return decorated_function
    return decorator


def admin_required(f):
    return permission_required(1)(f)