from django.urls import path
from inventory.category import views

urlpatterns = [
    path('', views.inventory_view_category, name='inventory_view_category'),
]
