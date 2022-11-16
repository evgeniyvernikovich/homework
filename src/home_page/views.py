from django.shortcuts import render
from django.views import generic
from book import models

# Create your views here.
def user_login(request):
    if request.method == 'get':
        return render(request, 'home_page/login.html', context={})

class HomePage(generic.TemplateView):
    template_name = 'home_page/home_page.html'
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['book1'] = 'Create'
        return context
    