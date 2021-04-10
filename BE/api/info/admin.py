from django.contrib import admin
from .models import Info
# Register your models here.


class InfoAdmin(admin.ModelAdmin):
    list_display = ('info_id', 'name', 'address', 'dob', 'phone', 'email', 'role_id', 'faculty_id')


admin.site.register(Info, InfoAdmin)
