from django.urls import path
from inventory.category import views

urlpatterns = [
    path('', views.inventory_view_category, name='inventory_view_category'),
    path('add_category', views.inventory_add_category, name='inventory_add_category'),
    path('info_update_category', views.inventory_info_update_category, name='inventory_info_update_category'),
    path('update_category', views.inventory_update_category, name='inventory_update_category'),
    path('delete_category', views.inventory_delete_category, name='inventory_delete_category')
]
