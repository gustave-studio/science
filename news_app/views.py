from django.shortcuts import render, redirect
from .models import NewsModel
from django.views.generic import CreateView
from .forms import NewsForm

# Create your views here.
def topfunc(request):
  news_list = NewsModel.objects.order_by('-id')[:4]
  return render(request, 'top.html', {'news_list': news_list})

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
