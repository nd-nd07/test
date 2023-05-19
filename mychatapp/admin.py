from django.contrib import admin
from . models import ChatMessage, Profile, Friend

# Register your models here.
admin.site.register([Profile, Friend, ChatMessage])