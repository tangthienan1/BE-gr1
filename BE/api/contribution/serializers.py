from rest_framework import serializers
from .models import Contribution


# from django.contrib.auth.models import User


class ContributionSerializer(serializers.HyperlinkedModelSerializer):
    file = serializers.FileField(max_length=None, allow_empty_file=False, allow_null=True, required=True)
    submission_date = serializers.DateTimeField(format="%d-%m-%Y")
    approval_date = serializers.DateTimeField(format="%d-%m-%Y")
    update_date = serializers.DateTimeField(format="%d-%m-%Y")

    class Meta:
        model = Contribution
        fields = '__all__'
