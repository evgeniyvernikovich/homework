# Generated by Django 4.1.2 on 2022-12-10 07:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0003_order'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='adress_user',
            field=models.TextField(default=1, verbose_name='Адрес'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='order',
            name='email_user',
            field=models.EmailField(default=1, max_length=40, verbose_name='Электронная почта'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='order',
            name='name_user',
            field=models.CharField(default=1, max_length=50, verbose_name='Имя пользвователя'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='order',
            name='phone_user',
            field=models.CharField(default=1, max_length=20, verbose_name='Телефон пользвователя'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='order',
            name='surname_user',
            field=models.CharField(default=1, max_length=50, verbose_name='Фамилия пользвователя'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('new', 'New order'), ('in_progress', 'In Progress'), ('done', 'Done')], default='new', max_length=300, verbose_name='Статус'),
        ),
    ]