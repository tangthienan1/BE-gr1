from rest_framework import serializers
from .models import Role

# from django.contrib.auth.models import User


class RoleSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Role
        fields = ['role_id', 'role_name']




