from django.db.models.query import QuerySet
from django.shortcuts import render
from django.contrib.auth.models import User
from .serializers import UserSerializer
from rest_framework import authentication, permissions
from django.contrib.auth.models import User
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.views import APIView
from rest_framework import viewsets
from django.http.response import Http404
from rest_framework.response import Response

@authentication_classes([authentication.TokenAuthentication])
@permission_classes([permissions.IsAuthenticated])
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

@authentication_classes([authentication.TokenAuthentication])
@permission_classes([permissions.IsAuthenticated])
class MyAccount(APIView):
    def get_object(self, username):
        try:
            return User.objects.get(username=username)
        except User.DoesNotExist:
            raise Http404

    def get(self, request, username, format=None):
        curr_user = self.get_object(username)
        serializer = UserSerializer(curr_user)
        return Response(serializer.data)

