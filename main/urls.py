from django.urls import path
from . import views

urlpatterns = [
 path('', views.status, name='status'),
 path('add', views.add, name='add'),
 path('gen', views.gen, name='gen')
]
