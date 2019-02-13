from django.urls import path
from . import views

urlpatterns = [
    path('', views.dbblog, name='blog'),
    path('form', views.input_post, name='input_post'),
    path('blog/<int:blog_id>', views.blog_detail, name='blog_detail'),

]