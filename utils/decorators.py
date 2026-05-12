from functools import wraps

from flask import session
from flask import redirect
from flask import url_for
from flask import flash


def login_required(f):

    @wraps(f)
    def decorated_function(*args, **kwargs):

        if 'user_id' not in session:

            flash('Please login first!', 'danger')

            return redirect(url_for('auth.login'))

        return f(*args, **kwargs)

    return decorated_function