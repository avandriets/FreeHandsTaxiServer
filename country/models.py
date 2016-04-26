from __future__ import unicode_literals
from django.db import models


class Country(models.Model):
    name_eng = models.CharField(max_length=50)
    name_rus = models.CharField(max_length=50)
