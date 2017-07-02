from django.db import models
import uuid

# Create your models here.
class Party(models.Model):
	id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
	created_at = models.DateTimeField(auto_now_add=True, editable=False)
	updated_at = models.DateTimeField(auto_now=True, editable=False)
	event_start_time = models.DateTimeField()
	event_end_time = models.DateTimeField()
	max_friends = models.IntegerField(default=10000)

class Friend(models.Model):
	id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
	created_at = models.DateTimeField(auto_now_add=True, editable=False)
	updated_at = models.DateTimeField(auto_now=True, editable=False)
	first_name = models.CharField(max_length=128)
	last_name = models.CharField(max_length=128)
	image_url = models.CharField(max_length=8192)
	url_content = models.BinaryField(default=b'')

class PartyFriends(models.Model):
	id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
	created_at = models.DateTimeField(auto_now_add=True, editable=False)
	updated_at = models.DateTimeField(auto_now=True, editable=False)
	party = models.ForeignKey('Party', models.DO_NOTHING, related_name='friends')
	friend = models.ForeignKey('Friend', models.DO_NOTHING)
	payed = models.BooleanField(default=False)
	checked_in = models.BooleanField(default=False)