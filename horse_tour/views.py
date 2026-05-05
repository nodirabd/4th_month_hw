from django.shortcuts import render
from . import models

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

# Create your views here.
