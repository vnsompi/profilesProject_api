from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView


class HelloApiView(APIView):
    """ test api view """

    def get(self, request, format=None):
        """return a test api view features"""
        an_apiview = [
            'Uses http methods as function (get, post, patch, put, delete)',
            'Is similar to a traditional Django view',
            'Gives you the most control over your application logic',
            'Is mapped manually to urls'
        ]
        return Response({'message': 'Hello!', 'an_apiview': an_apiview})

