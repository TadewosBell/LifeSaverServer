from flask import Flask, jsonify, render_template, request
from flask_cors import CORS
from flask_pymongo import pymongo,PyMongo
from mongoengine import connect
from bson.objectid import ObjectId
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
        user.setRole(content['role'])
        user.save()
        response['registered'] = True
    else:
        response['error'] = 'user exists'
    return jsonify(response)

@app.route('/SignIn', methods=['POST'])
def SignIn():
    response = {}
    content = request.get_json()
    foundUser= User.objects.with_id(content['email'])
    if not foundUser:
        response['error'] = 'User with specified email does not exist.'
    elif foundUser.password != content['password']:
        response['error'] = 'Incorrect Password.'
    else:
        foundUser.password = None
        response['user'] = foundUser.to_json()
        response['access_token'] = create_access_token(identity=content['email'])
        response['registered'] = True
    return jsonify(response)

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
    call.save()
    return '', 204

@app.route('/Missions/Users/<string:id>', methods=['GET'])
def get_users_for_mission(id):
    mission = Mission.objects.with_id(id)
    if not mission:
        return '', 404
    else:
        return User.objects(mission=mission).to_json()

@app.route('/Missions/Users', methods=['POST'])
def post_user_to_mission():
    id = request.args.get('mission')
    userEmail = request.args.get('user')
    mission = Mission.objects.with_id(id)
    user = User.objects.with_id(userEmail)
    if not mission or not user:
        return '', 404
    user.mission = mission
    user.save()
    return '', 201

@app.route('/Missions/Users', methods=['DELETE'])
def delete_user_from_mission():
    id = request.args.get('mission')
    userEmail = request.args.get('user')
    mission = Mission.objects.with_id(id)
    user = User.objects.with_id(userEmail)
    if not mission or not user:
        return '', 404
    user.mission = None
    user.save()
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
    print(content)
    created = Call().from_json(content)
    created.timeReceived = datetime.now()
    created.save(force_insert= True)
    return str(created.id), 201

@app.route('/Calls/<int:id>', methods=['PUT'])
def put_call(id):
    content = request.get_json()
    if Call.objects.with_id(id) == None:
        return '', 404
    call = Call(**content)
    call.id = id
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

@app.route('/Users/Calls/<string:email>', methods=['GET'])
def get_call_for_user(email):
    user = User.objects.with_id(email)
    result = Call.objects(mission=user.mission.id, active=True).first()
    if not result:
        return '', 404
    return result.to_json(), 200

@app.route('/Categories/<string:name>', methods=['DELETE'])
def delete_category(name):
    Category.objects(name=name).get().delete()
    return '', 204

@app.route('/Users', methods=['GET'])
def get_users():
    return User.objects().to_json()

@app.route('/Users/<string:email>', methods=['POST'])
def post_user(email):
    return User.objects(email=email).get().to_json()

@app.route('/Users/<string:email>', methods=['EDIT'])
def edit_user(email):
    content = request.get_json()
    ChangedUser = User().from_json(content)
    EditUser = User.objects(email=content['email']) 
    EditUser = ChangedUser(content['email'], content['firstName'],content['lastName'],content['password'])
    EditUser.save()
    return '', 201

@app.route('/Users/<string:name>', methods=['DELETE'])
def delete_User(email):
    User.objects(email=email).get().delete()
    return '', 204

@app.after_request
def after_request(response):
  response.headers.add('Access-Control-Allow-Origin', '*')
  response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
  response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE,OPTIONS')
  response.headers.add('Access-Control-Allow-Credentials', 'true')
  return response

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)