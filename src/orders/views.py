from django.shortcuts import render
from . import models, forms
from book import models as book_models
from django.views.generic import DeleteView, CreateView, TemplateView, ListView
from django.urls import reverse_lazy

# Create your views here.
def show_basket(request):
    context = {}
    context['basket'] = None
    if request.method == "POST":
        book_pk = request.POST.get('book_pk')
        amount = int(request.POST.get('amount'))
        if book_pk and amount:
            basket_id = int(request.session.get('basket_id', 0))
            if request.user.is_authenticated:
                user = request.user
            else:
                user = None
            if basket_id == 0:
                basket_id = None
            basket, created = models.Basket.objects.get_or_create(
                pk = basket_id,
                defaults={'user': user}
            )
            context['basket'] = basket
            if created:
                request.session['basket_id'] = basket.pk
            book = book_models.Book.objects.get(pk=int(book_pk))
            price = book.price
            BookBasket, created = models.BookBasket.objects.get_or_create(
                book=book,
                basket=basket,
                defaults={
                    'amount':amount,
                'price':price
                }
                
            )
            if not created:
                BookBasket.amount += amount
                BookBasket.save()
    else:
        basket_id = request.session.get('basket_id')
        if basket_id:
            basket = models.Basket.objects.get(pk = basket_id)
            context['basket'] = basket
    
    context['form'] = forms.OrderForm

              
    return render(
        request=request,
        template_name='orders/basket_view.html',
        context=context
    )

class DelPosition(DeleteView):
    model= models.BookBasket
    success_url = reverse_lazy('orders:sh-basket')
    template_name = 'orders/del_position.html'

class Order(CreateView):
    template_name = 'orders/create_order.html'
    model = models.Order
    form_class = forms.OrderForm
    success_url = reverse_lazy('orders:order-success')

    def form_valid(self, form):
        basket = models.Basket.objects.get(pk=self.request.session.get('basket_id'))
        form.instance.basket = basket
        return super().form_valid(form)
    
    def get_success_url(self) -> str:
        del self.request.session['basket_id']
        return super().get_success_url()

class OrderSuccsses(TemplateView):
    template_name = 'orders/success_order.html'

class OrderManager(ListView):
    model = models.Order
    template_name = 'orders/list_order.html'

class BasketMeneger(ListView):
    model = models.BookBasket
    template_name = 'orders/book_basket.html'
    