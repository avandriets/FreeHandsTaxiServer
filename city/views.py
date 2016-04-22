from City.models import City
from City.serializers import CitySerializer
from rest_framework import viewsets


class CityViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = City.objects.all()
    serializer_class = CitySerializer
