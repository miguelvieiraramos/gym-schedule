from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from mixins import ApiErrorsMixin
from users.services import create_user, get_user
from users.serializers import UserSerializer


class UserCreateApi(APIView):

    def post(self, request):
        user_serializer = UserSerializer(data=request.data)
        user_serializer.is_valid(raise_exception=True)

        create_user(**user_serializer.validated_data)

        return Response(status=status.HTTP_201_CREATED)


class UserDetailApi(ApiErrorsMixin, APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, user_id):
        user = get_user(id=user_id, current_user=request.user)

        user_serializer = UserSerializer(instance=user)

        return Response(user_serializer.data)
