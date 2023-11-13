from django.contrib import admin
from django.urls import path, include
from .views import topfunc

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', topfunc, name='top'),
]