from django.shortcuts import render, redirect, get_object_or_404
from .models import News, RecommendedVideo
from django.views.generic import CreateView
from .forms import NewsForm

# Create your views here.
def topfunc(request):
  news_list = News.objects.order_by('-id')[:4]
  videos_list = RecommendedVideo.objects.order_by('-id')[:4]
  return render(request, 'top.html', {'news_list': news_list, 'videos_list': videos_list})

def detail_page(request, pk):
    object = get_object_or_404(News, pk=pk)
    return render(request, 'detail_page.html', {'object':object})

def create_news(request):
    if request.method == 'POST':
        form = NewsForm(request.POST, request.FILES)
        if form.is_valid():
            new_news = form.save(commit=False)
            new_news.author = request.user
            new_news.save()
            return redirect('top')
    else:
        form = NewsForm()

    context = {'form': form}
    return render(request, 'create_news.html', context)

def edit_news(request, pk):
    instance = get_object_or_404(News, pk=pk)

    if request.user != instance.author:
        return redirect('top')

    if request.method == 'POST':
        form = NewsForm(request.POST, request.FILES, instance=instance)
        if form.is_valid():
            form.save()
            return redirect('top')
    else:
        form = NewsForm(instance=instance)

    context = {'form': form}
    return render(request, 'edit_news.html', context)
