#UserModel for end users
from flask_sqlalchemy import SQLAlchemy
from flask import Flask

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres:test123@localhost/missionplanner"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db = SQLAlchemy(app)
class User(db.Model):
    username = db.Column(db.String(32),primary_key = True)
    password = db.Column(db.String(32))

class Mission(db.Model):
    mid = db.Column(db.Integer,primary_key = True)
    streetloc = db.Column(db.String(500))
    typeofmission = db.Column(db.String(32))
    env = db.Column(db.String(32)) #Indoor/outdoor
    minmaj = db.Column(db.String(32)) #Minor/Major
    user = db.relationship(User)

class drones(db.Model):
    drone_id = db.Column(db.Integer,primary_key = True)
    sensors_type = db.Column(db.String(500))
    payload = db.Column(db.Integer)
    lifetime = db.Column(db.datetime)
db.create_all()
    
