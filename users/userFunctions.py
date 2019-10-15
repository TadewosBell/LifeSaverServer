
import pymongo
from app import mongo
import hashlib

userDb = mongo.db.userInfo

class User:
    def __init__(self, email, firstName, lastName, password):
        self.email = email
        self.first_name = firstName
        self.last_name = lastName
        self.password = hashlib.sha256(password.encode('utf-8')).hexdigest()

    def register(self):
        document = {'email':self.email,
                    'first_name': self.first_name,
                    'last_name': self.last_name,
                    'password': self.password}
        userDb.insert(document)
    def print(self):
        print(self.email)

def login(email,password):
    userData = userDb.find_one({'email', email})
    loginPassword = hashlib.sha256(password.encode('utf-8')).hexdigest()
    if(userData != None):
        if(userData['password'] == loginPassword):
            print('login')
            userData.pop('password', None)
            return userData
    else:
        print('no user found')
        #return a json object that has an error that is email not found

