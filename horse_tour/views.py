from django.shortcuts import render, get_object_or_404
from . import models
from django.core.paginator import Paginator

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
    })
def company_detail_view(request, id):
    company = get_object_or_404(models.Company, id=id)
    reviews = models.ReviewCompany.objects.filter(company=company)

    return render(request, 'company_detail.html', {
        'company': company,
        'reviews': reviews,
    })