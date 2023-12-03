from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class News(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    newsimage = models.ImageField(upload_to='')

    class Meta:
        verbose_name_plural = 'News'

class RecommendedVideo(models.Model):
    title = models.TextField()
    url = models.TextField()