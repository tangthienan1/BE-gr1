from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from django.http import Http404
from rest_framework import mixins
from rest_framework import generics
from .models import Info
from .serializers import InfoSerializer

class InfoList(APIView):
    def get(self, request, format=None):
        infos = Info.object.all()
        serializer = InfoSerializer(infos, many = true)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = InfoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class InfoDetail(APIView):
    def get_object(self, pk):
        try:
            return Info.object.get(pk=pk)
        except Info.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        info = self.get_object(pk)
        serializer = InfoSerializer(info)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        info = self.get_object(pk)
        serializer = InfoSerializer(info, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        info = self.get_object(pk)
        info.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

