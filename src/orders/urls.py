from django.urls import path
from . import views
app_name = 'orders'

urlpatterns = [
    path('basket/', views.show_basket, name='sh-basket'),
    path('del-position/<int:pk>/', views.DelPosition.as_view(), name='del-position'),
    path('create-order/', views.Order.as_view(), name='create-order'),
    path('success/', views.OrderSuccsses.as_view(), name='order-success'),
    path('list-order/', views.OrderManager.as_view(), name='list-order'),
    path('book-basket/', views.BasketMeneger.as_view(), name='book-basket'),

]