from functools import wraps
from flask import redirect
from flask import session as login_session

# Check whether user is logged in
def login_required(f):
    @wraps(f)
    def x(*args, **kwargs):
        if 'username' not in login_session:
            return redirect('/login')
        return f(*args, **kwargs)
    return x
