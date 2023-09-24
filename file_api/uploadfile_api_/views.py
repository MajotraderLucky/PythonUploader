from django.shortcuts import render
from rest_framework import generics
from .models import File
from .serializers import FileSerializer

class FileView(generics.ListCreateAPIView):
  queryset = File.objects.all()
  serializer_class = FileSerializer
