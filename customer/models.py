# coding=utf-8
from __future__ import unicode_literals
from CarTypes.models import CarTypes
from City.models import City
from django.db import models
from django.contrib.auth.models import User


class Customer(models.Model):
    first_name = models.CharField(max_length=50, verbose_name='Имя', null=False, blank=False, help_text='Имя')
    last_name = models.CharField(max_length=50, verbose_name='Фамилия', null=True, blank=True, help_text='Фамилия')
    car_registration_number = models.CharField(max_length=20, verbose_name='Рег номер автомобиля', null=True, blank=True, help_text='Рег номер автомобиля')
    car_model = models.CharField(max_length=30, verbose_name='Марка аватомобиля', null=False, blank=False, help_text='Марка аватомобиля')
    length = models.FloatField(verbose_name='Длинна', null=True, blank=True, help_text='Длинна м')
    width = models.FloatField(verbose_name='Ширина', null=True, blank=True, help_text='Ширина м')
    height = models.FloatField(verbose_name='Высота', null=True, blank=True, help_text='Высота м')
    volume = models.FloatField(verbose_name='Объем', null=True, blank=True, help_text='Объем м3')
    capacity = models.FloatField(verbose_name='Грузоподъемность', null=True, blank=True, help_text='Грузоподъемность т')
    is_driver = models.SmallIntegerField(verbose_name='Грузоперевозчик', null=False, blank=False, help_text='Грузоперевозчик')
    car_type = models.ForeignKey(CarTypes, verbose_name='Тип тр.', null=False, blank=False, help_text='Тип тр.')
    city = models.ForeignKey(City, verbose_name='Город', null=True, blank=True, help_text='Город')
    user = models.ForeignKey(User, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return u'%s  %s' % (self.first_name, self.last_name)