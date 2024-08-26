from rest_framework import serializers
from .models import Video, User

class VideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Video
        fields = [
            'id',
            'title',
            'description',
            'video',
            'thumbnail',
        ]
    
    def create(self, validated_data):
        video = Video.objects.create(
            # user=self.context['request'].user,
            user=User.objects.get(id=1),
            title=validated_data['title'],
            description=validated_data['description'],
            video=validated_data['video'],
            thumbnail=validated_data['thumbnail'],
        )
        return video