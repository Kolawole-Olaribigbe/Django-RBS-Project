from django.contrib import admin
from .models import Room, RoomType, Booking

# Register your models here.

admin.site.register(Room)
admin.site.register(RoomType)
admin.site.register(Booking)
