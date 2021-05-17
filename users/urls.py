from django.urls import path
from users.views import UserCreateListApi, UserDetailApi

app_name = 'users'

urlpatterns = [
    path('users', UserCreateListApi.as_view(), name='user-create-list-api'),
    path('users/<int:user_id>', UserDetailApi.as_view(), name='user-detail-api')
]
