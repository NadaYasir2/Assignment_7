
from django.urls import path
from . import views

urlpatterns = [
    path ( 'header/', views.header, name='header') ,
    path ( 'add/', views.add, name='add'),
]

