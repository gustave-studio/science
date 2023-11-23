from django.contrib import admin
from django.urls import path, include
from .views import topfunc, create_news

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', topfunc, name='top'),
    path('create_news/', create_news, name='create_news')
]