from flask import Flask,jsonify,request,render_template
from flask_restful import Resource,Api
from flask_jwt import JWT
from security import authenticate , identity

app = Flask(__name__)
app.secret_key = "wgetterminalnow"

api = Api(app)
jwt = JWT(app,authenticate,identity) #new endpoint /auth for authorization
#@jwt_required decorator for JWT authentication

class Mission(Resource):
    #@jwt_required
    def post(self):
        return render_template('mission.html') #Loading the mission form
    

api.add_resource(Mission,'/mission/')

app.run()

