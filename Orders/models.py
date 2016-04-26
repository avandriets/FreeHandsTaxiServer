from __future__ import unicode_literals

from City.models import City
from django.contrib.auth.models import User
from django.db import models


class Orders(models.Model):
    city = models.ForeignKey(City)
    user = models.ForeignKey(User, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
