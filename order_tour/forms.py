from django import forms
from . import models

class OrdersForm(forms.ModelForm):
    class Meta:
        model = models.Orders
        fields = '__all__'