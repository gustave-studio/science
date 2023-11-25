from django.contrib import admin
from .models import NewsModel
from django_summernote.admin import SummernoteModelAdmin

class NewsModelAdmin(SummernoteModelAdmin):
    summernote_fields = ('content',)

# Register your models here.
admin.site.register(NewsModel, NewsModelAdmin)