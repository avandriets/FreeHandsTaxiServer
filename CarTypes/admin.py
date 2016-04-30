from CarTypes.models import CarTypes
from django.contrib import admin


class CarTypesAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_at', 'updated_at')
    list_display_links = ('name', 'created_at', 'updated_at')

admin.site.register(CarTypes, CarTypesAdmin)