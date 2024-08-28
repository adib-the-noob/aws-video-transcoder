from django.db import models
from django.contrib.auth import get_user_model
from core.basemodel import BaseModel
from utils.aws.s3_config import upload_raw_video

User = get_user_model()


class Video(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    title = models.CharField(max_length=255)
    description = models.TextField()
    video = models.FileField()
    thumbnail = models.ImageField()

    def __str__(self):
        return self.title

    # def save(self, *args, **kwargs):
    #     try:
    #         x = upload_raw_video(f"{self.video.path}", "adib-source-bucket")
    #         print(x)
    #         super(Video, self).save(*args, **kwargs)
    #     except Exception as e:
    #         raise e