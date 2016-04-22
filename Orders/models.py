from __future__ import unicode_literals

from City.models import City
from django.contrib.auth.models import User
from django.db import models


class Orders(models.Model):
    city = models.ForeignKey(City, related_name='city')
    user = models.OneToOneField(User)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
