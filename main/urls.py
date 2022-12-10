from django.urls import path, include
from . import views

urlpatterns = [
 path('', views.status, name='status'),
 path('add', views.add, name='add'),
 path('gen', views.gen, name='gen'),
 path('list', views.list, name='list'),
 path('add_raw', views.add_raw, name='add_raw')
]
