from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import serializers
from rest_framework import status

from gym_schedule.auth.services import create_auth_token
from gym_schedule.utils import ApiErrorsMixin


class ObtainAuthToken(ApiErrorsMixin, APIView):
    class InputSerializer(serializers.Serializer):
        username = serializers.CharField(max_length=150)
        password = serializers.CharField(max_length=128)

    def post(self, request):
        input_serializer = self.InputSerializer(data=request.data)
        input_serializer.is_valid(raise_exception=True)

        token = create_auth_token(**input_serializer.validated_data)

        return Response({'token': token.key}, status=status.HTTP_200_OK)


class AuthTest(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        return Response({'message': 'Hello, world!'})

