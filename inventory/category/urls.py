from django.urls import path
from inventory.category import views

urlpatterns = [
    path('', views.inventory_view_category, name='inventory_view_category'),
    path('add_category', views.inventory_add_category, name='inventory_add_category'),
]
