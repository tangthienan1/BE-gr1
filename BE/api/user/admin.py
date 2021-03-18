from django.contrib import admin
from .models import User
# Register your models here.


# class UserAdmin(admin.ModelAdmin):
#     list_display = ('userID', 'userName', 'token', 'infoID')


# admin.site.register(User, UserAdmin)
admin.site.register(User)