from django.db import models
from django.contrib.auth.models import User

class ResumeProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')

    full_name = models.CharField(max_length=255, verbose_name="ФИО")
    birth_date = models.DateField(verbose_name="Дата рождения")
    phone = models.CharField(max_length=20, verbose_name="Номер телефона")
    city = models.CharField(max_length=100, verbose_name="Город проживания")
    education = models.CharField(max_length=255, verbose_name="Образование")
    experience_years = models.IntegerField(verbose_name="Опыт работы (лет)")
    desired_salary = models.IntegerField(verbose_name="Желаемая зарплата (KGS)")
    skills = models.TextField(verbose_name="Ключевые навыки")
    photo = models.ImageField(upload_to='photos/', verbose_name="Фотография соискателя") # Файл 1
    resume_file = models.FileField(upload_to='resumes/', verbose_name="Файл резюме (PDF/Docx)") # Файл 2

    def __str__(self):
        return self.full_name
