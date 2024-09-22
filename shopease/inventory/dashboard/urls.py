from django.urls import path
from inventory.dashboard import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
]