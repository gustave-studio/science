from django.contrib import admin
from django.urls import path, include
from .views import topfunc, NewsCreate

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', topfunc, name='top'),
    path('create/', NewsCreate.as_view(), name='create')
]