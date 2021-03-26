from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from django.http import Http404
from rest_framework import mixins
from rest_framework import generics
from .models import Contribution
from .serializers import ContributionSerializer


class ContributionList(generics.ListAPIView):
    queryset = Contribution.objects.all()
    serializer_class = ContributionSerializer


class ContributionDetail(generics.RetrieveAPIView):
    queryset = Contribution.objects.all()
    serializer_class = ContributionSerializer
