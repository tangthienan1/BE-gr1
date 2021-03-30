from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status, viewsets
from rest_framework.views import APIView
from django.http import Http404
from rest_framework import mixins
from rest_framework import generics
from .models import Role
from .serializers import RoleSerializer


class RoleList(viewsets.ModelViewSet):
    queryset = Role.objects.all()
    serializer_class = RoleSerializer


class RoleDetail(viewsets.ModelViewSet):
    queryset = Role.objects.all()
    serializer_class = RoleSerializer
