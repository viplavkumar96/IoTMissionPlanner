from flask import Flask,jsonify,request,render_template
from flask_restful import Resource,Api
from flask_jwt import JWT,jwt_required
from security import authenticate , identity
from models import Mission,User


app = Flask(__name__)
app.secret_key = "wgetterminalnow"

api = Api(app)
jwt = JWT(app,authenticate,identity) #new endpoint /auth for authorization4

@app.route('/mission', methods = ['GET', 'POST'])
@jwt_required
def mission():
    return render_template('mission.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    return render_template('login.html')

@app.route('/',methods = ['GET','POST'])
def home():
    return render_template('login.html')
    



app.run()

