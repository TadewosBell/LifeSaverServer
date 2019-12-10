from mongoengine import Document, EmbeddedDocument
from mongoengine.fields import *

class Region(Document):
    title = StringField()
    description = StringField()


class Location(EmbeddedDocument):
    address = StringField()
    coordinates = PointField()
    details = StringField()

class Mission(Document):
    title = StringField()
    region = ReferenceField(Region)

    def get_calls(self):
        return Call.objects(mission=self)

class User(Document):
    email = StringField(required=True,primary_key=True)
    firstName = StringField(required=True)
    lastName = StringField(required=True)
    password = StringField(required=True)
    isCallSpecialist = BooleanField()
    isOperationsChief = BooleanField()
    isMissionManagement = BooleanField()
    isFirstResponder = BooleanField()
    firstResponderRole = StringField()
    isVolunteer = BooleanField()
    details = StringField()
    mission = ReferenceField(Mission)
    
    def setRole(self, role):
        if role == 1:
            self.isFirstResponder = True
        if role == 2:
            self.isVolunteer = True
        if role == 3:
            self.isMissionManagement = True
        if role == 4:
            self.isOperationsChief = True
        if role == 5:
            self.isCallSpecialist = True

class Call(Document):
    id = SequenceField(primary_key=True)
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
    resolved = BooleanField()
    active = BooleanField()

class Category(Document):
    name = StringField(required=True)