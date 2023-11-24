from django.shortcuts import render, redirect, get_object_or_404
from .models import NewsModel
from django.views.generic import CreateView
from .forms import NewsForm

# Create your views here.
def topfunc(request):
  news_list = NewsModel.objects.order_by('-id')[:4]
  return render(request, 'top.html', {'news_list': news_list})

def detail_page(request, pk):
    object = get_object_or_404(NewsModel, pk=pk)
    return render(request, 'detail_page.html', {'object':object})

def create_news(request):
    if request.method == 'POST':
        form = NewsForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('top')
    else:
        form = NewsForm()

    context = {'form': form}
    return render(request, 'create_news.html', context)
