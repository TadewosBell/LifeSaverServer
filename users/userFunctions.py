
import pymongo
from app import mongo
import hashlib
from flask import jsonify
from flask_login import LoginManager 
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager
from flask_jwt_extended import (create_access_token)
from app import app

userDb = mongo.db.userInfo
bcrypt = Bcrypt(app)
jwt = JWTManager(app)

class User:
    def __init__(self, email="", firstName="", lastName="", password=""):
        self.email = email
        self.first_name = firstName
        self.last_name = lastName
        self.password = bcrypt.generate_password_hash(password).decode('utf-8')

    def register(self):
        document = {'email':self.email,
                    'first_name': self.first_name,
                    'last_name': self.last_name,
                    'password': self.password}
        #Doesn't register same user twice
        userDb.insert(document)
        #TODO HERE: MAKE THE ERROR VISIBLE TO THE USER THAT THE NAME IS ALREADY TAKEN

    def print(self):
        print(self.email)

def login(email="",password=""):
    userData = userDb.find_one({'email', email})
    if(userData != None):
        if(bcrypt.check_password_hash(userData['password'], password)):
            print('login')
            userData.pop('password', None)
            access_token = create_access_token(identity = {
                'first_name': userData['first_name'],
                'last_name': userData['last_name'],
                'email': userData['email'],
            })
            return jsonify({"token":access_token})      
        else:
            return jsonify({"result": "Incorrect password"})
    else:
        print('no user found')
        return jsonify({"result": "Email not found"})
