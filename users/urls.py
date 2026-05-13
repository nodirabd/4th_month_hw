from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('verify/', views.verify_code_view, name='verify_code'),
    path('dashboard/', views.dashboard_view, name='dashboard'),
]
