from django.contrib import admin
from .models import ResumeProfile

@admin.register(ResumeProfile)
class ResumeProfileAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'phone', 'city', 'desired_salary')

# Register your models here.
