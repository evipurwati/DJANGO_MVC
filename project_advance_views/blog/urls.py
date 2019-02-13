from django.urls import path
from . import views

urlpatterns = [
    path('', views.blog, name = 'blog'),
    path('db-blog', views.dbblog, name='db_blog'),
]