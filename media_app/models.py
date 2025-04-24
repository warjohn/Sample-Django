from django.db import models


class Video(models.Model):
    file = models.FileField(upload_to='videos/')
    processed_file = models.FileField(upload_to='processed_videos/', null=True, blank=True)

    class Meta:
        indexes = [
            models.Index(fields=['file']),
        ]

class Image(models.Model):
    file = models.ImageField(upload_to='images/')
    processed_file = models.ImageField(upload_to='processed_images/', null=True, blank=True)

    class Meta:
        indexes = [
            models.Index(fields=['file']),
        ]