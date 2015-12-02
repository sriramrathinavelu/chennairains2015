from django.db import models
from mongoengine import *

# Create your models here.

class ChennaiRains(Document):
	text = StringField(required=True, null=False)
	user = DictField()
	timestamp_ms = LongField()
	created_at = StringField()
	location = StringField(required=True, null=False)
	meta = {'strict' : False}

	def __str__(self):
		return self.text
