from Customer.models import Customer
from Customer.serializers import CustomerSerializer
from rest_framework import filters
from rest_framework import viewsets


class CustomerViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

    filter_backends = (filters.DjangoFilterBackend, filters.OrderingFilter,)
    filter_fields = ('is_driver', 'updated_at', 'city', 'first_name', 'last_name', 'car_type', 'user')
    ordering_fields = ('created_at', 'updated_at')
