from django.shortcuts import render
from . import models, forms
from django.http import HttpResponse, HttpResponseRedirect
import datetime
from django.views import generic


class CreateAuthor(generic.CreateView):
    model = models.Author
    form_class = forms.AuthorForm
    template_name = 'reference_books/create_update.html'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['operation_name'] = 'Create'
        return context

class UpdateAuthor(generic.UpdateView):
    model = models.Author
    form_class = forms.AuthorForm
    template_name = 'reference_books/create_update.html'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['operation_name'] = 'Update'
        return context
   
class DeleteAuthor(generic.DeleteView):
    model = models.Author
    template_name = 'reference_books/delete.html'

class ShowAuthor(generic.DetailView):
    model = models.Author
    template_name = 'reference_books/detail.html'

class ShowAuthors(generic.ListView):
    model = models.Author
    template_name = 'reference_books/list_author.html'  

class CreateSerie(generic.CreateView):
    model = models.Serie
    form_class = forms.SerieForm
    template_name = 'reference_books/create_update.html'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['operation_name'] = 'Create'
        return context
    
class UpdateSerie(generic.UpdateView):
    model = models.Serie
    form_class = forms.SerieForm
    template_name = 'reference_books/create_update.html'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['operation_name'] = 'Update'
        return context

class DeleteSerie(generic.DeleteView):
    model = models.Serie
    template_name = 'reference_books/delete.html'

class ShowSerie(generic.DetailView):
    model = models.Serie
    template_name = 'reference_books/detail.html'

class ShowSeries(generic.ListView):
    model = models.Serie
    template_name = 'reference_books/list_serie.html'   

class CreateGenre(generic.CreateView):
    model = models.Serie
    form_class = forms.SerieForm
    template_name = 'reference_books/create_update.html'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['operation_name'] = 'Create'
        return context
    
class UpdateGenre(generic.UpdateView):
    model = models.Serie
    form_class = forms.SerieForm
    template_name = 'reference_books/create_update.html'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['operation_name'] = 'Update'
        return context

class DeleteGenre(generic.DeleteView):
    model = models.Serie
    template_name = 'reference_books/delete.html'

class ShowGenre(generic.DetailView):
    model = models.Serie
    template_name = 'reference_books/detail.html'

class ShowGenres(generic.ListView):
    model = models.Serie
    template_name = 'reference_books/list_genre.html' 

class CreatePublishing(generic.CreateView):
    model = models.Publishing
    form_class = forms.PublishingForm
    template_name = 'reference_books/create_update.html'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['operation_name'] = 'Create'
        return context
    
class UpdatePublishing(generic.UpdateView):
    model = models.Publishing
    form_class = forms.PublishingForm
    template_name = 'reference_books/create_update.html'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['operation_name'] = 'Update'
        return context

class DeletePublishing(generic.DeleteView):
    model = models.Publishing
    template_name = 'reference_books/delete.html'

class ShowPublishing(generic.DetailView):
    model = models.Publishing
    template_name = 'reference_books/detail.html'

class ShowPublishings(generic.ListView):
    model = models.Publishing
    template_name = 'reference_books/list_publishing.html'
