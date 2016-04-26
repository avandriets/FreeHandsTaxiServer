from __future__ import unicode_literals

from django.contrib.auth.models import User
from django.db import models
from django.dispatch import receiver
from gcm.models import AbstractDevice
from gcm.signals import device_registered


class MyDevice(AbstractDevice):
    user = models.ForeignKey(User, null=True)

    @receiver(device_registered)
    def add_score(sender, **kwargs):
        #post = kwargs.get("post")
        print "Prived mifved"
        pass
