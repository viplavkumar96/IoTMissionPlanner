
#File that contains functions for authenticate users
#from models import User
from werkzeug.security import safe_str_cmp
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def authenticate(user,password): #method for authenticating users
    data = request.get_json()
    username = data['user']
    pwd = data['passwd'] 
    if safe_str_cmp(username,user) and safe_str_cmp(pwd,password):
        return user

def identity(payload): #To return the JWT token when user is successfully logged in
    user_id = payload['identity']
    return 
