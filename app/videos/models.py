from django.db import models
from django.contrib.auth import get_user_model
from core.basemodel import BaseModel
from utils.aws.s3_config import upload_raw_video

User = get_user_model()


class Video(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    title = models.CharField(max_length=255)
    description = models.TextField()
    video = models.FileField(upload_to='media/raw_videos/')
    thumbnail = models.ImageField(upload_to='media/thumbnails/')

    def __str__(self):
        return self.title

    # def save(self, *args, **kwargs):
    #     try:
    #         upload_raw_video(self.video.path, "adib-source-bucket")
    #         super(Video, self).save(*args, **kwargs)
    #     except Exception as e:
    #         raise e