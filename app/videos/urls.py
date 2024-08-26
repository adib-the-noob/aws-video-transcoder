from .views import upload_video
from django.urls import path

urlpatterns = [
    path('upload/', upload_video, name='upload_video'),
]