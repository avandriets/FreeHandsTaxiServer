from Dispatch.models import Dispatch
from django.contrib import admin


class DispatchAdmin(admin.ModelAdmin):
    list_display = ('name', 'city', 'updated_at', 'created_at')
    list_display_links = ('name', 'city', 'updated_at', 'created_at')

admin.site.register(Dispatch, DispatchAdmin)
