from rest_framework import serializers


class HelloSerializer(serializers.Serializer):
    """serializer for testing our API """
    name = serializers.CharField(max_length=20)

