from rest_framework import serializers
from .models import Contribution


# from django.contrib.auth.models import User


class ContributionSerializer(serializers.HyperlinkedModelSerializer):
    image = serializers.ImageField(max_length=None, allow_empty_file=False, allow_null=True, required=False)
    document = serializers.FileField(max_length=None, allow_empty_file=False, allow_null=True, required=False)
    
    class Meta:
        model = Contribution
        fields = '__all__'
