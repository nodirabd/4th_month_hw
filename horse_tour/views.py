from django.shortcuts import render, get_object_or_404
from . import models
from django.core.paginator import Paginator
from django.db.models import F
from django.views import generic
"""
def company_rating_view(request):
     if request.method == 'GET':
        companies = models.Company.objects.all().order_by('-id')
        context = {
            'companies': companies
        }
        return render(request, 
                      'companies.html',
                        context=context
                    )
"""


class CompanyRatingView(generic.ListView):
    template_name = 'companies.html'
    context_object_name = 'companies'
    model = models.Company

    def get_queryset(self):
        return self.model.objects.all().order_by('-id')
    


"""    
def company_list_view(request):
    query = request.GET.get('s', '')
    companies = models.Company.objects.all().order_by('-id')

    if query:
        companies = companies.filter(company_name__icontains=query)

    paginator = Paginator(companies, 3)
    page = request.GET.get('page')
    page_obj = paginator.get_page(page)

    return render(request, 'company_list.html', {
        'companies': page_obj,
        'query': query,
    })

"""


class CompanyListView(generic.ListView):
    template_name = 'company_list.html'
    model = models.Company
    paginate_by = 3

    def get_queryset(self):
        queryset = self.model.objects.all().order_by('-id')
        query = self.request.GET.get('s', '')
        if query:
            queryset = queryset.filter(company_name__icontains=query)
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['companies'] = context['page_obj']
        context['query'] = self.request.GET.get('s', '')
        return context
    


"""   

def service_list_view(request):
    query = request.GET.get('s', '')
    services = models.CompanyService.objects.all().order_by('-id')

    if query:
        services = services.filter(service_name__icontains=query)

    paginator = Paginator(services, 3)
    page = request.GET.get('page')
    page_obj = paginator.get_page(page)

    return render(request, 'service_list.html', {
        'services': page_obj,
        'query': query,
    })"""



class ServiceListView(generic.ListView):
    template_name = 'service_list.html'
    model = models.CompanyService
    paginate_by = 3

    def get_queryset(self):
        queryset = self.model.objects.all().order_by('-id')
        query = self.request.GET.get('s', '')
        if query:
            queryset = queryset.filter(service_name__icontains=query)
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['services'] = context['page_obj']
        context['query'] = self.request.GET.get('s', '')
        return context
    

    
    
"""def company_detail_view(request, id):
    company = get_object_or_404(models.Company, id=id)
    reviews = models.ReviewCompany.objects.filter(company=company)

    return render(request, 'company_detail.html', {
        'company': company,
        'reviews': reviews,
    })"""

class CompanyDetailView(generic.DetailView):
    template_name = 'company_detail.html'
    context_object_name = 'company'
    pk_url_kwarg = 'id'
    model = models.Company

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['reviews'] = models.ReviewCompany.objects.filter(company=self.object)
        return context