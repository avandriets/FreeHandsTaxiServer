from Orders.models import Orders
from rest_framework import serializers



class OrdersSerializer(serializers.ModelSerializer):

    class Meta:
        model = Orders
        fields = ('id', 'user', 'city', 'car_type', 'order_date', 'driver', 'status',
                  'from_address', 'to_address',
                  'from_latitude', 'from_longitude', 'to_latitude', 'to_longitude',
                  'description', 'price', 'updated_at', 'created_at')

    def create(self, validated_data):
        element = super(OrdersSerializer, self).create(validated_data)
        element.user = self.context['request'].user
        element.save()

        return element
