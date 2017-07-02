from django.contrib import admin

# Register your models here.
from .models import (
		Friend, 
		Party, 
		PartyFriends,
		)

# Register your models here.

class FriendAdmin(admin.ModelAdmin):
	model = Friend
	verbose_name_plural = 'Friends'
	list_display = ('first_name', 'last_name', 'image_url',)

class PartyAdmin(admin.ModelAdmin):
	model = Party
	verbose_name_plural = 'Parties'
	list_display = ('event_start_time', 'event_end_time', 'max_friends')

class PartyFriendsAdmin(admin.ModelAdmin):
	model = PartyFriends
	verbose_name_plural = 'PartiesFriends'
	list_display = ('party', 'friend')

admin.site.register(Party, PartyAdmin)
admin.site.register(PartyFriends, PartyFriendsAdmin)
admin.site.register(Friend, FriendAdmin)
