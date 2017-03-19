from DriverResponse.models import DriverResponse
from rest_framework import serializers


class DriverResponseSerializer(serializers.ModelSerializer):

    class Meta:
        model = DriverResponse
        fields = ('id', 'order', 'user', 'price', 'status', 'updated_at', 'created_at')