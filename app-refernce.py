from flask import Flask,jsonify,request

app = Flask(__name__) #Name for the application

#Requests
login_details = [{'name': 'Viplav', 'pass':'yoyo@7892'}]
#Decorator
@app.route('/') #Home Page of site
def home(): #A method that is called whenever '/' is requested
	return  "Hello,world"

#Creating endpoints
#Specifying the methods of request
@app.route('/login', methods=['POST','GET'])
def login():
	return jsonify({'login_details':login_details})

@app.route('/signup', methods = ['POST'])
def signup():
    request_data = request.get_json() #For converting JSON to dictionary
    new_user = {'name':request_data['name'], 'pass':request_data['pass']}
    login_details.append(new_user)
    return jsonify({'login_details':login_details})

app.run()



