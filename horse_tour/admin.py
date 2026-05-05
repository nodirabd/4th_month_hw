from django.contrib import admin

from  .import models

admin.site.register(models.Human)
admin.site.register(models.Horse)
admin.site.register(models.ReviewCompany)
admin.site.register(models.Company)
admin.site.register(models.CompanyService)
