from django import forms
from . import models

class AuthorForm(forms.ModelForm):
    class Meta:
        model = models.Author
        fields = ['name', 'cover', 'start_date', 'description']

class SerieForm(forms.ModelForm):
    class Meta:
        model = models.Serie
        fields = ['name', 'description']

class GenreForm(forms.ModelForm):
    class Meta:
        model = models.Genre
        fields = ['name', 'description']

class PublishingForm(forms.ModelForm):
    class Meta:
        model = models.Publishing
        fields = ['name', 'description']

    





    