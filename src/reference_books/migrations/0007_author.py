# Generated by Django 4.1.2 on 2022-10-23 14:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reference_books', '0006_delete_author'),
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Авторы книг')),
                ('start_date', models.DateField()),
                ('description', models.TextField(blank=True, null=True)),
            ],
        ),
    ]