from rest_framework import serializers
from .models import Faculty

# from django.contrib.auth.models import User


class FacultySerializer(serializers.ModelSerializer):
    class Meta:
        model = Faculty
        fields = ['facultyID', 'facultyName']




