from rest_framework import serializers
from .models import Comment
# from django.contrib.auth.models import User

class CommentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Comment
        fields = ['id', 'content', 'time', 'contributionID', 'infoID']






