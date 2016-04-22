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
from CarTypes.models import CarTypes
from City.models import City
from Country.models import Country
from Customer.models import Customer
from Orders.models import Orders
from django.conf.urls import url
from django.contrib import admin
from django.conf.urls import include, url
from django.contrib import admin
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'accounts', apiusr.views.UserView, 'list')
router.register(r'car_types', CarTypes.views.CarTypesViewSet, 'list')
router.register(r'cities', City.views.CarTypesViewSet, 'list')
router.register(r'countries', Country.views.CarTypesViewSet, 'list')
router.register(r'customer', Customer.views.CustomerViewSet)
router.register(r'orders', Orders.views.CustomerViewSet)


urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^rest/', include(router.urls)),
    url(r'^o/', include('oauth2_provider.urls', namespace='oauth2_provider')),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^auth/', include('rest_framework_social_oauth2.urls')),
    url(r'', include('gcm.urls')),
]
