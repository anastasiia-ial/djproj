from django.urls import path, include
from . import views

urlpatterns = [
 path('', views.status, name='status'),
 path('add', views.add, name='add'),
 path('gen', views.gen, name='gen')
]
