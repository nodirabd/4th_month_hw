from django.urls import path
from . import views

urlpatterns = [
    path('citation1/', views.Citation1View.as_view(), name='citation1'),
    path('citation2/', views.Citation2View.as_view(), name='citation2'),
    path('citation3/', views.Citation3View.as_view(), name='citation3'),
    path('', views.BookListView.as_view(), name='book_list'),
    path('book_detail/<int:id>/', views.BookDetailView.as_view(), name='book_id'),
]