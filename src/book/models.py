from django.db import models
from django.urls import reverse_lazy
from reference_books.models import Author, Genre, Serie, Publishing 



# Create your models here.
class Book(models.Model):
    name = models.CharField(
        max_length=35,
        verbose_name='Название книги')

    cover = models.ImageField(
        verbose_name='Фото обложки книги',
        upload_to = 'covers/%Y/%m/%d/'
    )
    price = models.DecimalField(
        verbose_name='Стоимость книги',
        max_digits=5,
        decimal_places=2)
    author_book = models.ManyToManyField(Author, related_name="author_books", verbose_name='Автор(ы) книги')
    serie_book = models.ForeignKey(Serie, on_delete = models.CASCADE, verbose_name="Серия книги")
    genre_book = models.ManyToManyField(Genre, related_name="genre_books", verbose_name='Жанр(ы) книги')
    year_of_publishing = models.DateField(verbose_name='Год издания')
    number_of_pages= models.PositiveSmallIntegerField(verbose_name='Количество страниц')
    binding_book = models.CharField(max_length=60, verbose_name='Переплет')
    format_book = models.CharField(max_length=60, verbose_name='Формат')
    isbn_book = models.CharField(max_length=30, verbose_name='ISBN')
    weight_book = models.PositiveSmallIntegerField(verbose_name='Вес книги')
    age_restrictions = models.PositiveSmallIntegerField(verbose_name='Возрастные ограничения')
    publishing_book = models.ForeignKey(Publishing, on_delete = models.CASCADE, verbose_name="Издательство книги")
    number_of_books = models.PositiveSmallIntegerField(verbose_name='Количество книг')
    date_creation = models.DateField(auto_now_add=True, verbose_name='Дата внесения в каталог')
    date_change = models.DateField(auto_now=True, verbose_name='Дата последнего изменения')

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name

    def get_absolute_url(self):
        # return f"/show-authors-list/{self.pk}/"  
        return reverse_lazy('books:sh-book-detail', kwargs={'pk':self.pk})    
