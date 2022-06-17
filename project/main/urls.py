from django.urls import URLPattern, path
from . import views

app_name = 'main'
urlpatterns = [
    path('', views.main, name='main'),
    path('<int:blog_id>/', views.detail, name='detail'),
    path('comment/create/<int:blog_id>/', views.comment_create, name='comment_create')
]