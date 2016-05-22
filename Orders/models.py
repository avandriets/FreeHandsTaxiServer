# coding=utf-8
from __future__ import unicode_literals

from CarTypes.models import CarTypes
from City.models import City
from django.contrib.auth.models import User
from django.db import models


# status
# 0 - Перевозчик не выбран
# 1 - Перевозчик выбран
# 2 - Успешно завершен
# 3 - Отменен

class Orders(models.Model):
    city = models.ForeignKey(City)
    car_type = models.ForeignKey(CarTypes, verbose_name='Тип тр.', null=True, blank=True, help_text='Тип тр.')
    order_date = models.DateTimeField(verbose_name='Дата заказа', null=True, blank=True)
    from_address = models.CharField(verbose_name='Откуда', max_length=50, null=True, blank=True)
    to_address = models.CharField(verbose_name='Куда', max_length=50, null=True, blank=True)
    from_latitude = models.FloatField(verbose_name='Откуда широта', null=True, blank=True, help_text='Адрес откуда широта')
    from_longitude = models.FloatField(verbose_name='Откуда долгота', null=True, blank=True, help_text='Адрес откуда долгота')
    to_latitude = models.FloatField(verbose_name='Куда широта', null=True, blank=True, help_text='Адрес куда широта')
    to_longitude = models.FloatField(verbose_name='Куда долгота', null=True, blank=True, help_text='Адрес куда долгота')
    description = models.CharField(verbose_name='Описание', max_length=50, null=True)
    price = models.DecimalField(verbose_name='Цена', null=True, max_digits=6, decimal_places=2)
    driver = models.ForeignKey(User, null=True, verbose_name='Водитель', related_name='driver')
    user = models.ForeignKey(User, null=True, related_name='owner')
    status = models.SmallIntegerField(default=0, verbose_name='Статус', null=False, blank=False, help_text='Статус заказа')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
