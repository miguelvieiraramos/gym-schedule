from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from gym_schedule.users.services import create_user, get_user, user_list
from gym_schedule.permissions import IsAuthenticatedOrCreateOnly
from gym_schedule.users.serializers import UserSerializer
from gym_schedule.utils import ApiErrorsMixin


class UserCreateListApi(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticatedOrCreateOnly]

    def post(self, request):
        user_serializer = UserSerializer(data=request.data)
        user_serializer.is_valid(raise_exception=True)

        create_user(**user_serializer.validated_data)

        return Response(status=status.HTTP_201_CREATED)

    def get(self, request):
        users = user_list(current_user=request.user)

        users_serializer = UserSerializer(instance=users, many=True)

        return Response(users_serializer.data)


class UserDetailApi(ApiErrorsMixin, APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, user_id):
        user = get_user(id=user_id, current_user=request.user)

        user_serializer = UserSerializer(instance=user)

        return Response(user_serializer.data)