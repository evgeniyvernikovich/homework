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

    def __repr__(self):
        return self.name

    def get_absolute_url(self):
        return f"/show-authors-list/{self.pk}/"      

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

    def __repr__(self):
        return self.name

    def get_absolute_url(self):
        return f"/show-series-list/{self.pk}/" 

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

    def __repr__(self):
        return self.name

    def get_absolute_url(self):
        return f"/show-genres-list/{self.pk}/"       
        
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

    def __repr__(self):
        return self.name

    def get_absolute_url(self):
        return f"/show-publishing-list/{self.pk}/"  