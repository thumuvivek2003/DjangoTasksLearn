# static_media/models.py

from django.db import models

class UploadedFile(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='uploads/')

    def __str__(self):
        return self.title
