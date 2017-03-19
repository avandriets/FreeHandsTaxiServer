# coding=utf-8
from __future__ import unicode_literals

from Cars.models import AbstractBaseTable, PhotoType
from City.models import City
from Dispatch.models import Dispatch
from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save


# gender 1-мужской 0-женский


class Customer(AbstractBaseTable):
    first_name = models.CharField(max_length=50, verbose_name='Имя', null=False, blank=False, help_text='Имя')
    middle_name = models.CharField(max_length=50, verbose_name='Отчество', null=False, blank=False, help_text='Отчество')
    last_name = models.CharField(max_length=50, verbose_name='Фамилия', null=True, blank=True, help_text='Фамилия')
    birth_date = models.DateTimeField(verbose_name='День рождения', null=True, blank=True, help_text='День рождения')
    phone_number = models.CharField(max_length=20, verbose_name='Номер телефона', null=True, blank=True, help_text='Номер телефона')
    gender = models.SmallIntegerField(verbose_name='Пол', null=False, blank=False, help_text='Пол 1-мужской 0-женский', default=1)
    document_number = models.CharField(max_length=20, verbose_name='Номер документа', null=True, blank=True, help_text='Номер документа удостоверяющего личность')
    driver_licence_number = models.CharField(max_length=20, verbose_name='Номер водительского удостоверения', null=True, blank=True, help_text='Номер водительского удостоверения')
    driver_licence_date = models.DateTimeField(verbose_name='Дата выдачи водительского удостоверения', null=True, blank=True, help_text='Дата выдачи водительского удостоверения')
    is_driver = models.SmallIntegerField(verbose_name='Грузоперевозчик', null=False, blank=False, help_text='Водитель - 1, 0 - пассажир')
    status = models.SmallIntegerField(verbose_name='Статус', null=False, blank=False, help_text='Статус -1 не инициализирован', default=-1)
    change_status_description = models.CharField(max_length=20, verbose_name='Описание смены статуса', null=True, blank=True, help_text='Описание смены статуса')
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    dispatch = models.ForeignKey(Dispatch, null=True, blank=True, verbose_name='Диспетчерская', help_text='Диспетчерская в привязке к городу')

    def __unicode__(self):
        return u'%s  %s' % (self.first_name, self.last_name)


@receiver(post_save, sender=User)
def create_profile_for_new_user(sender, created, instance, **kwargs):
    if created:
        profile = Customer(user=instance)
        profile.first_name = profile.user.first_name
        profile.last_name = profile.user.last_name
        profile.is_driver = 0
        profile.gender = 1
        profile.save()


class PhotoDocumentStorage(AbstractBaseTable):
    customer = models.ForeignKey(Customer, related_name='document_pictures')
    full_photoURL = models.FileField(verbose_name='Изображение', upload_to='images', null=True, blank=True)
    photo_type = models.ForeignKey(PhotoType, verbose_name='Тип фотографии', null=True, blank=True, help_text='Тип фотографии')


class PhotoDriverLicenceStorage(AbstractBaseTable):
    customer = models.ForeignKey(Customer, related_name='driver_licence_pictures')
    full_photoURL = models.FileField(verbose_name='Изображение', upload_to='images', null=True, blank=True)
    photo_type = models.ForeignKey(PhotoType, verbose_name='Тип фотографии', null=True, blank=True, help_text='Тип фотографии')
