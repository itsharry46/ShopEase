from django.urls import path
from inventory.product import views

urlpatterns = [
    path('', views.inventory_add_products, name='inventory_add_products'),
    path('category/', views.inventory_add_category, name='inventory_add_category'),
]
