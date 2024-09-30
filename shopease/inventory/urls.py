from django.urls import path, include
from inventory import views

urlpatterns = [
    path('', views.inventory_login, name='inventory_login'),
    path('logout/', views.inventory_logout, name='inventory_logout'),
    path('dashboard/', include('inventory.dashboard.urls')),
]
