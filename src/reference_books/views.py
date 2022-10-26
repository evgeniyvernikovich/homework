from django.shortcuts import render
from . import models, forms
from django.http import HttpResponse, HttpResponseRedirect
import datetime
from django.views import generic


class CreateAuthor(generic.CreateView):
    model = models.Author
    form_class = forms.AuthorForm
    template_name = 'reference_books/create.html'

class UpdateAuthor(generic.UpdateView):
    model = models.Author
    form_class = forms.AuthorForm
    template_name = 'reference_books/update.html'

class DeleteAuthor(generic.DeleteView):
    model = models.Author
    template_name = 'reference_books/delete.html'

class ShowAuthor(generic.DetailView):
    model = models.Author
    template_name = 'reference_books/detail.html'

class ShowAuthors(generic.ListView):
    model = models.Author
    template_name = 'reference_books/List.html'   

class CreateSerie(generic.CreateView):
    model = models.Serie
    form_class = forms.SerieForm
    template_name = 'reference_books/create.html'
    
class UpdateSerie(generic.UpdateView):
    model = models.Serie
    form_class = forms.SerieForm
    template_name = 'reference_books/update.html'

class DeleteSerie(generic.DeleteView):
    model = models.Serie
    template_name = 'reference_books/delete.html'

class ShowSerie(generic.DetailView):
    model = models.Serie
    template_name = 'reference_books/detail.html'

class ShowSeries(generic.ListView):
    model = models.Serie
    template_name = 'reference_books/List.html'   

class CreateGenre(generic.CreateView):
    model = models.Serie
    form_class = forms.SerieForm
    template_name = 'reference_books/create.html'
    
class UpdateGenre(generic.UpdateView):
    model = models.Serie
    form_class = forms.SerieForm
    template_name = 'reference_books/update.html'

class DeleteGenre(generic.DeleteView):
    model = models.Serie
    template_name = 'reference_books/delete.html'

class ShowGenre(generic.DetailView):
    model = models.Serie
    template_name = 'reference_books/detail.html'

class ShowGenres(generic.ListView):
    model = models.Serie
    template_name = 'reference_books/List.html' 

class CreatePublishing(generic.CreateView):
    model = models.Publishing
    form_class = forms.PublishingForm
    template_name = 'reference_books/create.html'
    
class UpdatePublishing(generic.UpdateView):
    model = models.Publishing
    form_class = forms.PublishingForm
    template_name = 'reference_books/update.html'

class DeletePublishing(generic.DeleteView):
    model = models.Publishing
    template_name = 'reference_books/delete.html'

class ShowPublishing(generic.DetailView):
    model = models.Publishing
    template_name = 'reference_books/detail.html'

class ShowPublishings(generic.ListView):
    model = models.Publishing
    template_name = 'reference_books/List.html'
