from rest_framework import serializers
from .models import Contribution

# from django.contrib.auth.models import User


class ContributionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Contribution
        fields = ['contributionID', 'subDate', 'aprvDate', 'status', 'img', 'document', 'infoID']





