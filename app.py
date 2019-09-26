from flask import Flask, jsonify
app = Flask(__name__)

from users import userFunctions

@app.route('/')
def hello_world():
    return 'Hello World'

@app.route('/JsonObject')
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
    response['username'] = username
    return jsonify(response)


if __name__ == '__main__':
   app.run()