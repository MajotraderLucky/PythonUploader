from django.urls import path
from .views import FileView, FileUploadView, index

urlpatterns = [
    path('', index, name='index'),
    path('files/', FileView.as_view(), name='file-list'),
    path('upload/', FileUploadView.as_view(), name='file-upload'),
]
