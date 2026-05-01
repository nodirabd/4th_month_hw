from django.urls import path
from . import views

urlpatterns = [
    #задание первого урока
    path('citation1/', views.citation1, name='citation1'),
    path('citation2/', views.citation2, name='citation2'),
    path('citation3/', views.citation3, name='citation3'),
    path('', views.book_list_view, name='book_list'),
    path('book_detail/<int:id>/', views.book_detail_view, name='book_id'),
]