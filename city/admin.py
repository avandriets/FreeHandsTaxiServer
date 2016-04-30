from City.models import City
from django.contrib import admin


class CityAdmin(admin.ModelAdmin):
    list_display = ('country', 'name', 'created_at', 'updated_at')
    list_display_links = ('country', 'name', 'created_at', 'updated_at')
    list_filter = ('country',)

admin.site.register(City, CityAdmin)
