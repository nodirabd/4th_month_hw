from django.db import models
from horse_tour.models import Company

class Orders(models.Model):
    name = models.CharField(max_length=20, verbose_name='your full name: ')
    choice_company = models.ForeignKey( Company,verbose_name='choose the company for horse tour', on_delete=models.CASCADE)
    number_card = models.PositiveIntegerField(default='12345678')
    photo = models.ImageField(upload_to='orders/', null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.name}--{self.choice_company}'