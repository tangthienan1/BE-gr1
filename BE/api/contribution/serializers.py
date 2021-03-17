from rest_framework import serializers
from .models import Contribution

# from django.contrib.auth.models import User


class ContributionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contribution
        fields = '__all__'




