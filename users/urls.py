from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.RegisterView.as_view(), name='register'),
    path('login/', views.LoginView.as_view(), name='login'),
    path('verify/', views.VerifyCodeView.as_view(), name='verify_code'),
    path('dashboard/', views.DashboardView.as_view(), name='dashboard'),
]