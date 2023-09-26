from django.shortcuts import render
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import File
from .serializers import FileSerializer
from file_api.tasks import process_file

class FileView(generics.ListCreateAPIView):
  queryset = File.objects.all()
  serializer_class = FileSerializer

class FileUploadView(APIView):
  def post(self, request):
    file_serializer = FileSerializer(data=request.data)
    if file_serializer.is_valid():
      file_serializer.save()
      file_id = file_serializer.data['id']
      # Run a task in the background using Celery.
      process_file.delay(file_id)
      return Response(file_serializer.data, status=status.HTTP_201_CREATED)
    else:
      return Response(file_serializer.errors, status=status.HTTP_400_BAD_REQUEST)