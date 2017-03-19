from Cars.models import CarTypes, CarsMarks, PhotoType, PhotoCarsStorage, Cars, Crew
from Cars.serializers import CarTypesSerializer, CarMarksSerializer, PhotoTypeSerializer, PhotoCarsStorageSerializer, CarsSerializer, CrewSerializer
from rest_framework import filters
from rest_framework import permissions
from rest_framework import viewsets


class CarTypesViewSet(viewsets.ReadOnlyModelViewSet):

    queryset = CarTypes.objects.all()
    serializer_class = CarTypesSerializer

    filter_backends = (filters.DjangoFilterBackend, filters.OrderingFilter,)
    filter_fields = ('name', 'updated_at',)

    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)


class CarsMarksViewSet(viewsets.ReadOnlyModelViewSet):

    queryset = CarsMarks.objects.all()
    serializer_class = CarMarksSerializer

    filter_backends = (filters.DjangoFilterBackend, filters.OrderingFilter,)
    filter_fields = ('name', 'updated_at',)

    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)


class PhotoTypeViewSet(viewsets.ReadOnlyModelViewSet):

    queryset = PhotoType.objects.all()
    serializer_class = PhotoTypeSerializer

    filter_backends = (filters.DjangoFilterBackend, filters.OrderingFilter,)
    filter_fields = ('name', 'updated_at',)

    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)


class PhotoCarsStorageViewSet(viewsets.ModelViewSet):

    queryset = PhotoCarsStorage.objects.all()
    serializer_class = PhotoCarsStorageSerializer

    filter_backends = (filters.DjangoFilterBackend, filters.OrderingFilter,)
    filter_fields = ('car', 'photo_type', 'updated_at',)


class CarsViewSet(viewsets.ModelViewSet):

    queryset = Cars.objects.all()
    serializer_class = CarsSerializer

    filter_backends = (filters.DjangoFilterBackend, filters.OrderingFilter,)
    filter_fields = ('car', 'photo_type', 'updated_at',)


class CrewViewSet(viewsets.ModelViewSet):

    queryset = Crew.objects.all()
    serializer_class = CrewSerializer

    filter_backends = (filters.DjangoFilterBackend, filters.OrderingFilter,)
    filter_fields = ('car', 'customer', 'updated_at',)
