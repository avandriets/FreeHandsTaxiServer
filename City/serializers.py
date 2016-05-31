from City.models import City
from rest_framework import serializers



class CitySerializer(serializers.ModelSerializer):
    country_name = serializers.ReadOnlyField(source='country.name', required=False)
    country_id = serializers.ReadOnlyField(source='country.id', required=False)

    class Meta:
        model = City
        fields = ('id', 'name', 'country_name', 'country_id', 'created_at', 'updated_at')
