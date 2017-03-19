# coding=utf-8
from __future__ import unicode_literals

from Cars.models import AbstractBaseTable
from Orders.models import Orders
from django.db import models
from django.contrib.auth.models import User

# 0 - не выбран
# 1 - выбран


class DriverResponse(AbstractBaseTable):
    order = models.ForeignKey(Orders, null=True, verbose_name='Заказ')
    user = models.ForeignKey(User, null=True, verbose_name='Водитель')
    price = models.DecimalField(verbose_name='Цена', null=True, max_digits=6, decimal_places=2)
