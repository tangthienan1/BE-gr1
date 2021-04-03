from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from django.http import Http404
from rest_framework import mixins
from rest_framework import generics
from .models import Info
from .serializers import InfoSerializer
from rest_framework import viewsets


class InfoList(viewsets.ModelViewSet):
    queryset = Info.objects.all()
    serializer_class = InfoSerializer


class InfoDetail(viewsets.ModelViewSet):
    queryset = Info.objects.all()
    serializer_class = InfoSerializer
