from City.models import City
from City.serializers import CitySerializer
from rest_framework import viewsets
from rest_framework import permissions




class CityViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = City.objects.all()
    serializer_class = CitySerializer

    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)