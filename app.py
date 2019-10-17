from flask import Flask, jsonify, render_template, request
from flask_cors import CORS
from flask_pymongo import pymongo,PyMongo
from mongoengine import connect
from config import *
from models import *
from datetime import datetime

app = Flask(__name__)

app.config.from_object("config")
app.config['CORS_HEADERS'] = 'Content-Type'
mongo = PyMongo(app)
CORS(app, resources={r"/*": {"origins": "*"}})
connect(db=MONGO_DBNAME, host=MONGO_URI)

app.config['CORS_HEADERS'] = 'Content-Type'

from users import userFunctions

@app.route('/GetRequest/<string:user_name>',methods=['GET'])
def getUser(user_name):
    response = {}
    user = userFunctions.User(user_name,'Tadewos','Bellete')
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

@app.route('/Missions', methods=['GET'])
def get_missions():
    return Mission.objects().to_json()

@app.route('/Missions/<string:id>', methods=['GET'])
def get_mission(id):
    return Mission.objects(id=id).first().to_json()

@app.route('/Missions', methods=['POST'])
def post_mission():
    content = request.get_json()
    created = Mission().from_json(content)
    created.save()

@app.route('/Missions/<string:id>', methods=['DELETE'])
def delete_mission(id):
    return True

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

@app.route('/Calls/<string:id>', methods=['DELETE'])
def delete_call(id):
    Call.objects(id=id).first().delete()

if __name__ == '__main__':
   app.run(debug=True)