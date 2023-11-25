from django.contrib import admin
from .models import News, RecommendedVideos
from django_summernote.admin import SummernoteModelAdmin

class NewsAdmin(SummernoteModelAdmin):
    summernote_fields = ('content',)

# Register your models here.
admin.site.register(News, NewsAdmin)
admin.site.register(RecommendedVideos)