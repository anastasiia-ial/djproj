from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.status, name='status'),
    path('add', views.add, name='add'),
    path('gen', views.gen, name='gen'),
    path('list_raw', views.list_raw, name='list_raw'),
    path('add_raw', views.add_raw, name='add_raw'),
    path('list_sku', views.list_sku, name='list_sku'),
    path('show_sku/<sku_id>', views.show_sku, name='show_sku'),
    path('add_sku', views.add_sku, name='add_sku'),
    path('update_raw/<raw_id>', views.update_raw, name='update_raw'),
    path('update_sku/<sku_id>', views.update_sku, name='update_sku'),
    path('delete_raw/<raw_id>', views.delete_raw, name='delete_raw'),
    path('delete_sku/<sku_id>', views.delete_sku, name='delete_sku'),
    # path('pdf_sku', views.pdf_sku, name='pdf_sku'),
]
