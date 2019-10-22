from mongoengine import Document, EmbeddedDocument
from mongoengine.fields import *

class Region(Document):
    id = ObjectIdField()
    title = StringField()
    description = StringField()

class User(Document):
    email = StringField(required=True)
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

class Call(Document):
    id = ObjectIdField()
    title = StringField()
    description = StringField()
    category = StringField()
    priority = StringField()
    timeReceived = DateTimeField()
    location = EmbeddedDocumentField(Location)
    callerName = StringField()
    callerPhoneNumber = StringField()
    region = ReferenceField(Region)
    createdBy = ReferenceField(User)
    lastModifiedBy = ReferenceField(User)

class Mission(Document):
    id = ObjectIdField()
    title = StringField()
    region = ReferenceField(Region) # mission team's covering area
    calls = ListField(ReferenceField(Call))
    created_by = ReferenceField(User)
    last_modified_by = ReferenceField(User)
    
#class Equipment(Document):
    #id = objectIdField()
    #title = StringField()
    #description = StringField()
    #region = ReferenceField(Region)

#class Team(Document):
    #id = ObjectIdFiend()
    #title = StringField()
    #mission = ReferenceField(Mission)
    #team_in = ReferenceField(User)
    #equipment = ListField(ReferenceField(Equipment))