from Customer.models import Customer
from rest_framework import serializers


class CustomerSerializer(serializers.ModelSerializer):
    country_name = serializers.ReadOnlyField(source='country.name', required=False)
    country_id = serializers.ReadOnlyField(source='country.id', required=False)
    city_name = serializers.ReadOnlyField(source='city.name', required=False)
    city_id = serializers.ReadOnlyField(source='city.id', required=False)
    user_id = serializers.ReadOnlyField(source='user.id', required=False)

    class Meta:
        model = Customer
        fields = ('id', 'first_name', 'last_name', 'is_driver', 'car_type',
                  'country_name', 'country_id', 'city_name', 'city_id',
                  'user_id', 'created_at', 'created_at'
                  )
