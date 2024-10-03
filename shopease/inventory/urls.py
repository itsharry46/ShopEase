from django.urls import path
from inventory import views

urlpatterns = [
    path('', views.inventory_login, name='inventory_login')
]
