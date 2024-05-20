from django.contrib import admin
from userauth.models import User, Profile

# Register your models here.
class UserAdmin(admin.ModelAdmin):
    search_fields = ['first_name', 'last_name']
    list_display = ['first_name', 'last_name', 'email', 'country']


class ProfileAdmin(admin.ModelAdmin):
    search_fields = ['last_name', 'user__first_name']
    list_display = ['first_name', 'last_name', 'country']

admin.site.register(User, UserAdmin)
admin.site.register(Profile, ProfileAdmin)
