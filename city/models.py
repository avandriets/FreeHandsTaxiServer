from __future__ import unicode_literals

from Cars.models import AbstractBaseTable
from Country.models import Country
from django.db import models


class City(AbstractBaseTable):
    country = models.ForeignKey(Country, related_name='vote')
    name = models.CharField(max_length=100)

    def __unicode__(self):
        return u'%s' % (self.name)
