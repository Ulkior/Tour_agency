# Generated by Django 5.0 on 2023-12-19 11:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tour', '0002_tours_slug'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='photos',
            options={'verbose_name': 'Изображение', 'verbose_name_plural': 'Изображения'},
        ),
        migrations.AlterModelOptions(
            name='tours',
            options={'verbose_name': 'Тур', 'verbose_name_plural': 'Туры'},
        ),
    ]