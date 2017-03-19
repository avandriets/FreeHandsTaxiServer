from Customer.models import Customer, PhotoDocumentStorage, PhotoDriverLicenceStorage
from Customer.serializers import CustomerSerializer, PhotoDocumentStorageSerializer, PhotoDriverLicenceStorageSerializer
from rest_framework import filters
from rest_framework import viewsets


class CustomerViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

    filter_backends = (filters.DjangoFilterBackend, filters.OrderingFilter,)
    filter_fields = ('is_driver', 'updated_at', 'first_name', 'last_name', 'user')
    ordering_fields = ('created_at', 'updated_at')


class PhotoDocumentStorageViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = PhotoDocumentStorage.objects.all()
    serializer_class = PhotoDocumentStorageSerializer

    filter_backends = (filters.DjangoFilterBackend, filters.OrderingFilter,)
    filter_fields = ('customer', 'updated_at', 'created_at')
    ordering_fields = ('created_at', 'updated_at')


class PhotoDriverLicenceStorageSerializerViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = PhotoDriverLicenceStorage.objects.all()
    serializer_class = PhotoDriverLicenceStorageSerializer

    filter_backends = (filters.DjangoFilterBackend, filters.OrderingFilter,)
    filter_fields = ('customer', 'updated_at', 'created_at')
    ordering_fields = ('created_at', 'updated_at')