from django.shortcuts import render
from . import models, forms
from django.views import generic

# Create your views here.
class CreateBook(generic.CreateView):
    model = models.Book
    form_class = forms.BookForm
    template_name = 'book/create_update.html'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['operation_name'] = 'Create'
        return context

class UpdateBook(generic.UpdateView):
    model = models.Book
    form_class = forms.BookForm
    template_name = 'book/create_update.html'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['operation_name'] = 'Update'
        return context
   
class DeleteBook(generic.DeleteView):
    model = models.Book
    template_name = 'book/delete.html'

class ShowBook(generic.DetailView):
    model = models.Book
    template_name = 'book/detail.html'

class ShowBooks(generic.ListView):
    model = models.Book
    template_name = 'book/list_book.html' 