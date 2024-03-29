# Generated by Django 5.0 on 2023-12-23 05:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tour', '0005_tours_everyday'),
    ]

    operations = [
        migrations.CreateModel(
            name='Booking_tour',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('number', models.CharField(max_length=16)),
                ('ot', models.CharField(max_length=8)),
                ('do', models.CharField(max_length=8)),
                ('checked', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name': 'Бронирование',
                'verbose_name_plural': 'Бронирования',
            },
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(max_length=16)),
                ('message', models.TextField(verbose_name='Сообшение')),
                ('tick', models.BooleanField(default=False, verbose_name='Ответили клиенту: ')),
            ],
        ),
    ]
