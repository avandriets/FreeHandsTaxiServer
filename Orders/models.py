# coding=utf-8
from __future__ import unicode_literals

from Cars.models import AbstractBaseTable
from City.models import City
from Dispatch.models import Dispatch
from django.contrib.auth.models import User
from django.db import models


# status
# 0 - Перевозчик не выбран
# 1 - Перевозчик выбран
# 2 - Успешно завершен
# 3 - Отменен


class Tariffs(AbstractBaseTable):
    name = models.CharField(max_length=20, verbose_name='Тариф', null=True, blank=True, help_text='Тариф')


class Street(AbstractBaseTable):
    name = models.CharField(max_length=20, verbose_name='Наименование', null=True, blank=True, help_text='Наименование')
    city = models.ForeignKey(City, null=True, blank=True, verbose_name='Город', help_text='Город')


class OrderState(AbstractBaseTable):
    name = models.CharField(max_length=20, verbose_name='Описание состояния', null=True, blank=True, help_text='Описание состояния')


class Orders(AbstractBaseTable):
    dispatch = models.ForeignKey(Dispatch, null=True, blank=True, verbose_name='Диспетчерская', help_text='Диспетчерская в привязке к городу')
    order_date = models.DateTimeField(verbose_name='Дата заказа', null=True, blank=True)
    datetime_from = models.DateTimeField(verbose_name='Дата время подачи', null=True, blank=True, help_text='Дата время подачи')
    minute_from = models.SmallIntegerField(default=0, verbose_name=' Через сколько минут выполнить заказ', null=True, blank=True, help_text=' Через сколько минут выполнить заказ');
    state_order = models.ForeignKey(OrderState, verbose_name='Дата время подачи', null=True, blank=True, help_text='Дата время подачи')

    from_street = models.ForeignKey(Street, verbose_name='Улица', null=True, blank=True, help_text='Улица откуда', related_name='from_street')
    from_house_number = models.CharField(verbose_name='Номер дома', max_length=50, null=True, blank=True)
    from_building = models.CharField(verbose_name='Строение', max_length=50, null=True, blank=True)
    from_entrance = models.CharField(verbose_name='Подъезд', max_length=50, null=True, blank=True)

    to_street = models.ForeignKey(Street, verbose_name='Улица', null=True, blank=True, help_text='Улица куда', related_name='to_street')
    to_house_number = models.CharField(verbose_name='Номер дома', max_length=50, null=True, blank=True)
    to_building = models.CharField(verbose_name='Строение', max_length=50, null=True, blank=True)
    to_entrance = models.CharField(verbose_name='Подъезд', max_length=50, null=True, blank=True)

    from_latitude = models.FloatField(verbose_name='Откуда широта', null=True, blank=True, help_text='Адрес откуда широта')
    from_longitude = models.FloatField(verbose_name='Откуда долгота', null=True, blank=True, help_text='Адрес откуда долгота')
    to_latitude = models.FloatField(verbose_name='Куда широта', null=True, blank=True, help_text='Адрес куда широта')
    to_longitude = models.FloatField(verbose_name='Куда долгота', null=True, blank=True, help_text='Адрес куда долгота')
    description = models.CharField(verbose_name='Описание', max_length=50, null=True)

    tariffs = models.ForeignKey(Tariffs, verbose_name='Тариф', null=True, blank=True, help_text='Тариф')
    cost = models.DecimalField(verbose_name='Цена', null=True, max_digits=6, decimal_places=2)
    user = models.ForeignKey(User, null=True, related_name='owner')
