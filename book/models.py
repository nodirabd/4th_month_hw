from django.db import models


class Book(models.Model):
    author = models.CharField(max_length=50, verbose_name='напишите имя автора')
    title = models.CharField(max_length=50, verbose_name='напишите назвнание книги')
    age_limit = models.PositiveIntegerField(verbose_name="Возрастное ограничение", default=0)
    description = models.TextField(verbose_name='напишите краткое описание', blank=True)
    release_date = models.DateField(verbose_name='укажите дату публикации')
    image = models.ImageField(upload_to='book/', verbose_name='загрузите обложку книги')
    book_file = models.FileField(upload_to='book/', verbose_name='загрузите pdf файл')
    TYPE_BOOK = (
        ("художественная литература", "художественная литература"),
        ("бизнес", "бизнес"),
        ("Медицина", "Медицина"),
        ("программирование", "программирование"),
        ("Саморазвитие", "Саморазвитие"),
        ("детская литература", "детская литература"),
        ("классика", "классика"),
        ("психология", "психология"),
    )
    quantity = models.PositiveIntegerField(verbose_name='укажите количество страниц', default=20, null=True)
    type_book = models.CharField(max_length=100, choices= TYPE_BOOK, default='классика')
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.title
# Create your models here.
