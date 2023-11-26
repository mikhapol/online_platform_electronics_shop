from django.conf import settings
from django.db import models

from users.models import NULLABLE


class Factory(models.Model):
    title = models.CharField(max_length=150, verbose_name='Название')
    description = models.TextField(verbose_name='Описание')
    link = models.URLField(verbose_name='Ссылка на поставщика')

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='Пользователь',
                             **NULLABLE)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Завод'
        verbose_name_plural = 'Заводы'


class Contacts(models.Model):
    email = models.EmailField(unique=True, verbose_name='Email')
    country = models.CharField(max_length=55, verbose_name='Страна')
    city = models.CharField(max_length=100, verbose_name='Город')
    street = models.CharField(max_length=100, verbose_name='Улица')
    home = models.PositiveSmallIntegerField(verbose_name='Номер дома')

    def __str__(self):
        return f'{self.country}, {self.city} - {self.email}'

    class Meta:
        verbose_name = 'Контакт завода'
        verbose_name_plural = 'Контакты заводов'


class Products(models.Model):
    title = models.CharField(max_length=50, verbose_name='Название')
    model = models.CharField(max_length=20, verbose_name='Модель')
    release = models.DateField(auto_now_add=True, verbose_name='Релиз',
                               help_text='Дата выхода продукта на рынок')

    vender = models.CharField(max_length=50, verbose_name='Поставщик',
                              help_text='Предыдущий по иерархии объект сети')

    debt = models.DecimalField(max_digits=12, decimal_places=2,
                               verbose_name='Задолженность',
                               help_text='Задолженность перед поставщиком в денежном выражении с точностью до копеек')

    creation = models.DateTimeField(auto_now_add=True,
                                    verbose_name='создание',
                                    help_text='Время создания (заполняется автоматически при создании)')
