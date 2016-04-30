from __future__ import unicode_literals
from django.db import models


class Country(models.Model):
    name_eng = models.CharField(max_length=50)
    name_rus = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    def __unicode__(self):
        return u'%s' % (self.name_rus)