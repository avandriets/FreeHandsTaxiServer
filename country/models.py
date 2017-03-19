from __future__ import unicode_literals

from Cars.models import AbstractBaseTable
from django.db import models


class Country(AbstractBaseTable):
    name_eng = models.CharField(max_length=50)
    name_rus = models.CharField(max_length=50)

    def __unicode__(self):
        return u'%s' % (self.name_rus)
