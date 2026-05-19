from django.urls import path
from . import views

urlpatterns = [
    path('companies/', views.CompanyListView.as_view(), name='company_list'),         
    path('companies/rating/', views.CompanyRatingView.as_view(), name='company_rating'), 
    path('companies/<int:id>/', views.CompanyDetailView.as_view(), name='company_detail'),
    path('services/', views.ServiceListView.as_view(), name='service_list'),        
]