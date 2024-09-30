from django.urls import path
from inventory.dashboard import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('product_dashboard/', views.dashboard, name='product_dashboard'),
]