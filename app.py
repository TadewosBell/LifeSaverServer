from flask import Flask, jsonify, render_template, request
from flask_cors import CORS
from flask_pymongo import pymongo,PyMongo
from flask_login import LoginManager 


app = Flask(__name__)

app.config.from_object("config")
mongo = PyMongo(app)
CORS(app)

app.config['CORS_HEADERS'] = 'Content-Type'

from users import userFunctions

@app.route('/GetRequest/<string:user_name>',methods=['GET'])
def getUser(user_name):
    response = {}
    user = userFunctions.User(user_name,'Tadewos','Bellete', 'password')
    user.print()
    user.register()
    return jsonify(response)

@app.route('/SignUp', methods=['POST'])
def SignUp():
    content = request.get_json()
    print(content)
    user = userFunctions.User(content['email'], content['firstName'],content['lastName'],content['password'])
    user.register()

    return jsonify(content)

@app.route('/SignIn', methods=['POST'])
def SignIn():
    content = request.get_json()
    print(content)
    token = userFunctions.login(content['email'], content['password'])
    return token

if __name__ == '__main__':
   app.run(debug=True)