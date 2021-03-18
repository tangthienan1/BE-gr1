from django.shortcuts import render
from rest_framework import generics

from .models import Contribution
from .serializers import ContributionSerializer


class ContributionList(generics.ListCreateAPIView):
    queryset = Contribution.objects.all()
    serializer_class = ContributionSerializer

class ContributionDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Contribution.objects.all()
    serializer_class = ContributionSerializer

