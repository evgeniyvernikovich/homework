from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()
statuses = (
    ('new', 'New order'),
    ('in_progress', 'In Progress'),
    ('done', 'Done'),
)

# Create your models here.

class Basket(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.PROTECT,
        related_name='baskets',
        verbose_name='Корзина',
        null=True,
        blank=True
    )
    def total_price(self):
        all_books = self.books.all()
        total_price = 0
        for book_position in all_books:
            total_price += book_position.price_total
        return total_price

class BookBasket(models.Model):
    book = models.ForeignKey(
        'book.Book',
        on_delete=models.PROTECT,
        verbose_name='Книги в корзине'
        )
    basket = models.ForeignKey(
        'orders.Basket',
        verbose_name='Корзина',
        related_name='books',
        on_delete=models.CASCADE
    )
    amount = models.IntegerField(
        verbose_name='Количество',
        default=1
    )
    price = models.DecimalField(
        "Price",
        max_digits=5,
        decimal_places=2
    )
    created_date = models.DateTimeField(
        'Created date',
        auto_now=False,
        auto_now_add=True
    ) 
    updated_date = models.DateTimeField(
        'Created date',
        auto_now=True,
        auto_now_add=False
    ) 
    @property
    def price_total(self):
        return self.price * self.amount
        
class Order(models.Model):
    status = models.CharField(
        verbose_name="Статус",
        max_length=300,
        choices=statuses,
        default='new'
    )
    basket = models.OneToOneField(
        'orders.Basket',
        verbose_name='Корзина',
        related_name='book',
        on_delete=models.PROTECT
    )
    contact_user = models.TextField(
        verbose_name="Дополнительная информация"
    )
    name_user = models.CharField(
        max_length=50,
        verbose_name='Имя пользвователя'
    )
    surname_user = models.CharField(
        max_length=50,
        verbose_name='Фамилия пользвователя'
    )
    email_user = models.EmailField(
        max_length=40,
        verbose_name = "Электронная почта"
    )
    phone_user = models.CharField(
        max_length=20,
        verbose_name='Телефон пользвователя'
    )
    adress_user = models.CharField(
        max_length=200,
        verbose_name="Адрес"
    )

    created_date = models.DateTimeField(
        'Created date',
        auto_now=False,
        auto_now_add=True
    ) 
    updated_date = models.DateTimeField(
        'Created date',
        auto_now=True,
        auto_now_add=False
    )  