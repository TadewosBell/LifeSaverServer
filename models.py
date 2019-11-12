from mongoengine import Document, EmbeddedDocument
from mongoengine.fields import *

class Region(Document):
    title = StringField()
    description = StringField()

class User(Document):
    email = StringField(required=True)
    firstName = StringField(required=True)
    lastName = StringField(required=True)
    password = StringField(required=True)
    isCallSpecialist = BooleanField()
    isOperationsChief = BooleanField()
    isMissionManagement = BooleanField()
    isFirstFesponder = BooleanField()
    firstResponderRole = StringField()
    isVolunteer = BooleanField()
    details = StringField()

class Location(EmbeddedDocument):
    address = StringField()
    coordinates = PointField()
    details = StringField()

class Mission(Document):
    title = StringField()
    region = ReferenceField(Region)
    created_by = ReferenceField(User)
    last_modified_by = ReferenceField(User)

    def get_calls(self):
        return Call.objects(mission=self)

class Call(Document):
    title = StringField()
    description = StringField()
    category = StringField()
    mission = ReferenceField(Mission)
    priority = StringField()
    timeReceived = DateTimeField()
    location = EmbeddedDocumentField(Location)
    callerName = StringField()
    callerPhoneNumber = StringField()
    region = ReferenceField(Region)
    createdBy = ReferenceField(User)
    lastModifiedBy = ReferenceField(User)

class Category(Document):
    name = StringField(required=True)