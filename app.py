from flask import Flask, jsonify, render_template, request
from flask_cors import CORS
from flask_pymongo import pymongo,PyMongo
from mongoengine import connect
from config import *
from models import *
from datetime import datetime
from flask_jwt_extended import (
    JWTManager, jwt_required, create_access_token,
    get_jwt_identity
)


app = Flask(__name__)

app.config.from_object("config")
app.config['CORS_HEADERS'] = 'Content-Type'
mongo = PyMongo(app)
CORS(app, resources={r"/*": {"origins": "*"}})
connect(db=MONGO_DBNAME, host=MONGO_URI)

app.config['CORS_HEADERS'] = 'Content-Type'

# Setup the Flask-JWT-Extended extension
app.config['JWT_SECRET_KEY'] = 'super-secret'  # Change this!
jwt = JWTManager(app)


#from users import userFunctions

@app.route('/GetRequest/<string:user_name>',methods=['GET'])
def getUser(user_name):
    response = {}
    user = userFunctions.User(user_name,'Tadewos','Bellete')
    user.print()
    user.register()
    return jsonify(response)

@app.route('/SignUp', methods=['POST'])
def SignUp():
    response = {}
    content = request.get_json()
    print(content)
    foundUsers = User.objects(email=content['email']).count()
    if foundUsers == 0:
        user = User(content['email'], content['firstName'],content['lastName'],content['password'])
        user.save()
        response['registered'] = True
    else:
        response['error'] = 'user exists'
    return jsonify(response)

@app.route('/SignIn', methods=['POST'])
def SignIn():
    response = {}
    content = request.get_json()
    foundUsers = User.objects(email=content['email'])
    if foundUsers.count() == 0:
        response['error'] = 'User with specified email does not exist.'
    elif foundUsers.get().password != content['password']:
        response['error'] = 'Incorrect Password.'
    else:
        response['access_token'] = create_access_token(identity=content['email'])
        response['registered'] = True
    return jsonify(response)

@app.route('/Missions', methods=['GET'])
def get_missions():
    return Mission.objects().to_json()

@app.route('/Missions/<string:id>', methods=['GET'])
def get_mission(id):
    return Mission.objects(id=id).get().to_json()

@app.route('/Missions', methods=['POST'])
def post_mission():
    content = request.get_json()
    created = Mission().from_json(content)
    created.save()
    return '', 201

@app.route('/Missions/<string:id>', methods=['DELETE'])
def delete_mission(id):
    Mission.objects(id=id).get().delete()
    return '', 204

@app.route('/Missions/<string:id>/Calls/<string:callId>', methods=['POST'])
def post_call_to_mission(id, callId):
    mission = Mission.objects(id=id).get()
    call = Call.objects(id=callId).get()
    if not mission or not call:
        return '', 404
    mission.calls.append(call)
    mission.save()
    return '', 204

@app.route('/Calls', methods=['GET'])
def get_calls():
    return Call.objects().to_json()

@app.route('/Calls/<string:id>', methods=['GET'])
def get_call(id):
    return Call.objects(id=id).to_json()

@app.route('/Calls', methods=['POST'])
def post_call():
    content = request.get_json()
    created = Call().from_json(content)
    created.timeReceived = datetime.now()
    created.save()
    return '', 201

@app.route('/Calls/<string:id>', methods=['DELETE'])
def delete_call(id):
    Call.objects(id=id).get().delete()
    return '', 204

if __name__ == '__main__':
   app.run(debug=True)