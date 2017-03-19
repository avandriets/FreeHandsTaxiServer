from Customer.models import Customer, PhotoDocumentStorage, PhotoDriverLicenceStorage
from rest_framework import serializers


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ('id', 'first_name', 'middle_name', 'last_name', 'is_driver', 'birth_date',
                  'phone_number', 'gender', 'document_number', 'driver_licence_number',
                  'driver_licence_date', 'status', 'change_status_description',
                  'user', 'dispatch', 'updated_at', 'created_at'
                  )

        # def create(self, validated_data):
        #     element = super(CustomerSerializer, self).create(validated_data)
        #     element.user = self.context['request'].user
        #     element.save()
        #
        #     return element


class PhotoDocumentStorageSerializer(serializers.ModelSerializer):
    class Meta:
        model = PhotoDocumentStorage
        fields = ('id', 'customer', 'full_photoURL', 'photo_type', 'updated_at', 'created_at')


class PhotoDriverLicenceStorageSerializer(serializers.ModelSerializer):
    class Meta:
        model = PhotoDriverLicenceStorage
        fields = ('id', 'customer', 'full_photoURL', 'photo_type')
