from Orders.models import Orders
from Orders.serializers import OrdersSerializer
from rest_framework import filters
from rest_framework import viewsets
from rest_framework import permissions



class OrdersViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Orders.objects.all()
    serializer_class = OrdersSerializer

    filter_backends = (filters.DjangoFilterBackend, filters.OrderingFilter,)
    filter_fields = ('user', 'updated_at', 'city', 'car_type')
    ordering_fields = ('created_at', 'updated_at')

    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)