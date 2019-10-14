
from mongoengine import *
import pymongo
from app import mongo
print(mongo.db.userInfo)
class User:
    collection = mongo.db.userInfo
    def __init__(self, userName, firstName, lastName):
        self.user_name = userName
        self.first_name = firstName
        self.last_name = lastName

    def save(self):
        document = {'user_name':self.user_name,
                    'first_name': self.first_name,
                    'last_name': self.last_name,}
        self.collection.insert(document)
    def print(self):
        print(self.user_name)
        