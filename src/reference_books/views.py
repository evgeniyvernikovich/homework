from django.shortcuts import render
from . import models, forms
import datetime
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.urls import reverse_lazy


class CreateAuthor(PermissionRequiredMixin, generic.CreateView):
    model = models.Author
    form_class = forms.AuthorForm
    template_name = 'reference_books/create_update.html'
    login_url = reverse_lazy('login')
    permission_required = 'reference_books.add_author'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['operation_name'] = 'Create'
        return context

class UpdateAuthor(PermissionRequiredMixin, generic.UpdateView):
    model = models.Author
    form_class = forms.AuthorForm
    template_name = 'reference_books/create_update.html'
    login_url = reverse_lazy('login')
    permission_required = 'reference_books.change_author'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['operation_name'] = 'Update'
        return context
   
class DeleteAuthor(PermissionRequiredMixin, generic.DeleteView):
    model = models.Author
    template_name = 'reference_books/delete.html'
    login_url = reverse_lazy('login')
    permission_required = 'reference_books.delete_author'

class ShowAuthor(LoginRequiredMixin, generic.DetailView):
    model = models.Author
    template_name = 'reference_books/detail.html'

class ShowAuthors(PermissionRequiredMixin, generic.ListView):
    model = models.Author
    template_name = 'reference_books/list_author.html'  
    login_url = reverse_lazy('login')
    permission_required = 'reference_books.view_author'

class CreateSerie(PermissionRequiredMixin, generic.CreateView):
    model = models.Serie
    form_class = forms.SerieForm
    template_name = 'reference_books/create_update.html'
    login_url = reverse_lazy('login')
    permission_required = 'reference_books.add_serie'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['operation_name'] = 'Create'
        return context
    
class UpdateSerie(PermissionRequiredMixin, generic.UpdateView):
    model = models.Serie
    form_class = forms.SerieForm
    template_name = 'reference_books/create_update.html'
    login_url = reverse_lazy('login')
    permission_required = 'reference_books.change_serie'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['operation_name'] = 'Update'
        return context

class DeleteSerie(PermissionRequiredMixin, generic.DeleteView):
    model = models.Serie
    template_name = 'reference_books/delete.html'
    login_url = reverse_lazy('login')
    permission_required = 'reference_books.delete_serie'

class ShowSerie(LoginRequiredMixin, generic.DetailView):
    model = models.Serie
    template_name = 'reference_books/detail.html'

class ShowSeries(PermissionRequiredMixin, generic.ListView):
    model = models.Serie
    template_name = 'reference_books/list_serie.html'   
    login_url = reverse_lazy('login')
    permission_required = 'reference_books.view_serie'

class CreateGenre(PermissionRequiredMixin, generic.CreateView):
    model = models.Serie
    form_class = forms.SerieForm
    template_name = 'reference_books/create_update.html'
    login_url = reverse_lazy('login')
    permission_required = 'reference_books.add_genre'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['operation_name'] = 'Create'
        return context
    
class UpdateGenre(PermissionRequiredMixin, generic.UpdateView):
    model = models.Serie
    form_class = forms.SerieForm
    template_name = 'reference_books/create_update.html'
    login_url = reverse_lazy('login')
    permission_required = 'reference_books.change_genre'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['operation_name'] = 'Update'
        return context

class DeleteGenre(PermissionRequiredMixin, generic.DeleteView):
    model = models.Serie
    template_name = 'reference_books/delete.html'
    login_url = reverse_lazy('login')
    permission_required = 'reference_books.delete_genre'

class ShowGenre(LoginRequiredMixin, generic.DetailView):
    model = models.Serie
    template_name = 'reference_books/detail.html'

class ShowGenres(PermissionRequiredMixin, generic.ListView):
    model = models.Serie
    template_name = 'reference_books/list_genre.html' 
    login_url = reverse_lazy('login')
    permission_required = 'reference_books.view_genre'

class CreatePublishing(PermissionRequiredMixin, generic.CreateView):
    model = models.Publishing
    form_class = forms.PublishingForm
    template_name = 'reference_books/create_update.html'
    login_url = reverse_lazy('login')
    permission_required = 'reference_books.add_publishing'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['operation_name'] = 'Create'
        return context
    
class UpdatePublishing(PermissionRequiredMixin, generic.UpdateView):
    model = models.Publishing
    form_class = forms.PublishingForm
    template_name = 'reference_books/create_update.html'
    login_url = reverse_lazy('login')
    permission_required = 'reference_books.change_publishing'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['operation_name'] = 'Update'
        return context

class DeletePublishing(PermissionRequiredMixin, generic.DeleteView):
    model = models.Publishing
    template_name = 'reference_books/delete.html'
    login_url = reverse_lazy('login')
    permission_required = 'reference_books.delete_publishing'

class ShowPublishing(LoginRequiredMixin, generic.DetailView):
    model = models.Publishing
    template_name = 'reference_books/detail.html'

class ShowPublishings(PermissionRequiredMixin, generic.ListView):
    model = models.Publishing
    template_name = 'reference_books/list_publishing.html'
    login_url = reverse_lazy('login')
    permission_required = 'reference_books.view_publishing'
