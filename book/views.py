from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def citation1(request):
    return HttpResponse("Ведь все взрослы были детьми, только мало кто из них об этом помнит.") #маленький принц
def citation2(request):
    return HttpResponse("Все приходит во время для того кто умеет ждать.") # война и мир Лев Толстой
def citation3(request):
    return HttpResponse("Муки и слезы - ведь это тоже жизнь.") # Анна Каренина Лев Толстой