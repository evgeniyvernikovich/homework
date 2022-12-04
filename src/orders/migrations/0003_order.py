# Generated by Django 4.1.2 on 2022-12-04 10:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0002_bookbasket'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('new', 'New order'), ('in_progress', 'In Progress'), ('done', 'Done')], max_length=300, verbose_name='Статус')),
                ('contact_user', models.TextField(verbose_name='Контактная информация')),
                ('created_date', models.DateTimeField(auto_now_add=True, verbose_name='Created date')),
                ('updated_date', models.DateTimeField(auto_now=True, verbose_name='Created date')),
                ('basket', models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, related_name='book', to='orders.basket', verbose_name='Корзина')),
            ],
        ),
    ]
