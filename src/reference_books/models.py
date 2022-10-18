from tabnanny import verbose
from django.db import models
from django.forms import CharField

# Create your models here.
class Author(models.Model):
    name = models.CharField(
        max_length=50,
        verbose_name='Авторы книг')

    def __str__(self):
        return self.name    

class Serie(models.Model):
    name = models.CharField(
        max_length=30,
        verbose_name='Серия')

    def __str__(self):
        return self.name

class Genre(models.Model):
    name = models.CharField(
        max_length=30,
        verbose_name='Жанр')

    def __str__(self):
        return self.name   
        
class Publishing(models.Model):
    name = models.CharField(
        max_length=100,
        verbose_name='Издателсьвто')

    def __str__(self):
        return self.name   