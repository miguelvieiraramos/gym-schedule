from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import serializers
from rest_framework.permissions import IsAuthenticated

from users.authentications import AppAuthentication
from users.serializers import UserSerializer
from users.services import create_user, create_auth_token


class CreateUserApi(APIView):

    def post(self, request):
        user_serializer = UserSerializer(data=request.data)
        user_serializer.is_valid(raise_exception=True)

        create_user(**user_serializer.validated_data)

        return Response(status=status.HTTP_201_CREATED)


class ObtainAuthToken(APIView):
    class InputSerializer(serializers.Serializer):
        username = serializers.CharField(max_length=150)
        password = serializers.CharField(max_length=128)

    def post(self, request):
        input_serializer = self.InputSerializer(data=request.data)
        input_serializer.is_valid(raise_exception=True)

        token = create_auth_token(**input_serializer.validated_data)

        return Response({'token': token.key}, status=status.HTTP_200_OK)


class AuthTest(APIView):
    authentication_classes = [AppAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        print(request.user)
        return Response({'message': 'Hello, world!'})