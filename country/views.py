from Country.models import Country
from Country.serializers import CountrySerializer
from rest_framework import viewsets
from rest_framework import permissions



class CountryViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    queryset = Country.objects.all()
    serializer_class = CountrySerializer
