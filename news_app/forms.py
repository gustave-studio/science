from .models import NewsModel
from django import forms
from django_summernote.widgets import SummernoteWidget
from django.conf import settings
import bleach
from bleach.css_sanitizer import CSSSanitizer

class HTMLField(forms.CharField):
    def __init__(self, *args, **kwargs):
        super(HTMLField, self).__init__(*args, **kwargs)
        self.widget = SummernoteWidget()

    def to_python(self, value):
        value = super(HTMLField, self).to_python(value)
        return bleach.clean(value, tags=settings.ALLOWED_TAGS, attributes=settings.ATTRIBUTES, css_sanitizer=CSSSanitizer())


class NewsForm(forms.ModelForm):
    class Meta:
        model = NewsModel
        fields = ('title', 'content', 'author', 'newsimage')
        labels = {'title':'タイトル', 'content':'投稿内容', 'author':'著者', 'newsimage':'表示画像'}

    content = HTMLField()