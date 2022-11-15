from django.shortcuts import render
from django.views import generic
from book import models

# Create your views here.
def user_login(request):
    if request.method == 'get':
        return render(request, 'home_page/login.html', context={})

class HomePage(generic.TemplateView):
    template_name = 'home_page/home_page.html'
    