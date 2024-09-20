from django.urls import path, include
from inventory import views

urlpatterns = [
    path('', views.index, name='login')
]
