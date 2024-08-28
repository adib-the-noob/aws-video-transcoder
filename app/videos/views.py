from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Video
from .serializers import VideoSerializer

def home(request):
    return render(request, 'home.html')


@api_view(['POST'])
def upload_video(request):
    serializer = VideoSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)

