from django.urls import path
from .views import FileView, FileUpload

urlpatterns = [
    path('files/', FileView.as_view(), name='file-list'),
    path('upload/', FileUpload.as_view(), name='file-upload'),
]
