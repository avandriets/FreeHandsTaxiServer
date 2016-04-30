from Country.models import Country
from django.contrib import admin


class CountryAdmin(admin.ModelAdmin):
    list_display = ('name_eng', 'name_rus', 'created_at', 'updated_at')
    list_display_links = ('name_eng', 'name_rus', 'created_at', 'updated_at')

admin.site.register(Country, CountryAdmin)
