from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status, viewsets
from rest_framework.views import APIView
from django.http import Http404
from rest_framework import mixins
from rest_framework import viewsets
from .models import User
from .serializers import UserSerializer


class UserList(viewsets.ModelViewSet):

    def get(self, request, format=None):
        snippets = Snippet.objects.all()
        serializer = SnippetSerializer(snippets, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = SnippetSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserDetail(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


