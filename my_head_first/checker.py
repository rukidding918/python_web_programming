from functools import wraps
from flask import session, render_template

def check_logged_in(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        if 'logged_in' in session:
            return func(*args, **kwargs)
        return render_template('noPermission.html')
    return wrapper