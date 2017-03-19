from Cars.models import CarTypes, CarsMarks, PhotoType, Crew
from rest_framework import serializers


class CarsSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarTypes
        fields = ('id', 'car_type', 'car_mark', 'car_registration_number', 'updated_at', 'created_at')


class CrewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Crew
        fields = ('id', 'car', 'customer', 'updated_at', 'created_at')


class CarTypesSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarTypes
        fields = ('id', 'name', 'created_at', 'updated_at')


class CarMarksSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarsMarks
        fields = ('id', 'name', 'created_at', 'updated_at')


class PhotoTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = PhotoType
        fields = ('id', 'full_photoURL', 'photo_type', 'created_at', 'updated_at')


class PhotoCarsStorageSerializer(serializers.ModelSerializer):
    class Meta:
        model = PhotoType
        fields = ('id', 'name', 'created_at', 'updated_at')
