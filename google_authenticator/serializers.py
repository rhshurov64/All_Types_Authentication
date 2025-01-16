from rest_framework import serializers


class TWoFaLoginInputSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=255)
    password = serializers.CharField(max_length=255)
    two_fa_code = serializers.CharField(max_length=6)
