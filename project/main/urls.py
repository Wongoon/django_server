from django.urls import URLPattern, path
from . import views

urlpatterns = [
    path('', views.first, name='first'),
    path('main/', views.main, name='main')
]