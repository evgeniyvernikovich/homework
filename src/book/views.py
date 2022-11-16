from django.shortcuts import render
from . import models, forms
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy

# Create your views here.
class CreateBook(LoginRequiredMixin, generic.CreateView):
    model = models.Book
    form_class = forms.BookForm
    template_name = 'book/create_update.html'
    login_url = reverse_lazy('login')

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['operation_name'] = 'Create'
        return context

class UpdateBook(LoginRequiredMixin, generic.UpdateView):
    model = models.Book
    form_class = forms.BookForm
    template_name = 'book/create_update.html'
    login_url = reverse_lazy('login')

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['operation_name'] = 'Update'
        return context
   
class DeleteBook(LoginRequiredMixin ,generic.DeleteView):
    model = models.Book
    template_name = 'book/delete.html'
    login_url = reverse_lazy('login')

class ShowBook(generic.DetailView):
    model = models.Book
    template_name = 'book/detail.html'

class ShowBooks(LoginRequiredMixin, generic.ListView):
    model = models.Book
    template_name = 'book/list_book.html' 
    login_url = reverse_lazy('login')