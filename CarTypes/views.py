from CarTypes.models import CarTypes
from CarTypes.serializers import CarTypesSerializer
from rest_framework import viewsets


class CarTypesViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = CarTypes.objects.all()
    serializer_class = CarTypesSerializer
