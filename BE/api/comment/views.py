from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status, viewsets
from rest_framework.views import APIView
from django.http import Http404
from rest_framework import mixins
from rest_framework import generics
from .models import Comment
from .serializers import CommentSerializer


class CommentList(generics.ListAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer


class CommentDetail(generics.RetrieveAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer


class CommentViewSet(viewsets.ModelViewSet):
    authentication_classes = []
    permission_classes = []
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    lookup_field = 'id'
