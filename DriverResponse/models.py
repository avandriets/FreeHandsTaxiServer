# coding=utf-8
from __future__ import unicode_literals

from Orders.models import Orders
from django.db import models
from django.contrib.auth.models import User

# 0 - не выбран
# 1 - выбран



class DriverResponse(models.Model):
    order = models.ForeignKey(Orders, null=True, verbose_name='Заказ')
    user = models.ForeignKey(User, null=True, verbose_name='Водитель')
    price = models.DecimalField(verbose_name='Цена', null=True, max_digits=6, decimal_places=2)
    status = models.SmallIntegerField(default=0, verbose_name='Статус', null=False, blank=False, help_text='Статус отклика')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
