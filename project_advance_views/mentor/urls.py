from django.urls import path
from . import views

urlpatterns = [
    path('', views.mentor, name = 'mentor'),
    path('db-mentor', views.dbmentor, name='db_mentor'),
]