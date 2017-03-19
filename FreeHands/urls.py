"""FreeHands URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Import the include() function: from django.conf.urls import url, include
    3. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
import apiusr.views
from Cars.views import CarsViewSet, CarTypesViewSet, CarsMarksViewSet, PhotoTypeViewSet, PhotoCarsStorageViewSet, CrewViewSet
from DriverResponse.views import DriverResponseViewSet
from django.conf.urls import include, url
from django.contrib import admin
from rest_framework import routers
from City.views import CityViewSet
from Country.views import CountryViewSet
from Customer.views import CustomerViewSet
from Orders.views import OrdersViewSet

router = routers.DefaultRouter()
router.register(r'cars', CarsViewSet, 'list')
router.register(r'car_types', CarTypesViewSet, 'list')
router.register(r'car_marks', CarsMarksViewSet, 'list')
router.register(r'photo_type', PhotoTypeViewSet, 'list')
router.register(r'car_photo', PhotoCarsStorageViewSet, 'list')
router.register(r'crew', CrewViewSet, 'list')
router.register(r'cities', CityViewSet, 'list')
router.register(r'countries', CountryViewSet, 'list')
router.register(r'customer', CustomerViewSet)
router.register(r'orders', OrdersViewSet)
router.register(r'drivers_response', DriverResponseViewSet)
router.register(r'accounts', apiusr.views.UserView, 'list')

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^rest/', include(router.urls)),
    url(r'^o/', include('oauth2_provider.urls', namespace='oauth2_provider')),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^auth/', include('rest_framework_social_oauth2.urls')),
    url(r'', include('gcm.urls')),
]
