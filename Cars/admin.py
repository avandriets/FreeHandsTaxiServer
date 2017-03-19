from Cars.models import CarTypes, CarsMarks, PhotoType, Crew, Cars
from django.contrib import admin


class CarTypesAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_at', 'updated_at')
    list_display_links = ('name', 'created_at', 'updated_at')

admin.site.register(CarTypes, CarTypesAdmin)


class CarsMarksAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_at', 'updated_at')
    list_display_links = ('name', 'created_at', 'updated_at')

admin.site.register(CarsMarks, CarsMarksAdmin)


class PhotoTypeAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_at', 'updated_at')
    list_display_links = ('name', 'created_at', 'updated_at')

admin.site.register(PhotoType, PhotoTypeAdmin)


class CrewAdmin(admin.ModelAdmin):
    list_display = ('car', 'customer', 'created_at', 'updated_at')
    list_display_links = ('car', 'customer', 'created_at', 'updated_at')

admin.site.register(Crew, CrewAdmin)


class PhotoCarsStorageAdmin(admin.ModelAdmin):
    list_display = ('car', 'full_photoURL', 'photo_type', 'created_at', 'updated_at')
    list_display_links = ('car', 'full_photoURL', 'photo_type', 'created_at', 'updated_at')

admin.site.register(Crew, CrewAdmin)


class CarsAdmin(admin.ModelAdmin):
    list_display = ('car_type', 'car_mark', 'car_registration_number', 'created_at', 'updated_at')
    list_display_links = ('car_type', 'car_mark', 'car_registration_number', 'created_at', 'updated_at')

admin.site.register(Cars, CarsAdmin)