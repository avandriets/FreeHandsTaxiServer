from Dispatch.models import Dispatch
from Dispatch.serializers import DispatchSerializer
from rest_framework import filters
from rest_framework import viewsets


class CustomerViewSet(viewsets.ReadOnlyModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Dispatch.objects.all()
    serializer_class = DispatchSerializer

    filter_backends = (filters.DjangoFilterBackend, filters.OrderingFilter,)
    filter_fields = ('is_driver', 'updated_at', 'first_name', 'last_name', 'user')
    ordering_fields = ('created_at', 'updated_at')

