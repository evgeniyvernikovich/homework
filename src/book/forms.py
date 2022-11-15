from django import forms
from . import models

class BookForm(forms.ModelForm):
    class Meta:
        model = models.Book
        fields = ['name', 'cover', 'prise', 'author_book', 'serie_book', 'genre_book', 'year_of_publishing', 'number_of_pages', 'binding_book', 
        'format_book', 'isbn_book', 'weight_book', 'age_restrictions', 'publishing_book', 'number_of_books']