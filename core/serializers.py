from . import models
from rest_framework import serializers


class MFAUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.MFAUser
        exclude = ["password"]
