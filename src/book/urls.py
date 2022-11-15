from django.urls import path
from . import views
app_name = 'book'

urlpatterns = [
    path('show-books-list/', views.ShowBooks.as_view(), name='sh-book-list'),
    path('show-book-create/', views.CreateBook.as_view(), name='sh-book-create'),
    path('show-book-update/<int:pk>/', views.UpdateBook.as_view(), name='sh-book-update'),
    path('show-book-delete/<int:pk>/', views.DeleteBook.as_view(), name='sh-book-delete'),
    path('show-book-detail/<int:pk>/', views.ShowBook.as_view(), name='sh-book-detail'),
]