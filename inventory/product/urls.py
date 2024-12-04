from django.urls import path
from inventory.product import views

urlpatterns = [
    path('', views.inventory_view_products, name='inventory_view_products'),
    path('add_products', views.inventory_add_products, name='inventory_add_products')
]
