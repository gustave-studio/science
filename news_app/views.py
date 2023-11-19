from django.shortcuts import render
from .models import NewsModel
from django.views.generic import CreateView
from django.urls import reverse_lazy

# Create your views here.
def topfunc(request):
  news_list = NewsModel.objects.order_by('-id')[:4]
  return render(request, 'top.html', {'news_list': news_list})

class NewsCreate(CreateView):
    template_name = 'news_create.html'
    model = NewsModel
    fields = ('title', 'content', 'author', 'newsimage')
    success_url = reverse_lazy('top')
