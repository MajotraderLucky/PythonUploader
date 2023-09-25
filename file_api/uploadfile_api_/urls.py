from django.urls import path
from .views import FileView, FileUploadView

urlpatterns = [
    path('files/', FileView.as_view(), name='file-list'),
    path('upload/', FileUploadView.as_view(), name='file-upload'),
]
