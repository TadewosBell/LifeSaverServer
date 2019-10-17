from mongoengine import Document
from mongoengine.fields import *

class Region(Document):
    id = ObjectIdField()
    title = StringField()
    description = StringField()

class User(Document):
    email = StringField(required=True)
    is_call_specialist = BooleanField()
    is_operations_chief = BooleanField()
    is_mission_management = BooleanField()
    is_first_responder = BooleanField()
    first_responder_role = StringField()
    is_volunteer = BooleanField()
    details = StringField()

class Call(Document):
    id = ObjectIdField()
    title = StringField()
    description = StringField()
    category = StringField()
    priority = StringField()
    time_received = DateTimeField()
    location_address = StringField()
    location_coordinates = PointField()
    location_details = StringField()
    caller_name = StringField()
    caller_phone_number = StringField()
    region = ReferenceField(Region)
    created_by = ReferenceField(User)
    last_modified_by = ReferenceField(User)

class Mission(Document):
    id = ObjectIdField()
    title = StringField()
    region = ReferenceField(Region)
    calls = ListField(ReferenceField(Call))
    created_by = ReferenceField(User)
    last_modified_by = ReferenceField(User)