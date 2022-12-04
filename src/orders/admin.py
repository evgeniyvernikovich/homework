from django.contrib import admin

# Register your models here.
from . import models
class BasketAdmin(admin.ModelAdmin):
    list_display = ('pk', 'user')
class BookBasketAdmin(admin.ModelAdmin):
    list_display = ('pk', 'book', 'basket', 'amount', 'price', 'created_date', 'updated_date')
class OrderAdmin(admin.ModelAdmin):
    list_display = ('pk', 'status', 'basket', 'contact_user', 'created_date', 'updated_date')

admin.site.register(models.Order, OrderAdmin)
admin.site.register(models.BookBasket, BookBasketAdmin)
admin.site.register(models.Basket, BasketAdmin)
