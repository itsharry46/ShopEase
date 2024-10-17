from django.urls import path
from inventory.dashboard import views

urlpatterns = [
    path('', views.inventory_dashboard, name='inventory_dashboard'),
]
