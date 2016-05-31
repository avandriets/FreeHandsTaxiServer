from DriverResponse.models import DriverResponse
from DriverResponse.serializers import DriverResponseSerializer
from rest_framework import filters
from rest_framework import viewsets
from rest_framework import permissions



class DriverResponseViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = DriverResponse.objects.all()
    serializer_class = DriverResponseSerializer

    filter_backends = (filters.DjangoFilterBackend, filters.OrderingFilter,)
    filter_fields = ('updated_at', 'user', 'order')
    ordering_fields = ('created_at', 'updated_at')

    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)