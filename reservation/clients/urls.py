
from django.urls import path
from . import views

urlpatterns = [
    path ( 'add_client/', views.add_client, name='add_client') ,
    path ( 'client_list/', views.client_list, name='client_list'),
]

