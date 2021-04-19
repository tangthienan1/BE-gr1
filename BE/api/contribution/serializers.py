
from rest_framework import serializers
from .models import Contribution



class ContributionSerializer(serializers.HyperlinkedModelSerializer):
    file = serializers.FileField(max_length=None, allow_empty_file=False, required=True)
    submission_date = serializers.DateTimeField(format="%d-%m-%Y")
    approval_date = serializers.DateTimeField(format="%d-%m-%Y")
    update_date = serializers.DateTimeField(format="%d-%m-%Y")

    class Meta:
        model = Contribution
        fields = '__all__'

class ContributionCreateSerializer(serializers.HyperlinkedModelSerializer):
    file = serializers.FileField(max_length=None, allow_empty_file=False, required=True)

    class Meta:
        model = Contribution
        fields = ['title', 'description', 'file']