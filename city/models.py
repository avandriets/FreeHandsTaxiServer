from __future__ import unicode_literals

from Country.models import Country
from django.db import models


class City(models.Model):
    country = models.ForeignKey(Country, related_name='vote')
    name = models.CharField(max_length=100)
