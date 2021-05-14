from django.urls import path
from users.views import CreateUserApi, ObtainAuthToken, AuthTest

app_name = 'users'

urlpatterns = [
    path('users', CreateUserApi.as_view(), name='create-users'),
    path('auth', ObtainAuthToken.as_view(), name='obtain-auth-token'),
    path('auth-test', AuthTest.as_view())
]
