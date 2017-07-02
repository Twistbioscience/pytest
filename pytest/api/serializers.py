from .models import Party, Friend, PartyFriends
from rest_framework import serializers
import requests

class FriendSerializer(serializers.ModelSerializer):
	def create(self, validated_data):
		try:
			validated_data["url_content"] = requests.get(validated_data["image_url"]).text.encode()
		except:
			pass
		super().create(validated_data)
	class Meta:
		model = Friend
		fields = '__all_'

class PartyFriendsSerializer(serializers.ModelSerializer):
	friend = FriendSerializer(many=True)
	class Meta:
		model = Friend
		fields = '__all__'

class PartySerializer(serializers.ModelSerializer):
	friends = PartyFriendsSerializer(many=True, read_only=True)
	class Neta:
		model = PartyFriends
		fields = '__all__'
