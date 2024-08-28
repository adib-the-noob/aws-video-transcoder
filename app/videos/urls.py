from django.urls import path
from .views import upload_video, home

urlpatterns = [
    path('', home, name='home'),
    path('upload/', upload_video, name='upload_video'),
]