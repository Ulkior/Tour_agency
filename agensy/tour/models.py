from django.db import models



class Tours(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название')
    slug = models.SlugField(unique=True, null=True)
    description = models.TextField(verbose_name='Описание')
    price = models.CharField(max_length=100, verbose_name='Цена')
    main_image = models.ImageField(upload_to='tour_photos/', verbose_name='Лицевое изображение')
    days = models.IntegerField(default=0, verbose_name='На сколько дней расчитан тур')
    everyday = models.CharField(default='Сумма не выбрана', max_length=100, verbose_name='Дневная оплата')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Тур'
        verbose_name_plural = 'Туры'

class Photos(models.Model):
    image = models.ImageField(upload_to='tour/photos/', verbose_name='Изображения тура')
    tour = models.ForeignKey(Tours, on_delete=models.CASCADE, verbose_name='Связан к туру', related_name='images')

    def __str__(self):
        return f"{self.tour.name}"

    class Meta:
        verbose_name = 'Изображение'
        verbose_name_plural = 'Изображения'



class Booking_tour(models.Model):
    name = models.CharField(max_length=100)
    number = models.CharField(max_length=16)
    ot = models.CharField(max_length=8)
    do = models.CharField(max_length=8)
    checked = models.BooleanField(default=False)


    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Бронирование'
        verbose_name_plural = 'Бронирования'



class Contact(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=16)
    message = models.TextField(verbose_name='Сообшение')
    tick = models.BooleanField(default=False, verbose_name='Ответили клиенту: ')
