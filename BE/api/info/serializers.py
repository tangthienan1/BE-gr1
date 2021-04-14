from rest_framework import serializers
from .models import Info

# from django.contrib.auth.models import User


class InfoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Info
        fields = ['info_id','name', 'address', 'dob', 'phone', 'email', 'role_id', 'faculty_id']




