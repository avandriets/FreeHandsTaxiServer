# coding=utf-8
from apiusr.serializers import UserSerializer
from django.contrib.auth.models import User
from rest_framework import viewsets
 


class UserView(viewsets.ModelViewSet):
    # queryset = User.objects.all()
    serializer_class = UserSerializer
    model = User

    def get_queryset(self):
        return User.objects.filter(id=self.request.user.id)
