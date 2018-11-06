#File that contains functions for authenticate users
#from models import User
from werkzeug.security import safe_str_cmp
from flask_sqlalchemy import SQLAlchemy
from models import User
from flask import flash,render_template


def authenticate(user,pwd): #method for authenticating users
    if user is not None and pwd is not None:
        user_data = User.query.filter_by(username = user,password = pwd) or None

        if user_data is not None:
                return user
        else:
                flash("User not logged in")
                return render_template("login.html")

def identity(payload): #To return the JWT token when user is successfully logged in
    user_id = payload['identity']
    return user_id

