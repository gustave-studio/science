from django.contrib import admin
from django.urls import path, include
from .views import topfunc, create_news, edit_news, detail_page

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', topfunc, name='top'),
    path('detail_page/<int:pk>', detail_page, name='detail_page'),
    path('create_news/', create_news, name='create_news'),
    path('edit_news/<int:pk>', edit_news, name='edit_news')
]