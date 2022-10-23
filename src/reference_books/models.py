from django.db import models

# Create your models here.
class Author(models.Model):
    name = models.CharField(
        max_length=50,
        verbose_name='Авторы книг')
    start_date = models.DateField(verbose_name='Дата записи')
    description = models.TextField(verbose_name='Описание',
        blank=True,
        null=True
    )

    def __str__(self):
        return self.name    

class Serie(models.Model):
    name = models.CharField(
        max_length=80,
        verbose_name='Серия')
    description = models.TextField(verbose_name='Описание',
        blank=True,
        null=True
    )

    def __str__(self):
        return self.name

class Genre(models.Model):
    name = models.CharField(
        max_length=50,
        verbose_name='Жанр')
    description = models.TextField(verbose_name='Описание',
        blank=True,
        null=True
    )

    def __str__(self):
        return self.name   
        
class Publishing(models.Model):
    name = models.CharField(
        max_length=100,
        verbose_name='Издателсьвто')
    description = models.TextField(verbose_name='Описание',
        blank=True,
        null=True
    )

    def __str__(self):
        return self.name   