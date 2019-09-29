from flask import Flask, jsonify, render_template
from flask_cors import CORS

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

#my change

@app.route('/hello')
def hello():
	return render_template('hello.html')
	

if __name__ == '__main__':
   app.run()