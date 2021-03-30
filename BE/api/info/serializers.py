from rest_framework import serializers
from .models import Info

# from django.contrib.auth.models import User


class InfoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Info
        fields = ['infoID', 'Name', 'Address', 'DoB', 'Phone', 'Email', 'roleID', 'facultyID']




