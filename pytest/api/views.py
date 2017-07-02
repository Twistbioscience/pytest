from django.shortcuts import render
from rest_framework import generics

from .models import Party, Friend
from .serializers import PartySerializer, FriendSerializer

# Create your views here.


class PartyListCreateView(generics.ListCreateAPIView):
	serializer_class = PartySerializer
	queryset = Party.objects.all()
	
class FriendListCreateView(generics.ListCreateAPIView):
	serializer_class = FriendSerializer
	queryset = Friend.objects.all()