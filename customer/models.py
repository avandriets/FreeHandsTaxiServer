from __future__ import unicode_literals

from CarTypes.models import CarTypes
from City.models import City
from django.db import models
from django.contrib.auth.models import User


class Customer(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    is_driver = models.SmallIntegerField
    car_type = models.ForeignKey(CarTypes, related_name='car_type')
    city = models.ForeignKey(City, related_name='city')
    user = models.OneToOneField(User)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
