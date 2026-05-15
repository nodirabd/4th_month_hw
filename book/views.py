from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from . import models
from django.core.paginator import Paginator
from django.db.models import F

def book_list_view(request):
    if request.method == 'GET':
        query = request.GET.get('s', '')
        query_book = models.Book.objects.all().order_by('-id')

        if query:
            query_book = query_book.filter(title__icontains=query)

        paginator = Paginator(query_book, 2)
        page = request.GET.get('page')
        page_obj = paginator.get_page(page)

        return render(request, 'book_list.html', {
            'books': page_obj,
            'query': query,
        })

def book_detail_view(request, id):
    if request.method == 'GET':
        book_id = get_object_or_404(models.Book, id=id)

        viewed_books = request.session.get('viewed_books', [])

        if id not in viewed_books:
            book_id.views = F('views') + 1
            book_id.save()
            book_id.refresh_from_db()

        viewed_books.append(id)
        request.session['viewed_books'] = viewed_books

        return render(request, 'book_detail.html', {'book': book_id})

def citation1(request):
    return HttpResponse("Ведь все взрослы были детьми, только мало кто из них об этом помнит.")

def citation2(request):
    return HttpResponse("Все приходит во время для того кто умеет ждать.")

def citation3(request):
    return HttpResponse("Муки и слезы - ведь это тоже жизнь.")