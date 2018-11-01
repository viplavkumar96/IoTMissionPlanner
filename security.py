
from models import User
#File that contains functions for authenticate users
#from models import User
from werkzeug.security import safe_str_cmp
from flask_sqlalchemy import SQLAlchemy

def authenticate(user,password): #method for authenticating users
    data = request.get_json()
    usernm = data['user']
    pwd = data['passwd'] 
    user_data = User.query.filter_by(username = usernm,password = pwd) or None
    if user_data is not None:
        return user

def identity(payload): #To return the JWT token when user is successfully logged in
    user_id = payload['identity']
    return 
