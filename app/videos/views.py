from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Video
from .serializers import VideoSerializer

@api_view(['POST'])
def upload_video(request):
    serializer = VideoSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)