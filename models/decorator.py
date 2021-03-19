import functools
from flask import session, flash, redirect, url_for


def require_login(f):
    @functools.wraps(f)
    def decorated_function(*args, **kwargs):
        if not session.get('name'):
            flash('login dulu ya', 'danger')
            return redirect(url_for('login_view.login_page'))
        return f(*args, **kwargs)

    return decorated_function()
