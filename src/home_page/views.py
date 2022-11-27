from django.shortcuts import render
from django.views import generic
from book import models

# Create your views here.

class HomePage(generic.TemplateView):
    template_name = 'home_page/home_page.html'
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['book1'] = models.Book.objects.get(pk=1)
        context['book2'] = models.Book.objects.get(pk=2)
        context['book3'] = models.Book.objects.get(pk=3)
        context['book4'] = models.Book.objects.get(pk=6)
        return context
    