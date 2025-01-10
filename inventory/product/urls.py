from django.urls import path
from inventory.product import views

urlpatterns = [
    path('', views.inventory_view_products, name='inventory_view_products'),
    path('inventory_view_products_fetch', views.inventory_view_products_fetch, name='inventory_view_products_fetch'),
    path('inventory_view_products_export_fetch', views.inventory_view_products_export_fetch, name='inventory_view_products_export_fetch'),
    path('add_products', views.inventory_add_products, name='inventory_add_products')
]
