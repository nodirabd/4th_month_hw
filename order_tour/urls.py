from django.urls import path
from . import views

urlpatterns = [
    path('orders_list/', views.orders_list_view, name='or_list'),
    path('orders_list/<int:id>/delete/', views.delete_order_view, name='del_order'),
    path('orders_list/<int:id>/update/', views.update_order_view, name='upd_order'),
    path('create_order/', views.create_order_view, name='cr_order'),
]