from django.urls import path
from . import views

urlpatterns = [
    path('', views.mentee, name = 'mentee'),
    path('db-mentee', views.dbmentee, name='db_mentee'),
]