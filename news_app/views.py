from django.shortcuts import render, redirect, get_object_or_404
from .models import News, RecommendedVideo
from django.views.generic import CreateView
from .forms import NewsForm, NewsListSearchForm
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
import pytz

def topfunc(request):
    """
    トップページを表示する
    
    Parameters
    ----------
    request : WSGIRequest
        Djangoリクエストオブジェクト
    """

    news_list = News.objects.order_by('-id')[:4]

    for news in news_list:
        jst = pytz.timezone('Asia/Tokyo')
        display_created_at = news.created_at.astimezone(jst).strftime('%Y年%m月%d日 %H:%M:%S')
        display_updated_at = news.updated_at.astimezone(jst).strftime('%Y年%m月%d日 %H:%M:%S')

        if display_created_at == display_updated_at:
            news.display_name = '投稿日'
            news.display_date = display_created_at
        else:
            news.display_name = '更新日'
            news.display_date = display_updated_at

    videos_list = RecommendedVideo.objects.order_by('-id')[:4]
    return render(request, 'top.html', {'news_list': news_list, 'videos_list': videos_list})

def detail_page(request, pk):
    """
    記事の詳細ページを表示する
    
    Parameters
    ----------
    request : WSGIRequest
        Djangoリクエストオブジェクト
    pk : int
        記事のID
    """

    object = get_object_or_404(News, pk=pk)
    return render(request, 'detail_page.html', {'object':object})

def create_news(request):
    """
    記事作成ページを表示する
    
    Parameters
    ----------
    request : WSGIRequest
        Djangoリクエストオブジェクト
    """

    if request.method == 'POST':
        form = NewsForm(request.POST, request.FILES)
        if form.is_valid():
            new_news = form.save(commit=False)
            new_news.author = request.user
            new_news.save()
            return redirect('top')
    else:
        form = NewsForm(initial={'author_display_name': request.user.get_full_name()})

    context = {'form': form}
    return render(request, 'create_news.html', context)

def edit_news(request, pk):
    """
    記事編集ページを表示する
    
    Parameters
    ----------
    request : WSGIRequest
        Djangoリクエストオブジェクト
    pk : int
        記事のID
    """

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
    """
    記事の一覧ページを表示する
    
    Parameters
    ----------
    request : WSGIRequest
        Djangoリクエストオブジェクト
    """

    news_list = ''
    form = ''
    page = request.GET.get('page', 1)

    if request.method == 'POST':
        form = NewsListSearchForm(request.POST)
        if form.is_valid():
            search_query = form.cleaned_data['search_query']
            news_list = News.objects.filter(title__icontains=search_query).order_by('-id')
    else:
        form = NewsListSearchForm()
        news_list = News.objects.order_by('-id')
    
    paginator = Paginator(news_list, 10)
 
    try:
        news = paginator.page(page)
    except PageNotAnInteger:
        news = paginator.page(1)
    except EmptyPage:
        news = paginator.page(paginator.num_pages)
    
    return render(request, 'news_list.html', {'news': news, 'form': form})
