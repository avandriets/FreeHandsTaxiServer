from __future__ import unicode_literals

import oauth2_provider
from django.contrib.auth.models import User
from django.db import models
from django.dispatch import receiver
from gcm.models import AbstractDevice
from gcm.signals import device_registered
from django.conf import settings
from oauthlib.oauth2 import BearerToken
from re import sub
from django.contrib.auth.decorators import login_required


class MyDevice(AbstractDevice):
    user = models.ForeignKey('auth.User', null=True)

    @login_required()
    @receiver(device_registered)
    def add_score(sender, **kwargs):

        header_token = kwargs['request'].META.get('HTTP_AUTHORIZATION', None)
        if header_token is not None:
            try:
                token_obj = oauth2_provider.models.AccessToken.objects.get(token=header_token[7:])
                kwargs['request'].user = token_obj.user
            except token_obj.DoesNotExist:
                pass
                # This is now the correct user
        print (kwargs['request'].user)

        device = sender.object
        user = kwargs['request'].user
        device.user = user
        device.save()
        pass
