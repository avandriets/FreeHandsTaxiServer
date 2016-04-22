from Orders.models import Orders
from rest_framework import serializers


class OrdersSerializer(serializers.ModelSerializer):
    user_id = serializers.ReadOnlyField(source='user.id', required=False)
    city_name = serializers.ReadOnlyField(source='city.name', required=False)
    city_id = serializers.ReadOnlyField(source='city.id', required=False)

    class Meta:
        model = Orders
        fields = ('id', 'user_id', 'city_name', 'city_id', 'created_at', 'created_at')
