from django.urls import path
from users.views import UserCreateApi, UserDetailApi

app_name = 'users'

urlpatterns = [
    path('users', UserCreateApi.as_view(), name='user-create-api'),
    path('users/<int:user_id>', UserDetailApi.as_view(), name='user-detail-api')
]
