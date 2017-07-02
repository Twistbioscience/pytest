from django.conf.urls import url,include
from .views import PartyListCreateView, FriendListCreateView

urlpatterns = [
	url(r'^party/$', PartyListCreateView.as_view()),
	url(r'^friend/$', FriendListCreateView.as_view()),
]