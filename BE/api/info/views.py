from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from django.http import Http404
from rest_framework import mixins
from rest_framework import generics
from .models import Info
from .serializers import InfoSerializer

class InfoList(generics.ListAPIView):
    queryset = Info.objects.all()
    serializer_class = InfoSerializer

class InfoDetail(generics.RetrieveAPIView):
    queryset = Info.objects.all()
    serializer_class = InfoSerializer
