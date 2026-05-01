from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .import models


#задание второго урока
def book_detail_view(request, id):
    if request.method == 'GET':
        book_id = get_object_or_404(models.Book, id=id) #получаем объект модели Book по id
        return render(request, 'book_detail.html', {'book': book_id}) #передаем объект модели Book в шаблон book_detail.html

def book_list_view(request):
    if request.method == 'GET': #проверяем метод запроса
        query_book = models.Book.objects.all().order_by('-id') #получаем все объекты модели Book
        return render(request, 'book_list.html', {'books': query_book})


#задание первого урока
def citation1(request):
    return HttpResponse("Ведь все взрослы были детьми, только мало кто из них об этом помнит.") #маленький принц
def citation2(request):
    return HttpResponse("Все приходит во время для того кто умеет ждать.") # война и мир Лев Толстой
def citation3(request):
    return HttpResponse("Муки и слезы - ведь это тоже жизнь.") # Анна Каренина Лев Толстой