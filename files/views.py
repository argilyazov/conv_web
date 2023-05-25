from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Files
from .serializers import FileSerializer
from rest_framework import viewsets, generics

from rest_framework import status
# Create your views here.

class FileAPIView(viewsets.ModelViewSet):
    queryset = Files.objects.all()
    serializer_class = FileSerializer

