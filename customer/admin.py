# coding=utf-8
from Customer.models import Customer
from django.contrib import admin
from django.utils.translation import gettext as _


class CustomerTypesListFilter(admin.SimpleListFilter):
    # Human-readable title which will be displayed in the
    # right admin sidebar just above the filter options.
    title = _('customer types')

    # Parameter for the filter that will be used in the URL query.
    parameter_name = 'is_driver'

    def lookups(self, request, model_admin):
        """
        Returns a list of tuples. The first element in each
        tuple is the coded value for the option that will
        appear in the URL query. The second element is the
        human-readable name for the option that will appear
        in the right sidebar.
        """
        return (
            ('1', _(u'Водитель')),
            ('0', _(u'Пассажир')),
        )

    def queryset(self, request, queryset):
        """
        Returns the filtered queryset based on the value
        provided in the query string and retrievable via
        `self.value()`.
        """
        # Compare the requested value (either '80s' or '90s')
        # to decide how to filter the queryset.
        if self.value() == '1':
            return queryset.filter(is_driver=1)
        if self.value() == '0':
            return queryset.filter(is_driver=0)


class CustomerAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'customer_type', 'car_registration_number', 'car_model', 'car_type', 'city', 'user', 'created_at', 'updated_at')
    list_display_links = ('first_name', 'last_name', 'car_registration_number')
    list_filter = (CustomerTypesListFilter, 'city', 'car_type')

    def customer_type(self, obj):

        if obj.is_driver == 1:
            return u"Водитель"
        else:
            return u"Пассажир"


    customer_type.short_description = 'Driver ?'

    fieldsets = (
        ('Customer data', {
            'fields': ('first_name', 'last_name', 'is_driver', 'city', 'user')
        }),
        ('Car description', {
            'fields': ('car_registration_number', 'car_model', 'car_type')
        }),
        ('Advanced car options', {
            'classes': ('collapse',),
            'fields': ('length', 'width', 'height', 'volume', 'capacity'),
        }),
    )

    def view_car_registration_number(self, obj):
        return obj.car_registration_number

    view_car_registration_number.short_name = 'car_number'

admin.site.register(Customer, CustomerAdmin)
