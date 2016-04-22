from CarTypes.models import CarTypes
from rest_framework import serializers


class CarTypesSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarTypes
        fields = ('id', 'name', 'created_at', 'updated_at')
