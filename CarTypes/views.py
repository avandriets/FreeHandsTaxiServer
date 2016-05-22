from CarTypes.models import CarTypes
from CarTypes.serializers import CarTypesSerializer
from rest_framework import permissions
from rest_framework import viewsets
from rest_framework import filters


class CarTypesViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = CarTypes.objects.all()
    serializer_class = CarTypesSerializer

    filter_backends = (filters.DjangoFilterBackend, filters.OrderingFilter,)
    filter_fields = ('name', 'updated_at',)

    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
