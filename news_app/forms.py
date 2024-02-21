from .models import News
from django import forms
from django_summernote.widgets import SummernoteWidget
from django.conf import settings
import bleach
from bleach.css_sanitizer import CSSSanitizer

# NOTE: なくてもdjango-summernoteを使用出来そうなので、
#       運用して問題なければ削除する。
#
# class HTMLField(forms.CharField):
#     def __init__(self, *args, **kwargs):
#         super(HTMLField, self).__init__(*args, **kwargs)
#         self.widget = SummernoteWidget()
#
#     def to_python(self, value):
#         value = super(HTMLField, self).to_python(value)
#         return bleach.clean(value, tags=settings.ALLOWED_TAGS, attributes=settings.ATTRIBUTES, css_sanitizer=CSSSanitizer())

class NewsForm(forms.ModelForm):
    class Meta:
        model = News
        fields = ('title', 'content', 'author_display_name', 'newsimage')
        labels = {'title':'タイトル', 'content':'投稿内容', 'author_display_name':'著者名', 'newsimage':'表示画像'}

        widgets = {'content': SummernoteWidget()}