from django.db import models


# django mongo connection test
from mongoengine import *
import datetime


# Connection to Mongodb
db = {
	'name': 'carcrew_test',
	'username': 'admin',
	'password': 'secretpassword',
	'host': 'mongodb://localhost/carcrew_test'
}

# connect(
#     name = db['name'],
#     username = db['username'],
#     password = db['password'],
#     host = db['host']
# )

# connect to the database in mongodb://localhost:27017/carcrew_test
connect(db['name'])



# Models


# part_air_filter1 = Part(name='Air Filters', meta_description='desc', quantity = 2, status='available')
# part_air_filter1.save()
class Part(Document):
	name = StringField(max_length = 500, required = True)
	meta_description = StringField(max_length=2000, required=True)
	quantity = IntField(required=True)
	created = DateTimeField(default=datetime.datetime.now)
	updated = DateTimeField(default=datetime.datetime.now)
	
	STATUS_CHOICE = ('available', 'unavailable')
	status = StringField(choices=STATUS_CHOICE)



class Garage(Document):
	pass

