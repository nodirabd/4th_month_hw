from django.urls import path
from . import views

urlpatterns = [
    path('companies/', views.company_rating_view, name='company_rating'),
]