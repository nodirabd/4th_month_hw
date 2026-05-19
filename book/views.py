from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from . import models
from django.core.paginator import Paginator
from django.db.models import F
from django.views import generic
"""
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
"""
class BookListView(generic.ListView):
    template_name = 'book_list.html'
    model = models.Book
    paginate_by = 2

    def get_queryset(self):
        queryset = self.model.objects.all().order_by('-id')
        query = self.request.GET.get('s', '')
        if query:
            queryset = queryset.filter(title__icontains=query)
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['books'] = context['page_obj']
        context['query'] = self.request.GET.get('s', '')
        return context

"""     
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

        return render(request, 'book_detail.html', {'book': book_id})"""

class BookDetailView(generic.DetailView):
    template_name = 'book_detail.html'
    context_object_name = 'book'
    pk_url_kwarg = 'id'
    model = models.Book

    def get_object(self, queryset=None):
        obj = super().get_object(queryset)
        request = self.request
        viewed_books = request.session.get('viewed_books', [])

        if obj.pk not in viewed_books:
            self.model.objects.filter(pk=obj.pk).update(views=F('views') + 1)
            viewed_books.append(obj.pk)
            request.session['viewed_books'] = viewed_books
            obj.refresh_from_db()
        return obj
"""     
def citation1(request):
    return HttpResponse("Ведь все взрослы были детьми, только мало кто из них об этом помнит.")


def citation2(request):
    return HttpResponse("Все приходит во время для того кто умеет ждать.")

def citation3(request):
    return HttpResponse("Муки и слезы - ведь это тоже жизнь.")"""
class Citation1View(generic.View):
    def get(self, request):
        return HttpResponse("Ведь все взрослы были детьми, только мало кто из них об этом помнит.")

class Citation2View(generic.View):
    def get(self, request):
        return HttpResponse("Все приходит во время для того кто умеет ждать.")

class Citation3View(generic.View):
    def get(self, request):
        return HttpResponse("Муки и слезы - ведь это тоже жизнь.")