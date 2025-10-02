from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from . import  serializers
from rest_framework import status
from rest_framework import viewsets
from . import  models
from . import  permissions
from rest_framework.authentication import TokenAuthentication
from .serializers import HelloSerializer



class HelloApiView(APIView):
    """ test api view """
    serializer_class = serializers.HelloSerializer

    def get(self, request, format=None):
        """return a test api view features"""
        an_apiview = [
            'Uses http methods as function (get, post, patch, put, delete)',
            'Is similar to a traditional Django view',
            'Gives you the most control over your application logic',
            'Is mapped manually to urls'
        ]
        return Response({'message': 'Hello!', 'an_apiview': an_apiview})

    def post(self, request, format=None):
        """create a hello message with name """
        serializer = serializers.HelloSerializer(data=request.data)
        if serializer.is_valid():
            name = serializer.data.get('name')
            message = 'Hello {0}'.format(name)
            return Response({'message': message})
        else:
            return Response(
                serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk=None):
        """handles updating an object"""

        return Response({'message': 'put'})

    def patch(self, request, pk=None):
        """patch request, only updates fields provides in the request """

        return Response({'message': 'patch'})


    def delete(self, request, pk=None):
        """delete an object handles deletion"""

        return Response({'message': 'delete'})


class HelloViewSet(viewsets.ViewSet):
    """test api viewSet"""

    serializer_class =serializers.HelloSerializer

    def list(self, request):
        """return a hello message"""

        a_viewset = [
            'Uses actions (list, create, retrieve, update, partial_update)',
            'Automatically maps to URLs using Routers',
            'Provides more functionality with less code'

        ]

        return Response({'message': 'Hello!', 'a_viewset': a_viewset})

    def create(self, request):
        """Using the create method to create a new hello message"""
        serializer = serializers.HelloSerializer(data=request.data)
        if serializer.is_valid():
            name = serializer.data.get('name')
            message = 'Hello {0}'.format(name)
            return Response({'message': message})

        else:
            return Response(
                serializers.errors, status=status.HTTP_400_BAD_REQUEST
            )

    def retrieve(self, request, pk=None):
        """return a hello message by id"""
        return Response({'http_method': 'GET'})

    def update(self, request, pk=None):
        """update an object  and it handles updating fields"""

        return Response({'http_method': 'PUT'})

    def partial_update(self, request, pk=None):
        """handles updating part of an object"""

        return Response({'http_method': 'PATCH'})

    def destroy(self, request, pk=None):
        """handles deleting an object"""
        return Response({'http_method': 'DELETE'})


"""for userProfile """
class UserProfileViewSet(viewsets.ModelViewSet):
    """"handles ViewSet  for user profile"""
    serializer_class = serializers.UserProfileSerializer
    queryset = models.UserProfile.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.UpdateOwnProfile,)
