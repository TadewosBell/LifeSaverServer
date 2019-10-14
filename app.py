from flask import Flask, jsonify, render_template
from flask_cors import CORS
from flask_pymongo import pymongo,PyMongo

app = Flask(__name__)

app.config.from_object("config")
mongo = PyMongo(app)
CORS(app)

app.config['CORS_HEADERS'] = 'Content-Type'

from users import userFunctions

@app.route('/GetRequest/<string:user_name>',methods=['GET'])
def getUser(user_name):
    response = {}
    user = userFunctions.User(user_name,'Tadewos','Bellete')
    user.print()
    user.save()
    return jsonify(response)

	

if __name__ == '__main__':
   app.run(debug=True)