# coding=utf-8
from django.db import models


class AbstractBaseTable(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class CarTypes(AbstractBaseTable):
    name = models.CharField(max_length=100)

    def __unicode__(self):
        return u'%s' % self.name


class CarsMarks(AbstractBaseTable):
    name = models.CharField(max_length=20, verbose_name='Марка автомобиля', null=True, blank=True, help_text='Марка автомобиля')


class PhotoType(AbstractBaseTable):
    name = models.CharField(max_length=20, verbose_name='Тип фото', null=True, blank=True, help_text='Тип фото')


class Cars(AbstractBaseTable):
    car_type = models.ForeignKey(CarTypes, verbose_name='Тип авто', null=True, blank=True, help_text='Тип авто')
    car_mark = models.ForeignKey(CarsMarks, verbose_name='Марка автомобиля', null=True, blank=True, help_text='Марка автомобиля')
    car_registration_number = models.CharField(max_length=20, verbose_name='Рег номер автомобиля', null=True, blank=True, help_text='Рег номер автомобиля')


class PhotoCarsStorage(AbstractBaseTable):
    car = models.ForeignKey(Cars, related_name='cars_pictures')
    full_photoURL = models.FileField(verbose_name='Изображение', upload_to='images', null=True, blank=True)
    photo_type = models.ForeignKey(PhotoType, verbose_name='Тип фотографии', null=True, blank=True, help_text='Тип фотографии')


class Crew(AbstractBaseTable):
    car = models.ForeignKey(Cars, related_name='cars_crew')
    customer = models.ForeignKey(Cars, related_name='customer_crew')
