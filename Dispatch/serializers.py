from Dispatch.models import Dispatch
from rest_framework import serializers


class DispatchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dispatch
        fields = ('id', 'name', 'city', 'updated_at', 'created_at')