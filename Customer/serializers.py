from Customer.models import Customer
from rest_framework import serializers


class CustomerSerializer(serializers.ModelSerializer):
    # country_name = serializers.ReadOnlyField(source='country.name', required=False)
    # country_id = serializers.ReadOnlyField(source='country.id', required=False)
    # city_name = serializers.ReadOnlyField(source='city.name', required=False)
    # city_id = serializers.ReadOnlyField(source='city.id', required=False)
    # user_id = serializers.ReadOnlyField(source='user.id', required=False)

    class Meta:
        model = Customer
        fields = ('id', 'first_name', 'last_name', 'phone_number', 'is_driver', 'car_type', 'user',
                  'car_type', 'city',  'car_registration_number',
                  'car_model', 'length', 'width', 'height', 'volume', 'capacity'
                  , 'updated_at', 'created_at'
                  )

    # def create(self, validated_data):
    #     element = super(CustomerSerializer, self).create(validated_data)
    #     element.user = self.context['request'].user
    #     element.save()
    #
    #     return element
