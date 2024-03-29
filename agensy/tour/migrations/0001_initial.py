# Generated by Django 5.0 on 2023-12-19 07:35

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tours',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Название')),
                ('description', models.TextField(verbose_name='Описание')),
                ('price', models.CharField(max_length=100, verbose_name='Цена')),
                ('main_image', models.ImageField(upload_to='tour_photos/', verbose_name='Лицевое изображение')),
            ],
        ),
        migrations.CreateModel(
            name='Photos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='tour/photos/', verbose_name='Изображения тура')),
                ('tour', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='tour.tours', verbose_name='Связан к туру')),
            ],
        ),
    ]
