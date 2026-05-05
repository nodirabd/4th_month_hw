from django.db import models
#валидаторы чтоб можно было ограничить оценку от 1 до 5
from django.core.validators import MaxValueValidator, MinValueValidator

# One TO One
class Human(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField()

    def __str__(self):
        return self.name
    
class Horse(models.Model):
    choice_human = models.OneToOneField(Human, on_delete=models.CASCADE)
    horse_name = models.CharField(max_length=50)
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return f'{self.choice_human.name} - {self.horse_name}'

# ManyToMany
class CompanyService(models.Model):
    service_name = models.CharField(max_length=50)
    description = models.TextField()

    def __str__(self):
        return self.service_name

class Company(models.Model):
    company_name = models.CharField(max_length=50)
    company_service = models.ManyToManyField(CompanyService, blank=True, related_name='companies')
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.company_name

# One To Many и Доп ДЗ
class ReviewCompany(models.Model):
    choice_human = models.ForeignKey(Human, on_delete=models.CASCADE, related_name='reviews')
    company = models.ForeignKey(Company, on_delete=models.CASCADE, null=True, related_name='reviews')
    

    rating = models.IntegerField(
        default=1,
        validators=[
            MinValueValidator(1, message="Оценка только от 1 до 5"),
            MaxValueValidator(5, message="Оценка только от 1 до 5")
        ]
    )
    
    text = models.TextField()
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        #  если компания есть, берем её имя, если нет Нет компании
        name_of_company = self.company.company_name if self.company else "Без компании"
        return f'{self.choice_human.name} - {name_of_company} - {self.rating}'