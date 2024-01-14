from django.shortcuts import render, redirect, get_object_or_404
from .models import News, RecommendedVideo
from django.views.generic import CreateView
from .forms import NewsForm
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.
def topfunc(request):
  news_list = News.objects.order_by('-id')[:4]

  for news in news_list:
      display_created_at = news.created_at.strftime('%Y年%m月%d日 %H:%M:%S')
      display_updated_at = news.updated_at.strftime('%Y年%m月%d日 %H:%M:%S')
      if display_created_at == display_updated_at:
          news.display_name = '投稿日'
          news.display_date = display_created_at
      else:
          news.display_name = '更新日'
          news.display_date = display_updated_at

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

def news_list(request):
    news_list = News.objects.order_by('-id')

    page = request.GET.get('page', 1)
    paginator = Paginator(news_list, 10)
    try:
        news = paginator.page(page)
    except PageNotAnInteger:
        news = paginator.page(1)
    except EmptyPage:
        news = paginator.page(paginator.num_pages)
    
    return render(request, 'news_list.html', {'news': news})
