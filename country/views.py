from Country.models import Country
from Country.serializers import CountrySerializer
from django.shortcuts import render
from rest_framework import viewsets


class CountryViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Country.objects.all()
    serializer_class = CountrySerializer
