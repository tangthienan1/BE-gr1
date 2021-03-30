from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status, viewsets
from rest_framework.views import APIView
from django.http import Http404
from rest_framework import mixins
from rest_framework import generics
from .models import Faculty
from .serializers import FacultySerializer

class FacultyList(viewsets.ModelViewSet):
    queryset = Faculty.objects.all()
    serializer_class = FacultySerializer

class FacultyDetail(viewsets.ModelViewSet):
    queryset = Faculty.objects.all()
    serializer_class = FacultySerializer

