from django.db import models

# Create your models here.
class NewsModel(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    author = models.CharField(max_length=50)
    newsimage = models.ImageField(upload_to='')