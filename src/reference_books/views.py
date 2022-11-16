from django.shortcuts import render
from . import models, forms
from django.http import HttpResponse, HttpResponseRedirect
import datetime
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy


class CreateAuthor(LoginRequiredMixin, generic.CreateView):
    model = models.Author
    form_class = forms.AuthorForm
    template_name = 'reference_books/create_update.html'
    login_url = reverse_lazy('login')

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['operation_name'] = 'Create'
        return context

class UpdateAuthor(LoginRequiredMixin, generic.UpdateView):
    model = models.Author
    form_class = forms.AuthorForm
    template_name = 'reference_books/create_update.html'
    login_url = reverse_lazy('login')

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['operation_name'] = 'Update'
        return context
   
class DeleteAuthor(LoginRequiredMixin, generic.DeleteView):
    model = models.Author
    template_name = 'reference_books/delete.html'
    login_url = reverse_lazy('login')

class ShowAuthor(generic.DetailView):
    model = models.Author
    template_name = 'reference_books/detail.html'

class ShowAuthors(LoginRequiredMixin, generic.ListView):
    model = models.Author
    template_name = 'reference_books/list_author.html'  
    login_url = reverse_lazy('login')

class CreateSerie(LoginRequiredMixin, generic.CreateView):
    model = models.Serie
    form_class = forms.SerieForm
    template_name = 'reference_books/create_update.html'
    login_url = reverse_lazy('login')

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['operation_name'] = 'Create'
        return context
    
class UpdateSerie(LoginRequiredMixin, generic.UpdateView):
    model = models.Serie
    form_class = forms.SerieForm
    template_name = 'reference_books/create_update.html'
    login_url = reverse_lazy('login')

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['operation_name'] = 'Update'
        return context

class DeleteSerie(LoginRequiredMixin, generic.DeleteView):
    model = models.Serie
    template_name = 'reference_books/delete.html'
    login_url = reverse_lazy('login')

class ShowSerie(generic.DetailView):
    model = models.Serie
    template_name = 'reference_books/detail.html'

class ShowSeries(LoginRequiredMixin, generic.ListView):
    model = models.Serie
    template_name = 'reference_books/list_serie.html'   
    login_url = reverse_lazy('login')

class CreateGenre(LoginRequiredMixin, generic.CreateView):
    model = models.Serie
    form_class = forms.SerieForm
    template_name = 'reference_books/create_update.html'
    login_url = reverse_lazy('login')

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['operation_name'] = 'Create'
        return context
    
class UpdateGenre(LoginRequiredMixin, generic.UpdateView):
    model = models.Serie
    form_class = forms.SerieForm
    template_name = 'reference_books/create_update.html'
    login_url = reverse_lazy('login')

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['operation_name'] = 'Update'
        return context

class DeleteGenre(LoginRequiredMixin, generic.DeleteView):
    model = models.Serie
    template_name = 'reference_books/delete.html'
    login_url = reverse_lazy('login')

class ShowGenre(generic.DetailView):
    model = models.Serie
    template_name = 'reference_books/detail.html'

class ShowGenres(LoginRequiredMixin, generic.ListView):
    model = models.Serie
    template_name = 'reference_books/list_genre.html' 
    login_url = reverse_lazy('login')

class CreatePublishing(LoginRequiredMixin, generic.CreateView):
    model = models.Publishing
    form_class = forms.PublishingForm
    template_name = 'reference_books/create_update.html'
    login_url = reverse_lazy('login')

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['operation_name'] = 'Create'
        return context
    
class UpdatePublishing(LoginRequiredMixin, generic.UpdateView):
    model = models.Publishing
    form_class = forms.PublishingForm
    template_name = 'reference_books/create_update.html'
    login_url = reverse_lazy('login')

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['operation_name'] = 'Update'
        return context

class DeletePublishing(LoginRequiredMixin, generic.DeleteView):
    model = models.Publishing
    template_name = 'reference_books/delete.html'
    login_url = reverse_lazy('login')

class ShowPublishing(generic.DetailView):
    model = models.Publishing
    template_name = 'reference_books/detail.html'

class ShowPublishings(LoginRequiredMixin, generic.ListView):
    model = models.Publishing
    template_name = 'reference_books/list_publishing.html'
    login_url = reverse_lazy('login')
