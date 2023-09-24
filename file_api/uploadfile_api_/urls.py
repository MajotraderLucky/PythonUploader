from django.urls import path
from .views import FileView

urlpatterns = [
    path('files/', FileView.as_view(), name='file-list'),
]
