from django.urls import path
from . import views

urlpatterns = [
    path('companies/', views.company_list_view, name='company_list'),         
    path('companies/rating/', views.company_rating_view, name='company_rating'), 
    path('companies/<int:id>/', views.company_detail_view, name='company_detail'),
    path('services/', views.service_list_view, name='service_list'),        
]