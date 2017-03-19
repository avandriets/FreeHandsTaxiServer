# coding=utf-8
from __future__ import unicode_literals

from Cars.models import AbstractBaseTable
from City.models import City
from django.db import models


class Dispatch(AbstractBaseTable):
    name = models.CharField(max_length=30)
    city = models.ForeignKey(City, verbose_name='Город', null=True, blank=True, help_text='Город')
