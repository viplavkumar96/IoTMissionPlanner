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

    def __init__(self, username, password):
        self.username = username
        self.password = password

class Mission(db.Model):
    mid = db.Column(db.Integer,primary_key = True)
    streetloc = db.Column(db.String(500))
    typeofmission = db.Column(db.String(32))
    env = db.Column(db.String(32)) #Indoor/outdoor
    minmaj = db.Column(db.String(32)) #Minor/Major
    #user = db.relationship(User,db.ForeignKey('user.username'))


class drones(db.Model):

    drone_id = db.Column(db.Integer,primary_key = True)

    sensor_temp = db.Column(db.Integer)
    sensor_smoke = db.Column(db.Integer)
    sensor_video = db.Column(db.Integer)

    payload = db.Column(db.Integer)

    battery_life = db.Column(db.Date)

db.create_all()
    

