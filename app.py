from flask import Flask, jsonify, render_template
from flask_cors import CORS
from users.priority_level import PriorityLevel

app = Flask(__name__)
CORS(app)

app.config['CORS_HEADERS'] = 'Content-Type'

from users import userFunctions

@app.route('/')
def hello_world():
    return 'Hello World'

@app.route('/JsonObject', methods=['POST'])
def returnJson():
    response = {}
    response['testString'] = '1'
    response['testNumber'] = 1
    response['testBool'] = False
    response['functionReturn'] = userFunctions.simpleFunction()
    return jsonify(response)

@app.route('/GetRequest/<string:username>',methods=['GET'])
def getUser(username):
    response = {}
    response['userName'] = username
    return jsonify(response)

@app.route('/CurrentCall/<string:username>', methods=['GET'])
def getCurrentCall(username):
    response = {
        'priority':  PriorityLevel.HIGH.value, 
        'title': 'Tree down on power line', 
        'service': 'Electrical',
        'address': '1000 Hilltop Cir, Baltimore, MD 21250',
        'dateTime': '3:00 AM EST',
        'locationDetails': 'West Hill Apartments',
        'description': 'Power is out, large tree fell on power line.',
        'phoneNumber': '(555) 555-5555'
    }
    return jsonify(response)

#my change

@app.route('/hello')
def hello():
	return render_template('hello.html')
	

if __name__ == '__main__':
   app.run()