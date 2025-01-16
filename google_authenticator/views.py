from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.viewsets import ViewSet, ModelViewSet
from rest_framework.response import Response
from rest_framework import status
from core.models import MFAUser
from core.serializers import MFAUserSerializer
from drf_yasg.utils import swagger_auto_schema


class TwoFactorLoginApi(APIView):
    # generate browsable api
    serializer_class = MFAUserSerializer

    def get(self, requets):
        users = MFAUser.objects.all()

        seralizer = MFAUserSerializer(users, many=True)

        return Response(seralizer.data, status=status.HTTP_200_OK)

    @swagger_auto_schema(request_body=MFAUserSerializer)
    def post(self, request):
        serializer = MFAUserSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserAPI(ModelViewSet):
    queryset = MFAUser.objects.all()
    serializer_class = MFAUserSerializer
