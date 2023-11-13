from django.db import models

# Create your models here.

class Video(models.Model):
    file_path = models.FileField(upload_to="video/")
    name = models.CharField(max_length=60)
    likes = models.IntegerField(default=0)
    description = models.TextField(null=True)
    is_published = models.BooleanField(default=True)

    def __str__(self):
        return self.name