from flask import Flask, jsonify, render_template, request
from flask_cors import CORS
from flask_pymongo import pymongo,PyMongo
from mongoengine import connect
from bson.objectid import ObjectId
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
    mission = Mission.objects.with_id(id)
    mission.get_calls()
    return mission.to_json()

@app.route('/Missions', methods=['POST'])
def post_mission():
    content = request.get_json()
    created = Mission().from_json(content)
    created.save()
    return '', 201

@app.route('/Missions/<string:id>', methods=['DELETE'])
def delete_mission(id):
    Mission.objects.with_id(id).delete()
    return '', 204

@app.route('/Missions/Calls/<string:id>', methods=['GET'])
def get_calls_for_mission(id):
    mission = Mission.objects.with_id(id)
    if not mission:
        return '', 404
    else:
        return Call.objects(mission=mission).to_json()

@app.route('/Missions/Calls', methods=['POST'])
def post_call_to_mission():
    id = request.args.get('mission')
    callId = request.args.get('call')
    mission = Mission.objects.with_id(id)
    call = Call.objects.with_id(callId)
    if not mission or not call:
        return '', 404
    call.mission = mission
    call.save()
    return '', 201

@app.route('/Missions/Calls', methods=['DELETE'])
def delete_call_from_mission():
    id = request.args.get('mission')
    callId = request.args.get('call')
    mission = Mission.objects.with_id(id)
    call = Call.objects.with_id(callId)
    if not mission or not call:
        return '', 404
    call.mission = None
    return '', 204

@app.route('/Calls', methods=['GET'])
def get_calls():
    return Call.objects().to_json()

@app.route('/Calls/<string:id>', methods=['GET'])
def get_call(id):
    return Call.objects.with_id(id).to_json()

@app.route('/Calls', methods=['POST'])
def post_call():
    content = request.get_json()
    created = Call().from_json(content)
    created.timeReceived = datetime.now()
    created.save()
    return '', 201

@app.route('/Calls/<string:id>', methods=['PUT'])
def put_call(id):
    content = request.get_json()
    if Call.objects.with_id(id) == None:
        return '', 404
    call = Call(**content)
    call.id = ObjectId(id)
    call.save()
    return '', 201

@app.route('/Calls/<string:id>', methods=['PATCH'])
def patch_call(id):
    attrs = [
        'title',
        'description',
        'category',
        'priority',
        'timeReceived',
        'callerName',
        'callerPhoneNumber',
        'region'
    ]
    content = request.get_json()
    call = Call.objects.with_id(id)
    if not call:
        return '', 404
    for attr in attrs:
        if attr in content:
            setattr(call, attr, content[attr])
    if 'location' in content:
        call.location = Location().from_json(content['location'])
    call.save()
    return '', 201

@app.route('/Calls/<string:id>', methods=['DELETE'])
def delete_call(id):
    Call.objects.with_id(id).delete()
    return '', 204

@app.route('/Categories', methods=['GET'])
def get_categories():
    return Category.objects().to_json()

@app.route('/Categories', methods=['POST'])
def post_category():
    content = request.get_json()
    created = Category().from_json(content)
    if Category.objects(name__exists=created.name):
        return '', 400 #already exists
    created.save()
    return '', 201

@app.route('/Categories/<string:name>', methods=['DELETE'])
def delete_category(name):
    Category.objects(name=name).get().delete()
    return '', 204

if __name__ == '__main__':
   app.run(debug=True)