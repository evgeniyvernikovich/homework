from django.shortcuts import render
from . import models, forms
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.urls import reverse_lazy

# Create your views here.

class CreateBook(PermissionRequiredMixin, generic.CreateView):
    model = models.Book
    form_class = forms.BookForm
    template_name = 'book/create_update.html'
    login_url = reverse_lazy('login')
    permission_required = 'book.add_book'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['operation_name'] = 'Create'   
        return context

class UpdateBook(PermissionRequiredMixin, generic.UpdateView):
    model = models.Book
    form_class = forms.BookForm
    template_name = 'book/create_update.html'
    login_url = reverse_lazy('login')
    permission_required = 'book.change_book'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['operation_name'] = 'Update'
        return context
   
class DeleteBook(PermissionRequiredMixin ,generic.DeleteView):
    model = models.Book
    template_name = 'book/delete.html'
    login_url = reverse_lazy('login')
    permission_required = 'book.delete_book'

class ShowBook(generic.DetailView):
    model = models.Book
    template_name = 'book/detail.html'

class ShowBooks(generic.ListView):
    model = models.Book
    template_name = 'book/list_book.html' 
    

