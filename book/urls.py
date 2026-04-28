from django.urls import path
from . import views

urlpatterns = [
    path('citation1/', views.citation1, name='citation1'),
    path('citation2/', views.citation2, name='citation2'),
    path('citation3/', views.citation3, name='citation3'),
]