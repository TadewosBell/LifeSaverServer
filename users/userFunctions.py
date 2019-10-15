
import pymongo
from app import mongo
import hashlib

class User:
    collection = mongo.db.userInfo
    def __init__(self, email, firstName, lastName, password):
        self.email = email
        self.first_name = firstName
        self.last_name = lastName
        self.password = hashlib.sha256(password.encode('utf-8')).hexdigest()

    def save(self):
        document = {'email':self.email,
                    'first_name': self.first_name,
                    'last_name': self.last_name,
                    'password': self.password}
        self.collection.insert(document)
    def print(self):
        print(self.email)
        