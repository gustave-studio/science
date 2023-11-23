from .models import NewsModel
from django import forms

class NewsForm(forms.ModelForm):
    class Meta:
        model = NewsModel
        fields = ('title', 'content', 'author', 'newsimage')
        labels = {'title':'タイトル', 'content':'投稿内容', 'author':'著者', 'newsimage':'表示画像'}